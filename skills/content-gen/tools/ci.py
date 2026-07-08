#!/usr/bin/env python3
"""ci.py — lean CI for the whole course suite (stdlib-only).

  Tier 1  gates     tool selftests + validate_course all (incl. drafts) on every
                    course found, + writer-style facts/tells on every draft when
                    the writer-style skill is resolvable
  Tier 2  fixtures  golden bad-manifests must trip their expected flags
  Tier 3  metrics   deterministic per-draft metrics table (words, visuals, walls,
                    time-to-first-do) — the text-block-aesthetics dashboard
  Tier 4  smoke     collect per-lesson verify commands; list them (default) or
                    execute the allowlisted ones with --run-smoke
  Tier 5  verify     compile/run every fenced code block the courses ship
                    (verify_code.py). A real compile/run FAILURE fails the tier;
                    a SKIP (toolchain needs the pinned container) is reported, not
                    failed. Set VERIFY_ENV=docker to run against the pinned image.

    python3 ci.py                     # tiers 1-5 (smoke = list only)
    python3 ci.py --tiers 1,3         # subset
    python3 ci.py --run-smoke         # tier 4 executes allowlisted commands

Exit 0 = all green; 1 = any failure. Courses discovered under the skill's
examples/ and the repo's content/courses/.
"""
from __future__ import annotations

import argparse
import copy
import shlex
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate_course as vc                      # noqa: E402
import verify_code as vcode                        # noqa: E402
from course_lib import load_manifest, flatten_lessons  # noqa: E402

REPO = HERE.parent.parent.parent
SMOKE_ALLOWLIST = {"python3", "python", "shasum", "sha256sum", "printf", "echo", "openssl"}


def course_dirs() -> list[Path]:
    dirs = []
    for base in (HERE.parent / "examples", REPO / "content" / "courses"):
        if base.is_dir():
            dirs += [d for d in sorted(base.iterdir()) if (d / "manifest.json").is_file()]
    return dirs


def writer_style_dir() -> Path | None:
    import os
    cand = [Path(p) for p in [os.environ.get("WRITER_STYLE_SKILL", "")] if p]
    cand += [Path.home() / "Developer/GigaClaude/writer-style-skill/skills/writer-style"]
    for c in cand:
        if (c / "tools" / "validate_voice.py").is_file():
            return c
    return None


def t1_gates() -> bool:
    ok = True
    r = subprocess.run([sys.executable, str(HERE / "test_tools.py")],
                       capture_output=True, text=True)
    print(("PASS" if r.returncode == 0 else "FAIL") + " - tool selftests")
    ok = ok and r.returncode == 0

    for d in course_dirs():
        m = load_manifest(d)
        hard = False
        for name, fn in vc.CHECKS.items():
            res = fn(m)
            hard = hard or res["hard"]
            for f in res["flags"]:
                if f.startswith(vc.HARD):
                    print(f"   {d.name}/{name}: {f}")
        res = vc.check_drafts(d, m)
        hard = hard or res["hard"]
        for f in res["flags"]:
            if f.startswith(vc.HARD):
                print(f"   {d.name}/drafts: {f}")
        print(("PASS" if not hard else "FAIL") + f" - gate {d.name}")
        ok = ok and not hard

    w = writer_style_dir()
    if w is None:
        print("skip - writer-style not resolvable (set WRITER_STYLE_SKILL); facts/tells skipped")
        return ok
    vv = w / "tools" / "validate_voice.py"
    card = w / "profiles" / "kaue" / "kaue.card.yaml"
    for d in course_dirs():
        for draft in sorted((d / "lessons" / "drafts").glob("*.md")):
            facts = d / "lessons" / "facts" / (draft.stem + ".facts.md")
            if facts.is_file():
                r = subprocess.run([sys.executable, str(vv), "diff", "--facts", str(facts),
                                    "--styled", str(draft)], capture_output=True, text=True)
                print(("PASS" if r.returncode == 0 else "FAIL") + f" - facts {d.name}/{draft.name}")
                ok = ok and r.returncode == 0
            if card.is_file():
                r = subprocess.run([sys.executable, str(vv), "tells", "--file", str(draft),
                                    "--card", str(card)], capture_output=True, text=True)
                print(("PASS" if r.returncode == 0 else "FAIL") + f" - tells {d.name}/{draft.name}")
                ok = ok and r.returncode == 0
    return ok


def t2_fixtures() -> bool:
    """Golden bad-manifests: each mutation must trip its expected flag substring."""
    def mut_id(m): m["modules"][0]["id"] = "Not Kebab"
    def mut_surface(m): m["lessons"][0]["research"] = {
        "claims": [{"id": "C1", "mcp": "trust-me-bro", "status": "verified"}]}
    def mut_artifact(m):
        m["lessons"][0]["brief"]["artifact"] = {"id": "a", "consumes": ["b"]}
        m["lessons"][1]["brief"]["artifact"] = {"id": "b"}
    def mut_signature(m): m["lessons"][0]["brief"]["hook"] = "like the Movie Review app"
    def mut_passive(m): m["lessons"][0]["brief"]["assessment"] = "watch the recording"
    def mut_capstone(m): m["assessment"]["capstone"]["requires_skills"] = ["never-taught"]

    fixtures = [
        ("non-kebab id", mut_id, vc.check_dag, "not kebab-case"),
        ("non-kit research surface", mut_surface, vc.check_research, "non-kit surface"),
        ("backward artifact edge", mut_artifact, vc.check_artifacts, "built later"),
        ("corpus signature", mut_signature, vc.check_briefs, "corpus signature"),
        ("passive assessment", mut_passive, vc.check_briefs, "passive"),
        ("untaught capstone skill", mut_capstone, vc.check_capstone, ""),
    ]
    ok = True
    for name, mut, check, needle in fixtures:
        m = copy.deepcopy(vc._good_manifest())
        mut(m)
        res = check(m)
        hit = res["hard"] and (not needle or any(needle in f for f in res["flags"]))
        print(("PASS" if hit else "FAIL") + f" - fixture: {name}")
        ok = ok and hit
    return ok


def t3_metrics() -> bool:
    print(f"{'draft':44} {'words':>5} {'vis':>3} {'types':>2} {'wall':>4} {'1st-do':>6}")
    for d in course_dirs():
        for draft in sorted((d / "lessons" / "drafts").glob("*.md")):
            mx = vc.draft_metrics(draft.read_text("utf-8"))
            first = mx["first_code_words"]
            print(f"{d.name + '/' + draft.stem:44} {mx['prose_words']:>5} "
                  f"{mx['visual_valid']:>3} {len(mx['visual_types']):>2} "
                  f"{mx['longest_wall']:>4} {str(first if first is not None else '-'):>6}")
    return True  # informational; the enforced thresholds live in tier 1's drafts gate


def t4_smoke(run: bool) -> bool:
    ok = True
    found = 0
    for d in course_dirs():
        m = load_manifest(d)
        for l in flatten_lessons(m):
            v = l.get("brief", {}).get("verify")
            if not isinstance(v, dict) or not v.get("command"):
                continue
            found += 1
            cmd = v["command"]
            expect = str(v.get("expect", ""))
            head = shlex.split(cmd.split("|")[0].strip())[0] if cmd.strip() else ""
            allowed = head in SMOKE_ALLOWLIST and "|" not in cmd.replace("| shasum", "").replace(
                "| python3", "").replace("| wc", "")
            # conservative: only single-purpose pipelines of allowlisted tools run
            parts_ok = all(shlex.split(seg.strip())[0] in SMOKE_ALLOWLIST | {"wc"}
                           for seg in cmd.split("|") if seg.strip())
            if run and parts_ok:
                r = subprocess.run(["bash", "-c", cmd], capture_output=True, text=True, timeout=15)
                hit = r.returncode == 0 and (expect in r.stdout if expect else True)
                print(("PASS" if hit else "FAIL") + f" - smoke {l['id']}: {cmd[:60]}")
                ok = ok and hit
            else:
                status = "run-eligible" if parts_ok else "listed (needs live env)"
                print(f"   smoke {l['id']}: {cmd[:70]}  [{status}]")
    print(f"{'PASS' if ok else 'FAIL'} - smoke tier ({found} verify commands found)")
    return ok


def t5_verify() -> bool:
    """Compile/run every fenced code block the courses ship. FAIL fails; SKIP is reported."""
    import os
    if os.environ.get("VERIFY_ENV") == "docker":
        ok = True
        for d in course_dirs():
            rc = vcode.run_docker(str(d), "")
            print(("PASS" if rc == 0 else "FAIL") + f" - verify(docker) {d.name}")
            ok = ok and rc == 0
        return ok
    harness = bool(os.environ.get("VERIFY_HARNESS"))
    ok = True
    for d in course_dirs():
        drafts = d / "lessons" / "drafts"
        rows = []
        for f in sorted(drafts.glob("*.md")):
            rows += vcode.verify_file(f)
        if harness:                                  # heavy: real anchor build + tsc, opt-in
            rows += vcode.run_harness(d)
        fails = [r for r in rows if r[2] == "FAIL"]
        skips = [r for r in rows if r[2] == "SKIP"]
        for fn, blk, _, det in fails:
            print(f"   FAIL {d.name}/{fn} {blk}: {det[:70]}")
        if harness:
            for fn, blk, st, det in rows:
                if blk in ("tsc", "anchor build"):
                    print(f"   {st} {d.name}/{fn}: {det[:70]}")
        n_pass = sum(1 for r in rows if r[2] == "PASS")
        print(("PASS" if not fails else "FAIL")
              + f" - verify {d.name} ({n_pass} PASS · {len(fails)} FAIL · {len(skips)} SKIP)")
        ok = ok and not fails
    print("   (SKIP = declared toolchain unavailable locally; VERIFY_ENV=docker for full coverage)")
    return ok


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="lean CI for the course suite")
    ap.add_argument("--tiers", default="1,2,3,4,5")
    ap.add_argument("--run-smoke", action="store_true")
    a = ap.parse_args(argv)
    tiers = {t.strip() for t in a.tiers.split(",")}
    ok = True
    if "1" in tiers:
        print("== tier 1: gates =="); ok = t1_gates() and ok
    if "2" in tiers:
        print("== tier 2: fixtures =="); ok = t2_fixtures() and ok
    if "3" in tiers:
        print("== tier 3: metrics =="); t3_metrics()
    if "4" in tiers:
        print("== tier 4: smoke =="); ok = t4_smoke(a.run_smoke) and ok
    if "5" in tiers:
        print("== tier 5: verify =="); ok = t5_verify() and ok
    print("\nCI: " + ("GREEN" if ok else "RED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
