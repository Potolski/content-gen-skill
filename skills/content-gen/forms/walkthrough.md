# Form: walkthrough

A guided tour of something that already exists — a repo, a program, a protocol flow,
a transaction. The reader builds nothing; they come out able to navigate and reason
about the artifact. If the reader builds, it is a `tutorial`.

**Subtypes** (`subtype: article | repo`):
- `article` (default) — standalone piece, reader has no repo open. 1000–3000
  words; visuals `light` (dataflow diagrams earn their keep here more than
  anywhere); Hook required.
- `repo` — an annotated README/doc that rides next to the code, reader has the
  repo open. 50–400 words; tables and code fences over diagrams; Hook optional
  (lookup-density, not teaching-density).

## Brief extras (beyond §F core)
- `subject_ref` — the exact artifact toured: repo+commit, program id, tx signature,
  protocol version. Pin it; walkthroughs rot when the subject moves.
- `waypoints` — the ordered stops of the tour (file/function/account/instruction),
  each with the one thing to see there.
- `vantage` — the thread that orders the stops: a user action traced end-to-end, a
  lifecycle, an attack path.

## Structure recipe (the output IS)
1. **Hook** — why anyone opens this hood (a bug, a fee, a design rumor, an exploit).
2. **The map** — the vantage in one paragraph + where we'll stop (this is the anchor
   visual at `light`+).
3. **Waypoints** — one section per stop: show the real code/data (quoted, pinned),
   say what it does, say *why it's this way* — the design decision or constraint.
4. **The trade-off** — what this design buys and what it costs; what you'd do
   differently and when.
5. **Where to go next** — 2–3 concrete follow-the-thread pointers into the subject.

## Checklist
- [ ] `subject_ref` pinned (commit/version/signature) and every quote real.
- [ ] Each waypoint names a *why*, not just a *what*.
- [ ] The vantage thread survives start to finish — no detours that drop it.
- [ ] Trade-off named; claims grounded (`../references/research-grounding.md`).
