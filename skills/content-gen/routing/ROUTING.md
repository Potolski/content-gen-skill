# ROUTING — choosing the structure by course type, audience, and outcome

The router picks the **course backbone** and the **lesson template**, then stacks at most one or two guest
patterns. It routes on **what the course is for and who it's for** — the analog of the voice skill routing
on a piece's "dominant job." The design spine (`../design-spine.md`) is always on and is **not** a pattern
you choose; it applies underneath whatever the router picks.

> The one routing rule: **route on the course's terminal outcome and the learner's prior model — not on
> the topic.** "A Solana course" is not a structure; "ship 5 verified programs / understand the account
> model / pass an audit CTF, for an EVM dev / a beginner / a working Solana dev" is.

---

## 1. Two layers to route: backbone (course) + template (lesson)

- **Lesson template (almost always):** `overview-lab-challenge` is the default. Use `completion-loop`
  instead for beginner/syntax modules (finer grain). Trim to overview + retrieval for pure-concept lessons.
- **Course backbone (the shape):** pick by the table below. The common default is a **`challenge-ladder`
  backbone opened by a `concept-spine` module** (build engine + a mental-model on-ramp) — model first, then
  ship.

## 2. Backbone selection table

| If the course's dominant goal is… | Lead backbone | Typical guest(s) |
|---|---|---|
| Ship real programs / portfolio / "I built N things" | **challenge-ladder** | concept-spine opener; overview-lab-challenge lessons |
| Build the Solana mental model (esp. for newcomers) | **concept-spine** → feeds a build pattern | map-from-known opener; completion-loop early |
| Onboard absolute beginners / new language (Rust) | **completion-loop** → graduating to challenge-ladder | concept-spine for the model |
| Deep "how it really works" / pre-audit | **build-it-twice** | concept-spine; security-epoch tier |
| Performance / compute-unit optimization | **optimization-loop** (measure → optimize → re-measure; before/after CU numbers are the proof) | build-it-twice for the abstraction-cost contrast; testing-thread to measure against |
| Security / audit / "build *secure*" | dev backbone **+ security-epoch as the late tier** | build-it-twice (audit both); challenge-ladder of attacks; testing-thread escalates to fuzzing |
| Transition an EVM/web2 dev fast | **map-from-known** opener → challenge-ladder or concept-spine | build-it-twice for the divergences |
| Build a client / frontend / dApp / mobile app or integrate (wallet, RPC, UI) | **client-integration** | concept-spine opener; challenge-ladder for on-chain parts |
| Non-technical understanding (users/ecosystem) | **concept-spine** (no builds) | map-from-known; analogy-heavy briefs |

**Cross-cutting threads (not backbones, not counted against the guest budget).** Some patterns thread
*through* whatever backbone the table picks rather than competing to lead:
- **`testing-thread`** — on **every developer/integration course**: introduce a test harness at the first
  build and reuse it as the acceptance gate on every rung, escalating to fuzzing in the security tier
  (`../patterns/testing-thread.md`). It is plumbing, so it doesn't spend a guest slot (§4).
- **`optimization-loop`** is *not* a thread — it is a late **tier/backbone** for a performance outcome
  (the row above), and it leans on `testing-thread` to have something to measure against.

## 3. The decision procedure (do this in order)

1. **Write the terminal outcome first** (`design-spine.md` §1). The verb decides a lot: *build/deploy* →
   build engine; *explain/understand* → concept engine; *secure/audit* → add security-epoch.
2. **Identify the prior model** (`../references/solana-syllabus-dag.md` §6). Strong adjacent prior (EVM/web2) → open with
   **map-from-known**. None → open with **concept-spine** (and **completion-loop** for syntax).
3. **Pick the build engine** by how the learner best moves: motivated/independent → **challenge-ladder**;
   needs heavy guidance → **overview-lab-challenge** lessons under a gentle concept-spine; raw beginner →
   **completion-loop** first.
4. **Decide abstraction depth.** "Understand under the hood" / audit → add **build-it-twice** on the 1-2
   most illuminating artifacts. Otherwise Anchor-first, with at most a couple of native detours. For a
   **performance/optimization** outcome, use the **optimization-loop** backbone (measure → optimize →
   re-measure; the security-epoch loop shape applied to compute units), *not* build-it-twice. For a
   **client/dApp** outcome, add **client-integration**.
5. **Add the security tier if the outcome demands it** — always **late**, as **security-epoch**. If
   security is only a nice-to-have, use inline **Footguns** instead (no full tier).
6. **Set the lesson template** (default `overview-lab-challenge`; `completion-loop` for early/syntax) **and
   thread testing.** On any build/integration course, add **testing-thread**: a harness at the first build,
   reused as the acceptance gate on every rung (escalating to fuzzing in the security tier). It's a thread,
   not a guest (§4).
7. **Check the stacking budget** (§4) and the DAG (`../references/solana-syllabus-dag.md`). Then sequence.

### Decision rules for the hard cases (derived from the router-hardening drill)
These resolve the boundary cases the §3 procedure alone leaves ambiguous (see `../method/router-hardening.md`):

- **(a) Mixed two-domain course (e.g. "half security, half DeFi").** Default to a **track-split**. If it
  must be one course, **pick the backbone by the *terminal* outcome** and **demote the other domain to a
  guest tier with a named seam** (e.g. DeFi-build backbone → "harden the AMM you built" as a late
  security-epoch tier). Never run two co-leading backbones in one undivided course (§4).
- **(b) Two-audience course (e.g. "EVM devs AND absolute beginners").** Default to a **track-split — one
  track per prior model** (map-from-known for EVM; concept-spine + completion-loop for beginners). If forced
  into one track, **pick the primary audience** and **open with `map-from-known` for the secondary** so the
  off-model learners get an on-ramp instead of a cliff.
- **(c) Optimization / performance outcome.** Route the **`optimization-loop`** backbone (measure → change
  one thing → re-measure; before/after numbers are the proof). It is **late** — gate it behind a working,
  tested program — and pair it with **testing-thread** (the thing to measure against). Do *not* substitute
  build-it-twice; that teaches the abstraction, it doesn't reduce a measured cost.
- **(d) Under-specified "just teach Solana."** **Don't route a topic.** Push back for an **outcome + an
  audience** (the §3 inputs) before picking any shape — a subject is not a course (§6 topic-routing). Ask
  only for the missing critical field, then route.

## 4. Stacking budget (don't exhaust the menu)

- **Always on (free, not counted):** the **design spine**.
- **Threads (free, not counted):** **testing-thread** on any build/integration course — it threads through
  the backbone as the per-rung acceptance gate, so it does not spend a guest slot. (Don't *also* tag it as a
  guest; it's plumbing.)
- **Backbone: exactly 1.** The course's primary shape.
- **Guests: ≤ 2**, and on *different jobs* (e.g., an opener like map-from-known + a late tier like
  security-epoch). More than this and the course loses a clear shape.
- **Lesson template: 1** (with completion-loop as the early-module exception).
- **Never co-lead two build engines** (challenge-ladder + completion-loop as co-backbones fight on grain —
  sequence them instead: completion-loop early → challenge-ladder later).
- **3+ patterns** only for long, multi-track programs (e.g., a 9-week course with a distinct security
  track) where sections are physically separated — otherwise **split the course**.

## 5. Pattern → `dominant_job` → voice handoff

The router also annotates each lesson with the `dominant_job` the voice skill consumes
(`../lesson-brief-schema.md` §D). Tendencies by pattern (tag per *lesson*, not blindly per
pattern):

| Pattern | Typical lesson `dominant_job` | Voice craft |
|---|---|---|
| concept-spine | `derive-why` (intricate) / `show-how` (documented); opener `motivate` | Vitalik / Helius / spine |
| challenge-ladder | `show-how`; capstone & Ch.0 `motivate`; "why this design" rung `derive-why`/`economics` | Helius / spine / Vitalik / Hayes |
| overview-lab-challenge | overview `derive-why`/`show-how`; lab `show-how` | Vitalik / Helius |
| completion-loop | `show-how` (sparse prose — spend voice at module edges) | Helius |
| build-it-twice | contrast `derive-why`; each build `show-how`; reframe `demystify` | Vitalik / Helius / Hotz |
| security-epoch | `show-how` + `voice_notes: security caution`; "why the check" `derive-why` | Helius / Vitalik (wary of Hotz) |
| map-from-known | divergences `derive-why`; mappings `show-how`; feared-diff `demystify` | Vitalik / Helius / Hotz |
| optimization-loop | loop mechanics `show-how`; "why this is the bottleneck" `derive-why`; cost reframe `demystify` | Helius / Vitalik / Hotz |
| testing-thread | test-writing lessons `show-how` (+security `voice_notes` when a test is an exploit) | Helius |

Two `dominant_job` values cover jobs no single pattern owns: **`frame`** (Balaji — an ecosystem/thesis
*opener-guest*, e.g. a course or module intro that situates Solana in a bigger picture) and **`sustain`**
(Hayes — a long, non-economic, cold-audience lesson at abandonment risk). Both are guest moves, never
backbones; tag the specific lesson and see `../lesson-brief-schema.md` §D for the guest caveats
and the economics-vs-derivation tiebreaker. `client-integration` lessons are usually `show-how` (Helius).

## 6. Failure modes (caught in validation)

- **Topic-routing** — picking a shape from the subject ("it's technical, so challenge-ladder") instead of
  the outcome+audience. Re-route from the terminal outcome.
- **Passive course** — concept-spine with no build engine for a build outcome. Add challenge-ladder.
- **Beginner cliff** — challenge-ladder for absolute beginners with no completion-loop/concept-spine
  on-ramp. Insert the on-ramp.
- **Security too early** — security-epoch before build fluency. Move it to a late tier; use Footguns early.
- **Twice-build bloat** — build-it-twice on every artifact. Restrict to 1-2.
- **Over-stacking** — 3+ patterns crammed into a short course. Cut to backbone + ≤2 guests or split.
- **Untagged handoff** — briefs with no `dominant_job`. The voice router then guesses; always tag.

## 7. Worked routing examples

- **"Solana for Solidity devs, ship 4 programs, self-paced" (EVM dev, build outcome).** Backbone:
  **map-from-known** opener → **challenge-ladder**. Guest: **build-it-twice** on the accounts artifact (the
  biggest EVM divergence). Lessons: overview-lab-challenge. Security: inline Footguns. Tags: divergence
  lessons `derive-why`, build rungs `show-how`.
- **"Intro to Solana for total beginners, understand + build a counter" (beginner, mixed outcome).**
  Backbone: **concept-spine** (model) → **completion-loop** (first program) → graduate to one
  **overview-lab-challenge** build. No security tier. Opener `motivate`, concept lessons `derive-why`.
- **"Become a Solana auditor" (working Solana dev, secure/audit outcome).** Backbone: brief concept refresh
  → **build-it-twice** (audit native+Anchor) → **security-epoch** as the spine, assessed by CTF + Trident
  fuzzing. Skip beginner on-ramps (gate on prior fluency). Tags: walkthroughs `show-how` + security
  `voice_notes`.
- **"What is Solana? for non-technical ecosystem folks" (non-technical, understand outcome).** Backbone:
  **concept-spine** only, analogy-heavy, no builds; proof = explain-it-back. Opener `motivate`, concepts
  `derive-why`/`demystify`.

> After routing, **validate empirically**: run a handful of real course topics through this procedure and
> check for the failure modes in §6 (see `../references/quality-bar.md`).
