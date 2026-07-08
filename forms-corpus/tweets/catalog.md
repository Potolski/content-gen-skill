# Catalog: Tweet (single high-signal post) — Solana ecosystem

Curated, currently-reachable exemplars of the single technical tweet (and, for contrast,
a few reference *threads* — the long end of the form). Every URL was verified live via the
public Twitter/X oEmbed endpoint (HTTP 200 + author name) in July 2026; dates are decoded
from each tweet's snowflake ID. **No tweet text is reproduced** — each entry is metadata
plus one original characterizing sentence and a structural note, per corpus IP rules.

Ordered roughly by subtype: announcements → founder/explainer → dev & crate drops →
benchmark/audit → commentary → reference threads.

---

### Announcements / "what shipped" (single tweet)

1. **Token Extensions are live** — Solana (@solana) —
   <https://x.com/solana/status/1750158439530307870> — (2024-01) — The canonical product
   announcement blurb: a one-line "it's here" for Token-2022 with a link to the deep dive.
   *Structure:* shipped-noun hook + branded card + one link; no explanation, all reach.

2. **Colosseum hackathon announced** — Solana (@solana) —
   <https://x.com/solana/status/1750581495310553272> — (2024-01) — A timely,
   event-driven announcement whose entire job is a date and a link to sign up.
   *Structure:* announcement hook + media + single CTA link; decays after the event.

3. **Jito-bundle tipping is live** — Jupiter (@JupiterExchange) —
   <https://x.com/JupiterExchange/status/1784234743711859049> — (2024-04) — A "what
   shipped" post announcing MEV-protection tipping via Jito bundles in the swap flow.
   *Structure:* feature-live hook + benefit line + link; in-group Jito/MEV jargon assumed.

### Founder / one-idea explainer (longform single post)

4. **Asynchronous Program Execution (APE)** — toly (@aeyakovenko) —
   <https://x.com/aeyakovenko/status/1804937522998591577> — (2024-06) — The longform
   single post doing an essay's job: one design thesis (decoupling execution) held in a few
   paragraphs. *Structure:* hook → mechanism → implication → open question; one thesis, no
   headings; catalogued elsewhere as a durable reference.

5. **The state-growth problem** — toly (@aeyakovenko) —
   <https://x.com/aeyakovenko/status/1796569211273445619> — (2024-05) — A single-post
   problem framing that names one issue (unbounded state growth) and gestures at solution
   space. *Structure:* problem-hook longform; evergreen; quoted for months as a primer.

### Benchmark / data drop (single tweet)

6. **20x average-vs-median fee gap** — toly (@aeyakovenko) —
   <https://x.com/aeyakovenko/status/1891323175981482087> — (2025-02) — The minimal
   benchmark drop: one surprising ratio about fee distribution, almost no prose.
   *Structure:* number-as-hook + one line of context; designed to be screenshotted.

7. **Febo on p-token capacity** — Solana Developers (@solana_devs) —
   <https://x.com/solana_devs/status/2055047784726679645> — (2026-05) — A pull-quote
   promo tweet amplifying a core dev's line on p-token freeing network capacity, linking
   the Anza deep dive. *Structure:* quote-hook + attribution + one 👇 link; org-account
   amplification pattern.

### Dev tip / crate drop (single tweet)

8. **pinocchio-log crate drop** — febo (@0x_febo) —
   <https://x.com/0x_febo/status/1855598291783688236> — (2024-11) — A textbook crate-drop:
   crate name + one-line purpose, a `[tl;dr]` feature list (zero-deps, no_std, SDK-agnostic,
   `log!` macro), and a repo link. *Structure:* noun-hook + tl;dr bullets + one link; the
   cleanest single-tweet announcement skeleton in the set.

### Security / audit (reference thread — long end)

9. **P-Token audit findings** — Neodyme (@Neodyme) —
   <https://x.com/Neodyme/status/1958234163376717904> — (2025-08) — A security-firm thread
   translating a completed audit of the Pinocchio-based token program into "what the CU
   savings mean in practice". *Structure:* investigation hook ("we looked into 👇") →
   multi-tweet findings; a thread because it has several moves — the contrast case to #6/#8.

### Commentary / hot-take (single tweet)

10. **Ecosystem hot-take** — mert | helius.dev (@0xMert_) —
    <https://x.com/0xMert_/status/1944063902687350910> — (2025-07) — A high-reach opinion
    post about how teams operate in the ecosystem; illustrates the commentary subtype —
    valid single-tweet form, low teaching value. *Structure:* one-line take, no asset, no
    link; reach over instruction.

### Reference threads (the long end, for contrast)

11. **Local fee markets, explained** — 7Layer (@7LayerMagik) —
    <https://x.com/7LayerMagik/status/1615569374647287808> — (2023-01) — A concept
    explainer that needs a thread: block-space → fee-market mechanism → why it matters.
    *Structure:* multi-tweet build; each unit self-contained; the archetype of "this idea
    doesn't fit one tweet."

12. **fd_quic technical milestone** — Firedancer (@jump_firedancer) —
    <https://x.com/jump_firedancer/status/1654124396062158850> — (2023-05) — An engineering
    milestone thread on a high-performance QUIC/ingest implementation. *Structure:*
    announcement hook + multi-tweet technical detail; a milestone big enough to warrant a
    thread rather than a blurb.

---

**Coverage note.** Entries 1–8 and 10 are single tweets/posts (the form's core); 9, 11,
and 12 are threads included to sharpen the single-vs-thread boundary analyzed in `FORM.md`.
Subtypes represented: announcement (1,2,3), longform explainer (4,5), benchmark/data drop
(6,7), crate drop / dev tip (8), commentary (10), plus security/concept/milestone threads
(9,11,12). Authors span official (Solana, Solana Developers), infra/founders (toly, Anza
core dev via febo & solana_devs), tooling (febo), security (Neodyme), RPC/education
(0xMert_ / Helius), validators (7Layer), and clients (Firedancer).
