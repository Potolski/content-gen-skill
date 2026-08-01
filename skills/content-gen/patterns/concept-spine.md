# Pattern: concept-spine
> A dependency-ordered conceptual backbone — build the mental model *before and around* the builds.

## Signature strength
Makes an **alien model legible** by teaching concepts in strict prerequisite order, each grounded with a
diagram, fact-anchors (real numbers), and one concrete instance — and by **stating the reading order and
why** ("Accounts before Programs before PDAs before CPIs, because each builds on the last"). It is the
"understand *why* it works the way it works" layer.

## Route for (triggers)
- Solana's account model needs grounding before anyone can build (almost always true for newcomers).
- The **opening module** of nearly any developer course (the mental-model block).
- Conceptual or **non-technical** courses where the outcome is *understanding*, not shipping.
- Audiences who stall because they're pattern-matching without a model.

## Anti-triggers (don't lead with this when…)
- The audience are **motivated builders who learn by shipping** — a whole concept-spine course goes passive
  and gets abandoned (the textbook tell). Feed a build pattern instead.
- You're tempted to **front-load everything** — only teach the model as far as the first build needs;
  defer the rest to just-in-time (`design-spine.md` §4).

## The structure it produces
An ordered concept sequence walking the DAG (`references/solana-syllabus-dag.md`):
```
M1 Concept path: blockchain-as-state-machine → why-Solana (PoH/parallelism/fees)
   → Accounts → Programs → Instructions → Transactions/Fees → PDAs → CPIs
   each concept = { advance-organizer · definition · diagram · fact-anchors (exact numbers) ·
                    one concrete micro-example · "why this comes here" · retrieval question }
```
Then it **hands the model to a build pattern** (challenge-ladder / overview-lab-challenge).

## Why it works (mechanism)
Learning hierarchies (Gagné) + advance organizers + concrete-before-abstract + cognitive-load management:
one concept at a time, each anchored before the next depends on it.

## Stacks with
Opener for **map-from-known** (frame each concept against the learner's prior model); backbone that feeds
**challenge-ladder** or **overview-lab-challenge**; pairs with **build-it-twice** when depth ("why the
abstraction exists") is the goal. Never let it run the whole course for a hands-on audience.

## Voice handoff
Concept lessons tend to `derive-why` (Vitalik) for contested/intricate ideas or `show-how` (Helius) for
documented mechanics; the course opener is `motivate` (Kaue's spine). Tag per concept, not per module.

## Worked micro-illustration (Solana)
> Opening module, web2-dev audience. Concept 3 = **Programs**. Advance-organizer: "a program is a
> stateless function; its state lives in accounts you pass in." Diagram of program-account vs data-account.
> Fact-anchor: programs are immutable-by-default, deployed to an address. Concrete: point at the
> hello-world they'll build next. "Why here: you can't understand instructions until you know what a
> program *is*." Retrieval: "where does a Solana program keep its state?" `dominant_job: derive-why`.

## What this pattern deliberately EXCLUDES
It is **not the build engine** — on its own it produces passive courses. It does not handle syntax
onboarding (that's **completion-loop**) and it does not, by itself, prove capability (pair it with a build
+ assessment). Resist making it exhaustive; it grounds, it doesn't cover everything.

## Pulled from
Solana docs Core Concepts (states the order in prose) · RiseIn "Smart Contract Fundamentals" · Cyfrin
"Core Concepts" · Ackee lectures · the Anchor Book's concept pages.
