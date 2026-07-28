# Rendering a `visual` spec into an on-brand image

The writing pipeline leaves ` ```visual ` specs (type/title/purpose/data/prompt/alt).
The **render pass** turns each into an on-brand PNG the Claude-Design way: author HTML/CSS,
render it through WeasyPrint. Load `../brand/brand-guide.md` (tokens + palette) alongside this.

## The loop
1. `render_visuals.py extract <course>` — the work-list of every `visual` block.
2. `render_visuals.py scaffold <course>` — writes one brand-linked starter `lessons/assets/<lesson>/v<NN>-<type>.html` per block (canvas 1600×900, links `_brand.css`, the spec inlined as a comment).
3. **You author each `.viz`.** Open the starter, replace `<!-- TODO(render) -->` with real on-brand HTML that renders the spec's `data`. This is the creative step.
4. `render_visuals.py render <course>` — WeasyPrint → PDF → PNG (deterministic, no browser). `check` reports coverage.

## Two rules
- **`data` + `prompt` drive CONTENT; the brand drives STYLE.** Render exactly the nodes/rows/series the `data` names, in the structure the `prompt` describes. Ignore any styling words in an old `prompt` ("dark background, monospace, no icons") — those predate the brand; the look comes from the tokens, not the prompt.
- **WeasyPrint-safe CSS only.** OK: flexbox, grid, absolute positioning, borders, `border-radius`, `linear/radial-gradient`, `@font-face`, 2D transforms, inline `<svg>`. NOT OK (silently dropped or breaks reproducibility): `box-shadow`, `font-stretch`, `background-image: url()`, JavaScript, animation. Separate elements with borders / tint fills / full-bleed fields, never shadow.

## House style (every visual)
- Sits on the cream page; the content lives in a white card (`--surface-card`, `--radius-2xl`) OR a full-bleed emerald/dark field for a punchier one. Generous padding (`--space-7/8`).
- Lead with a short **eyebrow** (`class="stbr-eyebrow"`, the spec's one-line purpose or a 2-4 word tag) then the **title** as an Archivo heading (`<h2>`/`<h3>`, `--weight-black` for display weight since width is unavailable).
- **Emerald is the hero, yellow is the accent** — colour the ONE thing that matters yellow (the drop point, the winner, the highlighted bar); everything else greens/ink on white. Never yellow text on cream, never emerald text on dark.
- Optional: one morph blob bleeding off a corner as decoration — a sized `<div>` with an organic `border-radius` (e.g. `border-radius:47% 53% 44% 56% / 58% 42% 58% 42%`) filled `--stbr-yellow`/`--stbr-emerald`, `position:absolute`, partly off-canvas, `overflow:hidden` on the card. Never on top of text. Skip it if the diagram is dense.
- Text: Inter for labels/body, dark on light. Keep it legible at a glance; a diagram is not a paragraph.

## Connectors & arrows (WeasyPrint-safe)
Use **inline `<svg>`** for arrows/lines (a `<line>`/`<path>` in `--stbr-dark` or `--stbr-emerald`, ~2px, with a small triangle `<polygon>` arrowhead), OR CSS: a thin `<div>` line + a `::after` triangle via `border`. Label an arrow with a small Inter chip beside it. For a grid of nodes, place nodes with flex/grid and draw the connectors in one absolutely-positioned full-size `<svg>` layer behind them.

## Per type
- **flowchart** — nodes as white rounded boxes (dark title + optional Inter sub-line), left-to-right or top-down, arrows between. Mark the failure/drop node in yellow. One idea per node.
- **diagram** (architecture / dataflow) — component boxes + labeled connectors; if there's a "foundation" (a node the others sit on), make it a wide emerald/dark bar with cream type; others are white cards above it.
- **chart** — CSS bars/columns (`<div>` heights proportional to the real numbers — never fake them), emerald fill, the highlighted series/bar in yellow; Inter axis + value labels; a one-line caption.
- **table** — designed data table: header row `--surface-inverse` (or emerald) with cream type, body rows on white with `--border-subtle` dividers, alternating `--surface-paper` optional; shade the key row/cell faint yellow.
- **comparison** — 2–3 column cards side by side, a column header each, aligned attribute rows; a full-width **verdict band** at the bottom in emerald with cream type stating the takeaway.
- **annotated-code** — a dark code panel (`--surface-inverse`, `--font-mono`, cream text) with the snippet; call-outs in emerald/yellow chips pointing at the line that matters (an inline `<svg>` connector or an offset label).
- **timeline** — a horizontal rule with dot nodes, labels alternating above/below, dates/steps in Inter; the emphasized span drawn as a thicker emerald or yellow segment.

## Fidelity check before render
Every node/row/series in `data` appears; the one accent is the spec's actual point; contrast is legible; nothing relies on shadow; no `background-image`. Then `render`.
