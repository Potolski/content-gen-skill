# Form: Slide deck / talk (Solana technical talk deck)

Original pattern analysis for a writer producing a Solana technical talk deck — the kind
given at Breakpoint, Accelerate, Colosseum, Hacker Houses, meetups, and workshops. This
analyzes the *content form*, not the rendering tool. The edu-content skill's `slides`
form emits the **text spec** of such a deck (per-slide bullets + speaker notes + a visual
block); this document catalogs how real decks are built so a writer of that spec matches
practice.

Skill form file analyzed: `skills/edu-content/forms/slides.md`.
Exemplars cited live in `catalog.md` alongside this file. No verbatim third-party text is
reproduced here — every characterization is original.

---

## 1. Definition & scope

A **Solana technical talk deck** is a slide sequence built to be *presented live*, in a
fixed time box, to a room (or a stream) of developers. The deck is the visual spine; the
substance is *spoken*. This is the defining property and the one that separates it from
every reading form.

Two sub-genres dominate the ecosystem, and a writer must pick one up front:

- **Conference talk deck** (15–25 min). Narrative-first, one takeaway, few code slides,
  climaxes on a demo or a benchmark, ends on a CTA. Examples: Dean Little's *Writing
  Optimized Solana Programs* (Accelerate 2025), the Firedancer keynotes (Breakpoint
  2023–25), the Trident fuzzing talk (Breakpoint 2024).
- **Workshop deck** (60–180 min). A *teaching scaffold* wrapped around live coding and a
  paired repo. The deck itself is thin — the audience follows along in a terminal.
  Examples: `Solana-Workshops/solana-101`, the `solana-developers/professional-education`
  course decks, the Neodyme Breakpoint security workshop.

**How it differs from adjacent forms:**

- **vs tutorial** — a tutorial is self-paced, reader-driven, one buildable artifact,
  complete as text. A talk is presenter-driven, time-boxed, and *incomplete without the
  speaker* (the slides are cue cards). Same topic ("build an escrow"), opposite delivery.
- **vs walkthrough** — a walkthrough tours an existing artifact for a reader; a workshop
  deck may tour the same repo but paced by a live instructor with pauses for the room.
- **vs cookbook recipe** — a recipe is a copy-paste snippet with minimal framing; a talk
  is all framing and narrative, with code deliberately elided to the load-bearing lines.
- **vs course** — a course is the whole curriculum; a single conference talk is at most
  one module's worth, self-contained, with no assessment or progression gating.
- **vs essay/blog-post** — an essay argues a thesis to a reader in prose; a talk deck
  *asserts* beats and lets the voice-over argue. The deck's bullets would be a bad essay.

**When a writer should choose it:** you have a live audience and a clock; the deliverable
is spoken not read; you need a single takeaway to *land* through a narrative arc; and
there is a demo, benchmark, or reveal that carries the climax. If the artifact must stand
alone as text for a reader who was never in the room, write a tutorial or walkthrough
instead — or write the deck's *speaker notes* as the real content (which is exactly what
the skill's model forces).

---

## 2. Structural anatomy

The recurring skeleton of a strong Solana talk deck, in order. Required beats are marked
**[req]**; the rest are situational.

1. **Title slide [req]** — talk title, speaker handle, event/date. One line, not a
   paragraph. Often the program ID or repo URL is teased here for a workshop.
2. **Hook [req]** — the *felt problem*, a number, or a war story. Never an agenda.
   Dean Little's optimization talk opens on the cost of wasted compute units; the Trident
   talk opens on Solana's share of total hack losses. The hook earns the next 20 minutes.
3. **Credibility / who-am-I** — one slide, brief. Who you are, why you can speak to this.
   Skipped or merged into the hook in short talks.
4. **Agenda** — *optional and often cut* in a 20-minute talk; useful in a 2-hour workshop
   so the room knows the checkpoints. Good talks bury it or drop it.
5. **Concept beats [req]** — the body. One idea per slide, one slide per narrative
   transition. This is where accounts, PDAs, CPIs, CU, and the mental model get built,
   each on its own slide with a diagram. The arc walks a story: pain → naive fix → real
   fix → proof.
6. **Code slides** — 1–3 max in a talk, more in a workshop. Each shows the *load-bearing*
   lines only (≤15 lines), highlighted, the rest elided. Never a full file on screen.
7. **Live demo / benchmark [req for dev talks]** — the climax. "Switch to the terminal."
   A deployed devnet program, a fuzzer finding a bug, a CU counter dropping. This is why
   people came. A fallback screenshot slide is the professional's insurance against a
   failed demo.
8. **Recap [req]** — the 3–5 beats compressed back to one slide. Mirrors the arc.
9. **CTA / ask [req]** — the closing slide answers the hook: try the repo, run the tool,
   join the hackathon, adopt the pattern. *Not* "Thank you / Questions?".
10. **Resources / contact** — repo URL, docs, handle, program IDs. Because the deck ships
    as a recording, these links are the only durable artifact for a viewer.

**Reusable template (the skill's text-spec form):**

```markdown
# Deck: <talk title>
context: <event, minutes available, room type>
arc: <3–5 beats, e.g. pain → naive fix → real fix → proof → ask>
slides: <N>  (≈ minutes ÷ 1.5)

## Slide 1 — <hook title>
- <≤4 bullets, ≤10 words each — what's ON the slide>
speaker_notes: >
  30–90s of what the presenter SAYS. The substance lives here.
```visual
type: diagram | flowchart | chart | comparison | annotated-code | table
title / purpose / data / prompt / alt   (or: visual: none)
```

## Slide 2 — <concept beat> ...
```

Ground in real exemplars: the `professional-education` decks follow crypto → accounts/tx
→ tokens → Anchor → escrow across a 4-day arc; the Neodyme workshop is exploit-first,
progressive `level0`→`level4`, each level a vulnerability the room must break before the
fix is shown. Both are one-idea-per-slide with the real work happening in a paired repo.

---

## 3. Length, density & format

Real, measurable numbers from the catalog:

- **Conference talk:** 15–25 min ≈ **15–25 slides** at ~1–1.5 min/slide. The skill's
  `slide_budget = minutes ÷ ~1.5` matches this cleanly.
- **Workshop:** 60–180 min but the deck stays **10–20 slides** — live coding, not slides,
  fills the clock. Slide-count does *not* scale linearly with minutes here (see §8).
- **Marketing/roadmap deck** (e.g. the SpeakerDeck "Solana developer roadmap"): as thin as
  **7 slides**, one topic per slide, no code — a different, lower-density register.

**Code-to-prose ratio:** deliberately low *on the slides*. A strong 20-minute dev talk
carries **1–3 code slides**, each the minimal 5–15 lines with the load-bearing line
highlighted and everything else elided to `// ...`. The full code lives in the paired repo
and the live demo, never dumped on a slide. Workshops invert this only in the sense that
the *terminal* (not the deck) shows the full code.

**Visuals:** heavy, and the ecosystem's default. Account-model boxes, transaction-flow
arrows, PDA-derivation diagrams, CPI call graphs, before/after CU bar charts. This is why
the skill defaults `slides` to `visuals: rich` — nearly every concept beat earns a
diagram. Screenshots of Explorer, a fuzzer run, or a benchmark table are common.

**Heading style:** short noun or imperative phrases ("The account model", "Store the
bump", "Now break it"). Not sentences. The sentence is what the speaker says.

---

## 4. Voice, framing & conventions

**Register:** conversational-technical, written for the ear. Slide bullets are terse cues;
the spoken track (the skill's `speaker_notes`) carries the argument in full sentences.
A reader holding only the notes should be able to deliver the talk — that is the test.

**Hook conventions:** felt problem, a striking number, or a war story. The best Solana
talks open on *why you should care in the next 30 seconds*, not on a table of contents.
Optimization talks open on wasted CU; security talks open on funds lost; infra talks open
on a TPS ceiling.

**Introducing Solana concepts:** the audience is assumed Rust-literate but Solana-variable.
So accounts, PDAs, CPIs, and CU each get a one-line analogy plus a diagram on first use,
and are *named on the slide, explained in the notes*. A talk never assumes the room knows
what a PDA bump is; it never re-derives it from scratch either. CU is framed as the budget
metaphor; PDAs as program-owned addresses with no private key; CPIs as one program calling
another. Consistency of these framings across the deck is a quality signal.

**Code presentation norms:** elide aggressively, highlight the one line that matters,
monospace with syntax color, and *say the rest* rather than show it. A full `lib.rs` on a
slide is an anti-pattern — the room can't read 40 lines in 8 seconds.

**Citation / link norms:** because the deck ships as a *recording*, links can't be clicked.
Convention is a final resources slide (repo, docs, handle, program IDs) plus the same links
in the video description. Workshop decks put the repo URL on the title slide so the room can
clone before you start.

An illustrative *original* micro-example of the cue-vs-substance split (not a quote):
slide bullet reads `Store the canonical bump`; the speaker-notes track explains *why* —
recomputing `find_program_address` every call burns ~1,500 CU, so you persist
`ctx.bumps.vault` once and reuse it. The slide is the pointer; the notes are the payload.

---

## 5. Cadence & distribution

**Where it's published — and the key reality:** the talk deck rarely ships as a *deck*.
The durable artifact is the **recorded video** (YouTube, Solana Compass, event channels)
plus, for workshops, a **paired GitHub repo**. Standalone slides appear on SpeakerDeck or
Google Slides only sometimes; a PDF almost never. Solana Compass has become the de-facto
archive, aggregating Breakpoint/Accelerate talks with AI-generated transcripts and
summaries. So a writer's deck lives on primarily as *spoken words over slides*, which is
exactly why the speaker-notes track is the real deliverable.

**Cadence:** event-driven. Breakpoint (annual flagship), Accelerate, Colosseum, and the
seasonal Hacker House circuit set the calendar. Workshop decks are *evergreen and reused*
— `solana-101` was delivered at multiple Hacker Houses (Melbourne, Ho Chi Minh City, 2023)
off the same base deck. Conference keynotes are *timely* — a Firedancer update is stale by
the next Breakpoint; an intro-to-Anchor workshop is refreshed but reused for years.

**Promotion & series:** talks are promoted via X threads, the event schedule/agenda drop,
and the recording release weeks later. A series is built by (a) a recurring event slot
(the Firedancer team's annual keynote), (b) a versioned workshop repo iterated per event,
or (c) an org's education track (Ackee's School of Solana, presented *about* at Breakpoint
and delivered as a full course elsewhere).

---

## 6. Solana-specific conventions

- **Version pinning & staleness.** A dev talk names its Anchor version, its Agave/Solana
  version, and its framework choice (Anchor vs Pinocchio vs native). These decks date fast:
  a 2023 Anchor deck predates Anchor 1.0's breaking changes (`@coral-xyz/anchor` →
  `@anchor-lang/core`, `transfer` → `transfer_checked`, `Pubkey`-not-`AccountInfo` in
  `CpiContext`). A good deck states its toolchain on an early slide so viewers can judge.
- **devnet vs mainnet framing.** Demos run on devnet, localnet, or a Surfpool mainnet-fork;
  any mainnet action is flagged and de-risked. "This is devnet, don't paste your mainnet
  key" is a spoken norm.
- **Program IDs.** Deployed demos show their program ID (title or resources slide) so the
  room can inspect on Explorer.
- **Test-harness mentions.** LiteSVM, Mollusk, Surfpool, and Trident increasingly *are* the
  talk — the Trident fuzzing talk (Breakpoint 2024) is a whole deck about a test harness.
  Naming your harness is a credibility marker; `solana-test-validator` for unit tests reads
  as dated.
- **Security caveats.** Security talks (Neodyme, Trident) are exploit-first: break it live,
  then show the fix. Standard caveats — reinit attacks (`init_if_needed`), missing signer/
  owner checks, unchecked math, PDA-bump recomputation — headline these decks. A demo that
  ships exploitable code without the "don't do this in prod" flag is a red flag.

---

## 7. What good looks like — checklist

- [ ] Slide 1 is a *hook* (felt problem / number / story), never an agenda.
- [ ] One idea per slide; bullets are ≤4, ≤10 words, cues not prose.
- [ ] Speaker notes carry the substance — a reader with notes alone could deliver the talk.
- [ ] Slide count ≈ minutes ÷ 1.5 (talk) or held thin while live coding fills a workshop.
- [ ] A clear 3–5 beat arc (pain → naive fix → real fix → proof → ask) is visible.
- [ ] ≤3 code slides in a talk; each shows only load-bearing lines, one highlighted.
- [ ] A live demo / benchmark is the climax, with a fallback screenshot if it fails.
- [ ] Every number on a slide is grounded; every slide has a visual decision (block or none).
- [ ] Solana concepts (account, PDA, CPI, CU) are named on-slide, defined in notes, framed
      consistently across the deck.
- [ ] Toolchain versions pinned (Anchor/Agave/framework); demos flagged devnet vs mainnet.
- [ ] Closing slide is the *ask* answering the hook — not "Thank you / Questions".
- [ ] A resources slide carries repo, docs, handle, program IDs (the durable artifact).
- [ ] Security/"don't ship this" caveats present where code is exploitable.

---

## 8. Alignment with the edu-content skill

**A skill form exists** (`skills/edu-content/forms/slides.md`), so this is a
confirm-with-gaps comparison, not an add-recommendation.

**Where practice CONFIRMS the skill's model — strongly:**

- **One idea per slide; bullets as cues, not prose.** Universal in good decks. ✔
- **Hook-not-agenda opener; ask-not-"Thank you" closer.** The skill's arc discipline
  (slide 1 = felt problem, final slide = next step) matches the best real talks exactly. ✔
- **Speaker notes carry the substance.** The single most important match. Because Solana
  talks survive as *recordings*, the spoken track *is* the content — the skill's insistence
  that "a reader with notes alone could present it" is the right center of gravity. ✔
- **`visuals: rich` default.** Real decks are diagram-heavy (account boxes, tx flow, CU
  charts); the per-slide visual block is the correct model. ✔
- **`slide_budget` from minutes (~1–1.5 min/slide).** Matches conference-talk density. ✔
- **Every number grounded.** Matches the research-grounding norm for benchmarks/CU claims. ✔

**Where practice DIVERGES or reveals a gap the skill under-covers:**

1. **Workshop vs talk is not a first-class sub-mode.** The skill's `slide_budget =
   minutes ÷ ~1.5` over-produces for a *workshop*, where 90–180 minutes are filled by live
   coding and the deck stays deliberately thin (10–20 slides). The skill's `context` field
   hints at this ("workshop opener" vs "demo day") but the budget math doesn't branch. Gap:
   add a workshop mode where slide budget decouples from minutes and a "paired repo" is a
   required field.
2. **No first-class live-demo beat.** The demo is the *climax* of nearly every Solana dev
   talk, yet the skill's structure recipe has no demo slide convention — no "switch to
   terminal" handoff, no required fallback-screenshot slide for when a devnet demo fails.
   `narrative_arc` includes "proof" but proof-via-live-demo has specific staging needs.
   Recommend: a `demo` beat type with a mandatory fallback visual.
3. **Code-slide budget is implicit.** The skill says bullets are cues but gives no explicit
   guidance that a talk carries ≤3 code slides, each elided to load-bearing lines. Real
   decks are disciplined here; the skill should encode a code-slide budget + elision norm.
4. **Distribution reality is unaddressed.** The skill emits text and stops — fine — but the
   deck's real life is a *video + repo*, which makes the resources slide and the
   speaker-notes track disproportionately important. A one-line note in the form file would
   help writers weight these correctly.
5. **Version-pinning caveat missing from the slides checklist.** It lives in the broader
   research-grounding reference, but Solana decks date so fast that pinning Anchor/Agave
   versions belongs on the `slides` checklist itself.

**Verdict:** the skill's model is *correct at its core* and confirms the hardest-won norms
(notes carry substance, hook/ask discipline, rich visuals). It **diverges** by under-serving
the workshop sub-genre and by not making the live-demo beat and code-slide budget explicit —
additive gaps, not wrong foundations.

---

## 9. Takeaways for a writer

- **Write the speaker notes first, the slides second.** In this ecosystem the deck ships as
  a recording — the spoken track is the deliverable. If your notes read like a script, the
  slides can be sparse and you've done it right.
- **Open on a felt problem, not an agenda.** A number, a hack, a wasted-CU cost. Earn the
  next 20 minutes in the first 20 seconds.
- **Decide talk vs workshop before slide 1.** A 20-min talk is 15–25 narrative slides; a
  2-hour workshop is a thin deck plus a paired repo and a terminal. Don't build a 90-slide
  workshop deck — build 15 slides and a repo people clone from the title slide.
- **Elide code ruthlessly.** ≤3 code slides in a talk, each the 5–15 load-bearing lines with
  one highlighted. The room can't read a full `lib.rs` in eight seconds; say the rest.
- **Make the demo the climax, and insure it.** Stage the "switch to terminal" moment and
  keep a fallback screenshot slide. A failed devnet demo with no backup kills a good talk.
- **Frame accounts/PDAs/CPIs/CU consistently and pin your toolchain.** Name the concept on
  the slide, define it in the notes, and state your Anchor/Agave versions early so the deck
  ages gracefully.
- **End on the ask, then the resources.** The closing slide answers the hook (try this, run
  this, join this); the resources slide (repo, docs, handle, program IDs) is the only thing
  a later viewer can act on.
- **Ground every number.** CU deltas, TPS, benchmark bars — if it's on a slide it's a claim,
  and Solana audiences will check it.
