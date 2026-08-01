# PATTERNS — Cross-Course Synthesis (7 Solana Courses)

> A teacher-facing comparative teardown of the corpus, analyzing **course CONTENT and STRUCTURE
> only** — what is taught, in what order, how it is chunked, how a lesson is built, how concepts
> progress, and what practice/artifacts are embedded. Read this to decide *how to shape* a new
> Solana course: how to sequence it, pace it, and embed practice in it. Every claim is grounded in
> the seven `META.md` files (Blueshift, Solana Foundation, Cyfrin Updraft, freeCodeCamp, Ackee,
> RareSkills, Risein). Courses are referenced by name throughout.

---

## The 7 courses at a glance

| Course | Format | Scale | Audience | Ordering | Content cadence & grain | Practice & artifacts |
|---|---|---|---|---|---|---|
| **Blueshift** | Written MDX + compile-and-upload autograder (no video) | 28 courses / 174 lessons; 15 challenges / 49 mdx; 2 paths (est. 15h+18h of content) | Split: total newcomers (Path 1) **and** working devs going native/perf | Metadata-driven (`courses.meta.ts`), no filename numbers, no frontmatter; track (`language`) is primary axis | One concept per `.mdx` (lesson = one sitting, challenge = one build); frontloaded concept-spine → code; spiral reinforcement via build-it-twice across tracks | Compile a real deployable `.so` + upload → hidden server tests keyed to `instructionKey`; visible `RequirementList` spec; on-chain verify = build-debug-ship loop |
| **Solana Foundation** | Written, local-first Markdown/MDX (no video, no autograder) | 12 courses / 63 lessons / 51 challenges / 60 labs; ~52k lines | Devs who can already code (JS/TS assumed, Rust inline); ramps to intermediate | Single `priority` integer per course + per-course `lessons:` array = implicit DAG | Grain = the lesson (theory + numbered Lab + Challenge, one sitting); read→code-along→solo fade inside each lesson; spiral artifacts (Movie Review/Student Intro) across 11+ lessons | Code-along labs (`anchor test`, run-and-compare) + spec challenges w/ solution-as-reference; self-audit challenge in security course |
| **Cyfrin Updraft** | Video-first + written `+page.md` companion; local CLI | 9 modules / 48 md (31 real); 6 dual-track projects; 4 CTF | Aspiring devs, Rust practitioners, **auditors**; EVM "highly recommended" | Strict numeric dir prefixes; no sidecar metadata; sequence in folder names | Strictly linear, prerequisite-ordered; pace set by artifact difficulty (hello = 0 tasks → amm = 4 instructions) + scaffold fade, not clock | Proof-escalation ladder: LiteSVM → localnet+script → Devnet; CTF proof-by-exploit; quiz slots empty stubs |
| **freeCodeCamp** | Interactive in-browser (dev-container, real validator/Phantom) | 15 projects (10 learn + 5 build); **528 graded steps**; 1,576 hidden JS assertions | Early-intermediate devs w/ basic Rust+JS; no Solana assumed | Strict integer step order, mastery-gated; cross-project via README table | Grain emergent from step count (528 micro-steps + 5 builds); mastery-gate *is* the pace; 4 learn-pair→build epochs + ship coda | Live on-chain RPC verify + AST (Babeliser) + terminal/FS asserts + `cargo test`; a few `done` honor-gates |
| **Ackee** | Mixed: video-led + written Handbook + code tasks | 7 lecture-units + 3 bonus; 5 Tasks + capstone; Handbook = 4 ch + 2 appendices (~40pp) | Programmers new to Rust/Solana; leans **auditor** | Numbered dirs + single `\|Lecture\|Task\|` grid; Handbook ordered separately (MkDocs) | Grain = the lecture-unit; lockstep read/watch → run example → ship Task, one unit per sitting; written depth front-loaded (lessons 2-5 heavy, 1/6/7 thin); Handbook as parallel/spaced prep | 5 hands-on Tasks (one per unit) + integrative capstone program; `anchor test` on example repos; adversarial PoC exploit lab (lesson 7) + Trident fuzzing bonus |
| **RareSkills** | Written long-form blog (no video, no IDE, no grader) | 8 modules / 62 lessons ("60 Days" = cadence frame); practice embedded per-lesson | Engineers w/ **beginner-intermediate EVM/Solidity**; NOT absolute beginners | Human-curated editorial numbering; no machine metadata; prose back-links | Lesson = one self-contained sitting; linear-by-prose; difficulty-inversion pacing (EVM-1:1 wins frontloaded before the alien account model); uneven sizing (M4 accounts = 18 lessons) tracks cognitive load | Embedded "try this yourself" + end-of-lesson build challenges + `solana account` inspection as verify task; native rebuild (M7) & sBPF (M8) as terminal practice |
| **Risein** | Video (hosted LMS) | 1 course / 5 sections / 22 lessons; 3 guided builds + 1 capstone; ~6h (352 min) | Newcomers who learn by building; no prior Solana; no EVM framing | Numbered, linear, single-track; section number IS the order metadata | Uniform ~16-min lesson beat (every section = lessons × 16); one lesson = one sitting; concepts front-loaded (Section 01) then applied; scaffold fade across the arc | 3 guided code-along builds (Counter → Token Transfer → Restaurant Review) as worked examples + 1 freeform capstone; deploy/run as demonstrative check; no autograder |

**Fast reads from the table.** Formats split 3 written (Blueshift, Solana Foundation, RareSkills) /
2 video (Cyfrin, Risein — Cyfrin has a written companion) / 1 interactive-autograded (freeCodeCamp)
/ 1 mixed video-plus-handbook (Ackee). Only **two** courses mechanically grade the learner's work
(freeCodeCamp's 1,576 assertions, Blueshift's server autograder); the other five self-check by
running code and comparing output. Every course embeds *artifact-based* practice
(build / deploy / exploit / inspect) and **none** uses MCQ quizzes for real. Content grain spans two
orders of magnitude — Risein's single 22-lesson course vs Blueshift's 174 lessons + 49 challenge
pages.

---

## Axes of variation

### Format: written vs video vs interactive-autograded

- **Written, read-and-do:** Solana Foundation (local-first Markdown), RareSkills (long-form blog).
  Learner reads prose, copies code locally, self-checks. RareSkills has *no* interactivity at all;
  Solana Foundation is a pure read-lab-challenge shell.
- **Written + real autograder:** Blueshift (MDX reference + compile-and-upload `.so` verifier) and
  freeCodeCamp (in-browser dev-container, 528 mastery-gated steps). These are the only two that
  mechanically verify. freeCodeCamp is the purest "interactive" course — a real terminal, real local
  validator, real Phantom, real devnet/mainnet.
- **Video-first:** Risein (pure hosted video), Cyfrin Updraft (video + written `+page.md`
  transcript/companion; the markdown is deliberately incomplete without the video and the external
  monorepo).
- **Mixed:** Ackee — recorded video lectures + an evergreen written Handbook + submodule code repos.
  The corpus captures only the written substrate; the "real payload" is video.

**Designer read:** format dictates *where practice gets checked*. Video courses (Risein, Cyfrin)
can't auto-check inside a lesson, so the checking rung gets hoisted to a capstone (Risein) or an
out-of-band test suite you run yourself (Cyfrin). Interactive courses (freeCodeCamp) can gate every
step. Written self-run courses (RareSkills, Solana Foundation) embed no automated check at all — the
worked example + solution diff is the answer key.

### Sequencing philosophy: concept-first vs project-first vs map-from-known

- **Concept-first (spine before build):** Ackee (the whole Solana Handbook is a dependency-ordered
  concept-spine, read *before* the weekly build), Risein (Section 01 is a 6-lesson mental-model
  primer before any Counter code), Cyfrin (module 2 `2-core-concepts` walks accounts→programs→pda→cpi→idl
  before module 3's first program). Blueshift's Path 1 is a pure conceptual backbone
  (`digital-trust-problem` etc.) with zero code.
- **Project-first / just-in-time concepts:** freeCodeCamp (no upfront concept module at all —
  concepts arrive as `<dfn>` tooltips *inside* build steps; the explicit bet is "momentum over
  model"), Solana Foundation (mostly build-driven with thin concept lessons).
- **Map-from-known (order by prior-model mapping strength):** RareSkills is the corpus exemplar and
  the pattern's source-of-record — it **deliberately inverts** the Solana prerequisite DAG,
  frontloading EVM-1:1 topics (compute units ≈ gas, `msg.sender`, custom errors) in Module 3 *before*
  the alien account model in Module 4, to bank early wins. Cyfrin also uses map-from-known (a 5-axis
  EVM↔Solana lesson) but keeps the DAG intact. Blueshift's `evolution-programmable-blockchains`
  routes Ethereum→Solana. Solana Foundation maps to **web2** priors instead ("instruction handler ≈
  HTTP route handler") because its audience isn't EVM devs. Risein and Ackee do essentially no
  cross-chain mapping.

**A sharp sub-axis — fundamentals ordering.** Two courses invert the Solana-docs bottom-up canon
(Accounts→Programs→Instructions→Transactions→PDAs): **Risein goes top-down**
(Transactions→Instructions→Accounts→PDAs — start from what a user submits, decompose downward), and
**RareSkills macro-inverts** by EVM-mapping strength. Cyfrin, Ackee, and Blueshift keep the bottom-up
account-first spine. This is a real fork in the road — pick it deliberately.

### Content cadence & grain: concept-boundary / even-time-grain / gate-as-pace / difficulty-ramp / lecture-unit

- **Concept-boundary grain (chunk set by concepts, not time):** Solana Foundation (the lesson —
  theory + numbered Lab + Challenge — is the unit; no sub-lesson checkpoints), RareSkills (each
  lesson a self-contained worked-example essay), Blueshift (one concept per `.mdx`; the only size
  signal is per-path `estimatedHours`). Chunking follows concept boundaries, not a clock.
- **Even-time grain:** Risein normalizes *every* lesson to a ~16-min beat — the sharp finding is each
  section's budget is literally `lessons × 16` (every section divides to exactly 16.0). The cadence
  unit is the lesson-sitting, not the module; content is cut so one lesson ≈ one short study block.
- **Gate-as-pace:** freeCodeCamp has no clock but the mastery gate *is* the pacing mechanism — you
  cannot advance until the current step's hidden tests pass. Pace is emergent from ~528 steps
  (read one idea → do one thing → run → pass → advance).
- **Difficulty-ramp-as-pace:** Cyfrin paces by artifact scope (hello = 0 tasks → amm = 4
  instructions) and scaffold fade, not by clock.
- **Lecture-unit grain:** Ackee groups content into 7 sequential lecture-units, each pairing one
  lecture (video + README + Handbook chapter(s) + code-example repo) with one Task, meant to be taken
  one unit per sitting — a lockstep *read/watch → run example → ship Task* rhythm, with written depth
  front-loaded into the middle units. ("N-days" branding appears only in **RareSkills** — "60 Days" —
  and is explicitly a cadence motif, not enforced: 62 lessons don't map 1:1 to 60.)

### Practice & assessment: on-chain verify / autograded tests / embedded exercises / capstone

- **On-chain / live-ledger verify (as a learning task):** freeCodeCamp (13/15 files assert real
  validator state — deployed + `executable===true`, correct owner/authority, tx counts; the arc
  reaches a real **mainnet** deploy), Blueshift (uploaded `.so` run against hidden server tests),
  Cyfrin (proof-escalation: LiteSVM → localnet+demo script → Devnet Explorer).
- **Autograded tests:** freeCodeCamp (1,576 hidden JS assertions incl. AST via Babeliser), Blueshift
  (server verifier keyed to `requirements[].instructionKey`). The only two that mechanically grade.
- **Distributed per-unit exercises → capstone:** Ackee (5 hands-on Tasks, one per lecture-unit,
  converging on an integrative capstone program), freeCodeCamp (learn-pair → freeform `build-*` each
  epoch). Practice is distributed to build momentum, then synthesized in one integrative build.
- **Capstone / terminal solo build:** Ackee (final program), Risein ("Build Your Final Project"),
  freeCodeCamp (freeform `build-*` × 5 + ship-anything capstone), Cyfrin (the AMM/CPI rungs function
  as capstones). Solana Foundation and RareSkills have no single capstone (spiral artifacts /
  per-lesson challenges instead).
- **Embedded per-lesson exercises (self-verified):** RareSkills ("try this yourself" + build
  challenges + `solana account` inspection), Solana Foundation (run-and-compare labs + solution-diff
  challenges + self-audit challenge). The exercise ships inside the lesson; the worked example is the
  answer key.
- **Quizzes / MCQs:** effectively **none in the corpus**. Cyfrin has per-module quiz *stubs* (empty
  `---` bytes — a platform component, not authored content). No course grades a real MCQ — a striking
  corpus-wide absence, and the right instinct for a programming course.

### Framework stance: Anchor-first / native-first / dual-track / assembly-depth

- **Dual-track (build-it-twice) as architecture:** Blueshift (track/`language` is the *primary catalog
  axis* — same artifact built Anchor↔Pinocchio, web3.js↔Anchor, even in-lesson dual sections) and
  Cyfrin (native + Anchor on **all 6** build rungs, justified to serve auditors). These two make the
  framework the variable under study.
- **Anchor-first, then strip to native:** Solana Foundation (Anchor at priority 15 taught *before*
  native Rust at 50; native rebuilds the same Movie Review app — a two-course build-it-twice),
  RareSkills (Anchor throughout M1-6, then Module 7 rebuilds primitives native).
- **Module-level build-it-twice:** freeCodeCamp (native `solana_program` projects 1-3, then Anchor
  projects 7-9, explicitly narrated).
- **Assembly-depth ceiling:** RareSkills Module 8 (hand-written sBPF assembly) and Blueshift's
  Assembly track are the only two that descend to raw VM. RareSkills reaches Anchor → native →
  assembly, the deepest floor in the corpus.
- **Single abstraction level (framework left implicit):** Risein (outline never even names Anchor vs
  native — a gap), Ackee (Anchor-first with a Pinocchio bonus stub).

### Audience entry point: total beginner / EVM-transfer / already-coder

- **Total beginner (no code assumed beyond basics):** Risein (opens on "Solana introduction"),
  Blueshift Path 1, Solana Foundation (opens on "What is web3?").
- **Already-a-coder, new to Solana:** Solana Foundation (JS/TS assumed), freeCodeCamp (basic Rust+JS
  assumed), Ackee (any prior language), Cyfrin (Rust required).
- **EVM-transfer (prior model required):** RareSkills is exclusionary by design — near-useless to an
  absolute beginner and openly says so; Solidity is the real gate. Cyfrin makes EVM "highly
  recommended" to power its map-from-known.

---

## Recurring patterns (the reusable playbook)

Cross-cutting techniques that appear in 2+ courses, mapped to the house vocabulary
(build-it-twice, challenge-ladder, client-integration, completion-loop, concept-spine,
map-from-known, overview-lab-challenge, security-epoch). Candidate NEW patterns are flagged.

### build-it-twice — *the corpus's most universal device (5 of 7 courses)*
**What:** teach the same artifact/primitive at two abstraction levels (native↔Anchor, web3.js↔Anchor)
so the framework's magic becomes visible by contrast.
**Who:** Blueshift (promoted to the primary catalog axis — three grains: whole-challenge pairs,
whole-course pairs, in-lesson dual sections), Cyfrin (all 6 rungs, for auditors), freeCodeCamp
(module-level, projects 1-3 native then 7-9 Anchor), Solana Foundation (two-course, Anchor then
native rebuild of Movie Review), RareSkills (sequential — Anchor throughout, one late "strip to
native" module).
**When to use:** when your outcome is "understand what the framework hides" (auditing, deep
understanding). **Scope it:** the house guidance is twice-build only 1-2 artifacts; Cyfrin's
all-6-rungs bet is expensive and beginner-hostile. RareSkills' *sequential* variant (one late native
module) gets ~80% of the payoff at ~1× cost — steal that shape for most courses.

### concept-spine — *dependency-ordered mental model (5 of 7)*
**What:** a backbone of concepts taught in prerequisite order (accounts→programs→PDAs→CPIs) before or
alongside builds.
**Who:** Ackee (the Solana Handbook is a textbook-grade spine with its own DAG), Cyfrin (module 2),
Risein (Section 01, but top-down), Blueshift (Path 1 conceptual courses), Solana Foundation (the two
intro lessons). **Deliberately absent** in freeCodeCamp (just-in-time `<dfn>` tooltips instead —
momentum over model).
**When to use:** when the domain has genuinely alien primitives (Solana accounts qualify) and your
audience will otherwise cargo-cult. Skip it (freeCodeCamp-style) only if your grader can back-fill
understanding via contrast and you're optimizing for onboarding speed.

### security-epoch — *late, offense-first hardening tier (4 of 7)*
**What:** a distinct late module taught offense→defense (insecure code → exploit → patch → re-test),
gated behind build fluency.
**Who:** Blueshift (`program-security`, 11 lessons), Solana Foundation (`program-security`, priority
70, modeled on Coral's Sealevel Attacks — but *no* fuzzing/CTF), Cyfrin (module 9 CTF where you
**write the exploit** — "your exploit is successful if the test passes"), Ackee (lesson 7 +
adversarial PoC repo + Trident fuzzing bonus). RareSkills and Risein have no security tier at all.
**When to use:** always, if the outcome is "ship to mainnet." Concentrate it late, don't sprinkle it.
The strongest instances (Cyfrin, Ackee) assess with adversarial artifacts (write an exploit / run a
PoC), not quizzes.

### overview-lab-challenge — *read → guided → solo fade (5 of 7, at varying grain)*
**What:** three exposures at rising autonomy — worked example, code-along lab, independent build.
**Who:** Solana Foundation names it almost verbatim in `getting-started.md` (per-lesson: Overview
"don't code along" / Lab "absolutely code along" / Challenge "do it alone"). freeCodeCamp runs it at
*macro* grain (2 guided courses = lab, `build-*` = challenge). Ackee runs it at *lecture-unit* grain
(read Handbook → run example → ship Task). Risein hoists the Challenge rung to a single capstone.
Cyfrin's middle "lab" rung is thin (outsourced to video + hint snippets).
**When to use:** the default worked-example schedule for almost any skill course. Decide the *grain*
deliberately: per-lesson (Solana Foundation) for fine control, per-epoch (freeCodeCamp) for transfer,
capstone-only (Risein) only if you accept no interim proof.

### challenge-ladder — *escalating self-contained artifacts (5 of 7)*
**What:** a rung sequence of shippable builds, each isolating one new mechanism, scaffold fading
across rungs.
**Who:** Blueshift (vault→escrow→flash-loan→AMM, difficulty 1→3), Cyfrin
(hello→oracle→piggy→auction→amm→cpi on a shared monorepo), freeCodeCamp (5 freeform `build-*` rungs),
Risein (Counter→Token Transfer→Restaurant Review→capstone — a *softened, guided-build* variant),
Solana Foundation (per-lesson challenges, weaker as a ladder).
**When to use:** the spine of any build-oriented course. The canonical rung-1/2/3 artifacts recur
across the whole corpus (account-state → SPL token → PDA app). Give the hardest rung a *relatable*
domain artifact — Risein's "Restaurant Review" teaches the same PDA/per-user-state primitives as a
vault but is far more memorable.

### client-integration — *wire a user to a program (4 of 7)*
**What:** a sub-track covering the off-chain half — IDL-typed clients, wallet-adapter, RPC, sign
flows.
**Who:** freeCodeCamp (projects 2/10/11/12 — a textbook wallet-adapter arc ending in real Phantom
signing), Solana Foundation (`*-frontend` lesson series + mobile course), Blueshift (Mobile path + TS
track; MWA internals, Solana Pay, Codama), Ackee (lesson 6: `create-solana-dapp` + Codama). Cyfrin,
RareSkills, Risein largely skip the frontend.
**When to use:** when the outcome includes a usable dApp, not just a deployed program. Note it's the
most-*skipped* half — program-first courses (Cyfrin, RareSkills) treat it as out of scope.

### map-from-known — *bridge from a prior model (4 of 7)*
**What:** teach the new system as a translation of what the learner already knows.
**Who:** RareSkills (source-of-record; EVM→Solana as the entire framing overlay, incl. **false-friend
lessons** on EVM features that don't exist), Cyfrin (5-axis EVM↔Solana), Blueshift (Ethereum→Solana),
Solana Foundation (web2-flavored: HTTP-route-handler ≈ instruction handler). Risein and Ackee skip
it.
**When to use:** only when a strong shared prior exists and is a real prereq (gate on it, as
RareSkills/Cyfrin do). Forcing EVM analogies on true beginners *misleads* them — Solana Foundation
correctly maps to web2 instead because its audience isn't EVM devs.

### completion-loop — *tiny auto-checked steps (1 of 7 — but definitional there)*
**What:** many micro-chapters, each one idea + a near-complete seed + one blank to fill, instantly
auto-checked and mastery-gated.
**Who:** **freeCodeCamp only** — but it carries 528 of ~533 steps. The `--seed --force` block *is*
the "pre-seeded near-complete code" primitive.
**When to use:** the lowest-cognitive-load on-ramp for CLI/syntax/framework-macro onboarding.
Requires a real autograder — it's why only the interactive course can do it.

### Candidate NEW patterns the corpus reveals

- **reference-then-arena (Blueshift).** Hard-decouple explain (ungraded courses = a stable library)
  from prove (a separate graded challenge tree with its own metadata schema), joined only by prose
  cross-links. Lets one theory lesson be reused across many builds and staged/hidden via manifest
  edits. *Use when* you want a forkable reference library plus authentic proof for self-directed
  learners.
- **companion-textbook split / dual-medium spine (Ackee).** Put durable "why" in an evergreen
  versioned book (own DAG, diagrams) and disposable "how" in dated lesson notes that churn with the
  toolchain. *Use when* your framework churns fast (Anchor versions) but concepts don't — the book
  survives, the notes get rewritten each season.
- **proof-escalation ladder (Cyfrin, freeCodeCamp).** Graduate authenticity within a single exercise:
  LiteSVM unit test → localnet + demo script → Devnet/mainnet deploy. Bake `solana program close`
  (rent reclaim) in as hygiene. *Use when* you want a real "it's on-chain" moment cheaply.
- **proof-by-exploit / offense-first capstone (Cyfrin, Ackee).** Invert the green-test convention — a
  passing test means *you broke the program*. Learners write exploits, not patches. *Use when*
  training an auditor persona; gate behind build fluency.
- **grade-the-chain + deliberate-failure (freeCodeCamp).** Assert on live validator state
  (unfakeable) and *assign* commands that fail, grading the error string (airdrop rate-limit,
  insufficient funds) to build error-literacy. *Use when* authentic proof beats speed.
- **force-seed checkpoint (freeCodeCamp).** Overwrite the learner's file with a canonical checkpoint —
  dual purpose: divergence airbag (a mistake in step 12 doesn't brick step 40) *and* noise injection
  (hand over boilerplate so a step isolates one concept). *Use when* your grader is stateful across
  steps.
- **adversarial-AI / "verify-and-fix" loop (Cyfrin).** Name a doctrine that treats the LLM as an
  unreliable pair-programmer whose hallucinations you fix against docs — "the actual learning occurs
  in step 4." *Use to* convert inevitable LLM use into debugging practice.
- **even-grain lesson beat (Risein).** Normalize every lesson to a constant ~16-min budget as the
  pacing spine ("one lesson = one evening slot"). *Use when* self-paced planning matters — but
  actually *measure/cut* to the grain, don't back-compute a round number like Risein did.
- **self-audit capstone (Solana Foundation).** Re-point the assessment at the learner's *own* prior
  programs ("audit your earlier code for this vuln class"). *Use as* a near-free, portfolio-anchored
  authentic assessment.
- **question-titled lessons (RareSkills).** Title each lesson as the learner's own question ("PDA vs
  Keypair account", "why they don't exist") — doubles as SEO surface and a built-in map-from-known
  hook. *Use for* free top-of-funnel reference content.

---

## Lesson-anatomy templates compared

Three genuinely distinct lesson skeletons dominate the corpus. Pick by format and practice model.

### A. Solana Foundation — theory + numbered lab + thin challenge *(written, self-paced, self-run)*
```
--- frontmatter: title + objectives[] (1-4 Bloom verbs) + description ---
## Summary            (bulleted TL;DR, ALWAYS present)
## Lesson OR Overview (theory: prose + diagrams + code; read-only; 43 use "Lesson", 18 "Overview")
## Lab                (numbered code-along: ### 1. Starter → ### 2. … → anchor test)
## Challenge          (independent build, spec-only, solution linked as reference-not-crutch)
<Callout "Completed the lab?">  (end-of-lesson reflect-and-report beat)
```
**Fits:** a written, local-first course prioritizing a copyable template + breadth. The uniform shell
replicated across 60 lessons is its strength (though the Lesson/Overview split is avoidable drift).
Cyfrin uses a *split* variant of this: two distinct lesson *types* — read-only **concept lessons**
(thesis → field-by-field mechanism → Alice/Bob values → recap) cleanly separated from **exercise
READMEs** (spec → linked TODO tasks → hint-snippets → tiered proof). Keep concept and build in
different lesson types, not mashed together.

### B. freeCodeCamp — step + hidden test *(interactive, autograded, mastery-gated)*
```
## N                    (bare integer heading = one step)
### --description--     (ALWAYS: one idea + a command/blank to fill; <dfn> tooltips; tables)
### --tests--           (ALWAYS: 1..k human labels, each + a hidden ```js chai/__helpers assertion)
[### --seed--]          (OPTIONAL: #### --force-- overwrites file with canonical contents)
[### --before-all-- / --after-all--]  (OPTIONAL: load file into globals / cleanup)
## --fcc-end--          (terminal sentinel)
```
**Fits:** onboarding to CLI/syntax/framework macros where instant auto-check and mastery gating
matter. The atomic grain (one idea + near-complete seed + one blank) is the lowest-cognitive-load
on-ramp in the corpus, but demands a real autograder (1,576 hidden assertions here). Note `--hints--`
is *never* used — guidance lives entirely in the description.

### C. Blueshift — course lesson vs challenge (reference-then-arena) *(written + server autograder)*
```
COURSE lesson (ungraded reference):
  <ArticleSection> import → banner (first lesson only) → # H1 → intro hook (no heading)
  → <ArticleSection h2> wrapping prose + fenced code (×2-6) → optional dual Anchor|Pinocchio
  → optional widget (AnchorDiscriminatorCalculator) → Conclusion: What You've Learned + Next Steps → /challenges
CHALLENGE (graded arena, separate tree):
  challenge.mdx: banner → prereq course link → ## Installation → ## Template (skeleton)
  → per-instruction ## sections → ## Conclusion (build .so → "drop the file")
  verify.mdx: <RequirementList> of <Requirement> (human-readable grader spec; pins discriminators)
  pages/*.mdx: one sub-page per instruction (multi-instruction challenges)
```
**Fits:** an open reference library for already-technical, self-directed learners, where the same
concept is practiced at multiple difficulties without duplicating exposition. The three exposures
(worked example / guided middle / blank build) are split *across two trees* rather than nested in one
lesson — theory is a stable library, practice is a graded arena.

**When each fits, in one line:** Template A for a copyable written course with local practice;
Template B for interactive onboarding with real gating; Template C for a decoupled
reference-plus-arena catalog. Video courses (Risein, Cyfrin, Ackee) don't have a fully-observable
per-lesson written template — their real unit is the section / lecture-unit, and the written layer is
a companion (Cyfrin) or cheatsheet (Ackee) that is dead weight without the video.

---

## Practice & assessment spectrum

Ranked lightest (least embedded verification) → heaviest (most unfakeable). This ranks how much
*practice and checking* each course bakes into the content.

1. **RareSkills — none / self-run.** Embedded "try this yourself" + build challenges, self-checked by
   "does it run" + `solana account` inspection. No quiz, no grader — capability is *exercised but
   never objectively verified*; the worked example printed in the lesson is the answer key.
2. **Risein — capstone-only.** Three guided builds are worked examples with no acceptance criteria;
   all solo practice concentrated in one unguided final project. A learner can passively watch three
   builds and hit the capstone cold. No interim check.
3. **Solana Foundation — self-attest run-and-compare.** Code-along labs verified by "run it and match
   output," spec challenges with solution-as-reference, and the security course's **self-audit
   challenge** (audit your own prior code) as the most authentic beat. Practice is the spine (60/63
   labs, 51/63 challenges) but nothing enforces it — verification is self-honesty + a solution diff.
4. **Ackee — distributed tasks + adversarial capstone.** 5 hands-on Tasks (one per lecture-unit), a
   submitted integrative capstone program, an adversarial PoC exploit lab (lesson 7), and Trident
   fuzzing (bonus), all exercised by `anchor test` locally. Practice is distributed then synthesized;
   checking is run-the-tests + human Task review, not an automator.
5. **Cyfrin — proof-escalation ladder + CTF.** LiteSVM unit test → localnet + demo script → Devnet
   deploy verified on Explorer, plus module-9 proof-by-exploit ("green test = you broke it"). Self-run
   (the test *is* the grader), with graduated authenticity and a real on-chain moment.
6. **Blueshift — server autograder.** Compile a *real deployable* `.so`, upload, run against hidden
   server tests keyed to a visible `RequirementList` (`instructionKey` contract). High authenticity
   ceiling; the artifact *is* the assessment.
7. **freeCodeCamp — live-ledger + AST, mastery-gated to mainnet.** 528 mastery-gated steps, 1,576
   hidden assertions incl. AST (Babeliser) code-shape checks, live validator state (deployed +
   `executable`, owner/authority, tx counts), `cargo test` shell-outs, carried all the way to a real
   **mainnet** deploy. The heaviest, most unfakeable practice loop in the corpus.

**Tradeoffs.** Heavier practice-checking buys authenticity but costs enormously to build and *rots*:
freeCodeCamp's hard-pinned versions (Solana 1.17.18, Anchor 0.28, web3.js 1.78) silently break the
autograder; Blueshift's hidden tests need maintenance; both are heavy engineering. Lighter practice
(RareSkills, Risein) is cheap and churn-resistant but leaves mastery unverified — fine for
reference/on-ramp content, weak if you need objective proof-of-mastery as a feature. The sweet spot
for most courses is **Cyfrin's self-run proof-escalation ladder** (a real on-chain moment, no
autograder to maintain) or **Ackee's distributed-tasks-then-capstone** shape (small artifacts for
momentum, one integrative build for synthesis). And the corpus-wide verdict on **quizzes: nobody uses
them** — every serious practice mechanism here is artifact-based (build/deploy/exploit/inspect),
which is the right instinct for a programming course.

---

## What to steal for a new Solana course

Prioritized, opinionated, attributed. Roughly ordered by leverage-per-effort.

1. **Steal the fixed lesson shell + explicit three-exposure fade (Solana Foundation).** `Summary →
   theory → numbered Lab → thin Challenge → feedback callout`, with the autonomy fade *stated out
   loud* ("don't code along in Overview; absolutely code along in Lab; do it alone in Challenge").
   Highest ROI, near-zero cost. Fix its one flaw: pick ONE theory header, not Lesson/Overview.
2. **Steal `priority`-integer sequencing (Solana Foundation).** One sort key per course + a per-course
   `lessons:` array is the cheapest way to encode a curriculum DAG and reorder a catalog. Add an
   explicit `prerequisites:` field if you want the graph visible. Blueshift's fuller version
   (externalize *all* ordering/difficulty/grader-routing into a manifest, keep MDX frontmatter-free)
   lets you stage/hide units via data edits — worth it at catalog scale.
3. **Steal the short concrete challenge-ladder → capstone (Risein + the corpus consensus).** Counter →
   SPL token → PDA app (vault/escrow/review) → freeform capstone is the canonical artifact ladder
   five courses converge on. Needs no autograder to work. Give the rung-3 artifact a *relatable
   domain* (Risein's Restaurant Review > a generic vault).
4. **Steal build-it-twice — but as RareSkills' sequential module, not Cyfrin's every-rung double.**
   Teach Anchor throughout, then ONE late "strip the framework" module that rebuilds the same
   primitives native. ~80% of the "see what the macro hides" payoff at ~1× cost. Reserve
   Cyfrin/Blueshift's all-rungs dual-track for explicitly auditor-oriented outcomes.
5. **Steal the proof-escalation ladder + rent hygiene (Cyfrin).** LiteSVM unit test → localnet + demo
   script → Devnet deploy, with `solana program close` baked in as routine. Gives a real on-chain
   moment cheaply and teaches production hygiene. Modernize the harness to LiteSVM/Mollusk/Surfpool
   (the corpus's older courses predate these).
6. **Steal the late offense-first security-epoch with adversarial assessment (Ackee + Cyfrin).**
   Concentrate security in one late tier, teach exploit→patch, and assess by making the learner
   *write the exploit* (Cyfrin's "green test = you broke it") or run PoC tests + fuzz (Ackee's
   Trident). Gate behind build fluency. Don't sprinkle security; don't assess it with a quiz.
7. **Steal the companion-textbook split (Ackee).** Durable "why" in an evergreen versioned book,
   disposable "how" in dated lesson notes. Decouples your concept layer from Anchor-version churn —
   the single best structural hedge against rot in this fast-moving ecosystem.
8. **Steal the completion-loop + force-seed checkpoint (freeCodeCamp) — if you can afford an
   autograder.** One-idea-per-step + near-complete seed + one blank + instant auto-check is the best
   onboarding on-ramp there is; force-seed makes it robust to divergence and lets each step isolate
   one concept. Pair with grade-the-chain + deliberate-failure for unfakeable practice and debugging
   literacy.
9. **Steal map-from-known + false-friend lessons (RareSkills) — only for transition audiences.** Order
   the opener by mapping strength and dedicate whole lessons to "features you know that do NOT exist
   here, and why." Gate on the prior model; this misleads absolute beginners.
10. **Steal the self-audit capstone (Solana Foundation).** Re-pointing challenges at the learner's own
    prior code ("audit your earlier program for this vuln class") is a near-free, portfolio-anchored
    authentic assessment — the whole earlier track becomes the exercise surface.
11. **Steal surfaced time-on-task (Risein).** Publish an expected minute budget per unit — a cheap,
    high-value cadence affordance most self-paced courses lack. Measure it, don't back-compute it.

---

## Gaps & anti-patterns

**What NONE of them do well:**

- **Nobody unifies conceptual depth + real autograded practice + a maintained toolchain.** The
  heavy-practice courses (freeCodeCamp, Blueshift) are light on concept-spine; the deep-concept
  courses (RareSkills, Ackee's Handbook) have no autograder. No single course gives you Ackee's
  Handbook rigor *and* freeCodeCamp's live-ledger grading. A new course could win by combining a
  companion-textbook spine with a proof-escalation ladder.
- **Quizzes / spaced retrieval are essentially absent.** No course uses real MCQs or spaced-recall
  checks; Cyfrin's quiz slots are empty stubs. Retrieval practice (a cheap, evidence-backed learning
  device) is a wide-open gap — RareSkills' spiral reinforcement in the accounts module is the closest
  thing.
- **Toolchain rot is universal and unmanaged.** freeCodeCamp pins Solana 1.17.18 / Anchor 0.28 /
  web3.js 1.78; Cyfrin pins Anchor 0.31 (pre-1.0); Solana Foundation predates LiteSVM/Mollusk/Surfpool
  and `@solana/kit` entirely. Every course that pins versions is quietly rotting. Centralize versions
  and budget for re-pinning; prefer in-process SVM harnesses.
- **Client/frontend integration is the most-skipped half.** Cyfrin, RareSkills, and Risein largely
  omit wallet-adapter/RPC/dApp work — a program-first bias that leaves learners unable to ship a
  usable app.
- **Beginner on-ramp friction.** Local-toolchain-required is the default (Blueshift's program
  challenges, RareSkills, Cyfrin, Solana Foundation, Ackee); only freeCodeCamp (dev-container) and
  Blueshift's *one* TS challenge are zero-install. This is a real onboarding cliff for greener
  audiences.

**Anti-patterns to avoid (each observed in the corpus):**

- **Capstone-only practice with zero interim checks (Risein).** A learner passively watches guided
  builds and hits the capstone cold. Add a lightweight per-project gate — even "does it deploy + one
  assertion."
- **Honor-system alone when you need objective proof (RareSkills, Solana Foundation).** No grader or
  automated check means mastery is unverifiable. If proof-of-mastery matters as a content feature,
  bolt on an autograder or an on-chain verify *task*.
- **Thin video-stub READMEs presented as lessons (Ackee's lessons 6-7, bonus stubs; Cyfrin's empty
  quiz/sponsor slots).** A one-line README is dead weight without the video. Either accept the written
  layer is a cheatsheet or make it self-contained — don't ship 3-byte `---` stubs as content.
- **Transcript-repo gap (Cyfrin).** The markdown is unusable without an external monorepo + video. If
  a written course must stand alone, embed starter code + expected output inline instead of linking
  out.
- **Manifest drift (Blueshift: 28 dirs vs 27 listed, 15 challenge dirs vs 13 listed).**
  Metadata-as-source-of-truth is powerful but drifts silently — reconcile the manifest against disk.
- **Left-implicit toolchain (Risein).** A beginner course that never names Anchor vs native,
  Playground vs local, or how to run tests will lose learners at the on-ramp. Make the environment
  explicit.
- **Avoidable template drift (Solana Foundation's Lesson/Overview 43/18 split; Blueshift's dual
  meta.ts vs disk).** Uniformity is the whole value of a house template — pick one label and enforce
  it.
- **Over-relying on `done` honor-gates (freeCodeCamp's 25 in the Phantom course).** Un-assertable
  steps that gate on typing "done" are ungraded. Minimize them; find an indirect on-chain signal
  instead.
