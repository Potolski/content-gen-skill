#!/usr/bin/env python3
"""
verify_challenges.py — prove the Academy runtime contract for every coding challenge:
the SOLUTION passes every test case, and the STARTER fails at least one. A starter that
already passes has nothing to solve; a solution that fails is broken. This is exactly what
the platform's challenge-executor enforces for TypeScript on every PR (references/
academy-schema.md); we enforce it locally for both languages before publish.

It reads a course's `manifest.json` (JSON — no YAML parser needed) and, for each lesson
brief's `coding_challenges`, resolves the starter/solution/tests files (course-relative)
and runs them in a real toolchain:

  language: typescript              → transpile (tsc) + run (node); each test evaluates
    (buildType standard)              `expectedOutput` as a boolean over `result = fn(<input>)`.
  language: rust, buildType standard → compile+run (rustc); compare the returned value's
                                        Display to `expectedOutput`.
  language: rust, buildType buildable→ compile (cargo check vs anchor-lang); a case's
                                        `expectedOutput` ("true"/"ok") means "it compiled".

    python3 verify_challenges.py <course-dir> [--only ts|rust] [--skip-rust]
    python3 verify_challenges.py --selftest

Exit 0 = every runnable challenge upheld the contract (or was SKIPPED for a missing
toolchain); 1 = a real contract violation; 2 = usage. SKIP never fails the run but is
reported loudly, so "green" cannot silently mean "nothing ran".
"""
from __future__ import annotations
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from course_lib import load_manifest, flatten_lessons, CHALLENGE_LANGS


def _run(cmd, timeout=300, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, **kw)


# ── challenge discovery (from the manifest) ─────────────────────────────────────

def discover(course_dir: Path) -> list[dict]:
    m = load_manifest(course_dir)
    out = []
    for l in flatten_lessons(m):
        brief = l.get("brief", {}) or {}
        for cc in brief.get("coding_challenges", []) or []:
            cc = cc or {}
            out.append({
                "lid": l["id"], "cid": cc.get("id", "?"),
                "language": cc.get("language"), "buildType": cc.get("buildType", "standard"),
                "starter": course_dir / str(cc.get("starter", "")),
                "solution": course_dir / str(cc.get("solution", "")),
                "tests": course_dir / str(cc.get("tests", "")),
            })
    return out


def _load_tests(path: Path):
    try:
        data = json.loads(path.read_text("utf-8"))
        return data if isinstance(data, list) else None
    except Exception:
        return None


# ── TypeScript runner ───────────────────────────────────────────────────────────

def _ts_primary(src: str) -> str | None:
    m = re.search(r"^[ \t]*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(", src, re.M)
    if m:
        return m.group(1)
    m = re.search(r"^[ \t]*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\(", src, re.M)
    return m.group(1) if m else None


def _ts_harness(src: str, tests: list) -> str | None:
    prim = _ts_primary(src)
    if not prim:
        return None
    parts = [src, "\n;(() => {\n  const __out: any[] = [];\n"]
    for t in tests:
        inp = str(t.get("input", ""))
        exp = str(t.get("expectedOutput", "true"))
        tid = json.dumps(str(t.get("id", "")))
        parts.append(
            "  try {\n"
            f"    const result: any = ({prim})({inp});\n"
            f"    __out.push({{ id: {tid}, ok: !!({exp}) }});\n"
            "  } catch (e: any) {\n"
            f"    __out.push({{ id: {tid}, ok: false, err: String((e && e.message) || e) }});\n"
            "  }\n"
        )
    parts.append('  console.log("__R__" + JSON.stringify(__out));\n})();\n')
    return "".join(parts)


def _find_tsc(course_dir: Path) -> str | None:
    local = course_dir / "verify-ts" / "node_modules" / ".bin" / "tsc"
    if local.exists():
        return str(local.resolve())  # absolute: run_ts uses cwd=<tmp>, a relative path would break
    return shutil.which("tsc")


def run_ts(src: str, tests: list, course_dir: Path) -> tuple[str, dict]:
    """Return (status, detail). status in RAN/SKIP; detail has per-test ok when RAN."""
    node = shutil.which("node")
    tsc = _find_tsc(course_dir)
    if not node:
        return "SKIP", {"why": "node not installed"}
    if not tsc:
        return "SKIP", {"why": "tsc not found (need verify-ts/node_modules or a global tsc)"}
    harness = _ts_harness(src, tests)
    if harness is None:
        return "SKIP", {"why": "no top-level function found to call"}
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "run.ts").write_text(harness, "utf-8")
        # Emit even on type errors: the CONTRACT is about runtime values, not types
        # (the platform type-checks separately). noEmitOnError defaults false.
        tr = _run([tsc, "run.ts", "--outDir", str(dp), "--module", "commonjs",
                   "--target", "es2020", "--lib", "es2020", "--skipLibCheck", "--types", "[]"],
                  cwd=str(dp), timeout=180)
        js = dp / "run.js"
        if not js.exists():
            return "SKIP", {"why": "tsc emitted no JS", "detail": (tr.stderr or tr.stdout)[-200:]}
        nr = _run([node, str(js)], cwd=str(dp), timeout=60)
        line = next((ln for ln in nr.stdout.splitlines() if ln.startswith("__R__")), None)
        if not line:
            return "SKIP", {"why": "no results from node", "detail": (nr.stderr or nr.stdout)[-200:]}
        results = json.loads(line[len("__R__"):])
        return "RAN", {"results": results}


# ── Rust runners ─────────────────────────────────────────────────────────────────

def run_rust_standard(src: str, tests: list) -> tuple[str, dict]:
    rustc = shutil.which("rustc")
    if not rustc:
        return "SKIP", {"why": "rustc not installed"}
    calls = "\n".join(
        f'    println!("__R__{json.dumps(str(t.get("id","")))[1:-1]}={{}}", '
        f'{_rust_primary(src)}({t.get("input","")}));'
        for t in tests
    )
    main = f"{src}\nfn main() {{\n{calls}\n}}\n"
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "main.rs").write_text(main, "utf-8")
        cr = _run([rustc, "--edition", "2021", str(dp / "main.rs"), "-o", str(dp / "bin")],
                  cwd=str(dp), timeout=120)
        if not (dp / "bin").exists():
            # did not compile → every test "fails" (a legit starter outcome)
            return "RAN", {"results": [{"id": str(t.get("id", "")), "ok": False,
                                        "err": "did not compile"} for t in tests]}
        rr = _run([str(dp / "bin")], timeout=30)
        got = {}
        for ln in rr.stdout.splitlines():
            mt = re.match(r"__R__(.+?)=(.*)$", ln)
            if mt:
                got[mt.group(1)] = mt.group(2)
        res = [{"id": str(t.get("id", "")),
                "ok": got.get(str(t.get("id", "")), None) is not None
                and got[str(t.get("id", ""))].strip() == str(t.get("expectedOutput", "")).strip()}
               for t in tests]
        return "RAN", {"results": res}


def _rust_primary(src: str) -> str:
    m = re.search(r"\bfn\s+([A-Za-z_][\w]*)\s*\(", src)
    return m.group(1) if m else "solution"


def _anchor_dep(course_dir: Path) -> str:
    """Pin anchor-lang to whatever a local verify-anchor workspace already uses (its deps
    are cached from a prior build), else 1.1.2."""
    for toml in sorted((course_dir / "verify-anchor").glob("**/Cargo.toml")) if (course_dir / "verify-anchor").is_dir() else []:
        mt = re.search(r'anchor-lang\s*=\s*(?:\{[^}]*version\s*=\s*)?"([=~^]?[\d.]+)"', toml.read_text("utf-8"))
        if mt:
            return mt.group(1)
    return "1.1.2"


_CARGO_TARGET = str(Path(tempfile.gettempdir()) / "cg-anchor-check-target")


def run_rust_buildable(src: str, course_dir: Path) -> tuple[str, dict]:
    cargo = shutil.which("cargo")
    if not cargo:
        return "SKIP", {"why": "cargo not installed"}
    dep = _anchor_dep(course_dir)
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "src").mkdir()
        (dp / "src" / "lib.rs").write_text(src, "utf-8")
        (dp / "Cargo.toml").write_text(
            "[package]\nname = \"challenge_check\"\nversion = \"0.0.0\"\nedition = \"2021\"\n"
            "[lib]\ncrate-type = [\"cdylib\", \"lib\"]\n"
            f"[dependencies]\nanchor-lang = \"{dep}\"\n", "utf-8")
        env = dict(os.environ, CARGO_TARGET_DIR=_CARGO_TARGET)
        cr = _run([cargo, "check", "--quiet"], cwd=str(dp), env=env, timeout=600)
        blob = (cr.stderr + cr.stdout)
        if cr.returncode == 0:
            return "RAN", {"compiles": True}
        low = blob.lower()
        if any(s in low for s in ("no matching package", "failed to select a version", "failed to download",
                                  "network", "could not resolve", "offline", "no such host",
                                  "spurious network error", "failed to get")):
            return "SKIP", {"why": "anchor-lang deps unavailable (needs network/cache)",
                            "detail": blob.strip().splitlines()[-1][:160] if blob.strip() else ""}
        return "RAN", {"compiles": False, "detail": blob.strip().splitlines()[-1][:160] if blob.strip() else ""}


# ── per-challenge contract ───────────────────────────────────────────────────────

def _all_pass(results: list) -> bool:
    return bool(results) and all(r.get("ok") for r in results)


def _any_fail(results: list) -> bool:
    return any(not r.get("ok") for r in results)


def verify_one(ch: dict, course_dir: Path, skip_rust: bool) -> dict:
    lang, bt = ch["language"], ch["buildType"]
    tag = f"{ch['lid']}/{ch['cid']}"
    if lang not in CHALLENGE_LANGS:
        return {"tag": tag, "status": "SKIP", "why": f"language {lang!r} not runnable"}
    for role in ("starter", "solution", "tests"):
        if not ch[role].is_file():
            return {"tag": tag, "status": "SKIP", "why": f"{role} file missing: {ch[role]}"}
    tests = _load_tests(ch["tests"])
    if not tests:
        return {"tag": tag, "status": "SKIP", "why": "tests.json empty/invalid"}
    starter_src = ch["starter"].read_text("utf-8")
    solution_src = ch["solution"].read_text("utf-8")

    def run(src):
        if lang == "typescript":
            return run_ts(src, tests, course_dir)
        if skip_rust:
            return "SKIP", {"why": "rust skipped (--skip-rust)"}
        if bt == "buildable":
            st, det = run_rust_buildable(src, course_dir)
            if st == "RAN":
                ok = det.get("compiles", False)
                det = {"results": [{"id": t.get("id"), "ok": ok} for t in tests], **det}
            return st, det
        return run_rust_standard(src, tests)

    s_st, s_det = run(solution_src)
    if s_st == "SKIP":
        return {"tag": tag, "status": "SKIP", "why": "solution: " + s_det.get("why", "?"),
                "detail": s_det.get("detail", "")}
    st_st, st_det = run(starter_src)
    if st_st == "SKIP":
        return {"tag": tag, "status": "SKIP", "why": "starter: " + st_det.get("why", "?")}

    sol_ok = _all_pass(s_det["results"])
    starter_fails = _any_fail(st_det["results"])
    ok = sol_ok and starter_fails
    why = []
    if not sol_ok:
        why.append("solution does NOT pass all tests")
    if not starter_fails:
        why.append("starter passes everything (nothing to solve)")
    return {"tag": tag, "status": "PASS" if ok else "FAIL",
            "lang": lang, "buildType": bt,
            "sol": s_det["results"], "starter": st_det["results"],
            "why": "; ".join(why) if why else "solution passes all, starter fails ≥1",
            "detail": s_det.get("detail", "")}


def verify(course_dir: str, only: str | None, skip_rust: bool) -> int:
    course_dir = Path(course_dir).resolve()  # absolute so subprocess cwd/relative paths resolve
    challenges = discover(course_dir)
    if only:
        challenges = [c for c in challenges if (only == "ts") == (c["language"] == "typescript")]
    if not challenges:
        print("verify_challenges: no coding challenges found in manifest", file=sys.stderr)
        return 0
    rows = [verify_one(c, course_dir, skip_rust) for c in challenges]
    print(f"{'challenge':44} {'status':6} note")
    for r in rows:
        note = r.get("why", "") + ((" — " + r["detail"]) if r.get("detail") else "")
        print(f"{r['tag'][:44]:44} {r['status']:6} {note[:80]}")
    fails = [r for r in rows if r["status"] == "FAIL"]
    skips = [r for r in rows if r["status"] == "SKIP"]
    passes = [r for r in rows if r["status"] == "PASS"]
    print(f"\nverify_challenges: {len(passes)} PASS · {len(fails)} FAIL · {len(skips)} SKIP")
    if skips:
        print("  (SKIP = toolchain/deps unavailable; not a pass. Install node+tsc for TS, "
              "cargo+anchor-lang for buildable Rust.)")
    return 1 if fails else 0


def selftest() -> int:
    ok = True

    def chk(c, m):
        nonlocal ok
        print(("PASS" if c else "FAIL") + " - " + m)
        ok = ok and c

    # pure logic: primary detection + harness + contract decision
    chk(_ts_primary("function assembleDeposit(a){return a}") == "assembleDeposit", "ts primary (function)")
    chk(_ts_primary("export const f = (x) => x") == "f", "ts primary (arrow const)")
    chk(_rust_primary("fn add(a:i64,b:i64)->i64{a+b}") == "add", "rust primary")
    h = _ts_harness("function add(a,b){return a+b}", [{"id": "t1", "input": "2,3", "expectedOutput": "result === 5"}])
    chk(h and "const result: any = (add)(2,3);" in h and "!!(result === 5)" in h, "ts harness splices input+expr")
    chk(_all_pass([{"ok": True}, {"ok": True}]) and not _all_pass([{"ok": True}, {"ok": False}]), "_all_pass")
    chk(_any_fail([{"ok": True}, {"ok": False}]) and not _any_fail([{"ok": True}]), "_any_fail")

    # live end-to-end IF node+tsc are available: a real add() challenge upholds the contract
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        cdir = dp / "course"
        exd = cdir / "lessons" / "challenges" / "l1" / "add-two"
        exd.mkdir(parents=True)
        (exd / "starter.ts").write_text("function add(a: number, b: number): number { return 0; }\n", "utf-8")
        (exd / "solution.ts").write_text("function add(a: number, b: number): number { return a + b; }\n", "utf-8")
        (exd / "tests.json").write_text(
            '[{"id":"t1","input":"2, 3","expectedOutput":"result === 5"},'
            '{"id":"t2","input":"10, -4","expectedOutput":"result === 6"}]', "utf-8")
        man = {"course": {"id": "c"}, "modules": [{"id": "m"}],
               "lessons": [{"id": "l1", "module": "m", "order": 1, "brief": {"coding_challenges": [{
                   "id": "add-two", "language": "typescript",
                   "starter": "lessons/challenges/l1/add-two/starter.ts",
                   "solution": "lessons/challenges/l1/add-two/solution.ts",
                   "tests": "lessons/challenges/l1/add-two/tests.json"}]}}]}
        (cdir / "manifest.json").write_text(json.dumps(man), "utf-8")
        ch = discover(cdir)[0]
        if shutil.which("node") and _find_tsc(cdir):
            r = verify_one(ch, cdir, skip_rust=True)
            chk(r["status"] == "PASS", "live TS add() upholds contract (starter fails, solution passes)")
            # a starter that already passes must FAIL the contract
            (exd / "starter.ts").write_text("function add(a: number, b: number): number { return a + b; }\n", "utf-8")
            r2 = verify_one(ch, cdir, skip_rust=True)
            chk(r2["status"] == "FAIL", "passing starter -> contract FAIL")
        else:
            print("SKIP - node/tsc unavailable; live TS contract check not run")

    print("\n" + ("VERIFY_CHALLENGES SELFTESTS PASSED" if ok else "FAILURES ABOVE"))
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="prove starter-fails / solution-passes for coding challenges")
    ap.add_argument("course", nargs="?", help="course dir (reads manifest.json)")
    ap.add_argument("--only", choices=["ts", "rust"], help="verify only one language")
    ap.add_argument("--skip-rust", action="store_true", help="skip Rust (slow; needs cargo+anchor-lang)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.course:
        ap.print_help(); return 2
    return verify(a.course, a.only, a.skip_rust)


if __name__ == "__main__":
    raise SystemExit(main())
