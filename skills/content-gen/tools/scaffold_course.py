#!/usr/bin/env python3
"""
scaffold_course.py — materialize a course directory from a single manifest.json.

The manifest (JSON) is the machine source of truth the architect authors. This
tool emits the human/handoff tree (YAML + md) as a ONE-WAY projection of it:

    courses/<id>/
      course.yaml          modules/NN-slug/module.yaml
      manifest.json        lessons/briefs/<mNN-lN-id>.brief.yaml   (paste into /write-in-voice)
      cadence.yaml         lessons/research/<...>.research.yaml
      assessment.yaml      lessons/facts/<...>.facts.md            (feeds validate_voice diff --facts)
      _state.yaml          lessons/drafts/                          (writer output; feeds audit --lessons)
      course.lock.json     queue/NEXT.md
      README.md

Idempotent: re-emitting an unchanged manifest rewrites identical bytes. Human
edits are protected automatically — if a file's on-disk hash drifts from the
lockfile, emit skips it (use --force to overwrite).

    python scaffold_course.py emit  --manifest manifest.json --out courses/<id>
    python scaffold_course.py check --manifest manifest.json
    python scaffold_course.py --selftest
"""
from __future__ import annotations

import argparse
import json
import sys
import re
from pathlib import Path

from course_lib import to_yaml, load_manifest, flatten_lessons, sha256_text, LIFECYCLE


def _safe(fragment) -> str:
    """Filesystem-safe id fragment. The validator HARD-flags non-kebab ids; this is defense in depth."""
    return re.sub(r"[^a-z0-9-]", "-", str(fragment).lower()).strip("-") or "x"


def _slug(module_id: str) -> str:
    mid = module_id[len("module-"):] if module_id.startswith("module-") else module_id
    return _safe(mid)


def _prefix(mod_idx: int, order) -> str:
    return f"m{mod_idx:02d}-l{order}"


def plan_files(m: dict, drafts: frozenset = frozenset()) -> dict[str, str]:
    """Return {relative_path: text_content} for the whole tree, deterministically."""
    out: dict[str, str] = {}
    course = m.get("course", {})
    modules = m.get("modules", [])
    mod_idx = {mod["id"]: i for i, mod in enumerate(modules)}
    flat = flatten_lessons(m)
    by_id = {l["id"]: l for l in flat}

    # filename prefix + brief path per lesson
    lesson_file: dict[str, str] = {}
    for l in flat:
        pre = _prefix(mod_idx.get(l.get("module"), 99), l.get("order", 0))
        lesson_file[l["id"]] = f"{pre}-{_safe(l['id'])}"

    # course.yaml — the readable course-level projection
    course_doc = {
        "schema_version": m.get("schema_version", 1),
        "course": course,
        "dag": m.get("dag", {}),
        "glossary": m.get("glossary", []),
        "concept_ledger": m.get("concept_ledger", []),
        "references": {"cadence": "cadence.yaml", "assessment": "assessment.yaml",
                       "state": "_state.yaml", "manifest": "manifest.json"},
        "modules": [mod["id"] for mod in modules],
        "lessons": [l["id"] for l in flat],
    }
    out["course.yaml"] = to_yaml(course_doc)
    out["manifest.json"] = json.dumps(m, indent=2, ensure_ascii=False) + "\n"

    # modules
    for mod in modules:
        idx = mod_idx[mod["id"]]
        doc = dict(mod)
        doc["lesson_files"] = {lid: f"../../lessons/briefs/{lesson_file[lid]}.brief.yaml"
                               for lid in mod.get("lessons", []) if lid in lesson_file}
        out[f"modules/{idx:02d}-{_slug(mod['id'])}/module.yaml"] = to_yaml({"module": doc})

    # lessons: briefs + research + facts
    for l in flat:
        stem = lesson_file[l["id"]]
        out[f"lessons/briefs/{stem}.brief.yaml"] = to_yaml({"lesson": l["brief"]})
        research = l.get("research")
        if research:
            out[f"lessons/research/{stem}.research.yaml"] = to_yaml({"research": research})
            facts = research.get("frozen_facts", [])
            if facts:
                out[f"lessons/facts/{stem}.facts.md"] = "\n".join(facts) + "\n"
    out["lessons/drafts/.gitkeep"] = ""

    # cadence + assessment
    if m.get("cadence"):
        out["cadence.yaml"] = to_yaml(m["cadence"])
    if m.get("assessment"):
        out["assessment.yaml"] = to_yaml(m["assessment"])

    # 00-cover.md — the objective course cover (generated, never hand-authored)
    # cover lives with the lessons the reader consumes, named to sort first
    out["lessons/drafts/000-cover.md"] = _cover(m, modules, flat)

    # _state.yaml — progress ledger
    out["_state.yaml"] = to_yaml(_state(m, flat, lesson_file, drafts))

    # queue/NEXT.md — the ready-to-write packet
    out["queue/NEXT.md"] = _next_packet(m, flat, by_id, lesson_file, drafts)

    # README.md — human syllabus
    out["README.md"] = _readme(m, modules, flat)
    return out


def _cover(m: dict, modules: list[dict], flat: list[dict]) -> str:
    """The course landing page: a real welcome, then a scannable reference. Prose
    lives in manifest fields (course.overview, each module's artifact blurb); this
    only assembles them, so the cover is rich when the manifest is and never
    hand-edited. Generated fresh on every emit."""
    AUD = {"web2-dev": "developers coming from web2 / traditional software",
           "evm-dev": "developers with EVM / Solidity experience",
           "absolute-beginner": "programming beginners, new to code",
           "solana-dev-leveling-up": "developers already building on Solana",
           "non-technical": "non-technical readers"}
    c = m.get("course", {})
    aud = c.get("audience", {})
    L = ["# " + str(c.get("title", c.get("id", "Course"))), ""]

    # A cover is an INDEX, not a lesson: the one-line promise is the whole intro.
    # No narrative, history, or teaching content lives here — that opens the first
    # lesson. Everything below is scannable reference metadata.
    if c.get("one_line_promise"):
        L += ["**" + str(c["one_line_promise"]) + "**", ""]

    who = AUD.get(aud.get("who"), aud.get("who", "?"))
    line = "This course is written for **" + who + "**."
    if aud.get("prerequisites"):
        line += " Assumed background: " + ", ".join(aud["prerequisites"]) + "."
    L += ["## Who this course is for", "", line]
    if aud.get("prior_model"):
        L += ["", aud["prior_model"]]
    L += [""]

    builds = []
    for mod in modules:
        art = str(mod.get("artifact", "")).strip()
        if not art:
            continue
        name, _, blurb = art.partition(":")
        builds.append((name.strip(), blurb.strip(), mod.get("title", "")))
    if builds:
        L += ["## What you'll build", "",
              "One toolkit repo grows across the course - each project below is a "
              "rung, and the last one is assembled from all the earlier ones:", ""]
        for n, (name, blurb, mtitle) in enumerate(builds, 1):
            row = str(n) + ". **`" + name + "`**"
            if blurb:
                row += " - " + blurb
            if mtitle:
                row += " _(module: " + mtitle + ")_"
            L.append(row)
        L += [""]

    if c.get("terminal_outcomes"):
        L += ["## What you'll be able to do", "", "By the end, you can:", ""]
        L += ["- _" + str(o.get("bloom")) + "_ - " + str(o.get("statement"))
              for o in c["terminal_outcomes"]]
        L += [""]

    L += ["## The path, module by module", "",
          "Each module answers one driving question and fixes the previous era's limit:", "",
          "| # | Module | The question it answers | What you build |",
          "|---|---|---|---|"]
    for n, mod in enumerate(modules, 1):
        art = str(mod.get("artifact", "")).partition(":")[0].strip()
        L.append("| " + str(n) + " | " + str(mod.get("title", mod["id"])) + " | "
                 + str(mod.get("driving_question", "")) + " | " + art + " |")
    L += [""]

    nodes = m.get("dag", {}).get("nodes", [])
    if nodes:
        L += ["## Concepts you'll meet", "",
              "You'll build and use these, roughly in this order (each is introduced "
              "the moment a build needs it, never front-loaded):", "",
              " - ".join("`" + str(x) + "`" for x in nodes), ""]

    if c.get("toolchain"):
        L += ["## What you'll need", "",
              "Set these up as you go; the first module tells you exactly when each "
              "is required:", ""]
        L += ["- " + str(tool) for tool in c["toolchain"]]
        L += [""]

    lt = c.get("length_target", {})
    L += ["## Time & proof", ""]
    if lt:
        L.append("- **Time:** ~" + str(lt.get("hours", "?")) + "h across "
                 + str(lt.get("lessons", "?")) + " lessons (~"
                 + str(lt.get("weeks", "?")) + " weeks self-paced)")
    L += ["- **Proof of completion:** " + str(c.get("credential", "none")), ""]

    notes = c.get("routing", {}).get("notes")
    if notes:
        L += ["## How this course works", "", str(notes), ""]

    L += ["---", "_(Generated from manifest.json - do not hand-edit; re-emit to refresh.)_", ""]
    return "\n".join(L)


def _state(m: dict, flat: list[dict], lesson_file: dict[str, str], drafts: frozenset = frozenset()) -> dict:
    lesson_ids = {l["id"] for l in flat}
    rows = []
    next_to_write = None
    counts = {s: 0 for s in LIFECYCLE}
    for i, l in enumerate(flat):
        stem = lesson_file[l["id"]]
        research = l.get("research")
        status = "researched" if (research and research.get("status") == "verified") else "briefed"
        if stem in drafts:
            status = "drafted"
        counts[status] = counts.get(status, 0) + 1
        # blocked_by = lesson-id prerequisites not yet drafted (skill prereqs: DAG check)
        blocked = [p for p in l["brief"].get("prerequisites", [])
                   if p in lesson_ids and lesson_file[p] not in drafts]
        rows.append({
            "id": l["id"], "module": l.get("module"), "order": i + 1, "status": status,
            "brief": f"lessons/briefs/{stem}.brief.yaml",
            "research": f"lessons/research/{stem}.research.yaml" if research else None,
            "facts": f"lessons/facts/{stem}.facts.md" if (research and research.get("frozen_facts")) else None,
            "draft": f"lessons/drafts/{stem}.md" if stem in drafts else None,
            "dominant_job": l["brief"].get("dominant_job"),
            "blocked_by": blocked,
        })
        if next_to_write is None and not blocked and stem not in drafts:
            next_to_write = l["id"]
    return {
        "schema_version": 1, "course_id": m.get("course", {}).get("id"),
        "lifecycle": LIFECYCLE, "lessons": rows,
        "summary": {"total": len(flat), "by_status": counts,
                    "next_to_write": next_to_write},
    }


def _next_packet(m: dict, flat: list[dict], by_id: dict, lesson_file: dict[str, str], drafts: frozenset = frozenset()) -> str:
    st = _state(m, flat, lesson_file, drafts)
    nid = st["summary"]["next_to_write"]
    if not nid or nid not in by_id:
        return "# NEXT — nothing pending\n"
    l = by_id[nid]
    stem = lesson_file[nid]
    brief_yaml = to_yaml({"lesson": l["brief"]})
    facts = (l.get("research") or {}).get("frozen_facts", [])
    facts_block = "\n".join(f"- {f}" for f in facts) if facts else "_(no pre-verified facts — writer runs full Pass A)_"
    return f"""# NEXT TO WRITE — {nid}  (module: {l.get('module')})

Status: {st['summary']['by_status']} · paste the block below into `/write-in-voice` (the
writer-style skill, latest installed release) — or, if writer-style is absent, write the
lesson directly from the brief (SKILL.md §Scope & deliverable).
The dominant_job ({l['brief'].get('dominant_job')}) routes the voice. Frozen facts follow.

TARGET LENGTH: {l['brief'].get('est_length', '~3000-4500 words')} of prose — write to it. Course
lessons run long and cover real ground; a lesson under ~3000 words reads thin (forms/course.md).

```yaml
{brief_yaml.rstrip()}
```

## Frozen facts (verified — do NOT change these numbers/identifiers)
{facts_block}

## After the writer returns
1. Save the prose to: `lessons/drafts/{stem}.md`
2. If the writer-style skill is installed, run its validation per its own SKILL.md —
   resolve its install dir at runtime (never assume internal paths or profile names):
   the facts diff against `lessons/facts/{stem}.facts.md`, then its tells/audit pass.
3. Set `{nid}` → `drafted` in `_state.yaml` (`verified` once the checks pass).
4. Re-run `scaffold_course.py emit` — it detects drafts on disk and advances this file.
"""


_AUDIENCE = {"web2-dev": "developers coming from web2 / traditional software",
             "evm-dev": "developers with EVM / Solidity experience",
             "absolute-beginner": "programming beginners, new to code",
             "solana-dev-leveling-up": "developers already building on Solana",
             "non-technical": "non-technical readers"}


def _readme(m: dict, modules: list[dict], flat: list[dict]) -> str:
    """The standardized course README: a rich, scannable syllabus generated from the
    manifest. Course-specific narrative (a 'how it was built' section) is appended by
    hand on top; everything here is re-emittable."""
    c = m.get("course", {})
    aud = c.get("audience", {})
    lt = c.get("length_target", {})
    L = [f"# {c.get('title', c.get('id', 'Course'))}", ""]
    if c.get("one_line_promise"):
        L += [f"> {c['one_line_promise']}", ""]

    who = _AUDIENCE.get(aud.get("who"), aud.get("who", "readers"))
    intro = f"A hands-on course for **{who}**."
    if aud.get("prior_model"):
        intro += " " + str(aud["prior_model"])
    L += [intro, ""]

    length = (f"~{lt.get('hours', '?')}h across {lt.get('weeks', '?')} weeks, "
              f"{lt.get('lessons', '?')} lessons") if lt else ""
    meta = [f"**Format:** {c.get('format', 'self-paced')}"]
    if length:
        meta.append(f"**Length:** {length}")
    meta.append(f"**Status:** {c.get('status', 'draft')} · **Version:** {c.get('version', '0.1.0')}")
    L += [" · ".join(meta), ""]
    if aud.get("prerequisites"):
        L += ["**Prerequisites:** " + "; ".join(aud["prerequisites"]) + ".", ""]

    if c.get("terminal_outcomes"):
        L += ["## Terminal outcomes", ""]
        L += [f"- **{o.get('bloom')}**: {o.get('statement')}" for o in c["terminal_outcomes"]]
        L += [""]

    L += ["## Modules & lessons", "",
          "| # | Lesson | Module | Job | Difficulty |", "|---|---|---|---|---|"]
    by_mod = {mod["id"]: mod for mod in modules}
    for i, l in enumerate(flat, 1):
        b = l["brief"]
        mod = by_mod.get(l.get("module"), {})
        L.append(f"| {i} | {b.get('title', l['id'])} | {mod.get('title', l.get('module'))} "
                 f"| `{b.get('dominant_job')}` | {b.get('difficulty', '?')} |")
    L += [""]

    builds = [str(mod["artifact"]).partition(":")[0].strip()
              for mod in modules if str(mod.get("artifact", "")).strip()]
    if builds:
        L += ["You build a running toolkit as you go: "
              + ", ".join(f"`{b}`" for b in builds) + ".", ""]

    if c.get("toolchain"):
        L += ["## Toolchain", ""] + [f"- {t}" for t in c["toolchain"]] + [""]

    L += ["## How this course was generated", "",
          "Produced by **ContentGen** (`content-gen-skill`): the course is designed backward from a "
          "measurable capstone into `manifest.json` (a `course` object, a prerequisite DAG, modules, and "
          "per-lesson briefs), validated by deterministic gates (`validate_course.py`: DAG, briefs, ladder, "
          "capstone, outcomes), then each lesson is written from its brief through the `writer-style` voice "
          "router, finished with a visual-placeholder pass, and checked by the runnable-code verifier "
          "(`verify_code.py`). This README is generated from the manifest.", ""]

    cid = c.get("id", "course")
    L += ["## Layout", "", "```", f"{cid}/",
          "|- manifest.json   design of record: course, DAG, modules, lessons, capstone",
          "|- README.md       this file (generated)",
          "|- lessons/",
          "|  |- drafts/      the written lessons + 000-cover.md",
          "|  |- briefs/      per-lesson structured briefs",
          "|  \\- facts/       per-lesson atomic frozen-facts",
          "\\- _state.yaml     progress ledger", "```", ""]

    L += ["---", "_(Generated from manifest.json; do not hand-edit the sections above, re-emit to refresh. "
          "A course-specific narrative may be appended below by hand.)_", ""]
    return "\n".join(L)


# ── emit ────────────────────────────────────────────────────────────────────────

def emit(manifest_path: str, out_dir: str, force: bool) -> int:
    m = load_manifest(manifest_path)
    out = Path(out_dir)
    drafts = frozenset(p.stem for p in (out / "lessons" / "drafts").glob("*.md"))
    files = plan_files(m, drafts)

    lock_path = out / "course.lock.json"
    old_lock = {}
    if lock_path.is_file():
        try:
            old_lock = json.loads(lock_path.read_text("utf-8")).get("files", {})
        except json.JSONDecodeError:
            old_lock = {}

    new_lock: dict[str, dict] = {}
    written = skipped = 0
    for rel, content in files.items():
        target = out / rel
        if target.is_file() and rel in old_lock:
            cur = sha256_text(target.read_text("utf-8"))
            if cur != old_lock[rel]["sha256"] and not force:
                print(f"  skip (human-edited): {rel}  — use --force to overwrite")
                new_lock[rel] = {"sha256": cur, "edited_by_human": True}
                skipped += 1
                continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, "utf-8")
        new_lock[rel] = {"sha256": sha256_text(content), "edited_by_human": False}
        written += 1

    lock_path.write_text(json.dumps({"files": new_lock}, indent=2) + "\n", "utf-8")
    print(f"emit: {written} written, {skipped} skipped → {out}/")
    return 0


def check(manifest_path: str) -> int:
    m = load_manifest(manifest_path)
    files = plan_files(m)
    print(f"check: manifest parses (structural gate is validate_course.py) — course '{m.get('course', {}).get('id')}' — would write {len(files)} files:")
    for rel in sorted(files):
        print("   " + rel)
    return 0


def selftest() -> int:
    import tempfile
    from validate_course import _good_manifest
    ok = True

    def chk(c, msg):
        nonlocal ok
        print(("PASS" if c else "FAIL") + " - " + msg)
        ok = ok and c

    m = _good_manifest()
    # add a research scaffold to exercise research/facts emission
    m["lessons"][1]["research"] = {"lesson_id": "pda-state", "status": "verified",
                                   "frozen_facts": ["PDAs derive via find_program_address.",
                                                    "Rent-exempt min ~0.002 SOL (devnet)."]}
    with tempfile.TemporaryDirectory() as td:
        mf = Path(td) / "manifest.json"
        mf.write_text(json.dumps(m), "utf-8")
        out = Path(td) / "course"
        emit(str(mf), str(out), force=False)

        chk((out / "course.yaml").is_file(), "course.yaml written")
        cov = out / "lessons" / "drafts" / "000-cover.md"
        ctext = cov.read_text() if cov.is_file() else ""
        chk(cov.is_file() and "## The path, module by module" in ctext,
            "000-cover.md generated in lessons/drafts (sorts before every lesson)")
        chk((out / "manifest.json").is_file(), "manifest.json copied")
        brief = out / "lessons/briefs/m01-l1-pda-state.brief.yaml"
        chk(brief.is_file(), "lesson brief written with mNN-lN prefix")
        chk(brief.read_text().startswith("lesson:\n"), "brief is a paste-ready lesson: block")
        chk((out / "lessons/research/m01-l1-pda-state.research.yaml").is_file(), "research scaffold written")
        facts = out / "lessons/facts/m01-l1-pda-state.facts.md"
        chk(facts.is_file() and "find_program_address" in facts.read_text(), "facts.md projection written")
        chk((out / "lessons/drafts/.gitkeep").is_file(), "drafts/ dir created")
        chk((out / "_state.yaml").is_file() and "next_to_write" in (out / "_state.yaml").read_text(),
            "_state.yaml with next_to_write")
        chk("the-counter" in (out / "queue/NEXT.md").read_text(),
            "NEXT.md targets the first unblocked lesson")

        # a draft on disk advances the queue on re-emit
        (out / "lessons/drafts/m00-l1-the-counter.md").write_text("draft\n", "utf-8")
        emit(str(mf), str(out), force=False)
        chk("pda-state" in (out / "queue/NEXT.md").read_text(),
            "NEXT.md advances past drafted lesson")
        chk("status: drafted" in (out / "_state.yaml").read_text(),
            "_state.yaml reflects on-disk draft")

        # ambiguous strings stay strings in emitted YAML
        chk('"2026-07-06"' in to_yaml({"d": "2026-07-06"}) and '"0.002"' in to_yaml({"v": "0.002"}),
            "yaml quotes date-like and number-like strings")
        chk((out / "course.lock.json").is_file(), "lockfile written")
        chk((out / "modules/00-m-accounts/module.yaml").is_file(), "module dir uses NN-slug")

        # idempotent re-emit: identical bytes -> nothing changes
        lock1 = (out / "course.lock.json").read_text()
        emit(str(mf), str(out), force=False)
        chk((out / "course.lock.json").read_text() == lock1, "re-emit is idempotent")

        # human-edit protection: drift a file, re-emit without force -> preserved
        (out / "course.yaml").write_text("# hand-edited\n", "utf-8")
        emit(str(mf), str(out), force=False)
        chk((out / "course.yaml").read_text() == "# hand-edited\n", "human-edited file preserved")
        # --force overwrites
        emit(str(mf), str(out), force=True)
        chk((out / "course.yaml").read_text() != "# hand-edited\n", "--force overwrites human edit")

    print("\n" + ("SCAFFOLD SELFTESTS PASSED" if ok else "FAILURES ABOVE"))
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="content-gen scaffolder")
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    pe = sub.add_parser("emit")
    pe.add_argument("--manifest", required=True)
    pe.add_argument("--out", required=True)
    pe.add_argument("--force", action="store_true")
    pc = sub.add_parser("check")
    pc.add_argument("--manifest", required=True)
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if a.cmd == "emit":
        return emit(a.manifest, a.out, a.force)
    if a.cmd == "check":
        return check(a.manifest)
    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
