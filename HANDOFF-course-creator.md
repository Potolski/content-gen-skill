# Handoff → course-creator-skill (from writer-style evolution R2, 2026-08-21)

Findings from the two course audits that belong to the course pipeline, not this skill. Ordered by
severity × cheapness. Sources: R1 btc-to-sol audit + R2 speedrun audit (working data, this dir).

1. **Em-dash gate hole at the assessment layer** (cheapest high-value fix). dedash.py +
   validate_course.py cover lesson prose only; **97 em-dashes ship** across the two courses in
   quiz text (btc-to-sol lesson.yaml 76, speedrun 21), plus course.yaml descriptions and generated
   covers. Extend coverage to quiz blocks, covers, and yaml descriptions — or drop the hard-zero
   policy (see 2).
2. **dedash.py's unconditional em-dash→comma mapping mints comma splices** and destroys
   parenthetical boundaries (13 reconstructed before→after pairs in the R1 audit; definitional
   sentences hit worst). Replace by syntactic role: sentence-boundary dash → period/semicolon;
   appositive pair → commas/parens; list-introducing dash → colon. A zero-dash corpus now carries
   a *different* uniform fingerprint (comma-appositive chains).
3. **Cover template leaks another course's thesis as fact.** speedrun's 000-cover asserts a
   toolkit repo that doesn't exist, "the previous era's limit" in a 1-module course, and
   "~0 weeks" (degenerate output) — and the file is generated-authoritative ("do not hand-edit").
   Gate "era"/"rung"/ladder language on `modules count > 1` and `artifact_ladder length > 1`;
   assert cover time math against course.yaml (`hours: 0.2` also contradicts the "menos de 10
   minutos" promise).
4. **The fact layer has no automated floor.** Four confidently-precise false claims in one course
   (a 100× prize error, a wrong-chain Goldman attribution, a false revenue superlative, a
   cumulative-vs-circulating stablecoin figure) — all caught only because a fact-check agent
   happened to run. Make the sourced fact-check pass mandatory in the pipeline, not incidental.
5. **Parallel writer fanout leaves per-agent dialect strata** in fields nobody proofreads:
   speedrun's visual `prompt:` fields are English in l3, Portuguese in l2, hybrid in l1;
   "mobile-first" vs "phone-first" within one lesson; one untranslated "Zoom out." in PT prose.
   Add a post-fanout normalization pass over prompt/purpose/alt fields.
6. **Incompletely-applied owner fixes.** The staircase removal (owner, 2026-08-01) landed in
   l3's prompt + prose but not its `purpose:` line (spec now self-contradicts on re-render), and
   the rejected staircase metaphor still runs in l1. When an owner correction lands, sweep the
   corpus for the pattern, not just the file in view.
7. **btc-to-sol audience model contradicts itself in shipped metadata**: course.yaml `who:
   absolute-beginner` ("no coding required") vs the overview "for developers who live in a
   terminal and can read Python". Both render. Cross-check audience fields against overview text.
