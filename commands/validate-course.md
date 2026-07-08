---
description: "Run the deterministic structural gate on a generated course (DAG, briefs, ladder, capstone, outcomes)"
argument-hint: "--course content/courses/<id> (or --manifest manifest.json)"
---

Gate a generated course before handing lessons to `writer-style`. Run the
deterministic checks directly:

```bash
# Resolve the content-gen skill dir (plugin / project / clone), then call the tool with absolute paths:
SKILL="${CLAUDE_PLUGIN_ROOT:+$CLAUDE_PLUGIN_ROOT/skills/content-gen}"
[ -d "$SKILL" ] || SKILL=".claude/skills/content-gen"; [ -d "$SKILL" ] || SKILL="skills/content-gen"

# everything (exit 1 if any HARD fired):
python3 "$SKILL/tools/validate_course.py" all --course content/courses/<id>
# or a single dimension, against a manifest before emit:
python3 "$SKILL/tools/validate_course.py" dag --manifest manifest.json
```

Subcommands: `drafts` (≥2 visual blocks per written lesson — HARD) · `dag` (acyclicity, no-forward-deps, ids/skills resolve) · `briefs`
(schema completeness, `dominant_job` enum, gated-on-doing, id uniqueness) ·
`ladder` (artifact-rung monotonicity, difficulty/cadence) · `capstone` (requires
only taught skills) · `outcomes` (every terminal outcome ⇄ a proof) · `all`.

Interpret:
- **`[HARD]` flags → FIX before handoff.** They break the prerequisite-DAG walk or
  the writer handoff (cycles, forward deps, dangling ids, bad `dominant_job`,
  missing brief keys, ungated lessons, backward ladder, untaught capstone skill,
  orphan outcome).
- **`[advisory]` flags → weigh, don't auto-fix.** Smells (difficulty plateaus,
  weak Bloom verbs, guest-only job as a backbone, lessons absent from the release
  schedule). Confirm each is deliberate.

Structural correctness is mechanical; **pedagogical quality** (is the hook felt?
the tradeoff real? the `dominant_job` right?) is a human/agent judgement — see
`skills/content-gen/references/quality-bar.md`. There is intentionally no
"course score."
