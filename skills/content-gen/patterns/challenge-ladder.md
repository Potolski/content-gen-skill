# Pattern: challenge-ladder
> A sequence of escalating, self-contained build challenges on a shared scaffold — one "aha" and one
> shipped artifact per rung.

## Signature strength
**Momentum and proof through shipping.** Each rung is a real, deployable artifact that isolates exactly one
new mechanism (the shared scaffold absorbs the boilerplate). The artifact *is* the assessment, so progress
is visible and motivating. This is the most reliable engine for turning passive learners into builders.

## Route for (triggers)
- Hands-on, **motivated builders**; portfolio / "I shipped N programs" outcomes.
- Intermediate audiences (or beginners *after* a completion-loop / concept-spine on-ramp).
- When **momentum and authentic proof** matter more than exhaustive coverage.
- Credentialing via on-chain verification or deployed-artifact submission.

## Anti-triggers (don't lead with this when…)
- **Absolute beginners with no scaffold and no model** — each rung is too big a leap; precede with
  completion-loop (syntax) and concept-spine (model).
- **Non-technical / conceptual** courses (nothing to ship).
- The outcome is broad *understanding* rather than a set of built things.

## The structure it produces
```
Challenge 0  — toolchain + scaffold onboarding (deploy something trivial; pure tooling win)
Challenge 1..N — rungs up the artifact ladder (counter → token → vault/escrow → AMM → CPI)
   each rung = { forkable starter scaffold · spec + acceptance criteria · one new mechanism ·
                 deploy/verify · the trade-off · solution as resource }
Capstone — freeform build the learner designs
difficulty ramps; scaffolding fades (more TODOs early, blank repo late)
```
Artifacts can be **discrete** (one per rung — max portfolio) or **accreting** (one growing project — max
momentum).

## Why it works (mechanism)
Whole-task practice (4C/ID) + authentic/performance assessment + one-aha-per-unit + productive struggle +
the scaffold removing extraneous load so each rung isolates one concept.

## Stacks with
**concept-spine** (model first) as the upstream backbone; **map-from-known** as the Challenge-0 framing for
EVM devs; **security-epoch** as a late set of attack-the-program rungs. The lessons *inside* a rung often
use the **overview-lab-challenge** template.

## Voice handoff
Most rungs are `show-how` (Helius). Challenge 0 and the capstone framing are `motivate` (spine). A "why this
design" rung (e.g., why AMMs price the way they do) is `derive-why` (Vitalik) or `economics` (Hayes).

## Worked micro-illustration (Solana)
> Intermediate, on-chain-verified credential. Ladder: **0** scaffold+deploy hello → **1** SPL token mint →
> **2** PDA vault (deposit/withdraw) → **3** escrow (swap) → **4** constant-product AMM → **capstone** own
> protocol. Each ships a verified `.so`; the vault rung's trade-off: "PDA signing removes the key but the
> close/realloc paths are where funds leak." Rung 2 `dominant_job: show-how`; AMM rung `derive-why`.

## What this pattern deliberately EXCLUDES
It does **not teach the mental model** (pair with concept-spine) and is **not a low-load syntax onboarder**
(pair with completion-loop). It assumes a scaffold exists — specify it. Weak for learners who need heavy
hand-holding on every step.

## Pulled from
Speedrun Ethereum / Scaffold-ETH (the scaffold-is-the-innovation model) · Blueshift challenges (on-chain
verify + NFT) · freeCodeCamp integrated "Build" projects.
