# Visual review — the QA pass over rendered visuals

The render pass (`visual-rendering.md`) turns each ` ```visual ` spec into a PNG. But authoring
agents self-verify **structurally** (div balance, no forbidden CSS) and mis-predict how WeasyPrint
lays out flex / absolute / text — so overlaps, overflows, and misaligned components slip through.
This pass is the fix: a dedicated visual QA by **independent, spec-grounded reviewers (not the
card's author)** that actually LOOK at each rendered PNG, backed by deterministic checks. A course's
visuals are not "done" until this pass is clean. Do it right: a lone casual glance is unreliable —
tested head-to-head it both *misses* real defects and *hallucinates* fake ones. Structure it (see
**The reviewer protocol**).

## Two layers

1. **Automated (deterministic)** — `render_visuals.py review <course>` flags, per card:
   - **overflow** — the render spans >1 page (content taller than the 1600×900 canvas);
   - **forbidden CSS** in the authored `.viz` (`box-shadow`, `background-image:url(`,
     `font-stretch`, `position:fixed`, `display:contents` — WeasyPrint ignores the last
     one, so a grid/flex child relying on it lands wrong).
   `render` also FAILS any card whose PDF spans >1 page. This catches the overflow class 100% — it
   cannot see internal overlaps, which is layer 2.

2. **Visual (independent reviewers VIEW every PNG)** — this is the layer that actually catches the
   internal defects (overlaps, misalignment, unanchored connectors, contrast) the static pass can't
   see. It is NOT a single casual glance — structure it per **The reviewer protocol** below.

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

## The reviewer protocol (per card)

A reviewer that just "looks and judges" is unreliable — tested head-to-head, a holistic reviewer
missed a missing-connector defect and, on a clean-ish card, failed it for defects that weren't there.
Four things make the visual pass reliable; use all four.

1. **Spec-grounded.** Give the reviewer the card's ` ```visual ` spec (type + data + prompt) — what
   the card MUST contain. A "fresh" reviewer with no spec can't tell a Merkle tree is *missing its
   connectors*; a spec-grounded one checks "the spec names six edges — are all six drawn and
   touching?" Grounding kills the "looks fine" default.
2. **Map it out, don't judge holistically.** Make the reviewer first inventory the render like a
   scene graph — every box (position), every connector (its two endpoints + does it visibly TOUCH
   both, or fall short into empty space), every label/chip (inside its box? inside the canvas?) —
   *before* any verdict. Enumeration surfaces "this line ends in a gap" that a gestalt glance skips.
3. **Adversarial / default-to-broken.** Prompt: "assume this card IS broken until you prove
   otherwise; if unsure about an endpoint or overlap, LEAN to DEFECT." This inverts the leniency
   that makes reviewers rubber-stamp. It does not cause runaway false positives — a spec-grounded
   structured reviewer still PASSES a genuinely clean card, and step 3 of the loop rules out the
   occasional false alarm cheaply.
4. **Redundancy + resolution — because even a good single reviewer is stochastic.** On a *subtle*
   defect (≈30px connector gap) one structured reviewer caught it only about half the time. So run
   **≥2–3 independent reviewers per card and let ANY fail flag it** (consensus-to-PASS, not
   consensus-to-fail — one catcher is enough). And view at fidelity: the ≤~1900px many-image cap
   puts a whole 1600×900 card near the detection floor for pixel-level gaps/overlaps, so have the
   reviewer **crop and zoom** the regions it is unsure about (connector endpoints, box edges)
   instead of judging from the downscaled whole.

Each reviewer outputs: `MAP` (the inventory) · `SPEC-CHECK` (each required element present+correct /
missing / wrong) · `DEFECTS` (bullets or none) · `VERDICT` (PASS only if every spec element is
present+correct AND zero defects; else FAIL + the specific defect).

## The loop
1. `render_visuals.py review <course>` → note the automated flags (overflow / forbidden CSS).
2. For each card, run **2–3 independent reviewers** with the protocol above. The card is flagged if
   **any** reviewer returns FAIL.
3. Re-author each flagged card's `.viz` (author agent, given the exact defect — apply the *Fit &
   safety* rules in `visual-rendering.md`). The author LOOKS at the render; if a flag was a false
   alarm (the card is actually clean), it says so and leaves the card — this self-corrects over-flags.
4. `render_visuals.py decorate` + `render` (overflow now FAILS the render).
5. Re-review until **zero fails** across the reviewers and the automated layer, then personally
   spot-check the cards that were flagged.
