#!/usr/bin/env python3
"""
course_lib.py — shared, dependency-free helpers for the content-gen tools.

Single source of truth for:
  - the course manifest model (JSON in, validated here),
  - a minimal YAML *emitter* (dict/list/str/int/bool/None -> readable YAML),
  - DAG helpers (topological sort + forward-dependency walk),
  - the closed vocabularies the validator enforces (dominant_job enum,
    artifact-ladder rung order, lesson-brief required keys).

Design choice (mirrors writer-style's "no third-party deps" stance): the
machine source of truth is JSON (stdlib `json`, bulletproof). The emitted
human/handoff files are YAML, produced by the one-way emitter below. We never
PARSE YAML — only emit it — so there is no fragile regex YAML reader to rot.

    python course_lib.py --selftest
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

# ── closed vocabularies (the validator enforces these) ──────────────────────────

# The voice router input. Must match writer-style's lesson-brief-schema §D enum.
DOMINANT_JOBS = {
    "show-how", "derive-why", "demystify", "economics", "frame", "sustain", "motivate",
}
# Jobs writer-style uses ONLY as single-position guests, never a whole-lesson backbone.
# Allowed as a value, but flagged advisory when set as a lesson's dominant_job.
GUEST_ONLY_JOBS = {"frame", "demystify"}

# Canonical Solana artifact ladder (rung index -> the build). From
# references/solana-syllabus-dag.md §2. Module `artifact_rung` must be monotonic
# non-decreasing along course order; the capstone sits at the top.
ARTIFACT_LADDER = [
    "hello-world",            # 0  toolchain win
    "counter",                # 1  account state, read/write, init
    "spl-token",              # 2  mint -> transfer
    "pda-app",                # 3  vault / escrow / per-user state
    "payment-splitter",       # 4  SOL movement, signers, CPI to system program
    "defi",                   # 5  AMM / auction / fundraiser
    "cpi-composition",        # 6  factory -> child program
    "capstone",               # 7  freeform learner design
]

# Required keys on every lesson brief (lesson-brief-schema §C).
# `kind: build` (the default) also requires the build triad; `kind: concept`
# (non-technical / pure-model lessons) drops it — assessment still gates on doing
# (retrieval / explain-back counts as doing for a concept lesson).
BRIEF_CORE_KEYS = [
    "id", "title", "objectives", "prerequisites", "hook", "concept_spec",
    "the_tradeoff", "just_in_time", "assessment", "difficulty", "dominant_job",
]
BRIEF_BUILD_KEYS = ["artifact_spec", "exercise_spec", "fading"]
LESSON_KINDS = {"build", "concept"}
BRIEF_REQUIRED_KEYS = BRIEF_CORE_KEYS + BRIEF_BUILD_KEYS  # the build profile (back-compat)
# Bloom verbs that signal a measurable objective; "know/understand/learn" do not.
WEAK_BLOOM_VERBS = {"know", "understand", "learn", "be aware", "appreciate", "grasp"}

# Academy publish-schema vocab (references/academy-schema.md). The two interactive
# plugins content-gen can emit as first-class Academy blocks are OPTIONAL on a lesson
# brief (`quiz_blocks`, `coding_challenges`); when present they must satisfy these
# closed sets. Mirrors academy-courses schema/lesson.schema.json.
CHALLENGE_LANGS = {"rust", "typescript"}            # the Academy code runner compiles ONLY these
CHALLENGE_BUILD_TYPES = {"standard", "buildable"}   # code.buildType enum (deployable is a separate bool)

# Strings in an `assessment` field that mean "watch/read", i.e. NOT gated on doing.
PASSIVE_ASSESSMENT_RE = re.compile(
    r"\b(watch|read|review the video|listen|observe)\b", re.I
)
LIFECYCLE = ["briefed", "researched", "drafted", "verified", "published"]

LOG = lambda *a: print(*a, file=sys.stderr, flush=True)


# ── YAML emitter (one-way: Python object -> YAML text) ──────────────────────────

_SIMPLE_TOKEN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_\-./]*$")
_RESERVED = {"true", "false", "null", "yes", "no", "on", "off", "~", ""}
# Strings a YAML reader would silently re-type if emitted bare (numbers, dates, times).
_YAML_AMBIGUOUS = re.compile(
    r"^(?:[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
    r"|0[xob][0-9a-fA-F_]+"
    r"|\d{4}-\d{2}-\d{2}([Tt ].+)?"
    r"|\d+:\d+(:\d+)?)$"
)
# The documented id contract (output-contract.md): kebab-case; ids become filesystem paths.
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
# Kit surfaces a verified claim may cite (research-grounding.md §Dispatch is literal).
KIT_SURFACES = {"solana-dev", "context7", "helius", "surfpool", "deep-research",
                "solana-researcher", "solana-guide", "local-execution", "web", "websearch"}
# Visual placeholder contract (references/visual-placeholders.md).
VISUAL_TYPES = {"flowchart", "diagram", "chart", "table", "comparison", "annotated-code", "timeline"}
VISUAL_FIELDS = ("type", "title", "purpose", "data", "prompt", "alt")


def _scalar(v) -> str:
    """Render a single-line scalar. Bias: simple tokens bare, everything else
    double-quoted (safe; prose stays readable). Multiline strings are handled by
    the caller as block scalars."""
    if v is None:
        return "null"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if _SIMPLE_TOKEN.match(s) and s.lower() not in _RESERVED and not _YAML_AMBIGUOUS.match(s):
        return s
    esc = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{esc}"'


def _emit(obj, indent: int) -> list[str]:
    pad = "  " * indent
    out: list[str] = []
    if isinstance(obj, dict):
        if not obj:
            return [pad + "{}"]
        for k, v in obj.items():
            kk = _scalar(k)
            if isinstance(v, str) and "\n" in v:
                out.append(f"{pad}{kk}: |-")
                out.extend(f"{pad}  {ln}" for ln in v.split("\n"))
            elif isinstance(v, dict) and v:
                out.append(f"{pad}{kk}:")
                out.extend(_emit(v, indent + 1))
            elif isinstance(v, list) and v:
                out.append(f"{pad}{kk}:")
                out.extend(_emit(v, indent + 1))
            elif isinstance(v, dict):
                out.append(f"{pad}{kk}: {{}}")
            elif isinstance(v, list):
                out.append(f"{pad}{kk}: []")
            else:
                out.append(f"{pad}{kk}: {_scalar(v)}")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict) and item:
                inner = _emit(item, indent + 1)
                first = inner[0][len(pad) + 2:]  # strip one level of indent
                out.append(f"{pad}- {first}")
                out.extend(inner[1:])
            elif isinstance(item, list) and item:
                out.append(f"{pad}-")
                out.extend(_emit(item, indent + 1))
            elif isinstance(item, str) and "\n" in item:
                out.append(f"{pad}- |-")
                out.extend(f"{pad}    {ln}" for ln in item.split("\n"))
            else:
                out.append(f"{pad}- {_scalar(item)}")
    else:
        out.append(f"{pad}{_scalar(obj)}")
    return out



_CODE_LANGS = {"bash", "sh", "shell", "console", "python", "py", "rust", "rs",
               "solidity", "sol", "ts", "tsx", "typescript", "js", "javascript",
               "json", "toml", "yaml", "yml", "text", "diff", "sql"}


def _dedash_line(s: str) -> str:
    """Replace em/en-dashes and the spaced double-hyphen with grammatical punctuation.
    Preserves leading indentation and never collapses interior alignment spaces."""
    lead = s[:len(s) - len(s.lstrip(" "))]
    b = s[len(lead):]
    b = re.sub(r" ?[—–] ?", ", ", b)               # em/en dash (with at most one flanking space) -> comma
    b = re.sub(r" -- ", ", ", b)                    # spaced double-hyphen evasion -> comma
    b = re.sub(r"^,\s*", "", b)                     # no leading comma if dash was line-initial
    b = re.sub(r" +,", ",", b)                      # no space before comma
    b = re.sub(r",\s*,", ", ", b)                   # collapse doubled commas
    b = re.sub(r",\s*([.;:\!?])", r"\1", b)          # ", ." -> "."
    return lead + b


def dedash_text(md: str) -> str:
    """Strip em-dashes everywhere EXCEPT inside code fences (bash/python/etc.), where a
    dash may be syntax. Prose and `visual` blocks (which carry prose specs) are cleaned.
    Idempotent."""
    out, in_fence, in_visual = [], False, False
    for ln in md.split("\n"):
        st = ln.strip()
        if st.startswith("```"):
            if not in_fence:
                in_fence = True
                in_visual = st[3:].strip().lower() == "visual"
            else:
                in_fence = False
                in_visual = False
            out.append(ln)
            continue
        if not in_fence or in_visual:
            out.append(_dedash_line(ln))          # prose + visual specs -> comma de-dash
        else:
            # inside code/output fences: em-dashes only ever appear in comments here
            # (our code + strings are ASCII); convert to a plain hyphen, no syntax risk.
            out.append(re.sub(r" ?[—–] ?", " - ", ln) if ("—" in ln or "–" in ln) else ln)
    return "\n".join(out)


def count_prose_emdashes(md: str) -> int:
    """Count em/en-dashes (and spaced double-hyphen) OUTSIDE code fences — the ones a
    reader would ever see. `visual` blocks count; bash/python code fences do not."""
    n, in_fence, in_visual = 0, False, False
    for ln in md.split("\n"):
        st = ln.strip()
        if st.startswith("```"):
            if not in_fence:
                in_fence = True; in_visual = st[3:].strip().lower() == "visual"
            else:
                in_fence = False; in_visual = False
            continue
        if in_fence and not in_visual:
            continue
        n += ln.count("—") + ln.count("–") + ln.count(" -- ")
    return n


def to_yaml(obj) -> str:
    """Emit a Python object as readable YAML text (trailing newline)."""
    return "\n".join(_emit(obj, 0)) + "\n"


# ── manifest io ─────────────────────────────────────────────────────────────────

def load_manifest(path: str | Path) -> dict:
    p = Path(path)
    if p.is_dir():
        p = p / "manifest.json"
    if not p.is_file():
        raise SystemExit(f"course: no manifest at {p}")
    try:
        return json.loads(p.read_text("utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"course: manifest is not valid JSON ({p}): {e}")


def flatten_lessons(manifest: dict) -> list[dict]:
    """Lessons in canonical course order: by module order in course.modules, then
    by each lesson's `order` within its module. Returns the lesson objects."""
    mods = manifest.get("modules", [])
    mod_order = {m["id"]: i for i, m in enumerate(mods)}
    lessons = list(manifest.get("lessons", []))

    def key(l):
        return (mod_order.get(l.get("module"), 1_000_000), l.get("order", 0))

    return sorted(lessons, key=key)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ── DAG helpers ─────────────────────────────────────────────────────────────────

def topo_sort(nodes: list[str], edges: list[list[str]]) -> tuple[list[str], list[str]]:
    """Kahn's algorithm. edges are [from, to] = "from taught before to".
    Returns (order, cycle): on success cycle is []; on failure order is partial
    and cycle lists the nodes still entangled."""
    nodeset = list(dict.fromkeys(nodes))
    indeg = {n: 0 for n in nodeset}
    adj: dict[str, list[str]] = {n: [] for n in nodeset}
    for a, b in edges:
        if a in indeg and b in indeg:
            adj[a].append(b)
            indeg[b] += 1
    queue = [n for n in nodeset if indeg[n] == 0]
    order: list[str] = []
    while queue:
        n = queue.pop(0)
        order.append(n)
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                queue.append(m)
    if len(order) != len(nodeset):
        cycle = [n for n in nodeset if indeg[n] > 0]
        return order, cycle
    return order, []


# ── selftest ────────────────────────────────────────────────────────────────────

def selftest() -> int:
    ok = True

    def check(c, m):
        nonlocal ok
        print(("PASS" if c else "FAIL") + " - " + m)
        ok = ok and c

    # to_yaml: scalars, quoting, nesting, list-of-dicts, multiline
    y = to_yaml({"id": "abc-123", "title": "Store: do it (now)", "n": 3, "b": True,
                 "empty": None, "list": ["x", "y"],
                 "objs": [{"bloom": "implement", "statement": "derive a PDA"}],
                 "blk": "line1\nline2"})
    check("id: abc-123" in y, "simple token stays bare")
    check('title: "Store: do it (now)"' in y, "prose with colon is quoted")
    check("n: 3" in y and "b: true" in y and "empty: null" in y, "int/bool/None render")
    check("  - x" in y and "  - y" in y, "scalar list items")
    check("  - bloom: implement" in y and "    statement:" in y, "list-of-dicts aligns")
    check("blk: |-" in y and "  line1" in y and "  line2" in y, "multiline -> block scalar")

    # round-trip-ish: emitting a brief produces a `lesson:` block
    brief_y = to_yaml({"lesson": {"id": "the-counter", "dominant_job": "show-how"}})
    check(brief_y.startswith("lesson:\n") and "  id: the-counter" in brief_y,
          "brief wraps under lesson:")

    # topo_sort: acyclic order respects edges
    order, cycle = topo_sort(["a", "b", "c"], [["a", "b"], ["b", "c"], ["a", "c"]])
    check(not cycle and order.index("a") < order.index("b") < order.index("c"),
          "acyclic graph sorts in dependency order")
    # cycle detected
    _, cyc = topo_sort(["a", "b"], [["a", "b"], ["b", "a"]])
    check(set(cyc) == {"a", "b"}, "cycle is reported")
    # edge to unknown node is ignored, not a crash
    o2, c2 = topo_sort(["a"], [["a", "ghost"]])
    check(o2 == ["a"] and not c2, "edge to unknown node is ignored")

    # flatten_lessons orders by module then lesson order
    man = {"modules": [{"id": "m1"}, {"id": "m2"}],
           "lessons": [{"id": "l2", "module": "m2", "order": 1},
                       {"id": "l1b", "module": "m1", "order": 2},
                       {"id": "l1a", "module": "m1", "order": 1}]}
    flat = [l["id"] for l in flatten_lessons(man)]
    check(flat == ["l1a", "l1b", "l2"], "flatten_lessons sorts by module then order")

    # vocab sanity
    check("derive-why" in DOMINANT_JOBS and "frame" in GUEST_ONLY_JOBS, "vocab loaded")
    check(ARTIFACT_LADDER.index("counter") < ARTIFACT_LADDER.index("capstone"),
          "artifact ladder ordered")
    check(CHALLENGE_LANGS == {"rust", "typescript"} and "buildable" in CHALLENGE_BUILD_TYPES,
          "academy challenge vocab loaded")

    print("\n" + ("COURSE_LIB SELFTESTS PASSED" if ok else "FAILURES ABOVE"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    print(__doc__)
