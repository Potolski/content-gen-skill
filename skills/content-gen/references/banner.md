# Course banner — the Academy thumbnail

The one **course-level** visual: the image the Academy course card shows at 400×225
(and the `/cover.png` fallback replaces when absent). Rendered through the same
WeasyPrint pipeline as lesson visuals, standardized to the STBR brand. Everything
lives in `content/courses/<id>/branding/` (gitignored with the course).

## The loop

```
# photo mode: drop the course art FIRST, then scaffold
cp <course-art>.png content/courses/<id>/branding/banner-bg.png
python3 tools/render_visuals.py scaffold-banner content/courses/<id>
#   ... author branding/banner.html: eyebrow, title, pill texts; delete the TODO marker ...
python3 tools/render_visuals.py render-banner   content/courses/<id>
#   -> branding/banner.png  (full-res, for the eyeball review — never ships)
#   -> branding/banner.webp (1600x900, <=1MiB — what the export picks up)
python3 tools/academy_export.py emit --course ... --out ...   # thumbnail: assets/banner.webp
```

`scaffold-banner` keeps an authored `banner.html` (no `TODO(render)` marker) — delete
the file or re-add the marker to reset. It also drops `_brand.css`, `_render.css`, and
`logo.svg` beside the banner so the HTML is self-contained and re-renderable.

## Two modes

- **Photo mode** (a `branding/banner-bg.{png,jpg,jpeg,webp}` exists): the photo is placed
  as an `<img class="bg">` **element**, not `background-image: url()` (which stays
  forbidden CSS). Because **WeasyPrint has no `filter`/`backdrop-filter`**, any blur or
  darkening is pre-baked by `render-banner` (Pillow: cover-crop to 1600×900, then blur +
  brightness). The banner HTML declares its own backdrop treatment with a directive:

      <!-- banner-bg: blur=0 brightness=1.0 file=banner-bg-sharp.png -->

  `blur`/`brightness` feed the bake; `file` is the baked filename the HTML's
  `<img class="bg">` must reference. No directive = the heavy title-card treatment
  (blur 14, brightness 0.72, `banner-bg-blur.png`). "Liquid glass" panels are faked:
  translucent fill + hairline light border + a gradient sheen (`background-color` rgba +
  `background-image: linear-gradient(...)`), which reads as glass over the photo.
- **Pure-brand mode** (no photo): cream page + the per-course `.stbr-decor` blob layer +
  a white card — the standard visual house style, so any course gets a banner even
  without art.

**House composition (chosen 2026-08): "scrim"** — the art ships sharp (`blur=0
brightness=1.0`), a top+bottom gradient scrim makes room, type sits straight on the
image, pills are glass chips. Explore alternatives beside the main file
(`branding/banner-<variant>.html`) and render each with
`render-banner <course> --html branding/banner-<variant>.html` (outputs
`<stem>.png/.webp` beside it, never picked up by the export); promote the winner by
copying it over `banner.html`.

## Card anatomy (what you author)

- `.stbr-eyebrow` — short kicker, e.g. `// SOLANA CORE`. Uppercase, emerald.
- `logo.svg` — the Superteam mark, `horizontal-emerald.svg` by default (the cream logo
  vanishes on the cream card). Swap the file in `branding/` to rebrand.
- `.card-title` — Archivo Black ~82px. The banner is judged at 400px wide: keep it
  punchy, break lines deliberately with `<br>`, shrink a couple of px only if a long
  title needs it.
- `.meta` pills — level pill (emerald), `NN LESSONS · NN HOURS` stat pill (outline;
  match the course language), XP pill (yellow) with the **inline-SVG bolt — never the ⚡
  emoji** (Pango emoji fallback is unreliable under WeasyPrint).
- Match the pill texts to the manifest: `academy.difficulty`, lesson count,
  `academy.duration` (hours — see academy-schema.md), `academy.xpReward`.

## Contract (upstream)

1600×900 render (16:9), shipped as `banner.webp` ≤ **1 MiB** (platform hard cap;
`render-banner` compresses on a quality ladder and FAILs past the cap). The export emits
`thumbnail: assets/banner.webp` in `course.yaml` and ships `banner.html` + `logo.svg` +
the original `banner-bg.*` to linter-ignored `visual-src/` so the banner stays
re-renderable. `branding/banner.png` (full-res) and `banner-bg-blur.png` (derived bake)
never ship.

## Review

View `branding/banner.png` before exporting (visual-review.md spirit): title legible at
25% zoom, pills on one line, logo not cramped, blur strong enough that backdrop detail
doesn't fight the title, fonts actually Archivo/Inter (Google Fonts `@import` needs
network at render time — a fallback-font render looks subtly wrong).
