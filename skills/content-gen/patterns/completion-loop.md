# Pattern: completion-loop
> Many tiny chapters, each one idea + a near-complete artifact with one blank to fill — auto-checked,
> mastery-gated. The lowest-cognitive-load on-ramp.

## Signature strength
The **tightest feedback loop in the corpus** and the purest expression of completion problems (faded
worked examples). The learner is never staring at a blank file; they read one idea, write the one missing
piece, hit run, get instant verification, advance. Maximizes early wins and minimizes the "where do I even
start" wall.

## Route for (triggers)
- **Absolute beginners**; **language/syntax onboarding** (Rust-for-Solana, Anchor macro syntax).
- The **first module** of a beginner course, before any challenge-ladder.
- When you have (or can specify) an **auto-grader** and want momentum via many small victories.

## Anti-triggers (don't lead with this when…)
- **Intermediate/advanced** learners — the granularity bores them and triggers the expertise-reversal
  effect; graduate them to overview-lab-challenge / challenge-ladder.
- **Conceptual / non-technical** courses (nothing to type).
- No auto-grading/scaffold infrastructure is available (the pattern depends on instant checks).

## The structure it produces
```
Module = many chapters; one accreting artifact (e.g., a growing program)
Chapter = { one idea (2-5 sentences) · a pre-seeded near-complete code block · ONE TODO ·
            instant auto-check (regex/output/test) · advance only on pass }
grain: one concept per chapter; ~10-20 chapters per "lesson-sized" unit
```

## Why it works (mechanism)
Completion problems / faded worked examples (Sweller, van Merriënboer) + minimal extraneous load +
immediate feedback + mastery learning + one-aha-per-chapter. The scaffold carries everything except the
single new element.

## Stacks with
The **early module** of a beginner course that then **fades into** overview-lab-challenge and finally bare
challenge-ladder rungs. Pairs under a **concept-spine** that supplies the model the syntax expresses.

## Voice handoff
Mostly `show-how` (Helius). **Note for the writer:** completion-loop prose is intentionally sparse (one idea
per chapter), so the voice has a small surface — spend the voice budget on the *module* intro/outro
(`motivate`, spine), not every chapter.

## Worked micro-illustration (Solana)
> Beginner module: "Your first program, one line at a time." Ch.1 add `declare_id!` (TODO: paste your
> program id) → check it compiles. Ch.2 add the `#[program]` mod (TODO: name the fn) → check. Ch.3 add one
> instruction param (TODO) → check. … by Ch.12 they've written and deployed a working program without ever
> facing a blank file. `dominant_job: show-how`.

## What this pattern deliberately EXCLUDES
**Not for advanced learners.** It does **not build the big mental model** (pair with concept-spine) and
does not, alone, develop whole-task judgment (graduate to challenge-ladder). It is **infrastructure-heavy**
— it presumes an auto-grader; if none exists, downgrade to overview-lab-challenge.

## Pulled from
CryptoZombies (one-idea chapters, instant check, mastery gate) · freeCodeCamp auto-graded steps (Hello
World = 56 steps) · Scaffold completion problems.
