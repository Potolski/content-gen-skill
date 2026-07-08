# RareSkills — "60 Days of Solana" — META

> Pedagogical **analysis** for a course designer, not a content summary and not a reproduction of
> lesson prose. Grounded in the local capture
> `courses-corpus/rareskills/structure.md` (full 8-module TOC + stated framing) plus two live
> WebFetch reconnaissance passes of the public index and one representative lesson (voice/structure
> only, no prose reproduced).

---

## 1. Snapshot

- **Source & grounding:** Local capture `structure.md` (full 8-module TOC + stated framing) plus recon
  of the public index and one representative lesson (`post/solana-counter-program`). Lessons are
  **standalone, self-contained posts** — each is individually addressable and carries no cross-lesson
  runtime state, a structural fact that shapes how content is chunked. **This META is a structural
  capture only** — verbatim body text was deliberately **not** captured; section-level claims rest on
  the TOC, the stated pedagogical framing, and thin recon fetches, so lesson-*internal* claims are
  characterized, not transcribed.
- **Delivery format:** **Written** long-form technical blog. Code snippets inline; diagrams;
  CLI/test transcripts. No video, no in-browser IDE, no interactive grader.
- **Scale (verified against `structure.md` TOC):** **8 modules.** The brand is "60 Days," but the
  enumerated TOC actually lists **62 lesson entries** (5 + 5 + 5 + 18 + 10 + 3 + 8 + 8). The "60" is a
  title/cadence frame, not an exact count — a candid discrepancy worth flagging. **No separate
  challenge or assessment tier**; practice is embedded as per-lesson exercises (see §5). Per-lesson
  length is **not prescribed**.
- **Target audience:** Engineers with **beginner–intermediate Ethereum/Solidity** experience
  (`structure.md:16`). Explicitly **not** for absolute beginners — the entire scaffold assumes an EVM
  prior model to map from.
- **Prerequisites:** No Rust required (the language is taught just-in-time in Module 2). Solidity
  familiarity is the real gate; learners without it are pointed to a prerequisite Solidity tutorial
  first (`structure.md:17-18`).

---

## 2. Structural architecture

**Decomposition:** `course → 8 modules → numbered lessons`. There is **no** intermediate "unit,"
"challenge," or "project" tier and **no separate assessment artifact** — the lesson is the atomic unit
and it is a self-contained blog post. This is flatter than most corpus courses (no path/track layer,
no capstone).

**Ordering scheme:** Human-curated, **editorially numbered** modules (1–8) and numbered lessons within
each. Because this is a proprietary blog and not an open repo, there is **no machine-readable ordering
metadata** (no frontmatter `order:` field, no `_index`, no priority key) available to inspect — the
canonical ordering artifact I read is the curated TOC reproduced at `structure.md:36-114`, which
mirrors the public index sidebar. Sequence is enforced by prose links ("in the previous lesson…"),
not by data.

**Module taxonomy (real names, real counts — `structure.md:38-114`):**

| # | Module | Lessons | Role in the arc |
|---|--------|--------:|-----------------|
| 1 | Introductory Topics | 5 | Toolchain win + first EVM 1:1 maps (arithmetic, IDL, errors, upgradeability) |
| 2 | The Minimum Rust You Need to Know | 5 | Just-in-time language onboarding (syntax, macros, structs, visibility) |
| 3 | Important System-level Information in Solana | 5 | **Frontloaded intermediate maps** (clock/block vars, sysvars, logs/events, msg.sender, compute units) |
| 4 | Accounts and Storage in Solana | **18** | **The spine** — the genuinely alien model, with spaced reinforcement |
| 5 | Tokens on Solana | 10 | SPL → Metaplex → LiteSVM testing → Token-2022 → interest-bearing extension |
| 6 | Advanced Topics in Solana Development | 3 | Introspection, Ed25519 verification, Switchboard (oracle) |
| 7 | Native Solana Programs | 8 | **Strip Anchor** — rebuild the primitives raw |
| 8 | Solana Assembly (sBPF) | 8 | **Bare-metal descent** — hand-written assembly, the depth ceiling |

**Sequencing logic vs. the Solana DAG (`references/solana-syllabus-dag.md`).** The macro-order
**deliberately inverts** the canonical concept-spine. The DAG's hard rule is *accounts → programs →
PDAs → CPIs*, model-first. RareSkills instead frontloads **Module 3** (compute units ≈ gas, clock/
block vars, `msg.sender` analogues) *before* the account model in **Module 4**, because those topics
map ~1:1 from EVM and bank early wins (`structure.md:26-28`). This is a conscious soft-edge reorder
justified by audience — the map-from-known inversion the DAG file itself attributes to RareSkills
(`solana-syllabus-dag.md:112`).

*Inside* Module 4, however, the DAG is respected: initialize accounts (L1) → read/write (L2) →
mappings (L4) → storage cost/resizing (L5) → PDA vs Keypair (L10) → PDA ownership (L11) →
`init_if_needed`/reinit attack (L12) → `#[derive(Accounts)]` taxonomy (L16) → reading another
program's account (L17) → **CPI (L18)**. So the alien core is taught in strict prerequisite order; only
the *entry point* to the course is reordered for momentum.

Modules 5→8 walk the applied/descent layers: tokens ride the DAG's token sub-ladder
(`solana-syllabus-dag.md:85-88`: SPL → Metaplex metadata → Token-2022 → an extension), then the course
**descends the abstraction stack** — Anchor throughout (M1–6) → native/no-Anchor (M7) → raw sBPF
assembly (M8).

---

## 3. Lesson anatomy

Grounded in recon of `post/solana-counter-program` (Module 4, L2). A single lesson is a **worked-
example essay**, not a slide deck. Recurring section types, in order:

```
1. Framing / context        — 1–2 paras; links back to the prior lesson; sometimes a "how would you
                              do X" hook (the map-from-known frame lives HERE and in the title, more
                              than in the body)
2. Full code listing        — complete, runnable program with inline annotations (imports + module,
                              not fragments)
3. Conceptual walkthrough   — prose + a diagram; explains what each function/macro does "behind the
                              scenes"
4. Struct / context deep-dive — dedicated dissection of the Accounts context (e.g. the `Set` struct)
5. Alternative implementation — a refactor of the same code (e.g. mutable-reference pattern) to show
                              variation
6. CLI / on-chain verification — shell transcript (`solana account <addr>`) proving the state changed
7. Embedded exercises       — 2–3 "try this yourself" prompts interspersed, + a closing build
                              challenge (e.g. "write an increment function")
```

**Always present:** a task/question-shaped title, expository theory prose, at least one complete
runnable snippet. **Optional / lesson-dependent:** explicit "in Solidity you'd…" contrast (the counter
lesson had **none** in-body — the EVM mapping is carried by module framing and titles, not every
paragraph), diagrams, the alternative-implementation section, closing challenge.

Note the anatomy is **worked-example → completion/challenge**, the classic faded-guidance shape from
the canon (`instructional-design-canon.md:24-27`), but the fade is *within* a lesson (full code shown,
then "modify it") rather than across a graded ladder.

---

## 4. Content sequencing & pacing

Pedagogical grain only — how concepts are ordered and chunked, not any calendar.

- **Lesson = one self-contained sitting (the grain unit).** Content is chunked so each lesson is a
  complete worked-example essay consumable in a single session; the "60 Days" title frames a roughly
  one-lesson-per-sitting cadence. That is a *grain* signal, not a schedule — `structure.md:11-12` is
  explicit that exact per-lesson pacing is not prescribed, and the **62 enumerated lessons do not map
  1:1 to the "60,"** so the number is a cadence motif, not a count.
- **Linear-by-prose sequencing.** Order is carried by prose links ("in the previous lesson…"), not by
  metadata. Modules are individually addressable, but the concept flow assumes linear consumption;
  there are no goal tiers or intermediate checkpoints — progression is reader-driven and enforced only
  by narrative back-references.
- **Difficulty-inversion is the primary pacing device.** Easy EVM-equivalent wins (M1–M3) are
  frontloaded *before* the hard mental-model shift (M4 accounts), banking momentum before *"the
  different parts"* (`structure.md:28-30`). Pacing is engineered through **ordering and chunk size**,
  not time-gates.
- **Uneven module sizing mirrors conceptual difficulty.** The hardest concept gets the most surface —
  M4 (accounts) is **18** lessons while the onboarding modules (M1–M3) are 5 each and the advanced
  module (M6) is 3. Chunk count tracks cognitive load, with spaced return passes inside M4 (see §6),
  not calendar-even segments.

---

## 5. Learning artifacts & practice

Practice is **embedded in every lesson** rather than isolated in a separate tier — there is no quiz
bank or autograder. The practice layer is self-verified and built from four artifact types, each
forcing active production:

1. **Embedded "try this yourself" exercises** — each lesson interleaves 2–3 code-modification prompts
   mid-flow, making the learner mutate the just-shown program instead of only reading it.
2. **End-of-lesson build challenges** — a closing extend-the-program task (recon: the counter lesson
   closes with *"write an increment function"*). The learner's own running code is the success signal.
3. **Run + on-chain inspection as a learning task** — the acceptance loop is: run the program against a
   validator, then read state back with `solana account <addr>`. The CLI transcript printed in the
   lesson is the answer key, so the on-chain verify step is itself a hands-on exercise, not a passive
   demo.
4. **Deterministic testing technique** — Module 5 L7 ("Time travel testing with LiteSVM") teaches
   writing tests that manipulate the clock; here the practice is *authoring tests*, taught as a
   transferable skill.

Net: every lesson drives a **modify → build → run → inspect** loop, and mastery is self-checked against
the worked example. There is **no capstone project** — the terminal practice artifacts are instead the
depth modules (native rebuild in M7, sBPF assembly in M8), where the exercise is reconstructing the
same primitives from scratch.

---

## 6. Pedagogical devices

Mapped onto the house pattern vocabulary (`patterns/*.md`); new names coined where nothing fits.

- **map-from-known** *(house — `patterns/map-from-known.md`)* — the **primary framing overlay**, not
  the backbone. The whole course runs on *"I know how to do X in Ethereum — how do I do X in Solana?"*
  (`structure.md:23-24`). RareSkills is literally the pattern's source-of-record
  (`map-from-known.md:59-61`). It sequences by **mapping strength**: 1:1 maps first (compute units ≈
  gas, custom errors ≈ revert, `msg.sender`), partial maps next, alien parts last.

- **The RareSkills inversion** *(house device inside map-from-known)* — frontloading EVM-equivalent
  intermediate topics (Module 3) *before* Solana fundamentals (Module 4 storage/accounts) for early
  victories. Documented at `map-from-known.md:28-30` and `solana-syllabus-dag.md:112`.

- **false-friend lessons** *(house device, elevated to whole lessons — a signature)* — the map-from-
  known "flag false friends" move is promoted from a sentence to **entire lessons about EVM features
  that do NOT exist in Solana**: M1 L5 "Solana programs are upgradeable and do not have constructors,"
  M4 L7 "Function modifiers (view/pure/payable) & fallback functions: why they don't exist." Naming the
  absent mapping is treated as first-class content. This is the sharpest local instantiation of the
  false-friend rule (`map-from-known.md:8-9`).

- **concept-spine** *(house — `patterns/concept-spine.md`)* — Module 4 (18 lessons) IS a dependency-
  ordered account-model backbone, walked in DAG order (accounts → PDA → ownership → CPI). But the
  course refuses to *open* on it (anti-trigger: EVM builders would go passive), instead opening on the
  map-from-known layer and reaching the spine only after momentum is banked.

- **spaced reinforcement / spiral** *(house — canon `:33-35`)* — the 18-lesson accounts module
  revisits the same ownership/PDA/rent model repeatedly, *explicitly* acknowledging *"it doesn't all
  stick right away"* (`structure.md:31-33`). Over-provisioning the single hardest concept with spaced
  return passes is the standout use of retrieval/interleaving in the corpus.

- **worked-example → completion → challenge** *(house — canon `:24-27`)* — every lesson shows a full
  runnable program, then fades to "modify it" exercises and a build challenge. The fade lives inside
  the lesson, not across a grade book.

- **sequential build-it-twice (abstraction-descent variant)** *(house `patterns/build-it-twice.md`,
  re-shaped)* — instead of side-by-side native↔Anchor per artifact, RareSkills teaches **Anchor
  throughout (M1–6), then Module 7 rebuilds the same primitives natively** — reading account data (M7
  L2), CPI with invoke/invoke_signed (M7 L4), creating accounts for storage (M7 L5–6), security checks
  (M7 L8). It is "strip the abstraction" as a **whole late module** rather than a per-rung contrast —
  cheaper than doubling every build, and it maps onto the `build-it-twice` variant noted at
  `build-it-twice.md:30` ("Anchor-first → strip to native").

- **bare-metal descent (coined — no house pattern)** — Module 8 goes *below* the abstraction stack
  entirely into **hand-written sBPF assembly** (Rust→SBF compilation, VM instruction set, memory
  layout/registers, reading inputs in assembly, syscalls). No corpus pattern covers descending to
  assembly in an intro course. Propose adding **`bare-metal-descent`**: a terminal depth module that
  removes *all* frameworks to expose the VM, used as a depth-ceiling flex, not a productivity path.

- **question-titled lessons (coined)** — most lessons are titled as the learner's own question or a
  myth-buster ("...why they don't exist", "PDA vs Keypair account", "Owner vs authority"). Titles do
  double duty as navigation labels and as the map-from-known hook, so the framing device is baked into
  the table of contents itself, not just the intro paragraph.

---

## 7. Scaffolding & tooling

- **Local toolchain, no zero-install on-ramp.** The course assumes a local Anchor/Rust install; there
  is **no Solana Playground / in-browser IDE** (contrast the DAG's zero-install suggestion at
  `solana-syllabus-dag.md:118`). Module 1 L1 "Solana Hello World (installation & troubleshooting)"
  *is* the environment scaffold — setup is a lesson, not a provided container or repo.
- **No starter repos / no scaffold generator surfaced.** Code is delivered as complete inline listings
  the reader recreates; there is no `create-solana-dapp` handoff, no cloneable per-lesson repo evident
  in the capture.
- **Test harness:** Anchor's default TypeScript/mocha + `@solana/web3.js` for client reads (M4 L3
  "Read account data with Solana web3 js and Anchor"). **LiteSVM** is introduced mid-course (M5 L7,
  "Time travel testing with LiteSVM") for deterministic/clock-manipulation tests. No Mollusk, no
  Surfpool, no bankrun in the TOC. No autograder.
- **Verification loop:** run locally → inspect with `solana account`. The CLI is the feedback surface.
- **Descent tooling:** Module 7 drops Anchor (native `solana-program`, Borsh, manual invoke_signed);
  Module 8 uses raw SBF compilation and assembly tracing (compute-cost tracing at M8 L3). Toolchain
  complexity *rises* as the course descends, the inverse of a beginner ramp.

---

## 8. Voice & framing

- **Register:** professional-yet-approachable, dense technical exposition; "active learning over
  passive consumption" (index recon). Visual-heavy — diagrams sit next to code (cognitive-load-aware,
  canon `:20-22`).
- **Concept introduction:** via the learner's *question* (title-as-hook) and a mechanistic "behind the
  scenes" walkthrough — a **demystify** voice that narrates what a macro secretly does. One
  illustrative sentence (recon, single quote):

  > "Behind the scenes, set will load the storage, write the new value of x, serialize the struct, then store it back."

  That mechanistic "here's what the framework hides" register is the course's default and it pre-loads
  the Module 7/8 descent — the learner has already been told what Anchor abstracts before they strip
  it.
- **Motivation device:** the transition analogy — a competent EVM dev learns Solana faster than a
  blockchain novice (frontend→mobile beats backend→mobile, `structure.md:19-20`). Momentum-via-early-
  wins is the explicit engagement engine.

---

## 9. Distinctive signatures

What THIS course does that the others in the corpus do not:

1. **Macro-inverts the Solana DAG on purpose.** It is the corpus's canonical example of ordering by
   **EVM-mapping strength instead of prerequisite logic** — system-level/gas topics (M3) *before* the
   account model (M4). Every other developer course opens on the account model; RareSkills defers it to
   bank momentum.
2. **An 18-lesson accounts spine.** Most courses spend 2–4 lessons on accounts/PDAs. RareSkills spends
   **18**, with self-aware spaced reinforcement ("it doesn't all stick right away"). It over-provisions
   the single hardest concept by an order of magnitude.
3. **Unmatched depth ceiling for an "intro" course:** Anchor → **native** → **hand-written sBPF
   assembly**. No other corpus course descends to the VM/assembly layer at all.
4. **False-friends as whole lessons.** Dedicated lessons on things that *don't exist* (constructors,
   view/pure/payable modifiers, fallback functions) — the negative space of the EVM→Solana mapping is
   treated as teachable content, not a footnote.
5. **Every lesson is a self-contained, individually-addressable unit.** Each stands alone as a complete
   answer to one "how do I X in Solana" question — no cross-lesson runtime state, no shared repo
   required. The curriculum is therefore maximally reference-reusable: any lesson doubles as a
   standalone tutorial, and the structure never depends on a fixed entry point.
6. **Audience-exclusive by design.** It is nearly useless to an absolute beginner and openly says so —
   a rare, disciplined refusal to serve everyone.

---

## 10. Takeaways for a course designer

1. **Steal the mapping-strength reorder for transition audiences.** When learners have a strong
   adjacent prior (EVM, another chain, web2 backend), order the opening by *what maps 1:1* to bank
   wins, then hit the alien parts — even if that violates strict prerequisite order at the *macro*
   level. Keep the DAG intact *inside* the hard module (RareSkills does: M4 is DAG-clean).
2. **Steal false-friend lessons.** Dedicate real lessons to "features you know that do NOT exist here,
   and why." Naming the absent mapping defuses the most dangerous over-mappings — the thing a
   transition learner will otherwise assume works.
3. **Steal over-provisioning the hardest concept.** Give the genuinely alien model (accounts/PDAs/
   ownership) far more surface + spaced return passes than feels proportionate. 18 lessons with
   deliberate revisits beat one dense "accounts" lesson.
4. **Steal sequential build-it-twice as a module, not a per-artifact double.** Teach the abstraction
   throughout, then a single late "strip the framework" module that rebuilds the *same primitives*
   raw. It reveals what Anchor hides at ~1× cost instead of the 2× cost of doubling every build.
5. **Steal question-titled, standalone lessons.** Titles-as-questions double as the map-from-known
   hook and make each lesson a reusable, self-contained reference the learner can return to out of
   sequence.
6. **Know the practice layer is self-verified.** Mastery is checked entirely by self-run exercises and
   `solana account` inspection — there is no objective grader. If your design needs objective
   proof-of-mastery as a content feature, add autograded tests or on-chain verification *tasks* as
   first-class learning artifacts; the run-and-inspect loop is already there to build on.
7. **Avoid this model for absolute beginners.** The whole scaffold assumes an EVM prior; forced
   analogies mislead learners with no prior model (`map-from-known.md:16-19`). Gate on the prior, as
   RareSkills does (redirect Solidity-less readers out).
8. **When this model fits:** reference-style transition courses for engineers coming from an adjacent
   stack — and as a *depth* offering (native + assembly) that most curricula never reach. It is a
   springboard-and-ceiling design: fast onboarding via priors, unusually deep floor.
