# The three-layer model

How the skill composes (the course form; other forms route via `forms/FORMS.md` first). (Sibling note: `writer-style` has a *two*-layer model —
primary voice + secondary craft. Course architecture needs three.)

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. DESIGN SPINE  (design-spine.md)         — ALWAYS ON         │
   │    backward design · DAG-as-law · build-first · manage load ·  │
   │    fading triad · gate-on-doing · name-the-tradeoff           │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. PATTERN LAYER (patterns/*.md)           — ROUTED, not all   │
   │    1 backbone + a lesson template + ≤2 guests, chosen by       │
   │    OUTCOME + AUDIENCE (routing/ROUTING.md), never by topic     │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. DOMAIN REFERENCE (solana-syllabus-dag)  — THE CONSTRAINT    │
   │    prerequisite DAG · artifact ladder · token/security paths   │
   └──────────────────────────────────────────────────────────────┘
        the spine says HOW to teach · the patterns say HOW to SHAPE
        the course · the DAG says WHAT Solana forces on the order
```

## What each layer decides
- **Spine (always on).** The non-negotiables applied to *every* course regardless
  of topic or audience. You never skip it and never "turn it down." It is the
  reason a generated course feels like a builder's path, not a textbook.
- **Patterns (routed).** Reusable structural archetypes. The router picks them
  from the **terminal outcome + the learner's prior model** — not the subject. A
  course is **one backbone** (the primary shape) **+ one lesson template** (almost
  always `overview-lab-challenge`) **+ ≤2 guest patterns** (different jobs, not
  fighting the backbone).
- **Domain DAG (the constraint).** Solana's real dependency order. It is *law*:
  the spine and patterns arrange teaching, but they may never violate the DAG
  (accounts → programs → PDAs → CPIs → tokens → security). The validator enforces
  this mechanically.

## The stacking budget (keep it tight)
- **1 backbone + 1 lesson template + ≤2 guests.** Three or more co-leading
  patterns is a smell — either cut to the budget or split the course into tracks.
- **Never co-lead two build engines.** `challenge-ladder` and, say, a second
  build backbone fight each other; pick one and demote the other to a guest tier.
- **Guest-only jobs.** `frame` (Balaji) and `demystify` (Hotz) are guest moves in
  `writer-style`, so at the architecture level they're guest *positions*, not
  whole-lesson backbones. Tag a lesson's `dominant_job` as `frame`/`demystify`
  only when that move genuinely *leads* the lesson (the validator flags it
  advisory so you confirm).

## The runtime discipline (context stays lean)
The router (step 4) *names* the chosen patterns; step 5 **loads only those files**
— never all of `patterns/`. The spine is small and always loaded; the DAG is
loaded when sequencing. This keeps each architecture pass cheap and focused.

See `SKILL.md` for the step-by-step procedure, `routing/ROUTING.md` for the router,
and `design-spine.md` for the always-on rules.
