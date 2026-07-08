#!/usr/bin/env python3
"""
validate_course.py — the content-gen validator (deterministic, pre-emit gate).

Reads a course manifest (JSON) and runs structural checks. HARD failures break
the prerequisite-DAG walk or the writer-style handoff and must be fixed; ADVISORY
flags are smells a human weighs. Pedagogical *judgement* (is the hook felt? the
tradeoff real? the dominant_job correct?) is NOT here — that stays an LLM-judge
pass in references/quality-bar.md.

  dag       acyclicity, no-forward-deps, referential integrity of ids/skills
  briefs    per-lesson schema completeness, dominant_job enum, gated-on-doing, id uniqueness
  ladder    artifact-rung monotonicity, difficulty band, cadence coverage
  capstone  capstone requires only skills taught earlier
  outcomes  every terminal outcome has a proof and vice-versa; module traces resolve
  all       run everything; exit 1 if any HARD fired

    python validate_course.py all     --course courses/<slug>
    python validate_course.py dag     --manifest manifest.json
    python validate_course.py --selftest

Mirrors the writer-style skill's validator: pure-Python, stdlib-only, --selftest,
hard-vs-advisory split, exit codes (0 ok, 1 hard fail, 2 usage).
"""
from __future__ import annotations

import argparse
import re
import sys

from course_lib import (
    DOMINANT_JOBS, GUEST_ONLY_JOBS, ARTIFACT_LADDER, BRIEF_REQUIRED_KEYS,
    BRIEF_CORE_KEYS, BRIEF_BUILD_KEYS, LESSON_KINDS, ID_RE, count_prose_emdashes,
    KIT_SURFACES, VISUAL_TYPES, VISUAL_FIELDS,
    WEAK_BLOOM_VERBS, PASSIVE_ASSESSMENT_RE,
    load_manifest, flatten_lessons, topo_sort,
)

HARD = "[HARD] "
ADV = "[advisory] "

# Course-lesson length band (words). The brief's est_length target must reach the
# floor — that number is what the writer writes to. Raise the whole band by editing
# this one constant; every course the skill emits inherits it.
LESSON_TARGET_MIN = 3000


def _result(name, flags):
    hard = any(f.startswith(HARD) for f in flags)
    return {"name": name, "hard": hard, "flags": flags or ["ok: clean"]}


# ── dag ─────────────────────────────────────────────────────────────────────────

def check_dag(m: dict) -> dict:
    flags: list[str] = []
    for kind, ids in (("course", [m.get("course", {}).get("id")]),
                      ("module", [mod.get("id") for mod in m.get("modules", [])]),
                      ("lesson", [l.get("id") for l in m.get("lessons", [])])):
        for _id in ids:
            if _id is not None and not ID_RE.match(str(_id)):
                flags.append(f"{HARD}{kind} id '{_id}' is not kebab-case [a-z0-9-] — ids become filesystem paths")
    dag = m.get("dag", {})
    nodes = list(dag.get("nodes", []))
    edges = [list(e) for e in dag.get("edges", [])]
    nodeset = set(nodes)

    for a, b in edges:
        if a not in nodeset or b not in nodeset:
            flags.append(f"{HARD}dag edge references unknown node: {[a, b]}")

    order, cycle = topo_sort(nodes, edges)
    if cycle:
        flags.append(f"{HARD}prerequisite DAG has a cycle among: {sorted(cycle)}")

    modules = m.get("modules", [])
    mod_ids = [mod["id"] for mod in modules]
    mod_order = {mid: i for i, mid in enumerate(mod_ids)}
    if len(set(mod_ids)) != len(mod_ids):
        flags.append(f"{HARD}duplicate module id(s): {sorted({x for x in mod_ids if mod_ids.count(x) > 1})}")

    # module-level referential integrity
    for mod in modules:
        for dep in mod.get("depends_on", []):
            if dep not in mod_order:
                flags.append(f"{HARD}module {mod['id']} depends_on unknown module: {dep}")
        for sk in mod.get("requires_skills", []) + mod.get("teaches_skills", []):
            if sk not in nodeset:
                flags.append(f"{HARD}module {mod['id']} references unknown skill node: {sk}")

    # earliest course-position at which each skill is taught (module granularity)
    skill_taught_at: dict[str, int] = {}
    for mod in modules:
        idx = mod_order[mod["id"]]
        for sk in mod.get("teaches_skills", []):
            skill_taught_at[sk] = min(skill_taught_at.get(sk, idx), idx)

    flat = flatten_lessons(m)
    lesson_pos = {l["id"]: i for i, l in enumerate(flat)}
    lesson_ids = set(lesson_pos)

    for i, l in enumerate(flat):
        brief = l.get("brief", {})
        l_mod_idx = mod_order.get(l.get("module"), 1_000_000)
        for pre in brief.get("prerequisites", []):
            if pre in lesson_ids:
                if lesson_pos[pre] >= i:
                    flags.append(f"{HARD}forward dependency: lesson {l['id']} requires {pre} taught later")
            elif pre in nodeset:
                at = skill_taught_at.get(pre)
                if at is None:
                    flags.append(f"{HARD}lesson {l['id']} requires skill never taught: {pre}")
                elif at > l_mod_idx:
                    flags.append(f"{HARD}forward dependency: lesson {l['id']} requires skill {pre} taught later")
            else:
                flags.append(f"{HARD}lesson {l['id']} prerequisite resolves to nothing (typo?): {pre}")
    return _result("dag", flags)


# ── briefs ──────────────────────────────────────────────────────────────────────

def check_briefs(m: dict) -> dict:
    flags: list[str] = []
    lessons = m.get("lessons", [])
    ids = [l["id"] for l in lessons]
    dups = sorted({x for x in ids if ids.count(x) > 1})
    if dups:
        flags.append(f"{HARD}duplicate lesson id(s): {dups}")

    if lessons:
        ordered = flatten_lessons(m)
        if ordered and ordered[0].get("brief", {}).get("dominant_job") != "motivate":
            flags.append(f"{ADV}first lesson '{ordered[0].get('id')}' is not a course opener "
                         f"(dominant_job motivate) — courses open with a welcome lesson that already puts code in the reader's hands (forms/course.md)")
    for l in lessons:
        b = l.get("brief", {})
        lid = l.get("id", "?")
        # absent / null / empty-string is "missing"; an empty LIST/DICT is allowed
        # (prerequisites=[] is legal for the first lesson; just_in_time may be {}).
        kind = b.get("kind", "build")
        if kind not in LESSON_KINDS:
            flags.append(f"{HARD}brief {lid} kind not in enum {sorted(LESSON_KINDS)}: {kind!r}")
            kind = "build"
        required = BRIEF_CORE_KEYS + (BRIEF_BUILD_KEYS if kind == "build" else [])
        missing = [k for k in required
                   if k not in b or b[k] is None or (isinstance(b[k], str) and not b[k].strip())]
        if missing:
            flags.append(f"{HARD}brief {lid} missing required key(s): {missing}")
        if not b.get("objectives"):
            flags.append(f"{HARD}brief {lid} has no objectives (need ≥1 measurable, Bloom-tagged)")

        job = b.get("dominant_job")
        if job not in DOMINANT_JOBS:
            flags.append(f"{HARD}brief {lid} dominant_job not in enum: {job!r}")
        elif job in GUEST_ONLY_JOBS:
            flags.append(f"{ADV}brief {lid} dominant_job '{job}' is a guest-only job — usually a guest, "
                         f"not a whole-lesson backbone (see lesson-brief-schema §D)")

        a = b.get("assessment", "")
        gate_txt = str(a.get("gate", "")) if isinstance(a, dict) else str(a or "")
        if not gate_txt.strip():
            flags.append(f"{HARD}brief {lid} has no assessment gate (must gate on doing)")
        elif PASSIVE_ASSESSMENT_RE.search(gate_txt) and not _has_doing_verb(gate_txt):
            flags.append(f"{HARD}brief {lid} assessment is passive (watch/read) — gate on DOING")
        if kind == "build" and not b.get("verify"):
            flags.append(f"{ADV}brief {lid} has no verify command (verify: {{command, expect}} — "
                         f"the one-line paste-and-see proof; feeds the CI smoke tier)")
        # corpus-signature blocklist (frozen; references/corpus-signatures.txt)
        import json as _json
        hay = _json.dumps({k: b.get(k) for k in ("title", "hook", "concept_spec",
                          "artifact_spec", "color")}, ensure_ascii=False).lower()
        for sig in _signatures():
            if sig in hay:
                flags.append(f"{HARD}brief {lid} carries corpus signature '{sig}' — learn the move, "
                             f"never reuse the artifact/phrase (forms/course.md §Corpus stance)")

        d = b.get("difficulty")
        if isinstance(d, int) and not (1 <= d <= 3):
            flags.append(f"{ADV}brief {lid} difficulty {d} out of 1-3")

        for obj in b.get("objectives", []):
            stmt = (obj or {}).get("statement", "").lower()
            if any(w in stmt for w in WEAK_BLOOM_VERBS):
                flags.append(f"{ADV}brief {lid} objective uses a weak verb (know/understand…): {stmt!r}")

        # est_length is the writer's length CONTRACT — a short target yields a short
        # lesson, so the rule lives here: course lessons target ~3000-4500 words.
        import re as _re
        el = str(b.get("est_length", ""))
        nums = [int(n.replace(",", "")) for n in _re.findall(r"[\d,]+", el) if n.strip(",")]
        target = max(nums) if nums else 0
        if el and target and target < LESSON_TARGET_MIN:
            flags.append(f"{ADV}brief {lid} est_length target ~{target}w is short for a course "
                         f"lesson — the writer writes to this number; course lessons run "
                         f"~{LESSON_TARGET_MIN}-4500w (forms/course.md). Raise the target.")
    return _result("briefs", flags)


def _has_doing_verb(s: str) -> bool:
    return bool(re.search(
        r"\b(build|write|deploy|derive|implement|test|pass|ship|fix|run|submit|create)\b", s, re.I))


# ── ladder ──────────────────────────────────────────────────────────────────────

def check_ladder(m: dict) -> dict:
    flags: list[str] = []
    modules = m.get("modules", [])
    prev_rung = -1
    prev_band = 0
    for mod in modules:
        rung = mod.get("artifact_rung")
        if rung is None:
            flags.append(f"{ADV}module {mod['id']} has no artifact_rung")
            continue
        if rung < prev_rung:
            flags.append(f"{HARD}artifact ladder goes backward at {mod['id']} (rung {rung} < {prev_rung})")
        prev_rung = max(prev_rung, rung)
        band = mod.get("difficulty_band", prev_band)
        if band < prev_band:
            flags.append(f"{ADV}difficulty band dips at {mod['id']} ({band} < {prev_band}) — confirm a deliberate plateau")
        prev_band = band

    # cadence coverage (advisory): every lesson appears in the release schedule
    rel = (m.get("cadence", {}) or {}).get("release", {}) or {}
    sched = rel.get("schedule", [])
    if sched:
        scheduled = {lid for wk in sched for lid in wk.get("publish", [])}
        all_l = {l["id"] for l in m.get("lessons", [])}
        miss = sorted(all_l - scheduled)
        if miss:
            flags.append(f"{ADV}lessons absent from the release schedule: {miss}")
    return _result("ladder", flags)


# ── capstone ────────────────────────────────────────────────────────────────────

def check_capstone(m: dict) -> dict:
    flags: list[str] = []
    cap = (m.get("assessment", {}) or {}).get("capstone", {}) or {}
    taught = set()
    for mod in m.get("modules", []):
        taught.update(mod.get("teaches_skills", []))
    for sk in cap.get("requires_skills", []):
        if sk not in taught:
            flags.append(f"{HARD}capstone requires a skill never taught: {sk}")
    if not cap:
        flags.append(f"{ADV}no capstone defined")
    return _result("capstone", flags)


# ── outcomes ────────────────────────────────────────────────────────────────────

def check_length(m: dict) -> dict:
    """length_target.lessons must match the real lesson count (the cover renders it,
    first thing a learner reads). Prevents a stale hand-set count (the '20 lessons' bug)."""
    flags = []
    lt = m.get("course", {}).get("length_target", {})
    declared = lt.get("lessons")
    actual = len(m.get("lessons", []))
    if declared is not None and actual and declared != actual:
        flags.append(f"{HARD}length_target.lessons={declared} but the course has {actual} lessons "
                     f"— the cover states this; set it to {actual} and recompute hours")
    return _result("length", flags)


def check_outcomes(m: dict) -> dict:
    flags: list[str] = []
    course = m.get("course", {})
    outcome_ids = {o["id"] for o in course.get("terminal_outcomes", []) if "id" in o}
    proofs = (m.get("assessment", {}) or {}).get("proof_matrix", []) or []
    proven = {p.get("outcome") for p in proofs}

    for oid in sorted(outcome_ids - proven):
        flags.append(f"{HARD}terminal outcome has no proof in assessment: {oid}")
    for pid in sorted(proven - outcome_ids):
        flags.append(f"{HARD}proof_matrix references unknown outcome: {pid}")

    for mod in m.get("modules", []):
        traces = mod.get("traces_to", [])
        if not traces:
            flags.append(f"{ADV}module {mod['id']} traces to no terminal outcome")
        for t in traces:
            if t not in outcome_ids:
                flags.append(f"{HARD}module {mod['id']} traces_to unknown outcome: {t}")
    return _result("outcomes", flags)


def _signatures() -> list[str]:
    """Frozen corpus-signature blocklist (lowercased), one per line, # comments."""
    from pathlib import Path
    p = Path(__file__).resolve().parent.parent / "references" / "corpus-signatures.txt"
    if not p.is_file():
        return []
    out = []
    for ln in p.read_text("utf-8").splitlines():
        s = ln.strip()
        if s and not s.startswith("#"):
            out.append(s.lower())
    return out


def _parse_visuals(text: str):
    """Parse ```visual blocks. Returns (blocks, defects): blocks = [{fields, line}],
    defects = fence irregularities (closing fence carrying prose, unclosed block)."""
    lines = text.split("\n")
    blocks, defects = [], []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```visual":
            start = i + 1
            j = start
            body = []
            closed = False
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith("```"):
                    closed = True
                    if s != "```":
                        defects.append(f"line {j + 1}: visual closing fence carries prose "
                                       f"({s[:50]!a}) — the insert-only pass split a sentence")
                    break
                body.append(lines[j])
                j += 1
            if not closed:
                defects.append(f"line {start}: visual block never closed")
            fields = {}
            cur = None
            for s in body:
                import re as _re
                m2 = _re.match(r"^([a-z_]+):\s*(.*)$", s)
                if m2 and not s.startswith((" ", "\t")):
                    cur = m2.group(1)
                    fields[cur] = m2.group(2).strip().lstrip("|").strip()
                elif cur is not None and s.strip():
                    fields[cur] = (fields.get(cur, "") + " " + s.strip()).strip()
            blocks.append({"fields": fields, "line": start})
            i = j + 1
        else:
            i += 1
    return blocks, defects


def draft_metrics(text: str) -> dict:
    """Deterministic per-draft metrics: prose words, longest uninterrupted prose wall
    (words + ending line), prose words before the first code / any fence, visual stats."""
    lines = text.split("\n")
    in_fence = False
    first_code = None
    first_fence = None
    prose = 0
    run = 0
    longest = 0
    longest_end = 0
    for idx, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("```"):
            if not in_fence:
                in_fence = True
                info = s[3:].strip()
                if first_fence is None:
                    first_fence = prose
                if first_code is None and info != "visual":
                    first_code = prose
                if run > longest:
                    longest, longest_end = run, idx - 1
                run = 0
            else:
                in_fence = False
            continue
        if in_fence:
            continue
        w = len(ln.split())
        prose += w
        run += w
    if run > longest:
        longest, longest_end = run, len(lines)
    blocks, defects = _parse_visuals(text)
    valid = [b for b in blocks
             if all(b["fields"].get(k, "").strip() for k in VISUAL_FIELDS)
             and b["fields"].get("type") in VISUAL_TYPES]
    return {"prose_words": prose, "longest_wall": longest, "wall_end_line": longest_end,
            "first_code_words": first_code, "first_fence_words": first_fence,
            "visual_blocks": len(blocks), "visual_valid": len(valid),
            "visual_types": sorted({b["fields"].get("type") for b in valid}),
            "visual_defects": defects,
            "visual_alts": [b["fields"].get("alt", "") for b in valid],
            "visual_titles": [b["fields"].get("title", "") for b in valid]}


# Dead-zone thresholds: calibrated against the house's own good drafts (~400w reads
# fine); the point is text-block aesthetics — long explanation is broken by the thing
# it explains — never a fixed rhythm. Deliberate plateaus survive the advisory.
WALL_ADVISORY = 450
WALL_HARD = 700
FIRST_DO_FLOOR = 300      # prose words before the first runnable fence (build lessons)
FIRST_DO_FLOOR_OPENER = 150
# Visual density scales with length: one parsing visual per ~this many prose words,
# floor of 2. A ratio, not a fixed rhythm — the point is that a long lesson earns
# more graphics, not that graphics land on a metronome. Tune the divisor to taste.
VISUAL_WORDS_PER = 600
VISUAL_FLOOR_MIN = 2


def visual_floor(prose_words: int) -> int:
    import math
    return max(VISUAL_FLOOR_MIN, math.ceil(prose_words / VISUAL_WORDS_PER))


def check_drafts(course_dir, m: dict | None = None) -> dict:
    """Written-lesson gates (forms/course.md): >=2 PARSING visual blocks per lesson;
    no prose wall past the thresholds; code in hands early; no corpus signatures."""
    from pathlib import Path
    flags: list[str] = []
    d = Path(course_dir) / "lessons" / "drafts"
    drafts = sorted(d.glob("*.md")) if d.is_dir() else []
    if not drafts:
        return _result("drafts", ["ok: no drafts yet (gates apply as lessons get written)"])

    # stem -> (kind, is_opener) from the manifest, mirroring the scaffold's naming
    import re as _re
    stem_info = {}
    if m:
        mods = {mod["id"]: i for i, mod in enumerate(m.get("modules", []))}
        flat = flatten_lessons(m)
        for i, l in enumerate(flat):
            safe = _re.sub(r"[^a-z0-9-]", "-", str(l["id"]).lower()).strip("-") or "x"
            stem = f"m{mods.get(l.get('module'), 99):02d}-l{l.get('order', 0)}-{safe}"
            stem_info[stem] = {"kind": l.get("brief", {}).get("kind", "build"),
                               "opener": i == 0}

    import re as _re2
    sigs = _signatures()
    for p in drafts:
        if not _re2.match(r"m\d+-l\d", p.stem):
            continue  # not a lesson draft (e.g. 000-cover.md) — course-level, skip
        text = p.read_text("utf-8")
        # a lesson must open on its H1 title; anything before it is leaked editor/agent
        # scaffolding ("Returning the fixed lesson:", "I've identified...") — HARD.
        _first = next((ln for ln in text.split("\n") if ln.strip()), "")
        if not _first.startswith("# "):
            flags.append(f"{HARD}draft {p.name}: does not open on its H1 title — leaked "
                         f"editor/agent scaffolding before the title; strip everything above '# '")
        mx = draft_metrics(text)
        info = stem_info.get(p.stem, {})
        kind = info.get("kind", "build")
        opener = info.get("opener", False)

        # visual floor scales with length: max(2, ceil(prose_words / VISUAL_WORDS_PER))
        floor = visual_floor(mx["prose_words"])
        if mx["visual_valid"] < floor:
            broken = mx["visual_blocks"] - mx["visual_valid"]
            extra = f" ({broken} malformed/incomplete block(s) found)" if broken else ""
            flags.append(f"{HARD}draft {p.name}: {mx['visual_valid']} valid visual block(s){extra} — "
                         f"a {mx['prose_words']}-word lesson earns >={floor} that parse "
                         f"(1 per ~{VISUAL_WORDS_PER}w, floor {VISUAL_FLOOR_MIN}; "
                         f"type/title/purpose/data/prompt/alt; references/visual-placeholders.md)")
        for defect in mx["visual_defects"]:
            flags.append(f"{HARD}draft {p.name}: {defect}")
        if mx["visual_valid"] >= 2 and len(mx["visual_types"]) < 2:
            flags.append(f"{ADV}draft {p.name}: all visuals share one type "
                         f"({mx['visual_types']}) — two blocks, one visual idea; vary the kind")
        for alt, title in zip(mx["visual_alts"], mx["visual_titles"]):
            wc = len(alt.split())
            low = alt.lower()
            if (wc < 8 or wc > 30 or low == title.lower()
                    or low.startswith(("image of", "diagram of", "visual of", "illustration of"))):
                flags.append(f"{ADV}draft {p.name}: alt text weak ({alt[:50]!a}) — one 8-30 word "
                             f"sentence that stands in for the visual, not a label")

        # text-block aesthetics: prose walls
        if mx["longest_wall"] > WALL_HARD:
            flags.append(f"{HARD}draft {p.name}: {mx['longest_wall']}-word prose wall ending line "
                         f"{mx['wall_end_line']} — break long explanation with the thing it explains "
                         f"(a runnable fence or a visual), never past {WALL_HARD} words")
        elif mx["longest_wall"] > WALL_ADVISORY:
            flags.append(f"{ADV}draft {p.name}: {mx['longest_wall']}-word prose run ends line "
                         f"{mx['wall_end_line']} — confirm the plateau is deliberate")

        # time-to-first-do (needs the manifest to know kind/opener)
        if stem_info:
            floor = FIRST_DO_FLOOR_OPENER if opener else FIRST_DO_FLOOR
            first = mx["first_code_words"] if kind == "build" else mx["first_fence_words"]
            if first is None or first > floor:
                where = "no runnable fence at all" if first is None else f"first at word {first}"
                flags.append(f"{HARD}draft {p.name}: {where} — put a do-element in the reader's "
                             f"hands inside the first {floor} words ({'opener' if opener else kind})")

        # corpus signatures in prose
        low = text.lower()
        for sig in sigs:
            if sig in low:
                flags.append(f"{HARD}draft {p.name}: corpus signature '{sig}' — "
                             f"learn the move, never reuse it (forms/course.md §Corpus stance)")

        # setup guardrail: a tool invoked with no install step in the draft is the
        # "command not found on the happy path" class the round-2 review caught (advisory).
        _TOOLS = {"anvil": "foundryup", "forge": "foundryup", "cast": "foundryup",
                  "cargo build-sbf": "rustup", "cargo new": "rustup", "anchor ": "avm",
                  "solana ": "release.anza.xyz", "solana-keygen": "release.anza.xyz",
                  "bitcoind": "bitcoin", "npx tsx": "npm install", "ts-node": "npm install"}
        _low = text.lower()
        for tool, installer in _TOOLS.items():
            if tool in _low and installer.lower() not in _low and "install" not in _low.split(tool)[0][-400:]:
                flags.append(f"{ADV}draft {p.name}: invokes `{tool.strip()}` but shows no install step "
                             f"(expected `{installer}` or an install line) — beginners hit command-not-found")
                break

        # em-dash policy: the top AI tell — house ships essentially none. Counts prose +
        # visual-block specs, not code fences. tools/dedash.py drives this to 0.
        em = count_prose_emdashes(text)
        if em > 2:
            flags.append(f"{HARD}draft {p.name}: {em} em-dashes outside code — the em-dash is a top "
                         f"AI tell; run tools/dedash.py (house policy: essentially none)")
        elif em >= 1:
            flags.append(f"{ADV}draft {p.name}: {em} em-dash(es) outside code — run tools/dedash.py to clear")

        # depth bands (raised again 2026-07-06: foundational topics run long).
        # Advisory only + a wide band — the right length is topic-driven, not a target.
        words = mx["prose_words"]
        if words < 2400:
            flags.append(f"{ADV}draft {p.name}: {words} prose words — foundational course lessons "
                         f"run ~3000-4500 (more for keystone topics); this reads thin")
        elif words > 5500:
            flags.append(f"{ADV}draft {p.name}: {words} prose words — past ~5500; a lesson this long "
                         f"is usually two lessons — consider splitting, don't just cut explanation")

        # paragraph rhythm: prose must breathe — paragraphs vary from a 1-sentence
        # punch to a 4+-sentence developed run; uniform staccato reads stitched.
        paras = []
        cur = []
        fence = False
        for ln in text.split("\n"):
            s = ln.strip()
            if s.startswith("```"):
                fence = not fence
                continue
            if fence:
                continue
            if not s:
                if cur:
                    paras.append(" ".join(cur))
                    cur = []
            elif not s.startswith(("#", "-", "|", ">", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
                cur.append(s)
        if cur:
            paras.append(" ".join(cur))
        import re as _re2
        counts = [len([x for x in _re2.split(r"[.?]\s", p2) if x.strip()])
                  for p2 in paras if len(p2.split()) > 10]
        if counts:
            developed = sum(1 for c in counts if c >= 4)
            if developed == 0:
                flags.append(f"{ADV}draft {p.name}: no developed paragraph (4+ sentences) across "
                             f"{len(counts)} paragraphs — prose reads stitched; vary paragraph "
                             f"length from 1-sentence punches to 4-sentence runs")
            elif sum(counts) / len(counts) < 1.8:
                flags.append(f"{ADV}draft {p.name}: mean {sum(counts)/len(counts):.1f} sentences/"
                             f"paragraph — staccato; let some paragraphs develop")
    return _result("drafts", flags)


def check_research(m: dict) -> dict:
    """Kit dispatch is literal (research-grounding.md): a verified claim must cite a
    kit surface; briefed lessons without a research scaffold are flagged."""
    flags: list[str] = []
    for l in m.get("lessons", []):
        lid = l.get("id", "?")
        r = l.get("research")
        if not r:
            flags.append(f"{ADV}lesson {lid} has no research scaffold (SKILL.md step 9 is per-lesson)")
            continue
        for c in r.get("claims", []):
            surf = str(c.get("mcp", ""))
            if c.get("status") == "verified" and surf not in KIT_SURFACES:
                flags.append(f"{HARD}lesson {lid} claim {c.get('id', '?')}: status=verified via "
                             f"non-kit surface '{surf}' — dispatch a kit surface and record it, or "
                             f"mark the claim unverified (research-grounding.md §Dispatch is literal)")
    return _result("research", flags)


def check_artifacts(m: dict) -> dict:
    """The accretion graph: 'the toolkit becomes the bot' as a checkable DAG.
    Structured artifact edges are optional; once any lesson declares one, edges must
    run forward and non-terminal artifacts should be consumed downstream."""
    flags: list[str] = []
    flat = flatten_lessons(m)
    declared = []
    for i, l in enumerate(flat):
        art = l.get("brief", {}).get("artifact")
        if isinstance(art, dict) and art.get("id"):
            declared.append((art["id"], l["id"], i, art.get("consumes") or [], art.get("terminal")))
    if not declared:
        return _result("artifacts", ["ok: no structured artifact graph (prose artifact_spec only)"])
    pos = {}
    for aid, lid, i, cons, term in declared:
        if aid in pos:
            flags.append(f"{HARD}duplicate artifact id '{aid}' (lesson {lid})")
        pos[aid] = i
    consumed = set()
    for aid, lid, i, cons, term in declared:
        for c in cons:
            if c not in pos:
                flags.append(f"{HARD}lesson {lid} artifact '{aid}' consumes unknown artifact '{c}'")
            elif pos[c] >= i:
                flags.append(f"{HARD}lesson {lid} artifact '{aid}' consumes '{c}' built later — "
                             f"accretion runs forward only")
            else:
                consumed.add(c)
    last = max(p for p in pos.values())
    for aid, lid, i, cons, term in declared:
        if aid not in consumed and not term and i < last:
            flags.append(f"{ADV}artifact '{aid}' ({lid}) is consumed by nothing downstream — wire it "
                         f"in or flag terminal: <reason> ('the toolkit becomes the bot')")
    return _result("artifacts", flags)


CHECKS = {"dag": check_dag, "briefs": check_briefs, "ladder": check_ladder,
          "capstone": check_capstone, "outcomes": check_outcomes,
          "research": check_research, "artifacts": check_artifacts, "length": check_length}


# ── runner ──────────────────────────────────────────────────────────────────────

def _print(res: dict) -> None:
    mark = "FAIL" if res["hard"] else "ok"
    print(f"[{mark}] {res['name']}")
    for f in res["flags"]:
        print("   - " + f)


def run(m: dict, names: list[str]) -> int:
    any_hard = False
    for n in names:
        res = CHECKS[n](m)
        _print(res)
        any_hard = any_hard or res["hard"]
    print(f"\nGATE: {'FAIL (hard)' if any_hard else 'PASS'}")
    return 1 if any_hard else 0


def _good_manifest() -> dict:
    return {
        "schema_version": 1,
        "course": {
            "id": "demo", "title": "Demo",
            "terminal_outcomes": [{"id": "to-pda", "bloom": "create", "statement": "build a PDA app"}],
        },
        "dag": {"nodes": ["account-model", "programs-instructions", "pdas"],
                "edges": [["account-model", "programs-instructions"],
                          ["programs-instructions", "pdas"], ["account-model", "pdas"]]},
        "modules": [
            {"id": "m-accounts", "artifact_rung": 1, "difficulty_band": 1,
             "teaches_skills": ["account-model", "programs-instructions"],
             "requires_skills": [], "traces_to": ["to-pda"]},
            {"id": "m-pdas", "artifact_rung": 3, "difficulty_band": 2,
             "depends_on": ["m-accounts"], "teaches_skills": ["pdas"],
             "requires_skills": ["account-model"], "traces_to": ["to-pda"]},
        ],
        "lessons": [
            {"id": "the-counter", "module": "m-accounts", "order": 1, "brief": {
                "id": "the-counter", "title": "The counter",
                "objectives": [{"bloom": "implement", "statement": "write account state"}],
                "prerequisites": [], "hook": "h", "concept_spec": "c", "artifact_spec": "a",
                "exercise_spec": "e", "the_tradeoff": "t", "just_in_time": {"define": [], "footguns": []},
                "assessment": "anchor test passes", "difficulty": 1, "fading": "worked",
                "dominant_job": "show-how"}},
            {"id": "pda-state", "module": "m-pdas", "order": 1, "brief": {
                "id": "pda-state", "title": "PDA state",
                "objectives": [{"bloom": "implement", "statement": "derive a PDA"}],
                "prerequisites": ["the-counter", "account-model"], "hook": "h", "concept_spec": "c",
                "artifact_spec": "a", "exercise_spec": "e", "the_tradeoff": "t",
                "just_in_time": {"define": [], "footguns": []},
                "assessment": "test: two users get distinct PDAs", "difficulty": 2,
                "fading": "completion", "dominant_job": "derive-why"}},
        ],
        "assessment": {
            "proof_matrix": [{"outcome": "to-pda", "proven_by": "capstone"}],
            "capstone": {"id": "cap", "requires_skills": ["pdas", "account-model"]},
        },
        "cadence": {"release": {"schedule": [{"week": 1, "publish": ["the-counter", "pda-state"]}]}},
    }


def selftest() -> int:
    ok = True

    def check(c, m):
        nonlocal ok
        print(("PASS" if c else "FAIL") + " - " + m)
        ok = ok and c

    g = _good_manifest()
    check(not check_dag(g)["hard"], "good course: dag clean")
    check(not check_briefs(g)["hard"], "good course: briefs clean")

    # concept lesson: no build triad required, but bad kind is HARD
    import copy
    gc = copy.deepcopy(g)
    gc["lessons"][1]["brief"].update({"kind": "concept"})
    for k in ("artifact_spec", "exercise_spec", "fading"):
        gc["lessons"][1]["brief"].pop(k, None)
    check(not check_briefs(gc)["hard"], "concept lesson: build triad not required")
    gc["lessons"][1]["brief"]["kind"] = "video"
    check(any("kind not in enum" in f for f in check_briefs(gc)["flags"]),
          "bad kind is HARD")

    # non-kebab ids are HARD (they become filesystem paths)
    gi = copy.deepcopy(g)
    gi["modules"][0]["id"] = "../Evil Module"
    check(any("not kebab-case" in f for f in check_dag(gi)["flags"]),
          "non-kebab module id is HARD")
    check(not check_ladder(g)["hard"], "good course: ladder clean")
    check(not check_capstone(g)["hard"], "good course: capstone clean")
    check(not check_outcomes(g)["hard"], "good course: outcomes clean")

    # cycle
    c = _good_manifest()
    c["dag"]["edges"].append(["pdas", "account-model"])
    check(check_dag(c)["hard"], "cycle -> dag HARD")

    # forward dependency (lesson requires a later lesson)
    f = _good_manifest()
    f["lessons"][0]["brief"]["prerequisites"] = ["pda-state"]
    check(check_dag(f)["hard"], "forward lesson dep -> dag HARD")

    # dangling prerequisite
    d = _good_manifest()
    d["lessons"][1]["brief"]["prerequisites"] = ["ghost-lesson"]
    check(check_dag(d)["hard"], "dangling prereq -> dag HARD")

    # unknown skill node on a module
    u = _good_manifest()
    u["modules"][0]["teaches_skills"].append("ghost-skill")
    check(check_dag(u)["hard"], "unknown skill node -> dag HARD")

    # bad dominant_job enum
    j = _good_manifest()
    j["lessons"][0]["brief"]["dominant_job"] = "explain"
    check(check_briefs(j)["hard"], "bad dominant_job -> briefs HARD")

    # guest-only job as backbone -> advisory, not hard
    gj = _good_manifest()
    gj["lessons"][0]["brief"]["dominant_job"] = "frame"
    rj = check_briefs(gj)
    check(not rj["hard"] and any("guest-only" in x for x in rj["flags"]), "guest job as backbone -> advisory")

    # missing required brief key
    mk = _good_manifest()
    del mk["lessons"][0]["brief"]["hook"]
    check(check_briefs(mk)["hard"], "missing brief key -> briefs HARD")

    # passive assessment
    pa = _good_manifest()
    pa["lessons"][0]["brief"]["assessment"] = "watch the video walkthrough"
    check(check_briefs(pa)["hard"], "passive assessment -> briefs HARD")

    # duplicate lesson id
    dl = _good_manifest()
    dl["lessons"][1]["id"] = "the-counter"
    check(check_briefs(dl)["hard"], "duplicate lesson id -> briefs HARD")

    # ladder goes backward
    lb = _good_manifest()
    lb["modules"][1]["artifact_rung"] = 0
    check(check_ladder(lb)["hard"], "backward artifact rung -> ladder HARD")

    # capstone needs an untaught skill
    cs = _good_manifest()
    cs["assessment"]["capstone"]["requires_skills"] = ["cpis"]
    check(check_capstone(cs)["hard"], "untaught capstone skill -> capstone HARD")

    # orphan outcome
    oo = _good_manifest()
    oo["assessment"]["proof_matrix"] = []
    check(check_outcomes(oo)["hard"], "orphan outcome -> outcomes HARD")

    # module traces to unknown outcome
    mt = _good_manifest()
    mt["modules"][0]["traces_to"] = ["to-ghost"]
    check(check_outcomes(mt)["hard"], "module traces to unknown outcome -> outcomes HARD")

    # length_target.lessons must match actual count
    lc = _good_manifest(); lc["course"]["length_target"] = {"lessons": 99}
    check(check_length(lc)["hard"], "wrong length_target.lessons -> length HARD")

    # drafts visual floor
    import tempfile
    from pathlib import Path as _P
    with tempfile.TemporaryDirectory() as td:
        dd = _P(td) / "lessons" / "drafts"
        dd.mkdir(parents=True)
        VB = ("```visual\ntype: diagram\ntitle: t one\npurpose: p\ndata: d\nprompt: pr\n"
              "alt: a full sentence of at least eight words standing in\n```\n")
        VB2 = VB.replace("type: diagram", "type: chart").replace("t one", "t two")
        # ~640 prose words -> floor 2; two valid visuals must pass
        prose = ("word " * 80 + "\n\n```bash\nrun\n```\n\n") * 8   # fences break walls, early code
        (dd / "m00-l1-x.md").write_text("# T\n\n" + prose + VB, "utf-8")
        check(check_drafts(td)["hard"], "draft with 1 valid visual -> drafts HARD")
        (dd / "m00-l1-x.md").write_text("# T\n\n" + prose + VB + VB2, "utf-8")
        check(not check_drafts(td)["hard"], "draft with 2 valid visuals -> drafts clean")
        # empty visual blocks don't count toward the floor
        (dd / "m00-l1-x.md").write_text("# T\n\n" + prose + "```visual\n```\n```visual\n```\n", "utf-8")
        check(check_drafts(td)["hard"], "empty visual blocks don't satisfy the floor")
        # glued closing fence is a defect
        (dd / "m00-l1-x.md").write_text("# T\n\n" + prose + VB + VB2.replace("```\n", "``` glued prose\n", 1)
                                        .replace("```visual``` glued prose", "```visual"), "utf-8")
        # (rebuild simpler: valid + one glued block)
        glued = "```visual\ntype: chart\ntitle: t\npurpose: p\ndata: d\nprompt: pr\nalt: a full sentence of at least eight words here\n``` glued prose\n"
        (dd / "m00-l1-x.md").write_text("# T\n\n" + prose + VB + VB2 + glued, "utf-8")
        check(any("carries prose" in f for f in check_drafts(td)["flags"]),
              "glued closing fence flagged")
        (dd / "m00-l1-x.md").write_text("Returning the fixed lesson:\n\n# T\n\n" + prose + VB + VB2, "utf-8")
        check(any("H1 title" in f for f in check_drafts(td)["flags"]),
              "scaffolding before the H1 title -> drafts HARD")
        # prose wall past the hard cap
        (dd / "m00-l1-x.md").write_text("# T\n\n```bash\nrun\n```\n" + "word " * 720 + "\n" + VB + VB2, "utf-8")
        check(any("prose wall" in f for f in check_drafts(td)["flags"]),
              "700+ word prose wall -> drafts HARD")

    # research: verified claim via non-kit surface
    rg = _good_manifest()
    rg["lessons"][0]["research"] = {"claims": [
        {"id": "C1", "mcp": "canonical-record", "status": "verified"}]}
    check(check_research(rg)["hard"], "verified claim via non-kit surface -> research HARD")
    rg["lessons"][0]["research"]["claims"][0]["mcp"] = "solana-researcher"
    check(not check_research(rg)["hard"], "kit surface -> research clean")

    # artifacts: forward consumption
    ag = _good_manifest()
    ag["lessons"][0]["brief"]["artifact"] = {"id": "tool-a", "consumes": ["tool-b"]}
    ag["lessons"][1]["brief"]["artifact"] = {"id": "tool-b", "consumes": []}
    check(check_artifacts(ag)["hard"], "artifact consuming a later artifact -> artifacts HARD")
    ag["lessons"][0]["brief"]["artifact"] = {"id": "tool-a", "consumes": []}
    ag["lessons"][1]["brief"]["artifact"] = {"id": "tool-b", "consumes": ["tool-a"]}
    check(not check_artifacts(ag)["hard"], "forward accretion graph -> artifacts clean")

    # corpus signature in a brief
    cg = _good_manifest()
    cg["lessons"][0]["brief"]["artifact_spec"] = "build a Restaurant Review app"
    check(any("corpus signature" in f for f in check_briefs(cg)["flags"]),
          "corpus signature in brief -> HARD")

    # short est_length target flags (the length rule)
    sl = _good_manifest()
    sl["lessons"][0]["brief"]["est_length"] = "1400 words / ~12 min"
    check(any("est_length target" in f for f in check_briefs(sl)["flags"]),
          "short est_length target -> briefs advisory")
    sl["lessons"][0]["brief"]["est_length"] = "3500-4500 words / ~32 min"
    check(not any("est_length target" in f for f in check_briefs(sl)["flags"]),
          "on-band est_length -> clean")

    # (cover is index-only; no course.overview narrative is rendered or required)

    print("\n" + ("VALIDATOR SELFTESTS PASSED" if ok else "FAILURES ABOVE"))
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="content-gen validator")
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    for name in list(CHECKS) + ["drafts", "all"]:
        p = sub.add_parser(name)
        p.add_argument("--course", help="course directory (reads manifest.json)")
        p.add_argument("--manifest", help="manifest.json path")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.cmd:
        ap.print_help()
        return 2
    src = getattr(a, "course", None) or getattr(a, "manifest", None)
    if not src:
        print("course: pass --course <dir> or --manifest <file>", file=sys.stderr)
        return 2
    m = load_manifest(src)
    names = list(CHECKS) if a.cmd == "all" else ([] if a.cmd == "drafts" else [a.cmd])
    any_hard = False
    for n in names:
        res = CHECKS[n](m)
        _print(res)
        any_hard = any_hard or res["hard"]
    if a.cmd in ("drafts", "all") and getattr(a, "course", None):
        res = check_drafts(a.course, m)
        _print(res)
        any_hard = any_hard or res["hard"]
    print(f"\nGATE: {'FAIL (hard)' if any_hard else 'PASS'}")
    return 1 if any_hard else 0


if __name__ == "__main__":
    raise SystemExit(main())
