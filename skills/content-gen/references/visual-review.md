# Visual review — the QA pass over rendered visuals

The render pass (`visual-rendering.md`) turns each ` ```visual ` spec into a PNG. But authoring
agents self-verify **structurally** (div balance, no forbidden CSS) and mis-predict how WeasyPrint
lays out flex / absolute / text — so overlaps, overflows, and misaligned components slip through.
This pass is the fix: a dedicated visual QA by a **fresh reviewer (not the author)** that actually
LOOKS at each rendered PNG, backed by deterministic checks. A course's visuals are not "done"
until this pass is clean.

## Two layers

1. **Automated (deterministic)** — `render_visuals.py review <course>` flags, per card:
   - **overflow** — the render spans >1 page (content taller than the 1600×900 canvas);
   - **forbidden CSS** in the authored `.viz` (`box-shadow`, `background-image:url(`,
     `font-stretch`, `position:fixed`, `display:contents` — WeasyPrint ignores the last
     one, so a grid/flex child relying on it lands wrong).
   `render` also FAILS any card whose PDF spans >1 page. This catches the overflow class 100% — it
   cannot see internal overlaps, which is layer 2.

2. **Visual (a reviewer VIEWS every PNG)** — necessary because most glitches are internal layout
   defects the static pass can't see. Use a **fresh agent**, not the one that authored the card,
   and actually open each PNG.

## Glitch checklist — fail the card if ANY is true
- **Overflow / clipping** — text or a box cut at an edge, or content pushed off / missing.
- **Text overlap / collision** — a heading runs into body text; labels stack; lines touch.
- **Overlapping / misaligned panels** — cards or bars overlap, a panel sits half over another, or
  a row is offset from the row it should align with.
- **Out of bounds** — a component touches or bleeds past the canvas edge, or a chip/label spills
  outside its container. (Only the corner/border decoration may touch the edges.)
- **Malformed borders / nested boxes** — a doubled or misaligned border; an inner box that
  doesn't fit its parent.
- **Unanchored connectors** — arrow/SVG lines that don't start/end on the node they connect;
  arrowheads pointing at empty space.
- **Contrast / readability** — text too small; low-contrast pairing; text on the wrong background
  (dark text over a dark field, a label over a colored shape).
- **Decoration over content** — a background blob on top of / obscuring text or boxes (decoration
  must stay behind, in the margins).
- **Empty / broken region** — a blank card, a missing element the spec calls for, a stray artifact.

## The loop
1. `render_visuals.py review <course>` → note the automated flags.
2. VIEW every PNG (fresh reviewer) → per card, a verdict: **pass**, or **fail + the specific defect
   and its fix**.
3. Re-author each failing card's `.viz` (author agent, given the exact defect — apply the *Fit &
   safety* rules in `visual-rendering.md`).
4. `render_visuals.py decorate` + `render` (overflow now FAILS the render).
5. Re-review until **zero fails** on both layers.
