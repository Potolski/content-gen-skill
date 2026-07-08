# Visual placeholders — the final pass over generated text

`writer-style` is text-only, and this skill never generates images. Instead, the last
step of every writing pipeline inserts **placeholder blocks**: fenced, greppable specs
that carry everything a downstream visual tool (Claude Design, a diagramming agent, a
human designer) needs to produce the graphic later. The text must read complete even
if no visual is ever generated.

## The block format

A fenced code block with the `visual` info string. It renders as visible code in any
markdown viewer, survives copy-paste, and is machine-findable via the fence.

````markdown
```visual
type: flowchart
title: How a transaction reaches a validator
purpose: show the 5 hops and where a tx can be dropped
data: |
  wallet -> RPC node -> leader (QUIC) -> banking stage -> confirmed block
  drop points: RPC rate limit; leader queue full; blockhash expired
prompt: |
  Horizontal left-to-right flowchart, 5 nodes as labeled above, one arrow per hop.
  Mark the three drop points as red annotations on their arrows. Dark background,
  monospace labels, no decorative icons.
alt: A transaction hops wallet -> RPC -> leader -> banking stage -> block, and can drop at the RPC, the leader queue, or on blockhash expiry.
```
````

Field contract (all six required — a block that fails to parse does not count
toward any floor, and a closing fence must sit on its own line; the insert-only
pass must never split a sentence):
- `type` — `flowchart | diagram | chart | table | comparison | annotated-code | timeline`
- `title` — what it shows, outcome-led.
- `purpose` — one line: what the reader should take from it.
- `data` — the actual content the visual encodes (nodes/edges, series, rows). Text
  only, complete: the generator must not need the surrounding article.
- `prompt` — a self-contained generation prompt for the visual tool: layout, labels,
  emphasis, style. Write it so it works with zero additional context.
- `alt` — one sentence that stands in for the visual in text-only renders.

## The density setting (tweakable — never overdo it)

`visuals: none | light | rich` — set at intake (user flag or brief field), with
per-form defaults:

| Setting | Budget | Use |
|---|---|---|
| `none` | zero blocks | tweets, TL;DRs, blurbs; user opted out |
| `light` (default) | ≤1 per major section, ≤1 per ~600 words · threads instead budget a cover card + ~1 image per 2–3 units | tutorials, walkthroughs, explainers, essays, course lessons, threads |
| `rich` | up to 1 per section + 1 anchor visual near the top; **course lessons: scaled floor `max(2, ceil(prose_words / 600))`, validated by `validate_course.py drafts`** | slide decks, course lessons, visual-heavy explainers |

## Insertion recipe (what the pass does)

1. Run AFTER the prose is final (after writer-style voice/facts validation, when in
   use). The pass is **insert-only**: it never rewrites, reorders, or deletes a
   sentence — so a re-run of the facts diff still passes.
2. Scan for the four earn-a-visual signals: a process of ≥4 steps; a ≥3-way
   comparison; an architecture/dataflow with ≥3 components; a numeric trend or
   before/after. Nothing else earns one at `light`.
3. Insert the block directly after the paragraph that motivates it — mid-text, where
   the reader needs it, never appendixed at the end.
4. Respect the budget for the active density; when candidates exceed it, keep the
   ones closest to the piece's core objective. Never place two blocks adjacent.
5. Simple tabular facts stay as plain markdown tables in the text — the `table` type
   is reserved for designed data tables (decks, styled comparisons).
6. Fill `data` and `prompt` from the surrounding text and the brief's grounded facts;
   never invent numbers for a chart that the research pass didn't freeze.

Extraction for downstream tooling: `grep -n '^```visual' piece.md` finds every block.
