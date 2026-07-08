# Walkthrough — Curated Exemplar Catalog (Solana)

Real, currently-reachable exemplars of the **walkthrough** form — guided tours of an
*existing* artifact (repo, program, protocol flow, transaction, or vulnerability class) where
the reader builds nothing. Verified reachable as of **July 2026**. IP note: verbatim text is
only ever drawn from the open-licensed `exemplars/` set (the `solana-foundation/program-examples`
READMEs); every external entry below is metadata + one original characterizing sentence.

Legend: **[V]** = URL fetched/verified this session · **[S]** = sourced from the curated
`_seeds/solana-awesome.md` index (high-confidence, stable URL).

## Standalone article walkthroughs (self-contained, quote the pinned artifact)

| # | Title | Author / Org | URL | Year | Why it exemplifies the form + structural note |
|---|---|---|---|---|---|
| 1 | Lifecycle of a Solana Transaction | Umbra Research (Eugene Chen, buffalu__) | https://www.umbraresearch.xyz/writings/lifecycle-of-a-solana-transaction | 2023 | **[V]** Canonical "how the runtime processes a tx" tour — reader integrates nothing, just learns to reason about ordering/threads; vantage = a tx from wallet approval to confirmation, contrasted against Ethereum. |
| 2 | A Hitchhiker's Guide to Solana Program Security | 0xIchigo, bl0ckpain (Helius) | https://www.helius.dev/blog/a-hitchhikers-guide-to-solana-program-security | 2024 | **[V]** Alphabetical tour of vulnerability classes ("Account Data Matching" → "Type Cosplay"), each with vulnerable code + fix; vantage = the attacker mindset. |
| 3 | Solana Validator 101: Transaction Processing | Jito Labs | https://www.jito.wtf/blog/solana-validator-101-transaction-processing/ | 2024 | **[S]** Deep-dive tour of a transaction's path through the validator's banking stage; vantage = the tx lifecycle inside the leader. |
| 4 | Solana Banking Stage and Scheduler | Andrew Fitzgerald (apfitzge) | https://apfitzge.github.io/posts/solana-scheduler/ | 2024 | **[S]** Long-form tour of the Agave scheduler's historic/current/near-term designs; vantage = how transactions are scheduled onto threads. |
| 5 | The Solana eBPF Virtual Machine | Joe Caulfield (Anza) | https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine | 2024 | **[S]** Guided tour of the rBPF VM and how validators execute program bytecode; vantage = a program from bytes to execution. |
| 6 | Solana Internals (Part 1: Native On-Chain Programs) | Sec3 | https://www.sec3.dev/blog/solana-internals-part-1-what-are-the-native-on-chain-programs-and-why-do-they-matter | 2023 | **[S]** Opening part of a 4-part series touring the native programs baked into the runtime; series = vantage tiling across internals. |
| 7 | Solana: An Auditor's Introduction | OtterSec | https://osec.io/blog/2022-03-14-solana-security-intro | 2022 | **[S]** Tours the runtime's security boundaries and their implications for auditors; vantage = trust boundaries of the SVM. |
| 8 | How to Use Versioned Transactions on Solana | QuickNode Guides | https://www.quicknode.com/guides/solana-development/transactions/how-to-use-versioned-transactions-on-solana | 2024 | **[V]** Anatomy tour of the v0 transaction + Address Lookup Tables and the 1,232-byte limit; borderline tutorial but primarily decodes existing tx structure. |

## Repo / annotated-code walkthroughs (ride next to the code; short + code-adjacent)

| # | Title | Author / Org | URL | Year | Why it exemplifies the form + structural note |
|---|---|---|---|---|---|
| 9 | program-examples (the collection) | Solana Foundation | https://github.com/solana-foundation/program-examples | 2024 | **[V]** The parent repo of this form's exemplar set — MIT-licensed, per-example READMEs each tour one existing program across Anchor/Native/Pinocchio; CI-verified tours. |
| 10 | anchor-escrow-2024 | Dean Little (deanmlittle) | https://github.com/deanmlittle/anchor-escrow-2024 | 2024 | **[V]** Annotated reference escrow — "Let's walk through the architecture" with per-context (Make/Refund/Take) breakdowns; the canonical escrow tour the exemplar escrow README credits. |
| 11 | sealevel-attacks | Coral (coral-xyz) | https://github.com/coral-xyz/sealevel-attacks | 2022 | **[S]** Paired vulnerable/secure example programs touring Solana-specific exploit classes and the Anchor idioms that prevent them; vantage = one exploit per stop. |
| 12 | transaction-deep-dive | AlmostEfficient | https://github.com/AlmostEfficient/transaction-deep-dive | 2023 | **[V]** "Everything you need to know about Solana transactions" — code + Excalidraw diagrams + video touring memo/transfer/legacy-vs-versioned tx structure; diagram-anchored tour. |
| 13 | Solana Security Workshop (levels 0-4) | Neodyme Labs | https://workshop.neodyme.io/ | 2022 | **[V]** Progressive hands-on tour of intentionally vulnerable example programs; reader exploits (doesn't build), each level a waypoint with hint + solution. |
| 14 | mpl-bubblegum (compressed NFTs) | Metaplex Foundation | https://github.com/metaplex-foundation/mpl-bubblegum | 2024 | **[S]** Program + docs touring how Metaplex compressed NFTs and concurrent Merkle trees work; annotated-repo vantage over cNFT mint/transfer/burn. |

## Open-licensed internal anchors (from this form's `exemplars/`, MIT)

| # | Title | Author / Org | Path | Why it exemplifies the form + structural note |
|---|---|---|---|---|
| 15 | Anchor Escrow | Solana Foundation | `exemplars/tokens/escrow/anchor/README.md` | Pure design-decision walkthrough: problem hook (Alice/Bob counterparty risk) → "Changes from original" naming rationale → Credit; every note names a *why*. |
| 16 | Token-swap AMM | Solana Foundation | `exemplars/tokens/token-swap/README.md` | The long (3,561-word) Skeleton-B exemplar: concept → Design → Principals (explicit trade-offs) → instruction-by-instruction tour via **commit-pinned** GitHub permalinks. |
| 17 | Cross Program Invocation (CPI) | Solana Foundation | `exemplars/basics/cross-program-invocation/README.md` | Vantage-first tour: a numbered 4-step dependency sequence motivates CPI before any code; hand-pulls-lever thread traced end-to-end. |
| 18 | World Cup (Pinocchio) | Solana Foundation | `exemplars/games/world-cup/pinocchio/README.md` | Full-project tour via layout table + quick-start + Accounts/Instructions inventory; the "map" done as a table rather than a diagram. |
| 19 | Pyth (oracles) | Solana Foundation | `exemplars/oracles/pyth/README.md` | Protocol-flow tour: what a price feed *is*, its account shape (price/confidence/exponent), with the mainnet SOL/USD feed address quoted verbatim. |

## Notes on selection

- **Diversity:** runtime/tx-lifecycle (1, 3, 4), VM/internals (5, 6), security tours (2, 7, 11,
  13), tx-structure decodes (8, 12), annotated reference repos (9, 10, 14), plus the
  open-licensed anchors (15-19). Sources span Umbra, Helius, Jito, Anza, Sec3, OtterSec,
  QuickNode, Neodyme, Coral, Metaplex, and independent devs.
- **Excluded as adjacent forms:** step-by-step "build from scratch" pieces (RareSkills 60 Days,
  Loris Leiva "dApp from scratch," Blueshift paths) are **tutorials**; Solana Cookbook entries
  are **cookbook-recipes**; "Solana Summer" / theses are **essays/blog-posts**; the Solana
  whitepaper is a **whitepaper** — none are walkthroughs.
- **Rot watch:** entries 1, 3, 4, 5, 8 tour runtime/version-specific behavior and should be read
  against the Agave/protocol version they were written for; the annotated-repo entries (9-16)
  are evergreen to the extent their commits are pinned.
</content>
