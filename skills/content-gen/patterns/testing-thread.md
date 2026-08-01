# Pattern: testing-thread
> Testing woven through the whole course as the **acceptance gate on every build** — introduced at the first
> artifact, reused on every rung, escalated to fuzzing in the security tier. Never a single late module.

## Signature strength
Makes "tested" the **definition of done**, not an afterthought. A test harness shows up at the *first*
program and becomes the gate the learner must pass on every subsequent artifact — so verification is a
habit built rung by rung, not a topic bolted on at the end. The test *is* the acceptance criterion, which
means progress is provable and regressions are caught the moment they appear. Produces builders who ship
verified code by reflex.

## Route for (triggers)
- **Every developer course** — it is the gate on each artifact rung, the cross-cutting thread under the
  build backbone.
- The **escalation point into fuzzing** for security/audit tiers (the thread thickens into adversarial
  testing).
- Any outcome of the form "build, *test*, and deploy X" — the verb *test* is this thread.

## Anti-triggers (don't lead with this when…)
- **Don't make it a single late module** — "and now, the testing chapter" is the exact mistake this pattern
  prevents. Testing taught once at the end is testing the learner never internalizes.
- **Pure non-technical / conceptual courses** — nothing is built, so there is nothing to gate (use the
  concept-spine's explain-it-back instead).
- It is **not a backbone** — it threads *through* whatever build backbone the router picked; it doesn't
  replace it.

## The structure it produces
```
A cross-cutting thread, not a tier. Introduced at the FIRST build, reused everywhere:
  Rung 0/1  — introduce a harness alongside the first artifact (anchor test, or LiteSVM / Mollusk / bankrun)
  every rung — the harness is the acceptance gate: the artifact isn't "done" until its test passes
  fading   — heavy worked tests early (fill-in assertions) → write-your-own-test by the late rungs
  security tier — escalate to fuzzing (Trident) and/or a CTF; tests become adversarial
Harness choice (see solana-syllabus-dag.md §1, §7):
  Mollusk (in-process, single-instruction, CU bench, fixtures) · LiteSVM (in-process, full bank, CPIs,
  multi-instruction; anchor-litesvm for Anchor) · bankrun (TS) · anchor test · Surfpool (integration / fork)
```

## Why it works (mechanism)
Authentic / performance assessment (the test is the proof) + spaced, distributed practice (a little testing
on every rung beats one massed module) + gate-on-doing + fast feedback loops (in-process harnesses keep the
red-green-refactor loop tight, so the habit is cheap to keep). Testing learned *in situ*, against the
learner's own artifact, transfers; testing learned as a standalone topic does not.

## Stacks with
Threads under **challenge-ladder** and **overview-lab-challenge** (the test is each rung's acceptance
criterion); escalates into **security-epoch** (unit tests → exploit tests → Trident fuzzing); supplies
**optimization-loop** with the thing to measure against and the regression guard. It is the connective
tissue, not a guest that competes for the stacking budget — count it as a thread, not a backbone.

## Voice handoff
Test-writing lessons are `show-how` (Helius) — they walk a documented harness step by step. Tag generic
test lessons `show-how`. (When a test *is* an exploit in the security tier, the lesson follows
`security-epoch`'s handoff: `show-how` plus the security `voice_notes` caution; the "why this invariant
must hold" beat is `derive-why`.)

## Worked micro-illustration (Solana)
> First build = a counter. Alongside it, introduce a LiteSVM (or `anchor test`) harness: a test that
> initializes the counter, increments it, and asserts the stored value. From then on **every** rung ships
> with its acceptance test — the vault rung's test deposits then withdraws and asserts the balance; the rung
> is not "done" until it's green. In the security tier the same harness writes an *exploit* test, then
> escalates to **Trident** fuzzing the patched program. `dominant_job: show-how`.

## What this pattern deliberately EXCLUDES
**Not a late module, not a backbone, not optional on a build course.** It does not, on its own, teach the
mechanism under test (that's the rung's own lesson) and it is not a substitute for the adversarial depth of
**security-epoch** — early tests prove *intended* behavior; fuzzing/CTF proves resistance to *unintended*
inputs, and the thread escalates into that tier rather than replacing it. Don't over-spend voice on every
test lesson; the thread is plumbing the learner should feel as routine.

## Pulled from
solana-syllabus-dag.md's "testing is a thread, introduce it early" rule · the modern Solana testing pyramid
(Mollusk → LiteSVM → Surfpool) · `anchor test`, bankrun, `anchor-litesvm` · Trident (Ackee) fuzzing as the
security-tier escalation · the rust/anchor rules' "don't use solana-test-validator for unit tests — use
LiteSVM/Mollusk."
