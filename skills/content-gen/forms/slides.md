# Form: slides

A slide deck as TEXT — a per-slide spec a presenter or a design tool turns into the
actual deck. This skill never renders slides; it writes the complete spec.

**Length band:** 8–25 slides; one idea per slide. **Visuals default:** `rich`
(nearly every slide carries a `visual` block or an explicit `visual: none`).

## Brief extras (beyond §F core)
- `context` — where it's delivered (meetup talk, workshop opener, demo day) and the
  minutes available; both drive slide count.
- `narrative_arc` — the 3–5 beat story the deck walks (e.g. pain → naive fix → real
  fix → proof → ask).
- `slide_budget` — hard max, from minutes (≈1–2 min/slide).

## Structure recipe (the output IS)
A deck header (title, context, arc, total count), then one block per slide:

```markdown
## Slide N — <slide title>
- <at most 4 bullets, ≤10 words each — what's ON the slide>

speaker_notes: >
  What the presenter says — full sentences, 30–90 seconds worth. The substance
  lives here, not on the slide.

```visual
(per ../references/visual-placeholders.md — the slide's graphic, or `visual: none`)
```
```

Arc discipline: slide 1 is the hook (felt problem, never an agenda); one slide per
beat transition; the closing slide is the ask/next step, not "Thank you" — plus a
resources slide (repo, docs, program IDs: the only clickable artifact on a
recording). Write the speaker notes FIRST, the slides second — the deck ships as a
recording, so the spoken track is the deliverable; the bullet is a cue, the note is
the payload.

**The demo beat.** If the talk has a live demo, stage it as the climax and give its
slide a mandatory fallback visual (`type: annotated-code` or screenshot spec of the
expected result) — a failed devnet demo with no backup kills a good talk.

**Sub-mode: `workshop`** — hands-on session with a paired repo: decouple
`slide_budget` from minutes (exercise time dominates), require the repo link on
slide 2, and add per-exercise checkpoint slides ("you should now see…").

## Checklist
- [ ] Slide count ≤ `slide_budget`; one idea per slide; bullets are cues, not prose.
- [ ] Speaker notes carry the substance; a reader with notes alone could present it.
- [ ] Every number on a slide grounded; every slide has a visual decision (block or
      explicit none).
- [ ] The arc closes — final slide answers the hook; demo has a fallback visual.
