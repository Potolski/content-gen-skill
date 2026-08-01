---
description: "Create a finished piece of educational Solana content — tutorial, walkthrough, explainer, essay, litepaper, slides, tweet/thread/post (form auto-routed)"
argument-hint: "<topic/ask> [--form tutorial|walkthrough|explainer|essay|litepaper|slides|post|course] [--visuals none|light|rich] [--brief-only]"
---

The content ask is: $ARGUMENTS

Produce it with the **content-gen** skill (`skills/content-gen/SKILL.md`). Spawn the
**content-composer** agent (or run the procedure yourself):

1. **Route the form** (`skills/content-gen/forms/FORMS.md`): an explicit `--form`
   or in-ask name wins; infer otherwise; on ambiguity use the smallest
   fully-written form. `course` hands off to `/architect-course`.
2. **Run the shared pipeline** from the routed `forms/<form>.md`: single
   Bloom-tagged outcome → ground every claim
   (`references/research-grounding.md`, degradation ladder if the kit is absent) →
   content brief (`lesson-brief-schema.md` §F, tag `dominant_job`) → write the
   full text through the voice seam (SKILL.md §Scope & deliverable) → visual
   placeholder pass (`references/visual-placeholders.md`) at `--visuals` density
   (form default if unset).
3. **Check + emit**: run the form file's checklist; save to `content/<slug>/`
   (`brief.yaml` + `<slug>.md`); a `post` returns inline. `--brief-only` stops
   after the brief.

Deliver finished text with placeholder visual specs — never images, and never more
visuals than the density budget allows.
