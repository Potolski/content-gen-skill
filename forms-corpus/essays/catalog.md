# Catalog — Technical essay exemplars (Solana ecosystem)

Curated, URL-verified July 2026 (all returned HTTP 200 on check). Diverse across
company research blogs, independent shops, personal sites, Substack, and X. Each entry:
**Title** — Author/Org — URL — (year) — one original sentence on why it exemplifies the
form + a structural note. No source body text is reproduced (IP rules); entries are
metadata + my one-line characterization.

Legend for sub-mode: **[T]** thesis/argument-first · **[X]** expository/concept-first ·
**[O]** opinion/manifesto · **[S]** security-argument.

---

1. **Turbine: Block Propagation on Solana** — Ryan Chern, Helius —
   https://www.helius.dev/blog/turbine-block-propagation-on-solana — (2024) — **[X]**
   The canonical expository deep-dive: a mechanism (block fanout) explained from the
   problem down, diagram-led, closing on future-research pathways. *Structure: problem
   hook → Ethereum contrast → primer → tree mechanism with hero diagram → limitations →
   further reading.*

2. **The Truth about Solana Local Fee Markets** — Lostin, Helius —
   https://www.helius.dev/blog/solana-local-fee-markets — (2024) — **[T]**
   A thesis essay that argues the gap between local-fee-market theory and lived reality
   and what must improve. *Structure: promise-vs-reality hook → thesis → evidence
   sections with data → what needs to change (so-what).*

3. **Solana Issuance from First Principles** — Max Resnick, Anza —
   https://www.anza.xyz/blog/solana-issuance-from-first-principles — (2024) — **[T]**
   The purest first-principles argument in the corpus: re-derives issuance from scratch
   and asks whether today's is optimal. *Structure: first-principles reset hook →
   claim → derivation chain with curves → counter-cases → recommendation.*

4. **Consensus on Solana** — Ryan Chern, Helius —
   https://www.helius.dev/blog/consensus-on-solana — (2024) — **[X]**
   Explains PoH's role inside Tower BFT and slots without a contestable thesis — the
   expository sub-mode the skill under-models. *Structure: roadmap → primitives →
   consensus walk with diagrams → conclusion.*

5. **Lifecycle of a Solana Transaction** — Umbra Research —
   https://www.umbraresearch.xyz/writings/lifecycle-of-a-solana-transaction — (2023) —
   **[X]** Academic-register mechanism walk from submission to execution, with an
   Ethereum contrast throughout. *Structure: numbered sections, ingress→execution
   causal order, diagrams + footnotes.*

6. **The Solana eBPF Virtual Machine** — Joe Caulfield, Anza —
   https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine — (2024) — **[X]**
   Authoritative (written by the client team) explainer of the rBPF VM and how
   validators execute programs. *Structure: what/why → VM internals → how validators
   use it → wrap-up.*

7. **Solana Validator 101: Transaction Processing** — Jito Labs —
   https://www.jito.wtf/blog/solana-validator-101-transaction-processing/ — (2024) —
   **[X]** A validator-perspective deep dive on the transaction lifecycle through the
   banking stage. *Structure: staged pipeline walk, diagram-heavy, comparison notes.*

8. **Solana Nodes: A Primer on Solana RPCs, Validators, and RPC Providers** — Mert
   Mumtaz, Helius — https://www.helius.dev/blog/solana-nodes-a-primer-on-solana-rpcs-validators-and-rpc-providers
   — (2023) — **[X]** The "Primer on…" template: defines node types and their roles for
   a builder audience. *Structure: descriptive title → taxonomy sections → practical
   so-what (choosing a provider).*

9. **Solana Banking Stage and Scheduler** — Andrew Fitzgerald (apfitzge) —
   https://apfitzge.github.io/posts/solana-scheduler/ — (2023) — **[X]** A personal-site
   deep dive by a client engineer on historic/current/near-term scheduling design —
   deepest-trust, least-polished archetype. *Structure: chronological design
   evolution, prose-dominant, minimal decoration.*

10. **Solana Issuance / State Growth: "What is the State Growth Problem on Solana"** —
    Anatoly Yakovenko, X — https://x.com/aeyakovenko/status/1796569211273445619 —
    (2024) — **[T]** Thesis-grade argument published natively as X longform: names a
    problem, argues stakes, floats solutions. *Structure: no headers; paragraph beats
    functioning as sections; replies act as appendix/steelman.*

11. **Solana Thesis: The Fastest Horse Rises From the Ashes** — Ryan Watkins, Wilson
    Withiam, Daniel Cheung (Syncracy) — https://www.syncracy.io/writing/solana-thesis —
    (2023) — **[T]** A long investment thesis arguing the "why" of Solana with market
    and technical evidence. *Structure: macro hook → thesis → multi-pillar argument →
    risks (steelman) → outlook.*

12. **Solana Summer** — Packy McCormick, Not Boring —
    https://www.notboring.co/p/solana-summer — (2021) — **[O]** The narrative-opinion
    archetype: story-driven, long, timely, built for shareability rather than protocol
    precision. *Structure: story hook → narrative arc → thesis-as-vibe → optimistic
    close; images/embeds throughout.*

13. **The Helius Manifesto** — Mert Mumtaz, Helius —
    https://www.helius.dev/blog/manifesto — (2024) — **[O]** A manifesto: pure
    position-taking, values-first, no mechanism. Useful contrast to the technical
    modes. *Structure: mission hook → convictions → call to build.*

14. **Solana Smart Contracts: Common Pitfalls and How to Avoid Them** — Neodyme —
    https://neodyme.io/en/blog/solana_common_pitfalls/ — (2022) — **[S]** The security
    essay archetype: organized as pitfall → why it bites → mitigation, code-carrying but
    argument-led. *Structure: enumerated vulnerabilities, each a mini-argument with a
    fix.*

15. **Solana: An Auditor's Introduction** — OtterSec —
    https://osec.io/blog/2022-03-14-solana-security-intro — (2022) — **[S]** Frames the
    runtime and its security boundaries from an auditor's stance — expository with a
    security thesis running through it. *Structure: runtime primer → boundary-by-boundary
    analysis → implications.*

16. **Jump vs. the Speed of Light** — Kevin Bowers, Jump Crypto —
    https://jumpcrypto.com/writing/jump-vs-the-speed-of-light/ — (2022) — **[O]** A
    vision/opinion essay on physical limits motivating Firedancer — thesis-by-provocation.
    *Structure: provocative claim hook → physics framing → engineering ambition.*

17. **ok so what the fuck is the deal with solana anyway** — hana (2501babe) —
    https://2501babe.github.io/posts/solana101.html — (2022) — **[X]** The irreverent
    explainer that still teaches the account/runtime model correctly — proof voice can
    be loose while rigor stays tight. *Structure: informal hook → primitives explained
    conversationally → mental model assembled.*

18. **Solana Fees (Part 1)** — Umbra Research —
    https://www.umbraresearch.xyz/writings/solana-fees-part-1 — (2023) — **[X]** A
    series-opening expository piece on how fees work today, the ladder-building cadence
    pattern. *Structure: scope-setting intro → fee mechanics sections → "to be continued"
    hook into Part 2.*

19. **Primer on Solana's Token Extensions** — Yash Agarwal, Superteam —
    https://blog.superteam.fun/p/primer-on-solanas-token-extensions — (2024) — **[X]**
    A Substack "Primer on…" deep dive into Token-2022 use cases with a light narrative
    thesis about tokenization. *Structure: why-it-matters hook → extension-by-extension
    walk → use-case framing → outlook.*

20. **What is Firedancer? A Deep Dive into Solana 2.0** — 0xIchigo, Helius —
    https://www.helius.dev/blog/what-is-firedancer — (2024) — **[X]** Expository deep
    dive on the second validator client, blending mechanism explanation with a
    why-it-matters frame. *Structure: context hook → what/why → architecture sections →
    implications for the network.*
