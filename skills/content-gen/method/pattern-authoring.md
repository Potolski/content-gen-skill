# Method: pattern-authoring
> How to add or refresh a `patterns/*.md` file at the same quality bar — the required house-shape sections,
> the "pulled-from" provenance rule, the anti-trigger discipline, and how to wire the new pattern into the
> router, the SKILL.md quick-reference, and the syllabus DAG.

A pattern is a transferable **structural archetype**, not a tip. Adding one is cheap to do badly (another
vague "consider testing" box) and the whole value of the layer is that each pattern earns its place. Keep
this procedural and short.

> The one rule: **a pattern must route.** If you can't write the trigger that selects it *and* the
> anti-trigger that rejects it, it isn't a pattern yet — it's advice. Fold it into an existing pattern
> instead.

---

## Required house shape (mirror the existing files exactly)

A pattern file is a title + a one-line blockquote summary, then these sections **in this order**:

1. `# Pattern: <kebab-name>` + `> ` one-sentence summary (what shape it produces).
2. **## Signature strength** — the one thing it does better than anything else; why it works on a *learner*.
3. **## Route for (triggers)** — the outcome+audience signals that select it (never the topic).
4. **## Anti-triggers (don't lead with this when…)** — when *not* to lead with it, and what to use instead.
5. **## The structure it produces** — a fenced ``` block sketching the concrete shape (modules/rungs/loop).
6. **## Why it works (mechanism)** — the named learning-science mechanism(s), terse.
7. **## Stacks with** — which backbones/guests it composes with, and whether it's a backbone, guest, tier,
   or thread.
8. **## Voice handoff** — the typical `dominant_job` per lesson and the craft it triggers (see below).
9. **## Worked micro-illustration (Solana)** — one concrete, accurate Solana example ending in a
   `dominant_job:` tag.
10. **## What this pattern deliberately EXCLUDES** — the boundary; what it is *not* and must not absorb.
11. **## Pulled from** — provenance (see next section).

Match the tone of `../patterns/security-epoch.md` / `../patterns/build-it-twice.md`: dense, declarative, no filler, ~50–65 lines.

## The "pulled-from" provenance requirement
Every pattern ends with a **## Pulled from** line crediting the real courses/tools/sources the archetype is
distilled from (e.g. "Cyfrin Updraft build-it-twice," "Ackee + Trident," "Solana Compute Budget docs"). A
pattern with no provenance is a guess. Any **Solana technical fact** named in the file (tool names, API
names, CU numbers, ordering) must be **grounded** against the kit's live sources
(`../references/research-grounding.md`; the `solana-dev` MCP `Solana_Documentation_Search` /
`get_documentation`) — do **not** invent APIs. If a fact is load-bearing in a brief, it is load-bearing
here.

## Anti-trigger discipline
The anti-trigger section is what keeps the menu honest. Hold the line:
- State **what to use instead** for each anti-trigger (a pattern is defined as much by what it rejects).
- Distinguish it from its **nearest neighbor** explicitly (e.g. optimization-loop vs build-it-twice;
  testing-thread vs security-epoch) — the boundary case is where routers break.
- Name the **prerequisite** it assumes (e.g. "needs build fluency / a working program first") so it can't be
  routed too early.
- Respect the role taxonomy: a pattern is a **backbone**, a **guest/opener**, a **late tier**, a **thread**,
  or a **lesson template** — say which, and don't let two backbones co-lead (`../routing/ROUTING.md` §4).

## Voice-handoff alignment
The `## Voice handoff` section must use only the `dominant_job` enum from
`../lesson-brief-schema.md` §D: `show-how · derive-why · demystify · economics · frame · sustain ·
motivate`. Honor the rules there — `frame` and `demystify` are **guest-only** jobs (never tag a whole-lesson
backbone with them); security walkthroughs are `show-how` **plus** a security `voice_notes` caution; a
lesson whose real job is derivation is `derive-why` even if it's technical.

## Wiring a new pattern in (three places, all required)
After the file passes the house-shape bar, wire it so the router and the docs actually find it:

1. **`../routing/ROUTING.md`** — add it to the §2 backbone table (or note it as a thread/tier), add a row to
   the §5 pattern → `dominant_job` → voice-handoff table, and add any **decision rule** in §3 that selects
   it (especially for a hard/boundary case). Add it to the §4 stacking notes if it changes the budget (e.g.
   a thread that is *not* counted against the guest budget). Keep edits additive and in the existing table
   format.
2. **`../SKILL.md`** quick-reference table ("The pattern layer (quick reference)") — add one row:
   `| **<name>** | Shapes… | Lead when the course/audience needs… |`. This is the index; `../routing/ROUTING.md` stays
   the authority on *when*.
3. **`../references/solana-syllabus-dag.md`** — if the pattern formalizes something the DAG mentions (a
   thread, a late tier, an entry-point lean), update that note to point at the new
   `../patterns/<name>.md` and drop any "candidate / not yet formalized" caveat.

Then run the router-hardening drill (`router-hardening.md`) so a real set of briefs exercises the new
pattern, and confirm `SKILL.md` ↔ `../routing/ROUTING.md` ↔ the DAG agree.

## The done check
- [ ] All eleven house-shape sections present, in order, in the right tone.
- [ ] Trigger **and** anti-trigger both written; nearest-neighbor boundary stated; prerequisite named.
- [ ] Role declared (backbone / guest / tier / thread / template); no co-leading backbones.
- [ ] `## Pulled from` present; every Solana fact grounded against the kit (no invented APIs).
- [ ] `dominant_job` tags valid per schema §D (guest-only jobs not used as backbones).
- [ ] Wired into `../routing/ROUTING.md` (§2/§3/§5, §4 if needed), the `SKILL.md` table, and the DAG note.
- [ ] router-hardening re-run; the three docs agree.
