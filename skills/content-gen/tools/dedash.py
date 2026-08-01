#!/usr/bin/env python3
"""dedash.py — strip em-dashes (a top AI tell) from generated drafts, deterministically.

The em-dash is the single most recognizable machine tell, and the house policy is
to ship none. writer-style's linter only *advises* on em-dash overuse and counts
the whole file (so it over-reports our `visual` blocks); this is the enforcement
side: a mechanical pass that replaces em/en-dashes (and the spaced double-hyphen
evasion) with grammatical punctuation everywhere EXCEPT inside real code fences,
where a dash could be syntax. Idempotent.

    python3 dedash.py <course_dir>     # de-dash every lessons/drafts/*.md in place
    python3 dedash.py --file <draft>   # one file
    python3 dedash.py --selftest
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from course_lib import dedash_text, count_prose_emdashes  # noqa: E402


def dedash_file(p: Path) -> int:
    before = p.read_text("utf-8")
    after = dedash_text(before)
    if after != before:
        p.write_text(after, "utf-8")
    return count_prose_emdashes(after)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="strip em-dashes from drafts")
    ap.add_argument("target", nargs="?", help="course dir (de-dashes lessons/drafts/*.md)")
    ap.add_argument("--file", help="a single markdown file")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()
    files = []
    if a.file:
        files = [Path(a.file)]
    elif a.target:
        d = Path(a.target) / "lessons" / "drafts"
        files = sorted(d.glob("*.md")) if d.is_dir() else [Path(a.target)]
    if not files:
        print("dedash: pass a course dir or --file", file=sys.stderr)
        return 2
    total = 0
    for f in files:
        if not f.is_file():
            continue
        left = dedash_file(f)
        total += left
        print(f"  {f.name}: {left} em-dash(es) remain (in code fences, left intact)")
    print(f"dedash: done; {total} em-dash(es) remain outside code (should be 0)")
    return 0


def _selftest() -> int:
    ok = True
    def chk(c, m):
        nonlocal ok; print(("PASS" if c else "FAIL") + " - " + m); ok = ok and c
    chk(dedash_text("the fix — a clean env — nothing else.") == "the fix, a clean env, nothing else.",
        "spaced em-dashes -> commas")
    chk(dedash_text("word—word") == "word, word", "unspaced em-dash -> comma")
    chk(dedash_text("a range 1 -- 2") == "a range 1, 2", "spaced double-hyphen -> comma")
    code = "```bash\ncargo build --release  # a — b\n```\n"
    chk("—" not in dedash_text(code) and "cargo build --release" in dedash_text(code),
        "em-dash in a code comment -> hyphen, code intact")
    vis = "```visual\ndata: |\n  left: X — right: Y\n```\n"
    chk("—" not in dedash_text(vis), "em-dash inside a visual block IS stripped (it's prose spec)")
    chk(count_prose_emdashes("a — b\n```bash\nc — d\n```\n") == 1, "prose count excludes code fences")
    chk("---" in dedash_text("|---|---|"), "markdown table rule (hyphens) untouched")
    print("DEDASH SELFTESTS " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
