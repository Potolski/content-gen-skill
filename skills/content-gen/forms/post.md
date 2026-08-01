# Form: post

The social/short form, branched by `platform` — the shared rules dominate, so
tweet and thread are **sub-profiles here, not separate forms**. One takeaway, no
throat-clearing. On X, code and benchmarks are **images or links by necessity**
(no code blocks) — design around it, don't fight it.

## Sub-profiles

| `platform` | Shape | Band | Visuals |
|---|---|---|---|
| `tweet` | one move: a number, a shipped noun, a claim | ≤280 chars (~40–55 words); longform single 150–500 w | `none` |
| `thread` | 2+ moves: setup → mechanism → implication → CTA | 3–20 units, ~400–1200 words total | `light`, thread budget: a cover card on the hook + ~1 image per 2–3 units (media is load-bearing, not decoration) |
| `tldr` / `blurb` | compressed summary / announcement note | 50–300 words | `none` |

**Escalation rule:** count logical *moves*. One move = `tweet`. Two-plus = `thread`.
A thread cramming a whole article into 280-char cards is mis-scoped — write the
`explainer`/`essay` and **launch it with the thread** (the thread is the trailer,
the long form is the movie). Needs headings? It outgrew this form entirely.

## Brief (mini — inline, no file unless the user asks to save)
`form: post` · `platform` (above) · `takeaway` (the ONE thing) · `audience` ·
`dominant_job` (usually `demystify` or `motivate`) · `units` (threads: planned
count, 3–20) · `funnels_to` (threads: the canonical link the LAST unit lands on —
design the funnel, don't bolt it on) · `cta` (optional) · grounded fact(s) if any
number/API is claimed.

## Structure recipe (the output IS)
- **First line earns the read** — spend the *entire* budget there: the felt
  problem or the surprising number. Never "A thread on…", never "I'm excited to
  announce". A `tweet` must survive decontextualization: assume it is
  screenshotted with zero surrounding context and still lands.
- **Body** — the takeaway made concrete: one example, one number, or one
  before/after. A thread spends one move per unit; **each unit stands alone when
  quoted**; code/benchmarks appear as image placeholders (`visual` block,
  `type: annotated-code` or `chart`) or a link, never pasted text.
- **Close** — a `thread` closes on exactly one deferred canonical link
  (`funnels_to`); a `tweet`/`blurb` on the one-line so-what or CTA. No hashtag
  pileups.

## Checklist
- [ ] One takeaway; every sentence serves it; move-count matches the sub-profile.
- [ ] Any number/API named is grounded — short forms are quoted out of context
      and travel farthest, so a wrong number here does the most damage.
- [ ] Thread: each unit quotable standalone; media placeholders where code/data
      would go; last unit is the funnel.
- [ ] Reads like a person: no engagement-bait scaffolds, no emoji bullets unless
      the platform norm genuinely calls for it.
