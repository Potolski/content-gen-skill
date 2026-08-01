# Form: essay

A thesis-driven long-form argument. The reader comes out able to *defend or attack a
position*, not run a command. If the piece's spine is steps, route `tutorial`; if
it's a tour of an artifact, route `walkthrough`.

**Length band:** 1000–3500 words. **Visuals default:** `light` (charts for the
load-bearing numbers; skip decoration).

**Sub-mode: `expository`** — the mechanism deep-dive in essay register with no
contestable thesis (most Solana protocol writing). Replace `thesis` with a
`mental_model_promise`, make `steelman` optional, and anchor rigor instead on a
**required hero diagram** for any multi-hop mechanism plus **required
trade-offs/limitations**. Don't force a fake argument onto expository material —
and if the venue is a company blog rather than a research blog, consider routing
`explainer` instead (same payload, different register).

## Brief extras (beyond §F core)
- `thesis` — one falsifiable sentence. "X matters" is not a thesis; "X will replace Y
  for workload Z because W" is.
- `steelman` — the best argument against the thesis; the essay must engage it, not a
  strawman.
- `evidence_plan` — the 3–5 grounded facts/numbers the argument stands on.

## Structure recipe (the output IS)
1. **Hook** — the tension that makes the thesis worth arguing (a price, an outage,
   a migration, a fight).
2. **Thesis stated** — early and plainly; the reader knows what's being claimed by
   the end of the first section.
3. **The argument** — each section advances one link of the chain with its grounded
   evidence; concrete before abstract.
4. **The steelman** — the opposing case at full strength, and why the thesis
   survives it (or where it honestly doesn't — scope the claim).
5. **So what** — what the reader should do or watch differently now.

## Checklist
- [ ] Thesis falsifiable + steelman real (thesis mode) / hero diagram + limitations present (expository mode).
- [ ] Every load-bearing number grounded and frozen pre-writing.
- [ ] No section that doesn't advance the chain (cut the survey padding).
- [ ] Trade-offs named on any recommendation (`../design-spine.md` §7).
