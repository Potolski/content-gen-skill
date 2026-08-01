# FORMS — routing the content form (step 0, before anything else)

One skill, eight forms. Route the form **first**; then load only that form's file.
The form decides which pipeline steps run, what the brief must contain, and where
output lands. Exemplar corpora live at the repo root when present —
`courses-corpus/PATTERNS.md` (7-course teardown) and `forms-corpus/PATTERNS.md`
(cross-form synthesis; per-form `FORM.md` + `catalog.md`) — load them only when
studying or extending a form (adding one: `../method/pattern-authoring.md`).

## The eight forms

| Form | It is… | Deliverable | Output lands in |
|---|---|---|---|
| `course` | multi-module curriculum with a capstone (the meta-form) | validated filesystem of briefs + per-lesson prose | `content/courses/<id>/` |
| `tutorial` | one sitting, one buildable artifact, steps (reader RUNS it) | fully written text | `content/tutorials/<slug>/` |
| `walkthrough` | guided tour of an EXISTING artifact (reader NAVIGATES it) | fully written text | `content/walkthroughs/<slug>/` |
| `explainer` | expository mechanism deep-dive (reader UNDERSTANDS it) | fully written text | `content/explainers/<slug>/` |
| `essay` | thesis-driven argument (reader can ARGUE it) | fully written text | `content/essays/<slug>/` |
| `litepaper` | canonical protocol/token design-of-record (reader CITES it) | versioned paper text | `content/litepapers/<slug>/` |
| `slides` | slide deck as TEXT (per-slide spec + speaker notes) | deck spec document | `content/slides/<slug>/` |
| `post` | tweet / thread / TL;DR / blurb (`platform` sub-profiles) | short text | inline; saved: threads → `content/threads/<slug>/`, others → `content/posts/<slug>/` |

## Routing procedure

1. **Explicit ask wins.** "slides/deck/presentation/talk/workshop" → `slides` ·
   "tweet" → `post platform:tweet` · "thread/🧵" → `post platform:thread` ·
   "TL;DR/blurb/announcement note" → `post` · "tutorial/how do I build/
   step-by-step" → `tutorial` · "walkthrough/code tour/explain this
   repo|protocol|transaction" → `walkthrough` · "explainer/primer/deep-dive/how X
   works/what is X" → `explainer` · "essay/opinion/why X should" →
   `essay` · **"blog post/article about X"** → `explainer` when expository, `essay`
   when opinion-led — the bare word "post" is NOT a routing signal (a blog post is
   never `post`) · "cookbook/snippet/how do I X in 15 lines" → `tutorial` in
   `recipe` mode · "annotated README/docs for this repo" → `walkthrough`
   `subtype: repo` · "litepaper/whitepaper/tokenomics paper" → `litepaper` (see its scope
   guard — formal proof-bearing whitepapers are declined) · "course/curriculum/
   syllabus/bootcamp" → `course`.
2. **Infer from the payload when unnamed** — *what can the reader DO afterward?*
   RUN a thing → `tutorial`. NAVIGATE an existing thing → `walkthrough`.
   UNDERSTAND a mechanism → `explainer`. ARGUE a contestable claim → `essay`.
   CITE a canonical design → `litepaper`. A multi-week outcome or credential →
   `course`. A live audience + a clock → `slides`. One idea, timely, max reach →
   `post`.
3. **Default on ambiguity: fully written text, smallest form that serves the
   outcome** — `tutorial` if the ask names something buildable, `explainer` for a
   mechanism, else `essay`. Don't interrogate the user for small forms. The one
   exception: confirm before routing `course` when the user didn't say it — a
   course is a filesystem-scale commitment.
4. **Escalation ladder** (same idea, rising permanence): tweet → thread →
   explainer/essay → litepaper. Escalate when the current rung strains; the
   healthy pattern is a **pair** — the thread trails, the long form carries
   (`post.md` §escalation).
5. **Load `forms/<form>.md`** and nothing else from this directory.

## The shared pipeline (every non-course form)

Six steps, scaled by the form file; a `post` runs them in one breath, a
`litepaper` deliberately.

1. **Intake.** Topic, audience + prior model, the single terminal takeaway, length
   target, `visuals` density (default per form), `deliverable` mode (default
   `full-text`; `brief-only` on request).
2. **Outcome.** One measurable, Bloom-tagged statement of what the reader can do
   or defend after. Backward-design in miniature: the proof shapes the piece.
3. **Ground.** Verify every API name, number, and ordering claim that will appear
   — `../references/research-grounding.md` (use its degradation ladder when kit
   tooling is absent). Freeze verified facts before writing. **Pin the version and
   date the number** — the one convention no form skips.
4. **Brief.** Fill the content brief (`../lesson-brief-schema.md` §F) + the form's
   extra keys. Tag `dominant_job` — it routes the voice whether or not
   `writer-style` is installed.
5. **Write.** Produce the full text per the form's structure recipe. Voice seam:
   `writer-style` installed → hand the brief to `/write-in-voice` and use its
   output; not installed → write directly from the brief in a plain technical
   register (felt hook, named trade-offs, no persona imitation, no filler).
6. **Visual pass + check.** Insert visual placeholders per
   `../references/visual-placeholders.md` at the active density (insert-only),
   then run the form's checklist. Emit to the output location above with the
   brief alongside (`content/<form-plural>/<slug>/brief.yaml` + `<slug>.md`).

## Form → typical `dominant_job`

tutorial → `show-how` · walkthrough → `show-how` (or `derive-why` when the tour's
point is a design decision) · explainer → `show-how` for documented mechanisms,
`derive-why` for intricate/contested design · essay → `derive-why` / `frame` /
`economics` · litepaper → `economics` (tokenomics-led) or `derive-why`
(mechanism-led) · slides → deck-level job, usually `frame` or `motivate` openers
with `show-how` bodies · post → `demystify` / `motivate`. Tag what the piece
actually does, not the default.
