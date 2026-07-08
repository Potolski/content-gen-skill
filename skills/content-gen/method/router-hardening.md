# Method: router-hardening
> A repeatable procedure to stress the router against varied/adversarial briefs, find every misroute and
> SKILL.md↔ROUTING.md disagreement, patch `routing/ROUTING.md`, and re-run until the routing is stable.

The router (`../routing/ROUTING.md`) is only as good as the briefs it has survived. This is the structural
analog of the voice skill's routing-stress drill: deliberately try to break the router, then patch what
breaks. Run it whenever a pattern is added, a backbone changes, or a real course routes wrong.

> The one rule: **a routing decision you can't reproduce from the brief is a router bug, not a judgment
> call.** Every row below must fall out of the §3 decision procedure — if it only works because a human
> "knew," the rule is missing and belongs in ROUTING.md.

---

## The procedure (do this in order)

1. **Assemble ≥15 deliberately varied / adversarial briefs.** Span the axes that stress routing: audience
   (beginner / EVM / web2 / Rust-dev-new-to-chain / non-technical / mixed), outcome verb
   (build / understand / secure / optimize / integrate), length (3-hour → 9-week), and the hard cases
   (under-specified, two-domain, two-audience). The table below is the standing set — extend it, don't
   shrink it.
2. **Route each via `../routing/ROUTING.md` §3** — terminal outcome first, then prior model, then build engine, then
   abstraction depth, then security tier, then lesson template, then the stacking-budget check. Record the
   backbone + lesson template + guests for each.
3. **Flag every defect.** Three kinds: a **misroute** (the §3 output is wrong for the brief), a **boundary
   case** (two backbones are equally defensible — the tiebreaker is missing), and a **disagreement** (the
   `SKILL.md` quick-reference table and `../routing/ROUTING.md` imply different patterns for the same need).
4. **Patch `../routing/ROUTING.md`.** Add the missing decision rule, tiebreaker, or table row. Keep edits additive and
   consistent with the existing table formats; if `SKILL.md`'s quick-reference disagrees, reconcile the
   wording (note: `SKILL.md` is the quick index — `../routing/ROUTING.md` is the authority on *when* to pick a
   pattern).
5. **Re-run until stable.** Re-route the whole set after each patch. Stable = every brief routes the same
   way twice and no new boundary case appears. Then spot-check against the §6 failure modes.

---

## The standing routing table (route these NOW — ≥15 briefs)

Backbones/guests use the vocabulary of `../routing/ROUTING.md` §2 and the `../patterns/*` files. "Template"
is the lesson template (default `overview-lab-challenge`, abbr. **OLC**).

| # | Brief (one line) | Audience | Terminal outcome | Backbone + template + guests | Note |
|---|---|---|---|---|---|
| 1 | "Explain tokenomics + the SOL economy to our BD team" | non-technical | *understand* token/value flows; explain-it-back | **concept-spine** only, no builds; template trimmed to overview + retrieval; guest: map-from-known (from web2 finance) | `dominant_job` skews `economics` (Hayes) / `frame` opener (Balaji); proof = explain-it-back |
| 2 | "Solana for Solidity devs — ship 4 programs" | evm-dev | *build* 4 verified programs | **map-from-known** opener → **challenge-ladder**; OLC; guest: build-it-twice on the accounts artifact; **testing-thread** | accounts is the biggest EVM divergence; inline Footguns, not a tier |
| 3 | "Rust engineer, never touched a chain — become program-fluent" | rust-dev-new-to-chain | *build* core programs | **concept-spine** (account model + runtime) → **challenge-ladder**; OLC; **testing-thread** | skip Rust onboarding; map Rust ownership → account ownership; no completion-loop |
| 4 | "Become a Solana auditor" | solana-dev-leveling-up | *secure / audit* — pass a CTF | brief concept refresh → **build-it-twice** (audit native+Anchor) → **security-epoch** as the spine; OLC; **testing-thread** → Trident | gate on prior fluency; assessed by CTF + Trident; walkthroughs `show-how` + security `voice_notes` |
| 5 | "Make my program fit the CU budget / cut costs" | solana-dev-leveling-up | *optimize* — measured CU/heap reduction | **optimization-loop** backbone; OLC; **testing-thread** (measure against); guest: build-it-twice for the Anchor→Pinocchio cost contrast | late tier; before/after CU numbers are the proof; needs a working program first |
| 6 | "Build a Solana dApp frontend (wallet, RPC, IDL-typed client)" | web2-dev | *integrate* — ship a working dApp UI | **client-integration** backbone; OLC; guest: concept-spine opener; **testing-thread** (client tests) | rides the client sub-ladder; on-chain program given or built in a paired module |
| 7 | "Build a Solana data indexer / analytics backend" | web2-dev (backend) | *build* an indexer that tracks accounts/txs | **concept-spine** (account model, just enough) → **challenge-ladder** of backend rungs; OLC; **testing-thread** | data/infra course; defer deep on-chain authoring; map from DBs/streams |
| 8 | "Just teach Solana" | unspecified | **unspecified** | **DO NOT ROUTE** — push back for an outcome + audience (see ROUTING.md §3 rule (d) under-specified) | a topic is not a course; one missing critical field → ask, don't guess |
| 9 | "9-week multi-track program: core dev track + a security track" | mixed (cohort) | *build* + *secure* (separate tracks) | per-track backbones: **challenge-ladder** (core) and **security-epoch** (security), physically separated; OLC; **testing-thread** across both | the rare 3+-pattern case — allowed only because tracks are separated; otherwise split |
| 10 | "3-hour live workshop: deploy your first program" | absolute-beginner | *build* one deployed program | **completion-loop** → one **overview-lab-challenge** build; no security tier; light **testing-thread** (one given test) | time-boxed: no build-it-twice, no full security tier; one fast win |
| 11 | "Token-2022 deep dive (extensions, transfer hooks)" | solana-dev-leveling-up | *build* with Token-2022 extensions | **challenge-ladder** on the token sub-ladder; OLC; guest: concept-spine for the extension model; **testing-thread** | gate on SPL-token prereq; respect token→extension→transfer-hook order (DAG §3) |
| 12 | "Solana from absolute zero" | absolute-beginner | *understand* + *build* a counter | **concept-spine** (model) → **completion-loop** (first program) → graduate to one OLC build; **testing-thread** (introduced at the counter) | biggest scaffold; Rust just-in-time; no security tier; opener `motivate` |
| 13 | "Build a DeFi AMM (constant-product)" | solana-dev-leveling-up | *build* a working AMM | **challenge-ladder** climbing to the AMM rung; OLC; **testing-thread**; guest: security-epoch late (DeFi is exploit-bait) | AMM rung's "why it prices this way" lesson is `derive-why`/`economics` |
| 14 | "Half security, half DeFi — one course" | solana-dev-leveling-up | mixed: *build* DeFi **and** *secure* it | one course: **challenge-ladder** (DeFi build is the terminal artifact) backbone, **security-epoch** demoted to a late guest tier with a named seam ("harden the AMM you built"); OLC; **testing-thread** | mixed two-domain → ROUTING.md §3 rule (a): pick backbone by terminal outcome, demote the other to a guest tier |
| 15 | "One course for EVM devs **and** absolute beginners" | two audiences | *build* core programs | default **track-split** (one track per prior model: map-from-known for EVM, concept-spine+completion-loop for beginners); if forced single, primary audience + **map-from-known** opener for the secondary | two-audience → ROUTING.md §3 rule (b): track-split, or primary + map-from-known on-ramp |
| 16 | "Migrate our team from web3.js to @solana/kit" | solana-dev-leveling-up | *integrate* — port a client to kit | **map-from-known** opener (old API → new) → **client-integration**; OLC; **testing-thread** (client tests as the port's acceptance gate) | adjacent prior (web3.js) → map-from-known; small targeted course, no security tier |

## What good output looks like
- Every row's backbone falls out of §3 mechanically (outcome verb → engine; prior model → opener; etc.).
- The hard cases (#8, #14, #15) each point at a **named decision rule** in `../routing/ROUTING.md` §3 — not at a
  human's intuition.
- No row needs 3+ patterns *except* #9, and #9 only because its tracks are physically separated
  (`../routing/ROUTING.md` §4).
- `testing-thread` appears on every build/integration course as a thread (not counted against the guest
  budget); `optimization-loop` appears only on the performance outcome (#5).

## Failure modes this drill catches
The §6 failure modes of `../routing/ROUTING.md`, made concrete by the table: **topic-routing** (#13 routed to
challenge-ladder "because DeFi is technical" instead of from the build outcome — same answer, wrong
reason), **beginner cliff** (#12/#10 sent straight to challenge-ladder with no on-ramp), **security too
early** (#4 with security before build fluency), **twice-build bloat** (build-it-twice on every artifact in
#2), **over-stacking** (#14 kept as two co-backbones instead of backbone + demoted guest), and **untagged
handoff** (any row whose lessons ship without a `dominant_job`). If a brief trips one of these, the router —
not the brief — needs the patch.
