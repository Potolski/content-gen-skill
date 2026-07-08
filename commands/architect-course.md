---
description: "Architect a Solana course, emit it as a validated filesystem, and write the lessons through the voice seam"
argument-hint: "<course brief — idea, audience, terminal outcome, length>"
---

The course brief is: $ARGUMENTS — run intake (step 1) against it.

Design the full structure of a Solana/Web3 course and **emit it as a filesystem**
using the **content-gen** skill, then hand each lesson to `writer-style`. Spawn
the **course-architect** agent (or run the procedure yourself, `skills/content-gen/SKILL.md`).

1. **Confirm the brief**: the course idea, the **audience + prior model**
   (absolute-beginner / web2-dev / evm-dev / solana-dev-leveling-up /
   non-technical), the **terminal outcome**, scope/length, format, and credential
   goal. Prefer sensible defaults; ask only on a missing *critical* field.
2. **Backward design** the measurable, Bloom-tagged outcome(s) + the capstone
   first; **map the prerequisite DAG** (`skills/content-gen/references/solana-syllabus-dag.md`),
   grounding the order/APIs against the Solana AI Kit
   (`skills/content-gen/references/research-grounding.md`).
3. **Route** the backbone + lesson template + ≤2 guests by outcome+audience
   (`skills/content-gen/routing/ROUTING.md`); load **only** the routed patterns.
4. **Sequence** modules/lessons up the DAG (thread the artifact ladder, fade the
   scaffold), **write per-lesson briefs** (set `dominant_job`), **design cadence**
   (pedagogy + release) and **research scaffolds**, and pick the **assessment**.
   Ground every concrete API/number that lands in a brief.
5. **Assemble `manifest.json`** per `skills/content-gen/references/output-contract.md`.
6. **Validate, then emit:**
   ```bash
   SKILL="${CLAUDE_PLUGIN_ROOT:+$CLAUDE_PLUGIN_ROOT/skills/content-gen}"
   [ -d "$SKILL" ] || SKILL=".claude/skills/content-gen"; [ -d "$SKILL" ] || SKILL="skills/content-gen"
   python3 "$SKILL/tools/validate_course.py" all --manifest manifest.json     # fix every HARD
   python3 "$SKILL/tools/scaffold_course.py" emit --manifest manifest.json --out content/courses/<id>
   python3 "$SKILL/tools/validate_course.py" all --course content/courses/<id>        # re-check emitted tree
   ```
   Then run the LLM-judge items in `skills/content-gen/references/quality-bar.md`
   (hook felt? tradeoff real? `dominant_job` correct? truly backward-designed?).
7. **Write the lessons**: work `content/courses/<id>/queue/NEXT.md` through the voice
   seam (`skills/content-gen/SKILL.md` §Scope & deliverable) one lesson at a time;
   run the visual-placeholder pass on each draft; save to
   `content/courses/<id>/lessons/drafts/`; update `_state.yaml`; repeat. Note the human
   accuracy-review gate before publish.

Deliverable mode per `skills/content-gen/SKILL.md` §Scope & deliverable
(full-text default; `--brief-only` stops at the handoff packet). Never deploys.
