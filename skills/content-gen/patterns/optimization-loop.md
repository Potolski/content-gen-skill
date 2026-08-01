# Pattern: optimization-loop
> A late, diagnostic tier taught **measure → change one thing → re-measure**: baseline → optimize → prove
> the win with before/after numbers.

## Signature strength
Teaches performance the only way that doesn't lie: by **measuring first.** Each optimization is a
controlled experiment — establish a baseline number, change exactly one thing, re-measure, and name what
the change cost. The before/after delta **is** the proof and the assessment; there is no "trust me, this is
faster." Produces builders who optimize from evidence instead of folklore, and who can defend that a
program fits its compute-unit budget.

## Route for (triggers)
- **Performance / compute-unit outcomes** — "make it cheaper," "fit the CU budget," "reduce account size,"
  "lower latency," profiling tracks.
- **Solana devs leveling up** into optimization (the gap is efficiency, not capability).
- Any course whose terminal outcome includes "build programs that *fit the budget* / scale under load."

## Anti-triggers (don't lead with this when…)
- **Before a working program exists** — you cannot optimize what you can't yet run; premature optimization
  optimizes noise. It is always a **late** tier, after build fluency.
- **It is not build-it-twice** — that pattern reveals *why the framework exists* by contrast; this one
  reduces a *measured* cost. Reach for build-it-twice when the job is understanding the abstraction; reach
  for this when the job is a number going down.
- **Not a security pattern** — a faster handler that drops a check is a regression, not a win (see EXCLUDES).

## The structure it produces
```
Its own module/tier, gated behind a working, tested program. Per optimization target:
  baseline-measure (the honest starting number) → change ONE thing → re-measure →
  name the cost/tradeoff (what the win cost in readability, generality, or safety)
Measurement seams (see solana-syllabus-dag.md §7):
  sol_log_compute_units() in-program · "consumed X of 200000 CU" in program logs ·
  simulateTransaction for the tx-level number · Mollusk's MolluskComputeUnitBencher (CU table + deltas)
Target list: CU per instruction · heap (RequestHeapFrame) · account size / rent ·
  tx size · zero-copy vs (de)serialization · framework cost (Anchor → Pinocchio) · SetComputeUnitLimit fit
Tiering: 101 (measure + one obvious win) → 201 (zero-copy / layout / framework swaps)
Applied assessment: a before/after CU table that must show a real reduction (the delta is the grade).
```

## Why it works (mechanism)
Diagnostic / measure-first practice (you optimize the bottleneck, not the guess) + single-variable change
(isolate cause) + contrastive before/after cases + authentic assessment (the number, not a quiz). Seeing
the CU counter drop creates the "this is the bottleneck" intuition that a rule of thumb never could. It is
the **security-epoch loop shape** (baseline → intervene → re-test) aimed at compute units instead of
exploits.

## Stacks with
A **late tier** that rides a build backbone — **challenge-ladder** or **overview-lab-challenge** rungs.
Pairs naturally with **testing-thread** (you optimize *against a test* — the same harness that gates the
rung gives you the thing to measure and the regression guard). Can borrow **build-it-twice** for the one
"what the abstraction costs" contrast (Anchor → Pinocchio), but the loop, not the contrast, is the backbone.

## Voice handoff
The loop mechanics — how to profile, where the CUs go, how to set the limit — are `show-how` (Helius).
"Why *this* is the bottleneck" and "why this layout is cheaper" are `derive-why` (Vitalik). A "zero-copy is
just skipping deserialization" reframe can be `demystify` (Hotz) — but keep it honest; an optimization that
sounds clever and ships a regression is the failure mode.

## Worked micro-illustration (Solana)
> Optimization tier, CU-reduction target. **Baseline:** a transfer handler logs `consumed 6,266 of 200,000
> CU`; the bench records it. **Change one thing:** feature-gate the `msg!` debug logs out of the hot path.
> **Re-measure:** the bench delta shows the drop, and `SetComputeUnitLimit` can now be set tighter (you pay
> for requested CUs, not used). **Name the cost:** you lost in-program observability in release builds.
> `dominant_job: show-how`; the "why logging is expensive here" beat is `derive-why`.

## What this pattern deliberately EXCLUDES
**Not an early-course pattern** and **not a license to drop safety for speed** — every optimization is
re-run against the acceptance test (testing-thread) so a "faster" handler that breaks a check is caught and
rejected. It is **not build-it-twice**: don't use it to teach what the framework does, only to reduce a
measured cost. Exclude micro-optimizations with no measured payoff — if the number doesn't move, the change
doesn't ship (that is the anti-over-engineering floor applied to performance).

## Pulled from
Solana "How to Optimize Compute Usage" guide (measure → optimize, logging/data-types/serialization/PDA
costs) · Compute Budget docs (200K/instr, 1.4M/tx; simulate then `SetComputeUnitLimit` + 10% margin) ·
`sol_log_compute_units` (SPL logging example) · Mollusk `MolluskComputeUnitBencher` (CU table with deltas) ·
Pinocchio / zero-copy CU reductions vs Anchor · the `security-epoch` loop shape applied to compute units.
