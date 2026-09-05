# Strategy memo — "Solana Hackathon Expert: Build a Winning Project"

Status: **DRAFT v0.1 for the session-1 working session with David** (2026-09-05). Every proposal below
is a concrete default on the table, not a decision. Decisions land in the decision-log section at the
bottom and then flow into the charter/outline per `course-methodology.md`.

Owner questions this memo answers (from `hackathon-course-prompt.md` §mandate): (1) what "winning"
means per surface and which the course optimizes for; (2) journey-shaped vs skill-shaped; (3) how
central the agent tooling is; (4) assessment model + language; (5) what David uniquely knows.

---

## 0. What the surfaces look like today (live snapshot, 2026-09-05)

Walked live on 2026-09-05. These are **write-time probes**: Board A re-verifies every one before ship,
and the course writes them season-swappable ("as of the 2026 World's Fair season"), never "currently".

### Colosseum (global) — a venture competition, explicitly

- Current season: **Crypto World's Fair, hackathon Sep 14 to Oct 12 2026**, registration open, ~690
  builders in the arena at snapshot time. Colosseum runs global hackathons **twice a year** plus
  **Eternal**, an on-demand four-week startup sprint. (colosseum.com/hackathon)
- Multi-chain now ("open to builders across all blockchain ecosystems", with per-ecosystem prize
  tracks). Solana is a track, not the whole field. This changes the "why Solana" lesson: it is a
  judged claim, not the default.
- **Stated judging factors** (verbatim categories): Founder + Market Fit · Insight · Product +
  Execution · Potential Market Size · Founder Communication · Business Model · Traction. Then
  multiple internal evaluation rounds → shortlist → judge panel → **15-minute Zoom interview** for a
  smaller group → winners ~1 month after the deadline.
- **Submission portal asks for**: product name + description; chains/tools used; team backgrounds;
  team location; logo; GitHub repo (private allowed if hackathon@colosseum.com gets access); a
  **2–3 minute presentation video** ("one of the first resources judges review"); a **≤3 minute
  product-demo video**; **GTM strategy, demand validation, distribution plan**.
- Rules that disqualify: one submission per team and per person; new startups only (no prior raise
  / must disclose development history; misrepresentation = disqualification); team leader must
  complete the submission before the deadline.
- Prize that matters: select winners enter the **Accelerator with $250,000** from Colosseum's fund;
  74 portfolio startups so far. Unruggable's arc (honorable mention → honorable mention → track win →
  grand prize over 4 seasons) is a ready-made "winning is iterative" story, on their own site.
- Colosseum ships **Colosseum Copilot** itself (colosseum.com/copilot) for research across previous
  submissions. The kit's `ext/colosseum` skill wraps it.

### Superteam Earn (national / regional)

- earn.superteam.fun is **bounties / projects / grants** with sponsor listings, 213k+ users. There
  is no dedicated `/hackathon` route at snapshot time (404). National hackathon tracks appear as
  listings; **payouts for the seasonal hackathon are also made through Earn** (Passo Fundo page says
  so explicitly). So Earn is (a) where national tracks get submitted and (b) the payment rail for
  everything else, and (c) the post-hackathon income surface. Phase-2 research must confirm the
  listing/submission flow with Kaue (Superteam Brazil runs it).

### Seasonal / local — Solana × Cursor, Passo Fundo 2026 (the swappable worked example)

- Aug 31 to Sep 12 2026, two phases: **Phase 1 online** (minicourses, 1:1 mentoring, team formation,
  Aug 31–Sep 5) → **submission by Sep 9, 12:00** (leader sends **deck + video + repo** on the
  platform) → selection Sep 10 → **Phase 2 in person**, Pitch Day at UPF Parque Sep 12: **5-minute
  pitch, no questions**, same-day deliberation.
- Teams of 2–4, 18+, one team per person, at least one member physically present at the final.
- **Rubric, 0–10 per criterion, mean ranks**: Execução técnica · Inovação · Impacto · Apresentação.
  Tie-break: technical execution.
- Prizes: US$ 3,000 total (1,500 / 900 / 450 / 150 honorable mention) + Apollo incubator mentoring
  and a possible incubation invite. Kauê is on the schedule (Sep 3, "Desenvolvimento em Solana").
- Framing on the page: "Não precisa ser expert", regional-market / agro challenges. The audience for
  seasonal is wider and less technical than Colosseum's.

### What the three rubrics have in common (this is the course's spine)

Every surface scores the same four things under different names: **the problem is real (impact /
insight / market)** · **the thing works (execution / product)** · **the story lands (presentation /
founder communication / video)** · **this team can carry it (founder-market fit / team)**. Colosseum
adds two that the others do not: **business model** and **traction**. A project built to clear
Colosseum's bar clears the other two; the reverse is not true. That asymmetry is proposal 1.

---

## 1. "Winning" per surface, and what the course optimizes for

**Proposal: optimize for the Colosseum bar; ship one package with two "adapters".**

- The learner builds ONE submission package to Colosseum's spec (the superset). Two short adapter
  lessons translate it: to a **seasonal** submission (deck + video + repo, 5-minute no-questions
  pitch, in-person logistics) and to an **Earn** listing/track (bounty-style, fast cycle, regional
  judges, payout mechanics).
- "Winning" is defined per surface in lesson 2 as a literal reading of each rubric, and the course
  teaches the learner to **re-derive it each season from the live page** (the fact-discipline rule
  becomes a learner skill).
- Default stays the owner's: one course, three surfaces, seasonal module optional. Restructure only
  if David wants to narrow (e.g. Colosseum + seasonal, Earn as a lesson rather than an adapter).

Open for David: is Earn a real *hackathon* surface in Brazil right now, or mostly the payout and
post-hackathon rail? His answer decides whether Earn gets an adapter lesson or one section.

## 2. Journey-shaped vs skill-shaped

**Proposal: journey-shaped modules, skill-shaped lessons.**

- The module map mirrors the month (before the clock → week 1 → weeks 2–3 → week 4 → submit → after),
  because that is the real artifact ladder: each week's output is the next week's input, and the
  learner is most likely taking this course *during* a season.
- Each **lesson** is a self-contained skill with its own reusable artifact (an idea memo, an evidence
  pack, a scope card, a deck), so the course is still useful off-season and re-enterable mid-season
  ("I'm in week 3, I need the deck lesson").
- Rejected alternatives: pure journey (dies between seasons, punishes late entrants); pure discipline
  (research / build / pitch) loses the ladder, and the 1-month arc is the course's best hook.

## 3. How central is the agent tooling

**Proposal: tooling is the spine of the *build*, not the subject of the course.**

- Promise stays "leave with a submission-ready package for a real season", not "learn to hackathon
  with agents". Every build lesson runs through the kit (idea sprint, Colosseum research, scaffold,
  pitch deck, video), one setup lesson installs it, and the course states plainly that an agent
  team is how a 2–4 person team ships a demoable slice in two weeks in 2026.
- Why not the differentiator: **the dossier's tooling inventory is over-stated.** Verified on
  2026-09-05 in `solanabr/solana-ai-kit`: `plugin/skills/` ships **`hackathon`, `idea-sprint`,
  `pitch-deck`** (as submodules) plus `ext/colosseum` (Copilot wrapper) and the general ext skills
  (helius, solana-dev, sendai, metaplex, …). `find-next-crypto-idea`, `validate-idea`,
  `competitive-landscape`, `marketing-video`, `roast-my-product`, `product-review`, `cso`,
  `submit-to-hackathon` do **not** exist under those names at snapshot time. Phase-2 research must
  map each course step to a skill that actually exists (or to a plain Claude Code workflow) before
  any brief promises one. A course whose identity is "the 20 kit skills" rots with the kit.
- What the course *can* own: the **method** (the same four-criteria spine, the demoable-slice
  doctrine, the evidence pack), with tooling as the accelerant. Kit names are version-pinned facts
  with a freshness note, like an Anchor version.

## 4. Assessment model + language

**Proposal (assessment): quiz-led, artifact-gated, 3–4 honest TypeScript challenges.**

- Every lesson: scenario quiz (Academy grades it) + the lesson's artifact as the "do" element.
- TS challenges only where a pure function is the real skill, so grading is honest and deterministic:
  1. `validateSubmission(payload)` — checks a Colosseum-shaped payload for the required fields and
     the video-length / repo-access rules (submission module).
  2. `deadlineInLocal(deadlineUtcIso, tz)` — the timezone math that disqualifies real teams.
  3. `happyPathFits(steps[])` — the ≤7-step scope check (David's MVP worksheet, stance 15).
  4. `scoreAgainstRubric(rubric, scores)` — mean-of-criteria ranking with the Passo Fundo tie-break.
- `openEnded` reflections in the strategy lessons (ungraded by design). No Rust anywhere.
- Capstone = the submission-ready package; the credential moment is the learner's own package
  passing `validateSubmission` plus the deck/video artifacts checked in.

**Proposal (language): EN source, PT-BR overlay.** The repo now ships multi-language courses via
l10n overlays (`academy-courses` PR #51, merged; #53 used it for visão-geral). Author in English
(David's voice pack is calibrated on English), then overlay PT-BR for the seasonal module first and
the whole course when it earns it. Decide with Kaue before the outline locks.

## 5. What David uniquely knows (capture list for session 1)

These are sourced facts (attributed to David by name in the digest) AND the human-seam material for
every lesson. Prompts, not a form:

- Hackathons you competed in or judged: which surface, which season, outcome. One line each.
- The one thing that separated the winners you have seen from the rest. Then the second thing.
- A project that lost that should have won, and why it lost (judging optics, scope, video, timezone?).
- A project that won that surprised you.
- Your own worst hackathon mistake, and when in the month it happened.
- The demo video you remember. What it did in the first 20 seconds.
- Team formation: what a 2–4 person hackathon team needs on day 0, and the role nobody fills.
- Ideation: where good hackathon ideas actually came from in the teams you watched.
- Validation in one week: what you accept as evidence, what you dismiss.
- The seasonal → global path: have you seen a local win compound into Colosseum?
- Anything from your PM/estimation writing that maps onto a hackathon month (estimates as predictions,
  the 4–6 week MVP slice, the ≤7-step happy path, name the non-goals) — these are already in the voice
  pack's substance bank and can be cited as your positions.

## 6. Proposed shape (hypothesis for the outline; David reshapes)

Scale: **6 modules, 14 lessons + 1 optional module of 2** — btc-to-sol's neighborhood (7/15).

| Module (journey) | Lessons (skills) | Artifact rung |
|---|---|---|
| M1 Before the clock starts | 1 Opener: query the record (runs a Colosseum-corpus query in the first 150 words) · 2 Read the rubric: pick your surface, define winning · 3 The team on day 0 | surface brief + team card |
| M2 Week 1: idea to evidence | 4 Ideation with structure (problem-first vs capability-first, gap vs past winners) · 5 Market research at hackathon speed (on-chain / DeFi data as evidence, not vibes) · 6 The validation sprint and the kill/pivot call | idea memo → evidence pack |
| M3 Weeks 2–3: the demoable slice | 7 Product strategy: scope to what a judge can evaluate in 3 minutes · 8 Build sprint with an agent team (setup, scaffold, devnet) · 9 Capture the narrative while you build; roast + security pass | scope card → devnet demo slice + narrative log |
| M4 Week 4: the story | 10 GTM: distribution hypothesis, why-Solana / why-now as a judged claim · 11 The hackathon deck (vs the investor deck) · 12 The two videos: presentation and demo | GTM one-pager → deck → videos |
| M5 Submit, then keep going | 13 Submission mechanics per surface: Colosseum portal, Earn listing, seasonal platform; deadline math; disqualifiers · 14 After the deadline: interview, accelerator, grants, Earn, next season (conclusion) | submission package (capstone) |
| M6 (optional) The seasonal hackathon | 15 Reading this season's page (Passo Fundo 2026 as the worked example) · 16 Sponsor tracks and how a local win compounds into the global season | seasonal adapter |

Cadence: difficulty plateaus in M2 and M4 (research and writing skills), spikes in M3 (build) and
lesson 13 (mechanics). Retrieval checkpoint after M2 (re-derive the rubric for an unseen season page)
and before capstone (assemble the package from the rungs).

## 7. Timing

The World's Fair season closes **Oct 12 2026**. The pipeline will not ship a reviewed course by Sep 14,
so v1 targets the **next global season (~H1 2027)** and uses the World's Fair as a dated worked example
alongside Passo Fundo. If Kaue wants a partial drop during the season, the M4/M5 lessons (deck, video,
submission mechanics) are the ones a team mid-hackathon would pay for; flag as a scope decision.

## 8. Risks

- **Stale mechanics** (the brief's hazard): every §0 fact is a write-time probe; the course teaches
  "read the live page" as the skill.
- **Tooling drift**: kit skill names are pinned with a freshness note; no lesson promises a skill that
  phase-2 research did not find.
- **Voice extrapolation**: David's pack is calibrated on ~3.9k words of 2020 Medium prose with zero
  code blocks; `helius` carries the evidence layer at ~15%. A competition course can run warmer at the
  edges, but bodies stay calm. Validate with a blind A/B on lesson 1 before the parallel write.
- **Numbers**: prize amounts, builder counts, past-winner counts are exactly the confidently-precise
  claims the fact layer exists for. Source every one, date every one.

---

## Decision log (fills in during session 1)

| # | Decision | Chosen | Why | Date |
|---|---|---|---|---|
| D1 | Surface the course optimizes for | **Colosseum bar + two adapter lessons (seasonal, Earn)** | A package that clears Colosseum's superset rubric clears the other two; the reverse is false. | 2026-09-05 (David) |
| D2 | Journey vs skill shape | **Journey-shaped modules, skill-shaped lessons** | The month is the ladder and the hook; skill lessons keep it usable off-season and re-enterable mid-season. | 2026-09-05 (David) |
| D3 | Agent tooling centrality | **Spine of the build, not the subject** | Promise stays "submission-ready package"; kit inventory is smaller than the dossier claims, so names are pinned facts with freshness notes, never the identity. | 2026-09-05 (David) |
| D4 | Assessment model | **Quiz + artifact gates only; no coding challenges** | Process/strategy course; a TS challenge would grade a proxy, not the skill. `openEnded` reflections in strategy lessons; the capstone is the assembled package. §4's four TS challenge ideas are parked in the expansion memo. | 2026-09-05 (David) |
| D5 | Course language | **EN source + PT-BR l10n overlay** (confirm with Kaue) | Voice pack is calibrated on English; repo supports overlays (academy-courses #51). Seasonal module gets the overlay first. | 2026-09-05 (David); Kaue to confirm |
| D6 | Scale (modules / lessons) | _pending_ — proposal: 5 core modules / 14 lessons + optional M6 of 2 | btc-to-sol's neighborhood (7/15) per the brief. | |
| D7 | Seasonal module optional vs core | _pending_ — default: optional (owner's default, kept under D1) | | |
