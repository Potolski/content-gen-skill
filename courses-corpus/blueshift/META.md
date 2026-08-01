# Blueshift — Curriculum Analysis (META)

> Pedagogical teardown for a course designer. How Blueshift decomposes, sequences, paces, and
> drills Solana learning — content and structure only. All claims grounded in files under
> `courses-corpus/blueshift/content/`.

---

## 1. Snapshot

- **Corpus location**: files analyzed under `courses-corpus/blueshift/content/` (mirror of the
  learn.blueshift.gg lesson content).
- **Delivery format**: Written MDX articles (prose + fenced code) rendered as web lessons.
  No video. Interactivity is narrow but real: an in-lesson widget
  (`AnchorDiscriminatorCalculator`, 5 uses) and, for challenges, a **compile-and-upload sandbox**
  plus a hosted **Blueshift Sandbox Environment** for the TypeScript challenge
  (`challenges/typescript-mint-an-spl-token/challenge.mdx` — "zero-config sandbox … built-in
  editor with type support, pre-packaged libraries, a wallet, and an RPC node").
- **Scale (verified counts)**:
  - **2 learning paths** (`paths.meta.ts`) — 15 h and 18 h of content estimated.
  - **28 course directories** / **174 lesson `.mdx`** (`find courses -name '*.mdx'` = 174).
    Note: `courses.meta.ts` lists only **27**; `quantum-vault/` (1 stub lesson) exists on disk
    but is unlisted.
  - **15 challenge directories** / **49 challenge `.mdx`**. `challenges.meta.ts` lists only
    **13**; `anchor-memo/` and `pinocchio-memo/` exist on disk but are unlisted (staged/hidden).
- **Topic scope**: blockchain first-principles → Solana account/program model → tokens & NFTs →
  program development in Anchor, native Rust/Pinocchio, and sBPF Assembly → security hardening,
  testing harnesses, and a client-side mobile/TS vertical (track counts in §2).
- **Target audience**: Split. Path 1 (`introduction-to-blockchain-and-solana`, difficulty 1) is
  for total newcomers; the program-dev courses (Anchor/Rust/Assembly) and the difficulty-2/3
  challenges target working developers moving toward native and performance-critical Solana.
- **Prerequisites**: None hard-enforced. Soft prereqs are stated inline — every challenge that
  needs one links back to a course (`grep -l /courses/ challenges/*/challenge.mdx` = 12/15).

---

## 2. Structural architecture

**Decomposition (3 primary containers, loosely coupled):**

```
paths (2)  ──chain──▶  courses (28)  ──lessons──▶  lesson.mdx (174)
                            │
challenges (15) ──pages──▶ sub-page.mdx (49)  ──verify──▶ apiPath (server grader)
```

Courses (theory/reference) and challenges (graded builds) are **sibling top-level trees**, not
nested. A path chains only courses; challenges are reached separately from a global
`/challenges` index (see `courses/anchor-for-dummies/conclusion.mdx` → "Head to the
[Challenges section](/en/challenges)").

**Ordering scheme — fully metadata-driven, no numeric filename prefixes.** Three TypeScript
manifests are the single source of truth; `.mdx` files carry **no YAML frontmatter** at all:

- `content/courses.meta.ts` — array order = course order; each course has `slug`, `language`,
  `difficulty`, `isFeatured`, and an ordered `lessons: [{slug}]` array. Wrapped in
  `withCourseNumber(...)`, i.e. display numbers are computed, not authored.
- `content/challenges.meta.ts` — each challenge has `unitName`, `apiPath`, `difficulty`,
  `requirements: [{instructionKey}]`, optional `pages: [{slug}]`, and `tags`.
- `content/paths.meta.ts` — each path is `steps: [{type:"course", slug}]` with `estimatedHours`.

**Module taxonomy — the real organizing axis is `language`/track, not topic.** Track counts from
`courses.meta.ts`: General 12, Mobile 5, Anchor 3, Rust 3, Typescript 3, Assembly 1. Courses are
color-coded per track (`BRAND_COLOURS.anchor`, `.rust`, `.assembly`, `.mobile`, …). The same
*topic* recurs across tracks deliberately (see §6, build-it-twice):
- SPL Token → `spl-token-with-web3js` (TS) **and** `spl-token-with-anchor` (Anchor).
- Token-2022 → `token-2022-with-web3js` **and** `token-2022-with-anchor` (identical 13-lesson
  extension list, different language).
- Vault / Escrow / Flash-loan → paired `anchor-*` and `pinocchio-*` challenges.

**Sequencing logic / prereq graph:**
- **Paths are the only explicit DAG.** `introduction-to-blockchain-and-solana`:
  blockchain-fundamentals → evolution-programmable-blockchains → understanding-solana →
  tokens-on-solana → nfts-on-solana (a strict conceptual dependency chain). `solana-mobile-mastery`:
  mobile-dapp-fundamentals → mwa-deep-dive → embedded-wallets → solana-mobile-client →
  dapp-store-publishing (rising difficulty 1→2).
- **Only 10 of 28 courses sit in a path**; the other ~18 (Anchor, Pinocchio, security, testing,
  Token-2022, introspection, Codama, Winternitz, secp256r1, assembly) are **standalone / à la
  carte** — an intentionally flat, reference-library topology.
- **Cross-links substitute for hard gating.** Prereqs are prose links, e.g.
  `challenges/pinocchio-vault/challenge.mdx` → "start by reading the Introduction to Pinocchio".

**Difficulty distribution:** courses 23×d1, 4×d2 (the four advanced mobile courses); challenges
3×d1, 8×d2, 2×d3 (`pinocchio-amm`, `assembly-slippage`). Difficulty lives in metadata, not in
sequence position — a d3 challenge and a d1 course coexist in the same flat index.

---

## 3. Lesson anatomy

A lesson is a single `.mdx` file. There is **no frontmatter block**; identity/order come from
`courses.meta.ts`. The recurring internal template (grounded in
`courses/anchor-for-dummies/anchor-101.mdx`, `courses/blockchain-fundamentals/digital-trust-problem.mdx`):

```
import { ArticleSection } from "…/components/ArticleSection/ArticleSection";
![<course banner alt text>](/graphics/course-banners/<course>.png)   ← first lesson only
# <H1 lesson title>
<intro paragraph — motivating hook, no heading>
<ArticleSection name="…" id="…" level="h2" />   ← anchor-linkable section marker
  <prose>  +  ```rust / ```bash / ```toml fenced code```
<ArticleSection … />  (repeat 2–6×)
…
<ArticleSection name="Conclusion" id="conclusion" level="h2" />   ← where applicable
```

- **Always present**: the `ArticleSection` import (189 occurrences across the corpus; it is the
  single sectioning primitive — a self-anchoring `<h2>` with `name`/`id`/`level`), an `# H1`
  title, expository prose, and inline fenced code.
- **Optional**: banner image (top of a course's first lesson only); interactive widgets — only
  `AnchorDiscriminatorCalculator` appears, imported in 5 lessons (e.g.
  `courses/anchor-for-dummies/conclusion.mdx`).
- **Dedicated `conclusion` lesson** ends most courses (24 of 28 course dirs contain
  `conclusion.mdx`). It follows a fixed shell: congratulation → "What You've Learned" bullets →
  "Next Steps" pointing at `/en/challenges` (`courses/anchor-for-dummies/conclusion.mdx`).
- **In-lesson dual-framework split**: many General-track lessons carry parallel
  `<ArticleSection name="Anchor">` and `<ArticleSection name="Pinocchio">` blocks showing the
  same fix twice (`courses/program-security/signer-checks.mdx` has exactly this — insecure
  Anchor code, three Anchor fixes, then the Pinocchio `is_signer()` equivalent).

**Challenge anatomy differs** (`challenges/<slug>/`):
```
challenge.mdx : banner → prereq course link → ## Installation (cargo/anchor init)
              → ## Template (skeleton to fill) → per-instruction ## sections (Deposit/Withdraw…)
              → ## Conclusion (cargo build-sbf / anchor build → "drop the .so file")
verify.mdx    : <ChallengeTitle> + <RequirementList> of <Requirement title="Challenge N: …">
pages/*.mdx   : (multi-instruction challenges only) one sub-page per instruction
                e.g. pinocchio-escrow/pages/{make,take,refund,conclusion}.mdx
```
Sub-page order is driven by the `pages: [{slug}]` array in `challenges.meta.ts`; `requirements:
[{instructionKey}]` names the instructions the server grader expects.

---

## 4. Content sequencing & pacing

- **Grain = one concept per `.mdx`.** The lesson is the atomic unit; a course is an ordered
  `lessons: [{slug}]` array; each lesson holds 2–6 `ArticleSection` blocks (§3). Chunking is
  fine-grained and single-topic — a lesson is sized to one sitting, a challenge to one build.
- **Content scale, not schedule.** The only size signal is per-path `estimatedHours` in
  `paths.meta.ts` — 15 h (`introduction-to-blockchain-and-solana`) and 18 h
  (`solana-mobile-mastery`). Individual courses/lessons carry **no** duration estimate; grain is
  set by concept boundaries, not time boxes.
- **Frontloaded mental models, then code.** Path 1 sequences three pure-concept courses
  (blockchain-fundamentals → evolution-programmable-blockchains → understanding-solana) *before*
  any program is written — the "concept-spine" (§6). Within `understanding-solana`, order is
  accounts→ownership→programs→transactions, each concept a prerequisite for the next.
- **Spaced reinforcement via build-it-twice.** The same topic (SPL Token, Token-2022, vault,
  escrow, flash-loan) recurs across the Anchor / native / TS tracks, so a concept is re-encountered
  in a new framing rather than taught once (§6, framework-mirror axis) — spiral reinforcement
  promoted to a catalog-level sort key.
- **Advisory ordering, not linear march.** The concept graph is soft: path order, prose
  cross-links, and difficulty tiers *suggest* a route, but ~18 of 28 courses sit outside any path
  as à-la-carte reference (§2). The catalog is navigable in any order — a reference-library
  topology, not a fixed progression.
- **Progression unit = a read course or a shipped, verified program.** Advancement is discretized
  by artifact, not by a clock: the learner reads reference courses, then completes a challenge by
  building and submitting a working program (`challenges/pinocchio-vault/challenge.mdx`: "You can
  now test your program against our unit tests … click on the `take challenge` button and drop the
  file there!").

---

## 5. Learning artifacts & practice

- **The core practice artifact is a real, buildable program.** Each challenge has the learner
  build locally (`cargo build-sbf` for Pinocchio, `anchor build` for Anchor), producing a `.so`,
  then submit it. The submission is executed against Blueshift's hidden unit tests keyed to
  `requirements[].instructionKey` (e.g. `deposit`+`withdraw`; escrow `make`+`take`+`refund`; AMM
  `initialize`+`deposit`+`withdraw`+`swap`), routed by `apiPath` in `challenges.meta.ts`
  (e.g. `/v1/verify/anchor/vault`, `/v1/verify/pinocchio/amm`). **The artifact itself is the
  exercise** — no MCQs/quizzes exist anywhere (`grep -riE 'quiz|mcq|Question'` on components = 0
  hits).
- **The on-chain verify step is a learning task.** "Take the challenge" = compile → upload → run
  against the hidden suite → iterate until green. It is a build-debug-ship loop, the work measured
  in a working binary rather than filled-in blanks.
- **Requirement checklist as visible spec.** `verify.mdx` renders `<RequirementList>` of
  `<Requirement title="Challenge N: …">` items — the human-readable contract the learner must
  satisfy (`challenges/pinocchio-escrow/verify.mdx` even pins exact discriminator values:
  "instruction discriminator value of `1`"). It doubles as the exercise's acceptance criteria.
- **TypeScript variant is an in-browser lab.** `typescript-mint-an-spl-token` is built and checked
  inside the hosted Blueshift Sandbox rather than via local `.so` upload — same requirement
  contract, different harness (editor + wallet + RPC in the page).
- **Courses carry no embedded exercises.** They are pure worked-example + reference; all practice
  is externalized to the challenge tree (§6, reference-then-arena). The three exposures
  (read → guided → unguided) are split across the course/challenge boundary rather than nested in
  a single lesson.

---

## 6. Pedagogical devices

Mapped to the house pattern vocabulary; new names coined where nothing fits.

- **build-it-twice — the load-bearing device, applied at three grains.** This is Blueshift's
  organizing spine, expressed through the `language` field:
  1. *Whole-challenge pairs*: `anchor-vault`↔`pinocchio-vault`, `anchor-escrow`↔`pinocchio-escrow`,
     `anchor-flash-loan`↔`pinocchio-flash-loan` — the identical DeFi artifact built high-level
     (Anchor) and native (Pinocchio) to expose what the macros hide.
  2. *Whole-course pairs*: `spl-token-with-web3js`↔`spl-token-with-anchor`;
     `token-2022-with-web3js`↔`token-2022-with-anchor` (same 13-lesson extension list, two SDKs).
  3. *In-lesson dual sections*: General-track lessons carry side-by-side Anchor and Pinocchio
     blocks (`program-security/signer-checks.mdx`; also `secp256r1-on-solana`,
     `instruction-introspection`, `winternitz-signatures-on-solana` each with
     `*-with-anchor` + `*-with-pinocchio` lessons). **New name: "framework-mirror axis"** — the
     dual-track is promoted from a one-off technique to the catalog's primary sort key.

- **challenge-ladder.** The 15 challenges form escalating self-contained builds on a shared
  vault→escrow→flash-loan→AMM progression (`difficulty` 1→3), each isolating one new mechanism
  (PDA/CPI → two-party swap+ATA → introspection/atomicity → constant-product math + slippage).
  Assembly track adds a parallel rung set (memo → timeout → slippage).

- **security-epoch.** `program-security` (11 lessons) is a distinct hardening tier taught
  **offense→defense**: each lesson shows vulnerable code, narrates the exploit, then patches it
  (`signer-checks.mdx`: "At first glance, this looks secure … there's a fatal flaw" → attacker
  walkthrough → three fixes). Vulnerability classes: signer/owner/data-matching, duplicate-mutable,
  reinitialization, revival, arbitrary-CPI, type-cosplay, PDA-sharing.

- **concept-spine.** Path 1's first three courses are a dependency-ordered mental-model backbone
  built *before* any code, anchored with real facts (`digital-trust-problem.mdx`: DigiCash,
  E-gold, Liberty Reserve, Cyprus 2013 deposit seizure, Equifax 147 M breach). `understanding-solana`
  orders accounts→ownership→programs→transactions.

- **map-from-known.** `evolution-programmable-blockchains` routes Ethereum→Solana;
  `understanding-solana/why-solana-built` leads with the prior model before the alien parts.

- **client-integration.** The Mobile path + TS track own the off-chain half: wallet connect,
  MWA transport/session/encryption (`mwa-deep-dive`), RPC + Blinks (`solana-mobile-client`),
  Solana Pay transfer/transaction requests, and Codama IDL→SDK generation.

- **worked-example → challenge (fading across the course/challenge boundary).** Rather than the
  house **overview-lab-challenge** (read→guided→unguided *inside one lesson*), Blueshift **splits
  the three exposures across two trees**: courses = worked examples + reference; challenges =
  the unguided build. **New name: "reference-then-arena"** — theory is a stable library, practice
  is a separate graded arena, joined only by prose cross-links. The `challenge.mdx` itself then
  re-supplies a guided middle rung (Installation + Template + per-instruction walkthrough) before
  the fully-blank upload, so fading happens *within* the challenge, not the lesson.

- **compile-and-submit autograder (new name).** Practice is a locally-compiled `.so` verified by a
  hidden server test-suite keyed to declared `instructionKey`s — a completion loop measured in
  shipped binaries, not filled blanks.

---

## 7. Scaffolding & tooling

- **Local-first dev env** for program challenges. The challenge itself is the setup guide:
  `anchor init blueshift_anchor_vault` (Anchor) or `cargo new … --lib` + `cargo add pinocchio
  pinocchio-system` + `crate-type = ["lib","cdylib"]` (Pinocchio). No Docker/devcontainer; assumes
  Rust/Anchor toolchain installed (links to anchor-lang.com/docs/installation).
- **Starter templates inline, not repos.** Each `challenge.mdx` embeds a `## Template` code block
  (skeleton `lib.rs` with stubbed instructions) rather than shipping a git starter. The fixed
  placeholder program ID `2222…2222` is mandated so the hidden test harness can substitute it
  ("we use this under the hood to test your program").
- **A whole testing sub-curriculum** (not used to grade, but taught): `testing-with-mollusk`
  (Rust/Mollusk), `testing-with-litesvm` (TS + Rust), `testing-with-surfpool` (mainnet-fork).
  These teach the harnesses; the challenge grader is a separate hidden suite behind `apiPath`.
- **In-browser only for TS**: the Blueshift Sandbox (editor + wallet + RPC) hosts
  `typescript-mint-an-spl-token`. Everything else is build-locally-then-upload.
- **Autograder** = the `/v1/verify/...` endpoints; opaque to the learner (pass/fail against the
  `RequirementList`). No self-run test files ship with challenges.

---

## 8. Voice & framing

- **Register**: confident, plain-spoken, second-person, lightly playful ("for-dummies", "own every
  byte of your code"). Concept courses open with a concrete human stakes hook before any tech —
  Alice double-spends a coin on Bob and Carol before "blockchain" is defined.
- **Motivation devices**: real-world failure anecdotes as fact-anchors (bank seizures, data
  breaches); explicit "why this abstraction exists" framing; a shipped, test-passing program as the
  finish-line payoff ("test your program against our unit tests").
- **Concept introduction**: problem-first, then mechanism. Native/Pinocchio courses sell the
  *why-go-lower* case up front (fewer CU, smaller binary, zero dependency drag) before syntax.
- Illustrative voice (one line): *"Native development might sound daunting, but … by the end you'll
  understand every byte that crosses the program boundary."* (`pinocchio-for-dummies/pinocchio-101.mdx`)

---

## 9. Distinctive signatures

- **Track (`language`) is the primary axis, topic is secondary.** Most catalogs sort by topic;
  Blueshift deliberately teaches the *same* topic across Anchor/Rust/TS/Assembly so the framework
  becomes the variable under study — build-it-twice as a catalog-level architecture, not a lesson
  trick.
- **Hard course↔challenge separation.** Courses are pure, ungraded reference; challenges are a
  wholly separate graded tree with their own metadata schema (`apiPath`, `requirements`, `pages`).
  Joined only by prose links. Few corpora fully decouple explain-vs-practice.
- **Practice = compile a real on-chain program + upload `.so`.** Not code-in-browser blanks —
  an actual deployable artifact executed against hidden tests. High authenticity ceiling.
- **Metadata-as-source-of-truth with zero frontmatter.** Ordering, difficulty, tracks, sub-pages,
  grader routing all live in three `.meta.ts` files; `.mdx` is pure content. Clean CMS separation —
  and it drifts (28 dirs vs 27 listed; 15 challenge dirs vs 13 listed) revealing staging via
  manifest edits rather than file deletion.
- **Exotic frontier tracks** most beginner corpora omit: sBPF **Assembly** (write/verify raw
  assembly programs), **Winternitz** and **secp256r1** (post-quantum / passkey signatures),
  **instruction introspection**, **Codama** SDK generation.
- **Deep specialist mobile path** (MWA transport/session/encryption internals, embedded-wallet
  MPC/passkeys, dApp Store publishing) — a full client-side vertical rare in program-first courses.

---

## 10. Takeaways for a course designer

- **Steal: make the framework a variable, not a constant.** Building one artifact twice (Anchor↔
  Pinocchio, web3.js↔Anchor) is the single highest-leverage device here — it turns "what does the
  macro do?" from a question into something the learner *sees*. Promote it to an organizing axis
  when your domain has a low-level/high-level pair.
- **Steal: externalize all ordering/difficulty/routing into a manifest, keep content
  frontmatter-free.** `courses.meta.ts` / `challenges.meta.ts` / `paths.meta.ts` make re-sequencing,
  re-tiering, and grader wiring a data edit — and let you stage/hide units without touching files.
- **Steal: assess by shipping a real artifact + declared requirement checklist.** `requirements:
  [{instructionKey}]` + a visible `<RequirementList>` gives an unambiguous spec the autograder and
  the learner share — the exercise's acceptance criteria are visible up front.
- **Steal: decouple reference (courses) from arena (challenges), then bridge with cross-links.**
  Lets theory be a stable library reused across many builds, and lets the same concept be practiced
  at multiple difficulties without duplicating exposition.
- **Steal: hook concepts with real-world failure facts before defining terms.** Alice's
  double-spend / Cyprus / Equifax do more motivational work than an abstract definition.
- **Avoid / mind the gaps: no in-lesson pacing, no enforced sequencing, no in-lesson exercises.** A
  total beginner gets a reference library and a separate practice arena with nothing scaffolding the
  path between them — great for self-directed devs, thin for learners who need scaffolding and
  momentum. Add per-lesson checks or a guided lab tier if your audience is greener.
- **Avoid: local-toolchain-required challenges as the default.** Only the TS challenge is
  zero-config in-browser; every program challenge assumes a working Rust/Anchor install, a real
  onboarding cliff. Budget an in-browser build path if reach matters.
- **When this model fits**: a reference-plus-practice catalog for **already-technical** learners
  across many parallel tracks, where authentic artifacts (deployable programs) are the point and
  self-direction is assumed. It fits a broad reference library far better than a hand-held,
  heavily-scaffolded guided course.
