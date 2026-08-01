# Pattern: build-it-twice
> Build the same artifact at two abstraction levels — native ↔ Anchor (or strip Anchor → Pinocchio) — to
> reveal what the framework hides.

## Signature strength
Makes the **invisible visible.** By building one artifact twice — once with the manual mechanism, once with
the abstraction — the learner sees exactly what the macro/framework did for them, which is the fastest route
to *real* understanding (and to debugging, optimizing, and auditing later). "Why the abstraction exists,"
taught by contrast rather than assertion.

## Route for (triggers)
- **Intermediate → advanced**; **Solana devs leveling up**.
- The explicit goal "understand what Anchor does under the hood" / prepare to optimize or audit.
- Modules where a single artifact richly rewards a low-level vs high-level contrast (accounts validation,
  CPIs, serialization).

## Anti-triggers (don't lead with this when…)
- **Beginners** — doubling the build doubles the load and confuses; teach one path first.
- **Time-boxed intro courses** — it costs ~2× build time per artifact.
- **Productivity-first** goals — if the outcome is "ship apps fast," just teach Anchor with one or two
  "look under the hood" detours instead of a full twice-build.

## The structure it produces
```
Per chosen artifact:
  Build A — native / manual mechanism (feel the raw account handling, serialization, checks)
  Build B — same artifact in Anchor (the abstraction)
  Contrast — a "what the macro did for you" table (constraints, (de)serialization, error mapping)
Apply to the 1-2 artifacts where the contrast teaches most — NOT every rung.
(Variant: Anchor-first → strip to Pinocchio/native to "remove the abstraction.")
```

## Why it works (mechanism)
Contrastive cases / variation theory (you learn a concept by what varies across near-identical cases) +
schema-building + expertise development. The second build is mostly germane load because the artifact is
already familiar.

## Stacks with
A **guest layer** on a **challenge-ladder** rung or a **concept-spine** module; a natural partner for the
**security-epoch** (audit both implementations) and for optimization modules. Lessons inside each build use
**overview-lab-challenge**.

## Voice handoff
The contrast is `derive-why` (Vitalik — "why the framework makes this choice"); each individual build is
`show-how` (Helius). A "Anchor is just native-with-macros" reframe can be `demystify` (Hotz) — but keep it
honest, not reductive.

## Worked micro-illustration (Solana)
> Intermediate module, artifact = a vault. **Build A (native):** hand-roll account deserialization, the
> signer check, the lamport transfer. **Build B (Anchor):** `#[derive(Accounts)]` with `has_one`/`signer`
> constraints; `#[account]` for state. **Contrast table:** "the constraint replaced 14 lines of manual
> validation — and here's the one check it does *not* do for you." `dominant_job: derive-why`.

## What this pattern deliberately EXCLUDES
**Not for beginners or tight intro courses.** Don't apply it to **every** artifact — pick the one or two
where the contrast is most illuminating; twice-building everything is bloat that violates the
anti-over-engineering floor. It is a depth device, not a default.

## Pulled from
Cyfrin Updraft "build it twice" (Native + Anchor side-by-side) · Blueshift "remove the abstraction"
(Anchor → Pinocchio → crateless) · solana-developers/program-examples tri-framework parallel matrix.
