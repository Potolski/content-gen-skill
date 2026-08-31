#!/usr/bin/env python3
"""Split a course's quizzes out of manifest.json so they can be edited per-lesson, then merge back.

Why this exists: every quiz in the wave lives in `manifest.json` under
`lessons[].brief.quiz_blocks`. That is ONE file, so a fan-out of per-lesson editors would
race on it. `split` writes one JSON file per lesson, `merge` folds them back, and `report`
measures the defect the whole thing is for:

  the correct option is the LONGEST option in ~94% of single-select questions

which lets a learner pass without reading. Position spread is already fine; length is the tell.
`merge` refuses to change correctness — it only accepts edited labels/feedback, so a rewrite
pass cannot silently move which option is right.

  quiz_balance.py report <course>
  quiz_balance.py split  <course>            -> <course>/lessons/quizzes/<stem>.json
  quiz_balance.py merge  <course>            -> rewrites manifest.json in place
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _stem(lesson: dict, modules: list) -> str:
    """Mirror the draft stem so quiz files line up with drafts/ and assets/."""
    idx = {m["id"]: i for i, m in enumerate(modules)}
    mi = idx.get(lesson.get("module"), 99)
    return f"m{mi:02d}-l{lesson.get('order', 0)}-{lesson['id']}"


def _load(course: Path) -> tuple[Path, dict]:
    mp = course / "manifest.json"
    return mp, json.loads(mp.read_text("utf-8"))


def _single_select(q: dict) -> bool:
    opts = q.get("options", [])
    return (not q.get("multiSelect")) and len(opts) >= 2 and \
        sum(1 for o in opts if o.get("correct")) == 1


def cmd_report(course: Path) -> int:
    _, m = _load(course)
    n = longest = 0
    pos: dict[int, int] = {}
    worst: list[tuple[int, str]] = []
    for l in m.get("lessons", []):
        for blk in (l.get("brief", {}) or {}).get("quiz_blocks", []) or []:
            for q in blk.get("questions", []):
                if not _single_select(q):
                    continue
                opts = q["options"]
                corr = next(o for o in opts if o.get("correct"))
                n += 1
                pos[opts.index(corr)] = pos.get(opts.index(corr), 0) + 1
                lens = [len(o.get("label", "")) for o in opts]
                if len(corr.get("label", "")) == max(lens):
                    longest += 1
                    gap = max(lens) - sorted(lens)[-2]
                    worst.append((gap, q.get("id", "?")))
    if not n:
        print("no single-select questions found")
        return 0
    print(f"single-select questions: {n}")
    print(f"position spread: {dict(sorted(pos.items()))}")
    print(f"correct-is-longest: {longest}/{n} = {longest / n:.0%}"
          f"   (a learner can guess by length above ~40%)")
    worst.sort(reverse=True)
    if worst:
        print("widest length gaps (answer chars minus runner-up):")
        for gap, qid in worst[:8]:
            print(f"  +{gap:>4} chars   {qid}")
    return 0


def cmd_split(course: Path) -> int:
    _, m = _load(course)
    out = course / "lessons" / "quizzes"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for l in m.get("lessons", []):
        blocks = (l.get("brief", {}) or {}).get("quiz_blocks") or []
        if not blocks:
            continue
        (out / f"{_stem(l, m.get('modules', []))}.json").write_text(
            json.dumps({"lesson": l["id"], "quiz_blocks": blocks}, indent=2, ensure_ascii=False) + "\n",
            "utf-8")
        n += 1
    print(f"split: {n} lesson quiz file(s) -> {out}")
    return 0


def cmd_merge(course: Path) -> int:
    mp, m = _load(course)
    src = course / "lessons" / "quizzes"
    if not src.is_dir():
        print(f"merge: nothing at {src} (run split first)", file=sys.stderr)
        return 2
    by_id = {l["id"]: l for l in m.get("lessons", [])}
    merged = changed = 0
    problems: list[str] = []
    for f in sorted(src.glob("*.json")):
        doc = json.loads(f.read_text("utf-8"))
        l = by_id.get(doc.get("lesson"))
        if l is None:
            problems.append(f"{f.name}: unknown lesson id {doc.get('lesson')!r}")
            continue
        old = (l.get("brief", {}) or {}).get("quiz_blocks") or []
        new = doc.get("quiz_blocks") or []
        # Correctness is structural, not editorial: a rewrite pass may change wording only.
        # If the shape or the correct answer moved, refuse the whole file rather than
        # silently republish a quiz whose key changed.
        def shape(blocks):
            return [[(q.get("id"), tuple(o.get("id") for o in q.get("options", [])),
                      tuple(bool(o.get("correct")) for o in q.get("options", [])))
                     for q in b.get("questions", [])] for b in blocks]
        if shape(old) != shape(new):
            problems.append(f"{f.name}: question/option ids or correctness changed — refusing")
            continue
        if old != new:
            changed += 1
        l["brief"]["quiz_blocks"] = new
        merged += 1
    for p in problems:
        print(f"  REFUSED {p}", file=sys.stderr)
    if problems:
        print(f"merge: aborted, {len(problems)} file(s) failed the correctness check", file=sys.stderr)
        return 1
    mp.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", "utf-8")
    print(f"merge: {merged} lesson(s) folded back, {changed} with edits -> {mp}")
    return 0


def _selftest() -> int:
    ok = True

    def chk(c, msg):
        nonlocal ok
        print(("PASS - " if c else "FAIL - ") + msg)
        ok = ok and bool(c)

    q_ok = {"id": "q1", "multiSelect": False,
            "options": [{"id": "a", "label": "x", "correct": True}, {"id": "b", "label": "yy"}]}
    chk(_single_select(q_ok), "single-select detected")
    chk(not _single_select({"id": "q", "multiSelect": True, "options": q_ok["options"]}),
        "multiSelect excluded")
    chk(not _single_select({"id": "q", "options": [{"id": "a", "label": "x", "correct": True},
                                                   {"id": "b", "label": "y", "correct": True}]}),
        "two-correct excluded")
    chk(_stem({"id": "m01-l1", "module": "module-b", "order": 2},
              [{"id": "module-a"}, {"id": "module-b"}]) == "m01-l2-m01-l1",
        "stem uses positional module index")
    print("QUIZ_BALANCE SELFTESTS " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", choices=("report", "split", "merge"))
    ap.add_argument("course", nargs="?")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return _selftest()
    if not a.cmd or not a.course:
        ap.print_help()
        return 2
    course = Path(a.course)
    return {"report": cmd_report, "split": cmd_split, "merge": cmd_merge}[a.cmd](course)


if __name__ == "__main__":
    sys.exit(main())
