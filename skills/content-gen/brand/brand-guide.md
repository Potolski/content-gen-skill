# Superteam Brasil brand core

The shipped, token-driven brand system for on-brand visual rendering. Every generated
visual links `styles.css` (below) and uses its tokens. Aesthetic target: **Claude Design**
meets Superteam Brasil, "warm, earthy, optimistic". Flat, editorial, generous whitespace.

## Files here
- `styles.css` — the design system: color/type/spacing/effect tokens + base element styles. Link this one file. Fonts (Archivo + Inter) load via a Google Fonts `@import` at the top.
- `assets/shapes/morth-01…28.svg` — 28 organic "morph" blobs. Use LARGE as background decoration, bleeding off an edge. Recolor to a brand fill. Never outline, shadow, or shrink to a tiny icon.
- `assets/logos/{symbol,horizontal}-{emerald,cream,dark}.svg` — the mark. Use `cream` on emerald/dark fields, `emerald`/`dark` on cream. Never stretch, rotate, recolour outside the palette, or add effects. Most course visuals need NO logo; add it only for covers/title cards — the course banner (`references/banner.md`, `render_visuals.py scaffold-banner`) is exactly that case and defaults to `horizontal-emerald.svg` on the cream card.

## Palette (use the semantic tokens, not raw hex)
| role | token | value |
|---|---|---|
| hero green | `--stbr-emerald` / `--surface-brand` | `#008B4C` |
| deep green | `--stbr-green` / `--surface-brand-deep` | `#306C40` |
| accent | `--stbr-yellow` / `--surface-accent` | `#FFD23F` |
| page bg | `--stbr-cream` / `--surface-page` | `#F5E8CA` |
| ink / dark field | `--stbr-dark` / `--surface-inverse` | `#1B231D` |
| card | `--surface-card` | `#FFFFFF` |

**Default pairing: dark-green text (`--text-primary`) on cream (`--surface-page`), inside a white card (`--surface-card`).** For impact, use a full-bleed emerald or dark field (`--surface-brand` / `--surface-inverse`) with cream type (`--text-on-brand` / `--text-on-dark`). **Emerald is the hero; yellow is the accent** (use it sparingly, for the one thing that matters). Neutral text ramp: `--text-secondary`, `--text-muted`. Borders: `--border-subtle` (dividers), `--border-strong`.

## Type
- **Display** (`h1`–`h4`, `.stbr-eyebrow`): `var(--font-display)` = Archivo, weights 700/800/**900**. Headlines are lowercase or sentence-case; ALL-CAPS + `--tracking-caps` only for short eyebrow labels.
- **Body / labels**: `var(--font-body)` = Inter.
- **Code**: `var(--font-mono)`.
- Scale tokens: `--text-2xs … --text-6xl`; weights `--weight-regular … --weight-black`; line heights `--leading-tight/snug/normal`; tracking `--tracking-tight/wide/caps`.

## Vocabulary the generator should reach for
Surfaces `--surface-{page,paper,card,inverse,brand,brand-deep,accent}` · text `--text-{primary,secondary,muted,on-brand,on-accent,on-dark,link}` · borders `--border-{subtle,strong}` · radius `--radius-{sm,md,lg,xl,2xl,pill}` · spacing `--space-1…10` (8-pt) · families `--font-{display,body,mono}`. Prefer the semantic token over a raw `--stbr-*` hex.

## WeasyPrint constraints (the renderer)
Visuals render through WeasyPrint (HTML/CSS → PDF → PNG), which supports **flexbox, grid, absolute positioning, borders, gradients, `@font-face`, transforms** — but has limits to design around:
- **No `box-shadow`** (silently dropped). Fine: the brand is flat. Use `--border-subtle`/`--border-strong`, a tint fill, or a full-bleed field for separation instead of shadow.
- **`font-stretch` is dropped** (Archivo renders at normal width, not Semi-Expanded). Use **weight** (`--weight-black`) and size for display emphasis, not width.
- Use **solid colors and `linear/radial-gradient` only** — never `background-image: url(...)` (breaks reproducibility). Morph shapes go in as **inline `<svg>`** or CSS blobs (a sized `<div>` with an organic `border-radius`), recolored to a brand fill.
- **No JavaScript**, no animation (static render).
- Keep contrast legible: cream/emerald/dark give strong pairs; never put yellow type on cream, or emerald type on dark.
