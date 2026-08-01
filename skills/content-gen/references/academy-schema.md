# The Academy Publish Schema — the platform target contract

ContentGen's internal `manifest.json` (see `output-contract.md`) is the **authoring** representation.
This document is the **publish** representation: the exact YAML/JSON contract the **Superteam Academy**
platform (`github.com/solanabr/academy-courses`) validates and runs. `tools/academy_export.py` projects an
authored course into this shape under `content/academy/courses/<slug>/`; `tools/verify_challenges.py`
enforces the one runtime rule the platform enforces (starter fails, solution passes).

**Authoritative source.** The platform ships JSON Schemas and a linter; this doc mirrors them (pinned
2026-07-30 from `academy-courses@main`). When they disagree, the platform wins:
- `schema/course.schema.json`, `schema/lesson.schema.json`, `schema/quiz.schema.json`
- linter: `solanabr/superteam-academy` → `@superteam-lms/content-lint` (`pnpm --filter @superteam-lms/content-lint exec tsx src/cli.ts <content>`), plus `challenge-executor` for TS grading.

## Filesystem layout (mirrors `courses/_template/`)

```
courses/<slug>/
├── course.yaml                     # course manifest (modules → lesson ids)
└── lessons/<lesson-slug>/
    ├── lesson.yaml                 # ordered `blocks:` array
    ├── intro.md                    # a `prose` block's `src` (any name)
    └── <ex>/                       # one dir per code block (name is free: ts/, rs/, exercise/, program/…)
        ├── starter.{ts,rs}
        ├── solution.{ts,rs}
        └── tests.json
```
Every file in a lesson dir MUST be referenced by a block (`src`/`starter`/`solution`/`tests`/`idl`) or
linked from a prose `.md` — **no orphan files** (CI rule).

## `course.yaml`

Required: `id, slug, title, difficulty, duration, xpPerLesson, xpReward, modules`.
```yaml
id: course-btc-to-sol-evolution        # ^course-[a-z0-9-]+$ , ≤ 32 chars, PERMANENT
slug: btc-to-sol-evolution             # ^[a-z0-9-]+$
title: From Bitcoin to Solana
description: >-                          # optional
  ...
difficulty: beginner                    # beginner | intermediate | advanced
duration: 15                            # number (we use lesson count)
xpPerLesson: 20                         # 1..100
xpReward: 300                           # 0..5000  (see XP ceiling below)
creator: <SolanaWalletAddress>          # required in practice; Course.creator on-chain, immutable
# optional: creatorRewardXp, minCompletionsForReward, trackId, trackLevel, tags[], thumbnail, prerequisiteCourse
modules:                                # ≥1; ordered
  - key: crypto                         # ^[a-z0-9-]+$
    title: Trust math, not people
    description: ...                    # optional
    lessons: [lesson-b2s-trust-machine, lesson-b2s-hash-everything]   # each ^lesson-[a-z0-9-]+$
```

## `lesson.yaml`

Required: `id, slug, title, blocks`. `skills:` is accepted (used throughout the repo) though not in the
schema — populate it from `skills.yaml` slugs. `blocks` is ordered, ≥1, each a `oneOf` of 8 block types.
Every block has a kebab `key`; capability edges use `produces`/`consumes` (`funded-wallet`,
`deployed-program`).

```yaml
id: lesson-b2s-hash-everything          # ^lesson-[a-z0-9-]+$ , PERMANENT
slug: hash-everything
title: Hash Everything
skills: [solana-fundamentals, rust]     # slugs from skills.yaml
blocks:
  - { key: intro, type: prose, src: intro.md }
  - { key: watch, type: video, url: "https://youtu.be/..." }        # optional
  - key: check
    type: quiz
    questions: [ ... ]                   # see Quiz
  - key: exercise
    type: code                           # see Code
    language: rust
    ...
  - { key: reflect, type: openEnded, prompt: "What did you learn?", maxWords: 120 }   # never graded
```

### The 8 block types (required fields)
| type | required | notes |
|---|---|---|
| `prose` | `type, key, src` | `src` = a `.md` in the lesson dir |
| `video` | `type, key, url` | URI |
| `code` | `type, key, language, starter, solution, tests` | see Code |
| `quiz` | `type, key, questions` | see Quiz |
| `openEnded` | `type, key, prompt` | `maxWords` 20..500 (default 200); ungraded, gates nothing |
| `wallet-funding` | `type, key` | `produces: funded-wallet`; `amount` 0..5 (default 2); `network: devnet` |
| `program-explorer` | `type, key, idl` | consumes `deployed-program` |
| `deployed-program-card` | `type, key` | consumes `deployed-program` |

## Quiz block

```yaml
- key: check
  type: quiz
  questions:
    - id: q1                             # stable; correctness is keyed to option id, never position
      prompt: "Which of these stores state?"
      multiSelect: false                 # default false
      options:                           # 3 preferred (≥2 min); each {id, label, correct}, feedback on wrong
        - { id: a, label: Instructions, correct: false, feedback: "Inputs, not storage." }
        - { id: b, label: Programs, correct: false, feedback: "Stateless by design — code only." }
        - { id: c, label: Data accounts, correct: true }
      explanation: "..."                 # optional but expected; shown after answering
```
- `multiSelect: false` → **exactly one** `correct: true`; `true` → **≥ 1**.
- Put `feedback` on every wrong option and a substantive `explanation` on every question.
- **Authoring bar** (matches the published `btc-to-sol-evolution` course): scenario-driven, often
  two-part prompts ("what property is that, and why does it matter?") tied to something the learner
  just ran; 3 options; distractors are real plausible misconceptions matched to the answer in length
  and register — never joke options, never a giveaway-long correct label.
- **Vary the correct answer's position roughly evenly across the course.** Correctness is id-keyed,
  but learners see slots: a course where the right answer always sits first is guessable without
  reading (this shipped once — 33/33 on 'a'). `validate_course.py` HARD-fails >50% one-slot skew
  across ≥6 single-select questions and advises when the correct label is consistently the longest.

## Code block — the three test modes

```yaml
- key: exercise
  type: code
  language: typescript | rust            # ONLY these two
  buildType: standard | buildable        # default standard
  deployable: false                      # default false; true → produces: deployed-program
  starter: <ex>/starter.{ts,rs}
  solution: <ex>/solution.{ts,rs}
  tests:   <ex>/tests.json
  hints: [ "..." ]                       # optional
```
`tests.json` = `[{ id, input, expectedOutput, description? }]`. **Contract: the solution passes every case;
the starter fails at least one.** How a case is evaluated depends on the mode:

1. **TypeScript** (`language: typescript`). The file defines a primary function; the runner calls it with
   the case `input` (a verbatim JS argument list) and binds the return value to `result`; `expectedOutput`
   is a **boolean expression over `result`** (and the inputs).
   ```jsonc
   // input is spliced as-is → assembleDeposit('0wner…', 1000000n, 'B1ock…')
   { "id": "t1", "input": "'0wner…', 1000000n, 'B1ock…'", "expectedOutput": "result.feePayer === '0wner…'" }
   ```
   The starter type-checks but returns wrong values (e.g. `lifetimeBlockhash: ""`, `instructions: []`), so
   it fails ≥1 assertion. Keep the function **pure** (no live RPC/imports) so grading is deterministic.
   *(This is the mode the platform executes on every PR.)*

2. **Rust `standard`** (`language: rust`, default buildType). Plain function; the runner calls it with
   `input` and compares the returned value to `expectedOutput` (a **value**, not an expression).
   ```jsonc
   // fn add(a: i64, b: i64) -> i64 { a + b }
   { "id": "t1", "input": "2, 3", "expectedOutput": "5" }
   ```

3. **Rust `buildable`** (`buildType: buildable`, optionally `deployable: true`). A full Anchor program; a
   case's `expectedOutput` is `"true"`/`"ok"` and means **it compiled** against the pinned Anchor toolchain
   (anchor-lang 1.1.2). Enforce signatures with a hidden **verification harness** at the bottom of the file
   — a `#[doc(hidden)] #[allow(dead_code)] mod verify { use super::*; … }` whose type-level references
   (accessor fns, `const … : fn(Context<…>) -> Result<()> = …`) compile only when the required items exist
   with the exact names/signatures. The starter omits/comments-out those items so the harness fails to
   compile.
   ```jsonc
   { "id": "t1", "description": "compiles against anchor-lang 1.1.2", "input": "", "expectedOutput": "true" }
   ```
   Platform note: Rust challenges are **not** executed on the author's PR (only presence of
   starter/solution/tests is checked); they run when a learner submits. `verify_challenges.py` runs them
   locally anyway (`cargo check` against anchor-lang 1.1.2) so our contract is proven before publish.

## CI rules the export must satisfy
- **Permanent kebab ids.** `course-…` / `lesson-…`; course id ≤ 32 chars. Renaming a shipped id is rejected.
- **XP ceiling:** `xpPerLesson × lessonCount ≤ 10000`; `xpPerLesson` 1..100.
- **Challenges execute:** TS solution passes all cases, TS starter fails ≥1 (CI-enforced); Rust files just
  have to be present at PR time.
- **Creator wallet:** `course.creator` a real Solana address (immutable on-chain).
- **Capability ordering:** a `consumes` must follow a matching `produces` earlier in the course; only
  `wallet-funding` produces `funded-wallet`; only a `deployable` code block produces `deployed-program`.
- **No orphan files;** **quiz correctness keyed to stable option ids;** **`openEnded` never graded.**

## Images
Images live in a per-lesson `assets/` folder and are embedded from prose markdown with a relative
link and a full-sentence alt (the accessibility caption): `![alt sentence](assets/v01-diagram.png)`.
Upstream CI enforces **no orphan files** — every asset must be referenced from a block or prose.
A course may also keep the HTML sources that generated its images in a course-level `visual-src/`
folder (`visual-src/<lesson>/vNN-<kind>.html` + shared `_brand.css`/`_render.css`); it is
linter-ignored and never published, kept so visuals stay re-renderable from the repo.

## How ContentGen maps onto this (the export)
- `course-<internal-id>` (≤32 chars) / `lesson-<prefix>-<internal-id>`; module `key` = internal module slug.
- **prose** ← the written `lessons/drafts/<lesson>.md`. The Nth ```visual spec becomes
  `![alt](assets/vNN-<type>.png)` when its render exists in `lessons/assets/<stem>/` (run
  `render_visuals.py` BEFORE exporting); an unrendered spec degrades to a blockquote + warning.
- **assets** ← every raster image in `lessons/assets/<stem>/` is copied to
  `lessons/<slug>/assets/` — the rendered `vNN-*.png` visuals plus any hand-placed image
  (a photo, a source slide) that the draft references directly as `![alt](assets/<name>.png)`.
  PDFs (render intermediates) never ship. HTML sources + shared `_brand.css`/`_render.css`
  are copied to `visual-src/`.
- **quiz** ← the lesson brief's `quiz_blocks` (see `lesson-brief-schema.md` §C).
- **code** ← the lesson brief's `coding_challenges`; each challenge's `starter`/`solution`/`tests` files are
  copied into `<challenge-id>/` under the lesson dir. `language ∈ {rust, typescript}` only — Bitcoin/CLI/
  Python/Solidity lessons carry quizzes but no code block.
- `skills` ← mapped from the course DAG nodes to `skills.yaml` slugs.
