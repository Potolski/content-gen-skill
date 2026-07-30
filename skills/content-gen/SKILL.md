---
name: content-gen
description: "Use when creating educational Solana/Web3 content of any form — a course or curriculum, a hands-on tutorial, a code/protocol/transaction walkthrough, an explainer/primer/deep-dive, an essay or long-form article, a litepaper/whitepaper, a slide deck (text spec), or a tweet/thread/TL;DR — including planning, outlining, sequencing, scaffolding, or writing it. Triggers: 'write a tutorial/explainer/essay/thread/tweet/deck about X', 'design/architect/outline a Solana course', 'draft our litepaper', 'turn these notes into a lesson/article', 'explain X for developers', 'make slides for my talk'. Not for reference docs, marketing copy, or code review."
license: MIT
user-invocable: true
---

# ContentGen (Solana educational-content architect & writer)

One skill, eight content forms: **course · tutorial · walkthrough · explainer ·
essay · litepaper · slides · post** (tweets/threads are `post` sub-profiles). Built on three always-true layers — the pedagogical **design spine**
(`design-spine.md`, always on), the routed **pattern layer** (`patterns/*.md` via
`routing/ROUTING.md`, course-scale shapes), and the **Solana prerequisite DAG**
(`references/solana-syllabus-dag.md`, the order the domain forces) — plus a **form
router** (`forms/FORMS.md`) that decides which pipeline runs at all.

## Scope & deliverable (canonical — every other doc defers here)

- **Default deliverable: fully written text**, finished with a visual-placeholder
  pass (`references/visual-placeholders.md`; density `visuals: none|light|rich`).
  `deliverable: brief-only` is available when the user asks for just the
  structure/outline.
- **Voice seam:** every brief carries a `dominant_job` tag. If the sibling
  `writer-style` skill is installed, prose is written by handing the brief to
  `/write-in-voice` (its router consumes `dominant_job` directly). Resolve the
  **installed skill at runtime** — latest release, discovered by name, never a
  hardcoded path/version/profile file (upstream:
  github.com/solanabr/writer-style-skill). If it is not installed, this skill
  writes the prose itself from the brief — plain technical register, felt hook,
  named trade-offs, no persona imitation.
- **Courses** additionally emit a validated filesystem (`content/courses/<id>/`) of
  per-lesson briefs; lessons are then written one at a time through the same voice
  seam.
- Technical claims are **grounded at design time** against live sources
  (`references/research-grounding.md`) and still pass a **human accuracy review**
  before publish. The skill never deploys anything.
- **The generation pipeline is fixed** (skipping a stage is a defect, not a
  shortcut): **(1) research through the solana-ai-kit surfaces** — the
  `solana-researcher`/`solana-guide` agents, the `deep-research` skill, the
  `solana-dev`/`context7`/`helius` MCPs — never from model memory (degradation
  ladder only when the kit is absent); **(2) draft** — structure complete, every
  frozen fact placed; **(3) writer-style pass** produces the delivered text
  (mandatory when installed); **(4) visual-placeholder pass**; **(5) validators**
  (this skill's gate + writer-style's facts/tells); **(6) optional render + review pass** —
  `references/visual-rendering.md` turns the ` ```visual ` specs into on-brand PNGs, then
  `references/visual-review.md` QAs every render (fresh-eyes visual check + `render_visuals.py
  review`) and re-authors any glitched card (opt-in; needs WeasyPrint + a rasterizer).

## Step 0 — route the form (always first)

Load `forms/FORMS.md`. Explicit ask wins; infer otherwise; on ambiguity default to
the smallest fully-written form that serves the outcome. Then load **only**
`forms/<form>.md` for the routed form and follow its recipe through the shared
pipeline (FORMS.md §shared). `course` loads `forms/course.md` (the form recipe,
corpus-informed) and runs the pipeline below.

## The course pipeline

Each step names the docs it loads (stay lean — load only what the step needs) and
whether it MUST ground against live sources.

1. **Intake.** Course idea/goal, **audience** + prior model (absolute-beginner /
   web2-dev / evm-dev / solana-dev-leveling-up / non-technical), **terminal
   outcome**, scope & length, format, credential goal, `visuals` density,
   `deliverable` mode. Defaults over interrogation; ask only on a missing
   *critical* field.
2. **Backward design (always first).** Measurable, Bloom-tagged terminal
   outcome(s) + the capstone that proves them — *before* any module list. _Loads:_
   `design-spine.md` §1.
3. **Map the prerequisite DAG.** Derive the skill graph; entry point by prior
   model. **MUST GROUND** (order + that named primitives exist and are current).
   _Loads:_ `references/solana-syllabus-dag.md`, `references/research-grounding.md`.
4. **Route.** Backbone + lesson template + ≤2 guests by **outcome + audience**
   (never topic). _Loads:_ `routing/ROUTING.md`. Names patterns; doesn't load them.
5. **Load only the routed patterns.** Never all of `patterns/`.
6. **Sequence.** Modules/lessons up the DAG; thread the artifact ladder; ramp
   difficulty as a fading schedule; fast first win; one "aha" per lesson. **MUST
   GROUND** every concrete API/tool/number that will land in a brief. _Loads:_
   `design-spine.md` §§3–5.
7. **Write per-lesson briefs.** Fill `lesson-brief-schema.md` §C (set `kind:
   build|concept` and `dominant_job`). Voice-ready, not voice-written.
8. **Design cadence.** Pedagogy (fade / ramp / spiral / retrieval) + release
   (drip / effort / freshness). _Loads:_ `design-spine.md` §§5, 9.
9. **Research scaffolds.** Per lesson: claims/APIs/numbers to ground, with a
   `source_priority`; freeze verified facts. **MUST GROUND.** → `lessons/research/*`
   + `lessons/facts/*`.
10. **Assessment & capstone.** Proof model; **gate on doing**; capstone uses only
    taught skills. _Loads:_ `design-spine.md` §6.
11. **Validate, then EMIT.** Assemble `manifest.json`
    (`references/output-contract.md`); run the gate; fix every HARD; emit; re-check:
    ```bash
    python3 "$SKILL/tools/validate_course.py" all --manifest manifest.json
    python3 "$SKILL/tools/scaffold_course.py" emit --manifest manifest.json --out content/courses/<id>
    python3 "$SKILL/tools/validate_course.py" all --course content/courses/<id>
    ```
    Then the JUDGE items in `references/quality-bar.md`.
12. **Write the lessons.** Work `content/courses/<id>/queue/NEXT.md` through the voice seam
    (Scope & deliverable above), one lesson at a time; run the visual pass on each
    draft; update `_state.yaml`. In `brief-only` mode, stop after the handoff
    packet and note the human accuracy gate.

## What you load when (keep context lean)

| Step | Load | Ground? |
|---|---|---|
| 0 route form | `forms/FORMS.md` → one `forms/<form>.md` | no |
| 2 backward design | `design-spine.md` §1 | no |
| 3 map DAG | `references/solana-syllabus-dag.md` + `references/research-grounding.md` | **yes** |
| 4 route patterns | `routing/ROUTING.md` | no |
| 5 patterns | only the routed `patterns/*.md` | no |
| 6 sequence | `design-spine.md` §§3–5 | **yes** |
| 7 briefs | `lesson-brief-schema.md` | reuse step 6 |
| 8–10 cadence/research/assess | `design-spine.md` §§5,6,9 | **yes** |
| 11 emit | `references/output-contract.md`, `references/quality-bar.md`, `tools/` | — |
| 12 write | `references/visual-placeholders.md` (+ writer-style if installed) | reuse 9 |

If grounding tooling is unavailable, follow the degradation ladder in
`references/research-grounding.md` — never silently mark a claim verified from memory.

## Tools

Resolve the skill directory, then call tools with absolute paths:

```bash
SKILL="${CLAUDE_PLUGIN_ROOT:+$CLAUDE_PLUGIN_ROOT/skills/content-gen}"
[ -d "$SKILL" ] || SKILL=".claude/skills/content-gen"
[ -d "$SKILL" ] || SKILL="skills/content-gen"
# (you loaded this SKILL.md from disk — its parent directory is also a valid $SKILL)
python3 "$SKILL/tools/test_tools.py"                                 # all selftests
python3 "$SKILL/tools/validate_course.py" all --course content/courses/<id>  # deterministic gate
python3 "$SKILL/tools/scaffold_course.py" emit --manifest m.json --out content/courses/<id>
```

- `tools/validate_course.py` — `dag | briefs | ladder | capstone | outcomes | drafts | all`
  (`drafts` HARD-enforces the ≥2-visuals-per-lesson floor on written lessons).
  HARD = breaks the DAG walk or the writer handoff; ADVISORY = a smell to weigh.
- `tools/scaffold_course.py` — `emit` (idempotent; `--force`), `check` (dry-run). Honors
  human edits via `course.lock.json` hash drift.
- `tools/dedash.py` — strips em-dashes (the top AI tell) from drafts, deterministically:
  commas in prose/visual specs, hyphens in code comments, code/output fences protected.
  Run it as the final step of the writing pass; `validate_course.py drafts` HARD-fails
  a lesson with >2 em-dashes outside code (house policy: essentially none).
- `tools/verify_code.py` — **compiles/runs every code block the piece ships, for ANY
  form.** `verify_code.py <course-or-content-dir>` (or `--file <one.md>`) extracts each
  fenced block and dispatches it to a real toolchain; `--env docker` runs the pinned,
  version-matched image (`verify/Dockerfile`). FAIL = a real compile/run break; SKIP =
  that language needs the container (resolve with `--env docker`, never ship on SKIP).
  It is CI **tier 5** (`ci.py --tiers 5`). This is non-negotiable: **no piece that
  contains runnable code is "done" until `verify_code.py` is green on it.**
- `tools/render_visuals.py` — the **optional render + review pass**: turns each ` ```visual `
  spec into an on-brand PNG via the shipped `brand/` core + WeasyPrint (`extract → scaffold →
  author each `.viz` → decorate → render → review → check`). `render` FAILS any card that
  overflows the 1600×900 canvas; `review` adds a static QA (page-overflow + forbidden-CSS lint)
  that pairs with the fresh-eyes visual pass in `references/visual-review.md`. Deterministic, no
  browser; SKIP if WeasyPrint/rasterizer absent. Additive — the ` ```visual ` spec stays in the
  markdown; the PNG is written beside the lesson.
- Stdlib-only, each with `--selftest`. The deterministic gate applies to the
  **course** form; other forms gate on their form-file checklist — but `verify_code.py`
  runs on every form, because any piece can ship code.

## The pattern layer (course-scale shapes, quick reference)

| Pattern | Shapes… | Lead when the course/audience needs… |
|---|---|---|
| **concept-spine** | the mental-model backbone | model built before/around building; conceptual or non-dev courses |
| **challenge-ladder** | the build backbone | hands-on builders; one shipped artifact per rung |
| **overview-lab-challenge** | the default *lesson* template | read → guided → unguided |
| **completion-loop** | micro-lessons, faded worked examples | absolute beginners; lowest load |
| **build-it-twice** | abstraction-layered depth | "why the framework exists" — native↔Anchor |
| **security-epoch** | the late security tier | exploit→patch→fuzz/CTF; pre-mainnet |
| **map-from-known** | the audience-specific opener | strong adjacent priors (EVM→Solana) |
| **client-integration** | the off-chain/client side | dApp / mobile / frontend / SDK courses |
| **optimization-loop** | measure→optimize→re-measure | compute-unit / performance outcomes |
| **testing-thread** | testing as a thread, not a module | the acceptance gate on every build |

## Agents & commands
- `/create-content "<ask>"` — route the form and deliver the finished piece.
- `/architect-course "<brief>"` — the course pipeline end-to-end.
- `/validate-course --course content/courses/<id>` — the deterministic gate.
- agent `content-composer` — owns the non-course forms (route → brief → write →
  visual pass).
- agent `course-architect` — owns the course form (intake → emit → lesson writing).

## The one rule above all
**Route the form, design backward from a measurable outcome, ground every claim,
put the teaching inside something real (an artifact, a tour, an argument), name the
trade-off — then deliver finished text the reader can use, with visuals specified
but never overdone.** Educational content that is complete but unsequenced, or
polished but passive, fails the same way over-tidy prose does: it stops feeling
like a builder's path and starts feeling like a textbook.

See `three-layer-model.md` for how the layers compose, `forms/FORMS.md` for the
form router, `references/output-contract.md` for the course filesystem, and
`design-spine.md` for the non-negotiables.
