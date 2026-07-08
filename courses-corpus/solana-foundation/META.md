# META — Solana Foundation Developer Courses

> Pedagogical teardown for a course *designer*. Not a content summary. Every structural
> claim below is grounded in files under `content/`. Counts were verified with `find`/`grep`,
> not estimated.

---

## 1. Snapshot

- **Provenance:** https://solana.com/developers/courses — the Solana Foundation
  `developer-content` (the archived "Solana Course"). Every `metadata.yml` carries
  `author: unboxed` (Unboxed Software), so this is a single-author-house body under
  Foundation stewardship, not a multi-vendor catalog.
- **Delivery format:** **written, local-first**. Long-form Markdown lessons with fenced
  code blocks, MDX `<Callout>` components, and SVG diagrams referenced from
  `/public/assets/courses/unboxed/`. No video, no in-browser sandbox, no autograder — the
  learner works in a **local toolchain** (`onchain-development/local-setup.md`).
- **Scale (verified):**
  - **12 courses** (12 dirs under `content/`, each with a `metadata.yml`).
  - **63 lessons** (`find content -name '*.md' | wc -l` = 63).
  - **51 lessons carry a `## Challenge`**; **60 carry a `## Lab`**; **3 carry neither**
    (`getting-started`, `security-intro`, `intro-to-onchain` — pure orientation lessons).
  - **43 lessons end with a "Completed the lab?" feedback callout**.
  - **No stated hour budget anywhere** (`grep -ri "hours\|estimated time"` → incidental only).
- **Target audience:** developers new to Solana who can already program (TypeScript/JS
  assumed, Rust taught as needed). `getting-started.md` opens with "What is web3?" — it
  onboards true blockchain beginners, then ramps to program security and optimization for
  intermediate builders.
- **Prerequisites:** JS/TS fluency; a computer for local install (Node, Rust, Solana CLI,
  Anchor). Rust is not assumed — `native-onchain-development/hello-world-program.md` teaches
  "Rust Basics" inline.
- **Topic scope:** cryptography & clients → tokens/NFTs → Anchor programs → oracles/offchain
  data → token extensions → native Rust programs → optimization → state compression → program
  security → mobile / offline / pay specialties. Breadth-first over an intermediate depth ceiling.

---

## 2. Structural architecture

**Decomposition:** `implicit track → 12 courses → ordered lessons → (Lab steps + Challenge)`.
There is no "path" object and no cross-course challenge bank; the track is *emergent* from a
single sort key.

**Ordering scheme — the `priority` integer.** Each `content/<course>/metadata.yml` has a
`priority:` field. Lower = earlier. This is the ONLY sequencing metadata; there are no lesson
numbers in filenames (files are kebab-slugs like `anchor-pdas.md`). Within a course, order is
the explicit `lessons:` array in `metadata.yml`. Cited files: all 12 `*/metadata.yml`.

**The implicit priority-ordered track (real names + real lesson counts):**

| priority | course dir | title | lessons |
|---:|---|---|---:|
| 5  | `intro-to-solana` | Introduction to cryptography and Solana clients | 6 |
| 10 | `tokens-and-nfts` | Tokens and NFTs on Solana | 3 |
| 15 | `onchain-development` | Onchain program development (Anchor) | 6 |
| 20 | `connecting-to-offchain-data` | Connecting to offchain data (oracles/VRF) | 2 |
| 30 | `token-extensions` | Token Extensions | 15 |
| 50 | `native-onchain-development` | Native onchain program development | 9 |
| 60 | `program-optimization` | Program Optimization | 4 |
| 65 | `state-compression` | State Compression | 2 |
| 70 | `program-security` | Program Security | 11 |
| 99 | `mobile` | Solana Mobile Development | 3 |
| 99 | `offline-transactions` | Offline transactions (durable nonces) | 1 |
| 99 | `solana-pay` | Solana Pay | 1 |

**Sequencing logic (prereq graph):** the priorities encode a real DAG, not arbitrary numbers:
clients/keys (5) → tokens (10) → Anchor programs (15) → offchain data feeds (20) → token
extensions (30) → *then* the low-level native path (50) → optimization (60) → compression (65)
→ security hardening (70) → detached specialty tracks tied at 99 (mobile, offline, pay). Note
the deliberate ordering choice: **Anchor (high-level, priority 15) is taught before native
Rust (priority 50)** — abstraction-first, mechanism-later. Security is a **late, standalone
tier (70)**, after build fluency exists. The three priority-99 courses are leaf specialties
with no downstream dependents.

**Two courses self-declare non-linearity.** `program-security/security-intro.md` explicitly
tells the reader the security lessons may be taken in any order (`<Callout>` line 38-40:
"you are welcome to explore these lessons in whatever order suits you best"), unlike every
other course. So the track is *mostly* a chain with one deliberately unordered module.

---

## 3. Lesson anatomy

**Fixed template** (grounded in `intro-to-solana/intro-to-reading-data.md`,
`program-security/signer-auth.md`, `onchain-development/intro-to-anchor.md`,
`native-onchain-development/hello-world-program.md`):

```
---
title: <string>
objectives:                 # 1–4 Bloom-style verbs: "Use…", "Understand…", "Build…"
  - <objective>
description: <one-sentence hook>
---

## Summary                  # bullet TL;DR of key facts, ALWAYS present
## Lesson  (or ## Overview) # theory: prose + diagrams + code snippets, read-only
   ### <subtopic>           # H3 conceptual sub-sections
## Lab                      # hands-on, code-along, NUMBERED steps
   ### 1. Starter           # download starter branch → build up → run/test
   ### 2. <step> …
## Challenge                # independent build, spec-only prompts, solution linked
<Callout type="success" title="Completed the lab?">  # push to GitHub + Typeform link
```

**Always present:** frontmatter (`title`/`objectives`/`description`) and `## Summary`.
**Theory header is bimodal:** **43 lessons use `## Lesson`**, **18 use `## Overview`**
(the whole `token-extensions` course and the orientation lessons prefer "Overview"). Same
role, two labels — a designer copying this template should pick one.

**Lab is a numbered build ladder.** Steps are `### 1. Starter`, `### 2. …`, each adding one
element and ending in `anchor test`/script run. `signer-auth.md` labs go
`1. Starter → 2. Test insecure_withdraw → 3. Add secure_withdraw → 4. Test secure_withdraw`
— i.e. the lab itself is a build-the-insecure-then-secure sequence.

**Challenge is deliberately thin.** Just prompts + acceptance intent, with solution code
provided "as a helpful resource rather than a crutch" (`getting-started.md`). In the security
course every Challenge collapses to the same meta-task: *audit your own program (or an OSS
program) for this vulnerability class* (`signer-auth.md` §Challenge).

**Optional / outliers:** `## Challenge` absent in 12 lessons; both Lab and Challenge absent
in the 3 orientation lessons (`getting-started`, `security-intro`, `intro-to-onchain`) —
these are pure concept lessons and correctly do NOT fabricate a hollow lab.

---

## 4. Content sequencing & pacing

- **Grain = the lesson.** The atomic content chunk is one lesson: a theory pass + a numbered
  Lab + a Challenge, sized to a single sitting. There are **no sub-lesson checkpoints** — grain
  is deliberately coarse, so a concept is introduced, practiced, and closed inside one unit
  rather than sliced into micro-steps.
- **Macro-sequence = the `priority` DAG** (see §2): concepts are frontloaded model-first
  (cryptography → accounts → programs), then each course builds on the fluency of the prior one.
  Ordering is *suggested*, not enforced; the `program-security` course explicitly *removes*
  ordering (`security-intro.md`), letting its ten vulnerability lessons be traversed in any order.
- **Micro-sequence = a three-pass exposure cadence inside every lesson**, at rising autonomy —
  **read → code-along → solo** — stated verbatim in `getting-started.md`
  (Overview: *"not expected to code along"*; Lab: *"absolutely should… do the thing"*;
  Challenge: *"implement independently"*). This is the real pacing unit: the same concept is met
  three times with the scaffold fading each pass.
- **Spiral reinforcement across lessons.** Recurring artifacts (**Movie Review**, **Student
  Intro**) are revisited across 11+ lessons and two courses, so core concepts (PDAs, accounts,
  serialization) are re-encountered at rising complexity rather than taught once — spaced
  reinforcement built into the artifact choice, not a review quiz.
- **Learner-driven mastery pacing.** `getting-started.md` §"How do I use the course effectively?"
  frames pacing as self-managed: *"be brutally honest with yourself"* and repeat sections until
  understood; *"do every lab and every challenge"*; *"go above and beyond"* by extending the labs.
  The intended cadence is mastery-per-lesson, gated on comprehension rather than on any check.

---

## 5. Learning artifacts & practice

Every lesson embeds hands-on practice as first-class structure. **60 of 63 lessons carry a
`## Lab`; 51 carry a `## Challenge`** — practice is the spine, not an appendix.

- **Labs (embedded in 60 lessons)** — code-along builds with expected output shown. The learner
  reproduces a working program step by step and confirms it by running `anchor test` or an
  `esrun` script and **matching the shown output** — the run-and-compare is the self-check
  built into the artifact.
- **Challenges (embedded in 51 lessons)** — an independent build from a spec, with **solution
  code linked** as a reference (framed *"as a helpful resource rather than a crutch"*,
  `getting-started.md`). The learner produces new code, not just reads.
- **Self-audit task (the security course)** — in `program-security` the Challenge collapses to a
  single recurring practice task: **audit your own (or an OSS) program for this vulnerability
  class** (`signer-auth.md` §Challenge). The artifact turns the learner's own prior programs into
  the exercise surface.
- **Insecure→secure build drill** — security labs make the learner build the *vulnerable* path,
  exploit it, then build and re-test the *fixed* path (`insecure_withdraw` vs `secure_withdraw`
  in `signer-auth.md`), so the practice artifact demonstrates the bug before the patch.
- **Worked examples & starters** — every lab ships a `starter` branch to build up from and a
  `solution` branch to diff against; the scaffold-fade is baked into the branch pair (§7).
- **End-of-lesson reflection prompt** — **43 lessons close with**
  `<Callout type="success" title="Completed the lab?">` linking a per-lesson Typeform
  (`#answers-lesson=<uuid>`, e.g. in `signer-auth.md`). Structurally it is a uniform
  self-report + sentiment reflection appended to the lesson shell, prompting the learner to log
  that they pushed their work and reflect on the lesson.

Net practice model: **build it (lab) → build it alone (challenge) → audit it (security)**, with
run-and-compare and a solution diff as the embedded self-checks. No autograded gate — the
verification each artifact asks for is *run the code and read the output*.

---

## 6. Pedagogical devices (mapped to house patterns)

**`overview-lab-challenge` — the lesson shell, and the house pattern is literally named in
the source.** `getting-started.md` describes the three sections and their autonomy fade
almost word-for-word with the house pattern doc: Overview = "you are *not* expected to code
along"; Lab = "you *absolutely should* code along… your first opportunity to *do the thing*";
Challenge = "implement independently." This is a textbook worked-example → guided → solo
fade, applied uniformly across ~60 lessons.

**`security-epoch` — the `program-security` course (priority 70) is a canonical instance.**
Late, standalone tier gated behind build fluency; modeled explicitly on Coral's *Sealevel
Attacks* (`security-intro.md` line 13); taught **insecure → exploit → patch → re-test**
(the `insecure_withdraw` vs `secure_withdraw` build in `signer-auth.md`); vulnerability
classes match the house DAG list (signer, owner, data-matching, reinit, duplicate-mutable,
type-cosplay, arbitrary-CPI, bump-seed, closing/revival, PDA-sharing). Assessment is an audit
challenge, not a quiz. Deviations from the house ideal: **no fuzzing/Trident and no CTF** —
the "authentic adversarial" tier stops at manual audit.

**`build-it-twice` — the Movie Review / Student Intro apps are built once in Anchor and once
native.** The SAME recurring artifacts appear in both `onchain-development` (Anchor:
`anchor-pdas`, `anchor-cpi`) and `native-onchain-development` (raw Rust: `program-state-management`,
`program-derived-addresses`, `cross-program-invocations`). Building the identical program at
two abstraction levels is exactly the "make the invisible visible" contrast — here spread
across two whole courses rather than paired within one lesson.

**`client-integration` — a full off-chain sub-track exists.** `intro-to-solana` (read data →
write data → wallets), the `*-frontend` lesson series in `native-onchain-development`
(`serialize-instruction-data-frontend`, `deserialize-custom-data-frontend`,
`paging-ordering-filtering-data-frontend`), and the entire `mobile` course (MWA, Expo) own the
"wire a user to a program" half. IDL-typed clients and wallet-adapter flows are first-class.

**`concept-spine` — the two intro lessons.** `getting-started.md` and `intro-to-onchain.md`
walk model-before-build (web3 → Solana → accounts → programs → PDAs) with diagrams and
concrete tables, then hand off to a build course.

**`map-from-known` — present but weak, and web2-flavored.** The audience is beginners, not EVM
devs, so instead of Solidity mappings the course maps to *web development* priors:
"think of instruction handlers like HTTP route handlers, and incoming instructions like HTTP
requests" (`intro-to-onchain.md`). It's a framing device inside lessons, never a backbone.

**New device to name — "audit-your-own-code challenge" (self-audit capstone).** Unlike the
other courses' fresh-build challenges, security challenges redirect the learner to audit
*their own prior programs* for each class. It converts the whole earlier track into the
assessment surface. Worth stealing as a cheap, portfolio-anchored capstone.

**Absent devices worth noting:** no `completion-loop` (no tiny auto-checked steps — grain is
coarse, all local), no `challenge-ladder` capstone (challenges are per-lesson, not an
escalating shared-scaffold ladder), no spaced-quiz retrieval.

---

## 7. Scaffolding & tooling

- **Local-first dev environment.** A dedicated setup lesson (`onchain-development/local-setup.md`)
  installs Rust, Solana CLI, and Anchor. No in-browser IDE, no Playground dependency.
- **Starter repos via GitHub branches.** Labs begin at `### 1. Starter` by cloning a
  `starter` branch, e.g. `github.com/solana-developers/signer-auth/tree/starter`
  (11 lessons reference `git clone`; 34 reference "starter"; 50 reference "solution").
  The scaffold-fade is baked into the `starter → solution` branch pair.
- **Test harness = the classic Anchor/Mocha stack.** `anchor test` (23 lessons), `mocha`/`chai`
  (59 lessons reference chai), `solana-test-validator` (15). TypeScript client scripts run via
  **`esrun`** (19) against **web3.js v1** (`npm install … @solana/web3.js@1`).
- **Notably dated vs current house rules:** **0 mentions of LiteSVM, Mollusk, or Surfpool.**
  This corpus predates the in-process test-harness era the project's own `rust.md`/`anchor.md`
  rules now mandate — a designer forking this should modernize the harness.
- **No autograder.** Verification is "run it and read the output" + provided solution diff.
- **MDX component kit:** `<Callout>` in five flavors — `success` (44, the feedback CTA),
  `note` (30), `info` (3), `caution` (3), `warning` (1) — plus SVG diagrams under
  `/public/assets/courses/unboxed/`.

---

## 8. Voice & framing

- **Register:** warm, second-person, mentor-with-a-pep-talk. Ends orientation with
  *"Alright, that's it for the pep talk. Get after it!"* (`getting-started.md`).
- **Concept introduction is analogy-first from web2**, then formalized: HTTP-route-handler ≈
  instruction handler; key/value store ≈ PDA (with a worked table of seed→value examples in
  `intro-to-onchain.md`).
- **Summary-up-front:** every lesson leads with a bulleted `## Summary` before any prose —
  advance-organizer discipline.
- **Honesty as the motivational spine:** the course sells *self-assessment integrity*
  ("Be brutally honest with yourself") in place of external gates.
- **Security course shifts register deliberately:** `security-intro.md` promises
  "less prose and more code," and those lessons are contrastive insecure/secure code walks.

---

## 9. Distinctive signatures

What THIS corpus does that the sibling courses in the pattern library do not:

1. **One integer (`priority`) silently authors the entire curriculum DAG.** No path objects,
   no numbered files — the whole 12-course sequence is a sort key plus per-course `lessons:`
   arrays. Extremely low-ceremony curriculum wiring.
2. **Abstraction-before-mechanism ordering.** Anchor (priority 15) is taught *before* native
   Rust (priority 50) — the reverse of "raw first." Native then re-builds the same Movie
   Review app to reveal what Anchor hid: a two-course `build-it-twice` spanning ~15 lessons.
3. **A course that turns OFF its own ordering.** `program-security` explicitly grants
   free-order traversal — a rare intentional break from the linear chain.
4. **Practice by self-audit.** Security challenges point the learner back at their *own*
   earlier programs, making the prior track the exercise surface.
5. **Uniform end-of-lesson reflection prompt** — 43 lessons close the shell with the same
   `Completed the lab?` callout carrying a per-lesson `#answers-lesson=<uuid>`, a copyable
   structural signature that ends each lesson on a reflect-and-report beat.
6. **Uniform `Summary → Lesson/Overview → Lab(numbered) → Challenge → feedback-callout`
   shell** applied across 60 lessons with near-zero drift — a highly copyable house template.
7. **Recurring spiral artifacts** ("Movie Review", "Student Intro") threaded through 11+
   lessons across two courses, giving continuity without a single monolithic capstone.

---

## 10. Takeaways for a course designer

1. **Steal the `priority`-integer sequencing.** A single sort key per course + an explicit
   `lessons:` array is the cheapest possible way to encode a prereq DAG and reorder a whole
   catalog. Add a `prerequisites:` field if you want the graph explicit rather than implied.
2. **Steal the fixed lesson shell** (`Summary → theory → numbered Lab → thin Challenge →
   feedback callout`). Its uniformity is its strength — but **pick ONE theory header**
   ("Lesson" vs "Overview" split 43/18 here is avoidable inconsistency).
3. **Steal the stated three-exposure fade.** Telling the learner *"don't code along in
   Overview; absolutely code along in Lab; do it alone in Challenge"* makes the worked-example
   → guided → solo schedule explicit and self-enforcing.
4. **Steal the two-course `build-it-twice`** (Anchor then native, same artifact) when the
   outcome is "understand what the framework hides" — but only *after* build fluency; it
   doubles build time, so don't do it to beginners on every rung.
5. **Steal the self-audit capstone** from the security course: re-pointing challenges at the
   learner's own prior code is a nearly-free, portfolio-anchored authentic assessment.
6. **Avoid copying its tooling verbatim.** The harness (`anchor test` + mocha/chai +
   `solana-test-validator`, web3.js v1, `esrun`) is pre-LiteSVM/Mollusk/Surfpool and pre-`@solana/kit`.
   Keep the *starter→solution branch* scaffold-fade; modernize the test/runtime stack.
7. **Add a real verification artifact if you need one.** The labs/challenges self-check only by
   run-and-compare against a solution diff — there is no autograded step. If you want practice
   that confirms itself, layer an autograder or an on-chain "verify your program works" task onto
   this shell as an additional learning artifact.
8. **When to use this model:** a written, local-first developer course for a motivated,
   self-directed learner, where breadth and a copyable lesson template matter more than
   fine-grained checkpoints. Add `security-epoch` fuzzing/CTF and a `challenge-ladder` capstone
   if you want the hardening and momentum this corpus stops short of.
