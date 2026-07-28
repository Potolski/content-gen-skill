#!/usr/bin/env python3
"""render_visuals.py — turn a piece's ```visual specs into on-brand images.

The skill writes text + ` ```visual ` placeholder specs (type/title/purpose/data/prompt/
alt). This renders each spec the Claude-Design way: an AGENT writes on-brand HTML/CSS
(guided by references/visual-rendering.md + brand/brand-guide.md), and this tool wraps it
against the shipped brand stylesheet and renders it deterministically through **WeasyPrint**
(HTML/CSS → vector PDF) then rasterizes to PNG — no browser.

Split (mirrors verify_code): Python does the deterministic scaffolding + render; the model
does the creative HTML authoring in between.

    render_visuals.py extract  <course|--file X>   # the work-list: what to build
    render_visuals.py scaffold <course>            # write brand-linked <asset>.html starters
    #   ... agent fills each <asset>.html's .viz with on-brand markup ...
    render_visuals.py render   <course> [--dpi N]  # weasyprint -> PDF -> PNG (SKIP if absent)
    render_visuals.py check    <course>            # rendered vs unrendered report
    render_visuals.py --selftest

Assets land beside the lessons in `lessons/assets/<lesson-stem>/v<NN>-<type>.{html,pdf,png}`
(gitignored with the course). A FAIL is a real render error; SKIP = WeasyPrint/rasterizer
absent (install: `pip install weasyprint` + a rasterizer, or `pip install pymupdf`).
"""
from __future__ import annotations
import argparse
import hashlib
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from validate_course import _parse_visuals   # noqa: E402  (reuse the canonical parser)

SKILL = HERE.parent                          # skills/content-gen
BRAND_CSS = SKILL / "brand" / "styles.css"
RENDER_CSS = SKILL / "brand" / "render.css"
SHAPES_DIR = SKILL / "brand" / "assets" / "shapes"
CANVAS = (1600, 900)


def _slug(s: str) -> str:
    out = "".join(c if c.isalnum() else "-" for c in str(s).lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-") or "x"


# ---- brand "morph" decoration -------------------------------------------------
# The 28 organic shapes are the brand's background vocabulary. Each visual gets a
# UNIQUE arrangement, chosen deterministically from a hash of its asset_id so renders
# stay reproducible (no Math.random / wall-clock). Content = the spec; this = the style.
_SHAPES_CACHE: dict[str, tuple[str, str]] | None = None
_DECOR_RE = re.compile(r'<div class="stbr-decor".*?</div>\s*', re.DOTALL)


def _shapes() -> dict[str, tuple[str, str]]:
    """Load the morph SVGs once as {stem: (viewBox, inner_markup)}. The internal
    <defs>/<style> and class/id/fill attrs are stripped so we can recolour via a
    parent <g fill> (dodges the inline-SVG `.cls-1` collision + WeasyPrint quirks)."""
    global _SHAPES_CACHE
    if _SHAPES_CACHE is None:
        out: dict[str, tuple[str, str]] = {}
        for p in sorted(SHAPES_DIR.glob("morth-*.svg")):
            raw = p.read_text("utf-8")
            m = re.search(r'viewBox="([^"]+)"', raw)
            vb = m.group(1) if m else "0 0 100 100"
            body = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")]
            body = re.sub(r"<defs>.*?</defs>", "", body, flags=re.DOTALL)
            body = re.sub(r'\s(?:class|id|fill|style)="[^"]*"', "", body)
            out[p.stem] = (vb, body.strip())
        _SHAPES_CACHE = out
    return _SHAPES_CACHE


def _blob(rng, shapes, corner, key, fill, d_lo, d_hi, op_lo, op_hi) -> str:
    """One morph <svg>, bled off `corner`, with a random size/rotation/flip/opacity.
    `d` is the target LONGEST side; the rendered width/height follow the shape's own
    aspect ratio, and each corner offset is a fraction of THAT axis's size — so ~half
    the shape always stays on the page whether it's tall-narrow, wide-short, or round."""
    vb, body = shapes[key]
    p = vb.split()
    vbw, vbh = float(p[2]), float(p[3])
    d = rng.randint(d_lo, d_hi)
    w = round(vbw * d / max(vbw, vbh))
    h = round(vbh * d / max(vbw, vbh))
    # Bleed only a little: morphs don't fill their viewBox, so a big off-corner offset
    # can push the FILLED mass off-page. Keeping ~78-90% on-page reliably shows the shape.
    hx = -int(w * rng.uniform(0.10, 0.22))
    hy = -int(h * rng.uniform(0.10, 0.22))
    opacity = round(rng.uniform(op_lo, op_hi), 3)
    rot = rng.choice([0, 15, -15, 25, -25, 180])      # small angles keep the footprint predictable
    flip = " scaleX(-1)" if rng.random() < 0.5 else ""
    pos = {"tr": f"top:{hy}px;right:{hx}px;", "br": f"bottom:{hy}px;right:{hx}px;",
           "bl": f"bottom:{hy}px;left:{hx}px;", "tl": f"top:{hy}px;left:{hx}px;"}[corner]
    style = f"width:{w}px;{pos}opacity:{opacity};transform:rotate({rot}deg){flip};"
    return f'<svg viewBox="{vb}" style="{style}"><g fill="{fill}">{body}</g></svg>'


def _decor(asset_id: str) -> str:
    """A unique <div class="stbr-decor"> layer for this asset. Base: two green blobs
    on OPPOSITE corners (the diagonal frame that always reads), varied by which
    diagonal / shapes / sizes / rotations / emerald-vs-green. Plus an occasional third
    accent blob (may be yellow — safe because it's additive, never the sole element).
    Deterministic from asset_id, so every visual is distinct yet reproducible."""
    shapes = _shapes()
    keys = sorted(shapes)
    if len(keys) < 2:
        return ""
    rng = random.Random(int(hashlib.sha256(asset_id.encode("utf-8")).hexdigest()[:16], 16))
    diag = rng.choice([("tr", "bl"), ("tl", "br")])
    greens = ["#008b4c", "#306c40"]
    rng.shuffle(greens)
    pool = rng.sample(keys, len(keys))                  # distinct shapes, shuffled
    svgs = [_blob(rng, shapes, diag[0], pool[0], greens[0], 440, 620, 0.16, 0.22),
            _blob(rng, shapes, diag[1], pool[1], greens[1], 440, 620, 0.16, 0.22)]
    if rng.random() < 0.33 and len(keys) >= 3:          # occasional third accent
        free = rng.choice([c for c in ("tr", "br", "bl", "tl") if c not in diag])
        fill = rng.choice(["#008b4c", "#306c40", "#ffd23f"])
        lo, hi = (0.19, 0.26) if fill == "#ffd23f" else (0.12, 0.17)
        svgs.append(_blob(rng, shapes, free, pool[2], fill, 300, 430, lo, hi))
    return '<div class="stbr-decor" aria-hidden="true">\n  ' + "\n  ".join(svgs) + "\n</div>\n"


def work_list(course_dir: Path):
    """Every visual block across the course's drafts, as render work items."""
    drafts = course_dir / "lessons" / "drafts"
    items = []
    for draft in sorted(drafts.glob("*.md")):
        blocks, _ = _parse_visuals(draft.read_text("utf-8"))
        for i, b in enumerate(blocks, 1):
            f = b["fields"]
            vtype = _slug(f.get("type", "diagram"))
            asset_id = f"{draft.stem}/v{i:02d}-{vtype}"
            base = course_dir / "lessons" / "assets" / f"{draft.stem}" / f"v{i:02d}-{vtype}"
            items.append({
                "lesson": draft.stem, "idx": i, "type": f.get("type", ""),
                "title": f.get("title", ""), "purpose": f.get("purpose", ""),
                "data": f.get("data", ""), "prompt": f.get("prompt", ""),
                "alt": f.get("alt", ""), "asset_id": asset_id,
                "html": base.with_suffix(".html"), "pdf": base.with_suffix(".pdf"),
                "png": base.with_suffix(".png"),
            })
    return items


_STARTER = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="{css}">
<link rel="stylesheet" href="{render_css}">
<style>
  @page {{ size: {w}px {h}px; margin: 0; }}
  html, body {{ margin: 0; }}
  body {{ width: {w}px; height: {h}px; display: flex; align-items: center;
         justify-content: center; background: var(--surface-page); padding: 72px; }}
  .viz {{ position: relative; width: 100%; }}
</style></head>
<body>
<!-- {type}: {title}
     purpose: {purpose}
     data: {data}
     prompt: {prompt}
     BUILD .viz as on-brand HTML per skills/content-gen/references/visual-rendering.md.
     Header: <div class="stbr-eyebrow">..</div> + <h2 class="viz-title">..</h2>.
     Leave the .stbr-decor block untouched (per-asset brand decoration).
     WeasyPrint-safe CSS only: flexbox/grid/borders/gradients; NO box-shadow, NO
     background-image url(), NO JS. Use brand tokens (--surface-*, --text-*, --stbr-*). -->
{decor}<div class="viz">
  <!-- TODO(render): build this visual -->
</div>
</body></html>
"""


def cmd_scaffold(course_dir: Path) -> int:
    items = work_list(course_dir)
    assets = course_dir / "lessons" / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    # shared copies of the brand + render stylesheets, linked relatively (portable)
    local_css = assets / "_brand.css"
    if BRAND_CSS.is_file():
        local_css.write_text(BRAND_CSS.read_text("utf-8"))
    local_render = assets / "_render.css"
    if RENDER_CSS.is_file():
        local_render.write_text(RENDER_CSS.read_text("utf-8"))
    written = kept = 0
    for it in items:
        it["html"].parent.mkdir(parents=True, exist_ok=True)
        if it["html"].exists() and it["html"].read_text("utf-8").count("TODO(render)") == 0:
            kept += 1                                    # already filled by the agent, don't clobber
            continue
        it["html"].write_text(_STARTER.format(
            css=_rel(it["html"], local_css), render_css=_rel(it["html"], local_render),
            decor=_decor(it["asset_id"]), w=CANVAS[0], h=CANVAS[1],
            type=it["type"], title=it["title"],
            purpose=it["purpose"], data=it["data"], prompt=it["prompt"]))
        written += 1
    print(f"scaffold: {written} starter(s) written, {kept} filled asset(s) kept "
          f"({len(items)} visual blocks total) -> {assets}")
    return 0


def cmd_decorate(course_dir: Path) -> int:
    """(Re)apply the per-asset morph decoration to every asset HTML — refreshes the
    _render.css link + swaps in each asset's unique .stbr-decor block. Idempotent:
    the block is a stable function of asset_id. Use to retrofit already-authored
    visuals or re-roll the look after tuning render.css / _decor()."""
    assets = course_dir / "lessons" / "assets"
    if RENDER_CSS.is_file():
        (assets / "_render.css").write_text(RENDER_CSS.read_text("utf-8"))
    changed = 0
    for it in work_list(course_dir):
        h = it["html"]
        if not h.exists():
            continue
        s = h.read_text("utf-8")
        if "_render.css" not in s:
            s = s.replace('<link rel="stylesheet" href="../_brand.css">',
                          '<link rel="stylesheet" href="../_brand.css">\n'
                          '<link rel="stylesheet" href="../_render.css">', 1)
        block = _decor(it["asset_id"])
        s = (_DECOR_RE.sub(block, s, count=1) if 'class="stbr-decor"' in s
             else s.replace('<div class="viz">', block + '<div class="viz">', 1))
        h.write_text(s)
        changed += 1
    print(f"decorate: {changed} asset(s) given unique morph decoration -> {assets}")
    return 0


def _rel(html: Path, css: Path) -> str:
    import os
    return os.path.relpath(css, html.parent)


def _rasterize(pdf: Path, png: Path, dpi: int) -> tuple[bool, str]:
    try:
        import fitz  # pymupdf
        doc = fitz.open(str(pdf))
        doc[0].get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=False).save(str(png))
        doc.close()
        return True, "pymupdf"
    except ModuleNotFoundError:
        pass
    if shutil.which("pdftoppm"):
        r = subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-singlefile",
                            str(pdf), str(png.with_suffix(""))],
                           capture_output=True, text=True)
        return (r.returncode == 0 and png.exists()), "pdftoppm"
    if shutil.which("mutool"):
        r = subprocess.run(["mutool", "draw", "-r", str(dpi), "-o", str(png), str(pdf), "1"],
                           capture_output=True, text=True)
        return (r.returncode == 0 and png.exists()), "mutool"
    return False, "no-rasterizer"


def cmd_render(course_dir: Path, dpi: int, only: str | None) -> int:
    if not shutil.which("weasyprint"):
        print("render: SKIP - weasyprint not installed "
              "(`pip install weasyprint`; needs pango/cairo). No images produced.", file=sys.stderr)
        return 0
    items = [it for it in work_list(course_dir) if not only or only in it["asset_id"]]
    todo = [it for it in items if it["html"].exists()
            and "TODO(render)" not in it["html"].read_text("utf-8")]
    skipped = len(items) - len(todo)
    ok = fail = 0
    for it in todo:
        r = subprocess.run(["weasyprint", str(it["html"]), str(it["pdf"])],
                           capture_output=True, text=True)
        if r.returncode != 0 or not it["pdf"].exists():
            fail += 1
            print(f"  FAIL {it['asset_id']}: {(r.stderr or 'weasyprint error').strip().splitlines()[-1][:80]}")
            continue
        rok, how = _rasterize(it["pdf"], it["png"], dpi)
        if rok:
            ok += 1
        else:
            fail += 1
            print(f"  FAIL {it['asset_id']}: rasterize failed ({how})")
    print(f"render: {ok} PNG · {fail} FAIL · {skipped} not-yet-authored (still a TODO starter) "
          f"[dpi={dpi}]")
    return 1 if fail else 0


def cmd_extract(course_dir: Path, file: str | None) -> int:
    items = work_list(course_dir) if not file else _file_items(Path(file))
    print(f"{'asset_id':46} {'type':14} title")
    for it in items:
        print(f"{it['asset_id']:46} {it['type']:14} {it['title'][:60]}")
    print(f"\n{len(items)} visual block(s). Next: `scaffold`, author each .viz, then `render`.")
    return 0


def _file_items(md: Path):
    blocks, _ = _parse_visuals(md.read_text("utf-8"))
    out = []
    for i, b in enumerate(blocks, 1):
        f = b["fields"]
        out.append({"asset_id": f"{md.stem}/v{i:02d}-{_slug(f.get('type', 'x'))}",
                    "type": f.get("type", ""), "title": f.get("title", "")})
    return out


def cmd_check(course_dir: Path) -> int:
    items = work_list(course_dir)
    by_lesson: dict[str, list] = {}
    for it in items:
        by_lesson.setdefault(it["lesson"], []).append(it)
    total = done = 0
    for lesson, its in sorted(by_lesson.items()):
        rendered = sum(1 for it in its if it["png"].exists())
        total += len(its); done += rendered
        mark = "ok " if rendered == len(its) else "-- "
        print(f"  {mark}{lesson}: {rendered}/{len(its)} rendered")
    print(f"\ncheck: {done}/{total} visuals rendered across {len(by_lesson)} lessons")
    return 0


def selftest() -> int:
    ok = True
    def chk(c, m):
        nonlocal ok; print(("PASS" if c else "FAIL") + " - " + m); ok = ok and c
    chk(_slug("Annotated Code!") == "annotated-code", "slug kebabs + strips punctuation")
    chk(_slug("flowchart") == "flowchart", "slug passes clean type")
    md = ("# t\n\n```visual\ntype: flowchart\ntitle: A to B\npurpose: p\n"
          "data: |\n a -> b\nprompt: |\n draw it\nalt: a goes to b in one hop here ok\n```\n")
    import tempfile
    d = Path(tempfile.mkdtemp()); (d / "lessons" / "drafts").mkdir(parents=True)
    (d / "lessons" / "drafts" / "m01-l1-x.md").write_text(md)
    items = work_list(d)
    chk(len(items) == 1 and items[0]["asset_id"] == "m01-l1-x/v01-flowchart",
        "work_list builds a stable asset_id from the block")
    chk(items[0]["type"] == "flowchart" and "a -> b" in items[0]["data"], "carries type + data")
    cmd_scaffold(d)
    starter = items[0]["html"].read_text("utf-8")
    chk("TODO(render)" in starter and "_brand.css" in starter and "1600px 900px" in starter,
        "scaffold writes a brand-linked, canvas-sized starter")
    chk("_render.css" in starter and 'class="stbr-decor"' in starter and "<svg" in starter,
        "scaffold bakes in the render layer + per-asset decoration")
    d1 = _decor("m01-l1-x/v01-flowchart")
    chk('class="stbr-decor"' in d1 and d1.count("<svg") >= 2 and "morth" not in d1,
        "_decor emits a 2+ blob morph frame (no filename leak)")
    chk(_decor("m01-l1-x/v01-flowchart") == d1, "_decor is deterministic per asset_id")
    chk(d1 != _decor("m01-l1-x/v07-table"), "_decor varies across assets")
    cmd_decorate(d)
    redecor = items[0]["html"].read_text("utf-8")
    chk(redecor.count('class="stbr-decor"') == 1 and "_render.css" in redecor,
        "decorate keeps exactly one decor block + the render link")
    print("RENDER_VISUALS SELFTESTS " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="render ```visual specs into on-brand images")
    ap.add_argument("cmd", nargs="?",
                    choices=["extract", "scaffold", "decorate", "render", "check"])
    ap.add_argument("course", nargs="?")
    ap.add_argument("--file", help="extract from a single markdown file")
    ap.add_argument("--dpi", type=int, default=144, help="raster DPI (default 144 = 1.5x)")
    ap.add_argument("--only", help="render only asset_ids containing this substring")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if a.cmd == "extract":
        return cmd_extract(Path(a.course) if a.course else Path("."), a.file)
    if not a.course:
        print("render_visuals: pass a course dir", file=sys.stderr); return 2
    course = Path(a.course)
    if a.cmd == "scaffold":
        return cmd_scaffold(course)
    if a.cmd == "decorate":
        return cmd_decorate(course)
    if a.cmd == "render":
        return cmd_render(course, a.dpi, a.only)
    if a.cmd == "check":
        return cmd_check(course)
    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
