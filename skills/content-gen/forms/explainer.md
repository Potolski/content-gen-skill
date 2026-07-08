# Form: explainer

The expository mechanism deep-dive — the single most common form of real Solana
writing ("how Turbine works", "the transaction lifecycle", "what Alpenglow
changes"). The reader comes out **understanding a mechanism**, building nothing and
being sold nothing. Sits between `tutorial` and `essay`: expository not
argumentative, understanding not artifact. Aliases: primer, deep-dive, "how X
works". If it defends a contestable claim, route `essay`; if the reader types code,
route `tutorial`.

**Length band:** 1500–4000 words. **Visuals default:** `light` — but one **hero
diagram** of the mental model is near-mandatory; it carries the no-code sections.

## Brief extras (beyond §F core)
- `mechanism` — the subsystem explained, scoped ("Turbine's shred propagation",
  not "Solana networking").
- `mental_model` — the scaffolding laid FIRST, before the mechanism (often an EVM
  or web2 contrast); the hero diagram draws this.
- `grounding_set` — the numbers/CU costs/version targets/program IDs to freeze.
- `code_or_diagram` — which carries each major section (protocol explainers run
  ~0% code, diagram-carried; framework how-tos run up to ~45% code).
- `lifespan` — `evergreen | timely`; timely pieces date themselves in the title.

## Structure recipe (the output IS)
1. **Hook** — the felt question ("how does a block reach 2,000 validators in
   400ms?"), never "In this article we will…".
2. **The mental model** — the simplified picture + hero diagram, before any
   internals.
3. **The mechanism** — one concept per H2, strictly bottom-up (each section builds
   on the last); for catalog-style pieces, a fixed repeatable micro-template per
   item (e.g. vulnerability → scenario → mitigation).
4. **The numbers** — the grounded magnitudes that make it real (CU, ms, counts),
   version-pinned.
5. **Limits & trade-offs** — where the mechanism strains; what it costs.
6. **Further reading** — a deliberate link web (docs, SIMD, source), not a recap.

## Checklist
- [ ] Mental model laid before mechanism; hero diagram present (or explicitly
      declined for a how-to subtype).
- [ ] One concept per section; bottom-up order survives a shuffle test.
- [ ] Every number/version in `grounding_set` frozen and pinned.
- [ ] No thesis smuggled in — if you're arguing, re-route to `essay`.
- [ ] Prose outweighs code; if inverted, this drifted into a `tutorial`.
