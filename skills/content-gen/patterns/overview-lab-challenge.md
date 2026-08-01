# Pattern: overview-lab-challenge
> The default **lesson-level** template: read → guided build → unguided build. A three-exposure spiral with
> fading baked in.

## Signature strength
A **repeatable, self-contained lesson shell** that gives every lesson three exposures at rising autonomy —
study a worked example, build it with guidance, then build something like it alone. It operationalizes the
worked-example effect and fading at the grain of a single lesson, and it's consistent enough to apply
across an entire course.

## Route for (triggers)
- The **default `lesson_template`** for almost any developer course.
- When you want consistent lessons with built-in practice and a clean gate-on-doing.
- Inside a `concept-spine` or `challenge-ladder` backbone (it nests).

## Anti-triggers (don't lead with this when…)
- **Micro-syntax onboarding** — the triad's grain is too coarse; use **completion-loop** (many tiny
  auto-checked steps).
- A **pure concept** lesson with nothing to build — trim to Overview + a retrieval check (don't fabricate a
  hollow lab).

## The structure it produces
```
Lesson = {
  objectives (Bloom-tagged, 1-3)
  summary / TL;DR (key facts up front)
  OVERVIEW  — worked, annotated example; read-only ("you're not expected to code along yet")
  [quiz]    — OPTIONAL concept check (formative; immediate feedback; never gates)
  LAB       — code-along the same build; show expected output; one new element at a time
  CHALLENGE — solo variation; acceptance criteria; solution provided as a resource, not a crutch
  [code]    — OPTIONAL runnable coding challenge (Rust/TS only; starter fails, solution passes)
  recap + retrieval question + forward link
}
```
The bracketed `[quiz]`/`[code]` are the Academy plugins (brief `quiz_blocks`/`coding_challenges`,
lesson-brief-schema §H). They are additive and formative — the CHALLENGE/`assessment` is still what gates.

## Why it works (mechanism)
Worked-example → completion/guided → solo *is* the fading schedule (Sweller, scaffolding/ZPD). Three
exposures at rising autonomy operationalize the fading schedule; the closing retrieval adds the testing
effect (real spacing lives at module/course grain — design-spine §9). Maps
cleanly onto Merrill (demonstration → application → integration) and Gagné's nine events.

## Stacks with
**Nests inside** every backbone — it's the lesson unit, not a course shape. Pairs with **completion-loop**
for the early/easy lessons (finer grain) and graduates to bare **challenge-ladder** rungs as the course
fades support.

## Voice handoff
The Overview is often `derive-why` (Vitalik) or `show-how` (Helius); the Lab is `show-how` (Helius); the
lesson's framing/opener is `motivate` (spine). Tag the lesson by its **dominant** job (usually the
Overview's).

## Worked micro-illustration (Solana)
> Lesson: "Transfer SOL from a PDA." **Overview:** annotated `invoke_signed` example, read-only.
> **Lab:** add a `withdraw` instruction to the running vault; expected `anchor test` output shown.
> **Challenge:** add a `withdraw_to` a third party with an owner check; accept = unauthorized withdraw
> fails. Trade-off named: signing as a PDA is powerful but the seeds must match exactly or the CPI fails
> silently. `dominant_job: show-how`.

## What this pattern deliberately EXCLUDES
It is a **lesson template, not a course backbone** — it does not decide course-level sequencing or which
artifacts to build (that's the router + DAG + a backbone pattern). It does not handle credentialing or
capstones.

## Pulled from
Solana Foundation (Unboxed) Overview/Lab/Challenge + its "Course Guide" three-exposure model ·
freeCodeCamp guided→guided→unguided triads.
