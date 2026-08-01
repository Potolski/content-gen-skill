# Catalog: Thread (multi-tweet explainer) — Solana exemplars

Real, currently-reachable exemplars of the technical X thread as practiced in the Solana
ecosystem. Verified reachable as of July 2026. Each entry is **metadata + one original
characterizing sentence + a structural note** — no thread body text is reproduced (IP
rules: verbatim only from open-licensed exemplars saved under `exemplars/`, of which there
are none).

Two entries link the **threadreaderapp** unroll because it is a durable, public mirror of
the original X thread; the underlying X URL is given alongside.

| # | Title / Topic | Author / Org | URL | Year | Why it exemplifies the form + structural note |
|---|---|---|---|---|---|
| 1 | What are @solana's innovations? (8 innovations Q&A) | Solana (official) | https://x.com/solana/status/1171167053681528833 | 2019 | The archetypal "protocol in N points" thread from the official account — opens with a Q&A hook, then one numbered innovation per post (PoH, Tower BFT, Turbine, Gulf Stream…), pure sequence, minimal media. |
| 2 | Local Fee Markets on Solana | 7Layer / Overclock Validator | https://x.com/7LayerMagik/status/1615569374647287808 | 2023 | The gold-standard problem-hook explainer: opens by asking what local fee markets are and why they exist, then builds blockspace structure idea-by-idea to the payoff — evergreen, still re-surfaced. |
| 3 | Priority Fees & Local Fee Markets | Solana (official) | https://x.com/solana/status/1615571640372580352 | 2023 | Textbook "trailer for the blog" thread — a short hook on adoption, a few explanatory units, then a defer-to-long-form "read more 👇" close funneling to the fee-markets writeup. |
| 4 | Firedancer's fd_quic Technical Milestone | Firedancer (Jump) | https://x.com/jump_firedancer/status/1654124396062158850 | 2023 | Benchmark-driven announcement thread: hook on a networking milestone, body units of design rationale, and a hard-number evidence unit (single-core and multi-core throughput) that carries the whole thread. |
| 5 | ELI5 Solana Fees | Anatoly Yakovenko | https://x.com/aeyakovenko/status/1537270721570824192 | 2022 | Founder ELI5 register at its clearest — an explicit "ELI5" hook, then plain-language units walking down the ladder on base vs priority fees; shows register can be lowered without dumbing the substance. |
| 6 | What is the State Growth Problem on Solana? | Anatoly Yakovenko | https://x.com/aeyakovenko/status/1796569211273445619 | 2024 | The long-post ("X article") fork of the form — one dense mini-essay card rather than a numbered chain; seed corpus even labels it "X article," useful as the boundary case vs a classic thread. |
| 7 | Asynchronous Program Execution (APE) | Anatoly Yakovenko | https://x.com/aeyakovenko/status/1804937522998591577 | 2024 | Design-proposal thread that doubles as the social companion to a full blog writeup — floats a protocol change in-thread and lets the long-form Helius piece carry the depth. |
| 8 | Multiple Concurrent Leaders (MCL) | Anatoly Yakovenko | https://x.com/aeyakovenko/status/1810222589991583922 | 2024 | Roadmap/design thread aimed at a technical audience — assumes the reader knows scheduler and MEV vocabulary, sequences the design tradeoffs, no hand-holding; part of Anatoly's multi-year design arc. |
| 9 | Anchor account / discriminator dev tip | Armani Ferrante | https://twitter.com/armaniferrante/status/1459593818777423872 | 2021 | The dev-tip variant from a framework author — a focused thread that teaches one Anchor mechanic using **code screenshots** (not pasted text), the canonical example of how code is presented in threads. |
| 10 | Solana smart-contract security resources (42 posts) | 0xsanny (Sanny Kim) | https://threadreaderapp.com/thread/1508868586890223626.html  (orig: https://x.com/0xsanny/status/1508868586890223626) | 2022 | The mega-thread / resource-list variant — 42 units cataloging tutorials, pitfalls, and real exploit case studies; shows the long-list sub-genre and why an unrolled mirror matters for durability. |
| 11 | Start building on Solana as a Web2 dev (9 posts) | Solana (official) | https://threadreaderapp.com/thread/1483315577678544897.html  (orig: https://x.com/solana/status/1483315577678544897) | 2022 | The learning-path thread — a tight, numbered 9-unit onboarding sequence from docs → framework, each unit a single resource/step; the "curriculum in a thread" pattern. |

## How this set was chosen

- **Author diversity.** Official Solana account (protocol + onboarding), a founder
  (Anatoly, spanning ELI5 → long-post → design proposal), a validator operator (7Layer),
  a client team (Firedancer/Jump), a framework author (Armani/Anchor), and a security
  researcher (0xsanny) — the six author archetypes that produce Solana threads.
- **Sub-genre coverage.** Protocol-in-N-points (#1), problem-hook explainer (#2),
  trailer-for-blog (#3), benchmark announcement (#4), ELI5 (#5), long-post article (#6),
  design proposal (#7, #8), dev-tip-with-code-screenshots (#9), resource mega-thread
  (#10), learning path (#11).
- **Reachability.** All X URLs resolved in July 2026; the two long/mega threads also link
  a threadreaderapp unroll as a durable public mirror.

## Notes for the corpus owner

- **No `exemplars/` payloads.** X threads are proprietary; none are saved as open-licensed
  verbatim files, so this catalog is metadata-only by design. If open-licensed thread text
  is ever needed, prefer authors who publish under permissive terms or mirror their own
  threads on owned domains.
- **The blog↔thread pairing recurs.** Entries #3 and #7 are threads whose depth lives in a
  companion blog-post — the seed corpus lists many of those blogs under "Article." The
  edu-content skill has neither a `thread`-specific profile nor a `blog-post` form; both
  sides of this common pairing are under-modeled (see `FORM.md` §8).
- **Long-post drift.** #6 is a single ~long card, not a numbered chain. Expect more Solana
  "threads" to take this shape as X long-form adoption grows; the form family is the same
  but the skim contract differs.
