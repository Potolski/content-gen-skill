# Catalog — Litepapers / Whitepapers (Solana ecosystem)

Curated real exemplars of the litepaper/whitepaper form, spanning the full spectrum:
formal academic whitepapers → docs-embedded litepapers → spec-as-code (GitHub/SIMD) →
the explainer layer that popularizes them. URLs verified reachable July 2026.

**IP:** metadata + one original characterizing sentence per entry. No body text of any
paper is reproduced. This form's `exemplars/` dir is empty by design (no open-licensed
source).

## Formal whitepapers (PDF, math + proofs + references)

| # | Title | Author / Org | URL | Year | Why it exemplifies the form + structural note |
|---|-------|--------------|-----|------|-----------------------------------------------|
| 1 | Solana: A New Architecture for a High Performance Blockchain (the Solana whitepaper) | Anatoly Yakovenko | https://solana.com/solana-whitepaper.pdf | 2017 | The ecosystem's founding whitepaper and the reference template for the whole form. Structure: Abstract → §1 Introduction → §2 **Outline** → §3 Network Design → §4 Proof of History → §5 Proof of Stake Consensus → §6 Streaming Proof of Replication → §7 System Architecture → References; ~10pp original (32pp re-typeset), 8 figures, 9 refs, per-subsystem *Attacks* sections, heavy timing/limit math. |
| 2 | Alpenglow: A New Consensus for Solana (whitepaper v1.1) | Kniep, Sliwinski & Wattenhofer (Anza / ETH Zürich) | https://anza.xyz/alpenglow-1-1 | 2025 | The modern frontier: a full academic paper with **machine-checked safety/liveness proofs** and a Rust reference implementation. Structure: abstract/result-first → Votor (voting) → Rotor (dissemination) → formal proofs/appendices; stated trust modes (80% one-round / 60% two-round finality). |
| 3 | Alpenglow announcement + repo | Anza | https://www.anza.xyz/blog/alpenglow-a-new-consensus-for-solana · https://github.com/anza-xyz/alpenglow | 2025 | The paper's distribution + spec-as-code companion — shows the launch-blog-plus-repo pattern that now accompanies a serious Solana paper. |
| 4 | Drift Protocol v0 Devnet Feature Paper (Revision 1.1) | Drift Labs | https://cdn.prod.website-files.com/611580035ad59b20437eb024/61293b57e3103934ddc5535f_v0%20Devnet%20Feature%20Paper%20-%20Revision%201.1.pdf | 2021 | Textbook app-layer whitepaper: 18pp, **ToC with page numbers**, and a per-section *Current vs Future Implementation* split. Structure: Abstract → 1 Technical Overview (Components/Instructions/Data Structures) → 2 vAMM → 3 Trading Specs → 4 Margin → 5 Funding Rates → 6 Dynamic Fees → 7 Liquidations → 8 Risks → 9 Conclusion → 10 Disclaimer → 11 References. |
| 5 | Pyth Network: A First-Party Financial Oracle (whitepaper v2.0) | Pyth Data Association | https://pythdataassociation.com/whitepaper.pdf | 2022 | A short (6pp) formal paper proving the litepaper/whitepaper length spectrum. Structure: pull-oracle mechanism → aggregation + confidence intervals → §2.1 Update Fees → §2.2 Pull-vs-Push → tokenomics (10B supply, 85% locked, staged unlocks) → governance. |
| 6 | Alpenglow / SIMD-0326 | Solana Foundation (SIMD process) | https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md | 2025 | The **SIMD**: Solana's canonical protocol-level spec form (Markdown in GitHub), the code-native counterpart to a PDF whitepaper. Structure: motivation → new terminology → detailed design → security → backwards compatibility. |

## Litepapers (docs-embedded, mechanism + tokenomics, few/no proofs)

| # | Title | Author / Org | URL | Year | Why it exemplifies the form + structural note |
|---|-------|--------------|-----|------|-----------------------------------------------|
| 7 | Marinade Protocol — litepaper / system overview | Marinade Finance | https://docs.marinade.finance/ · https://docs.marinade.finance/marinade-protocol/system-overview | 2021–ongoing | The docs-embedded litepaper pattern: liquid-staking mechanism (mSOL rewards accrual, epoch revaluation, 400+ validator delegation strategy) + MNDE governance, at docs-page length, no proofs. |
| 8 | Meteora DLMM — product docs / litepaper | Meteora | https://docs.meteora.ag/ · https://www.meteora.ag/ | 2023–ongoing | Litepaper-grade explanation of a novel AMM primitive (discrete-price **liquidity bins**, zero-slippage-within-bin, dynamic volatility fees) delivered as living docs rather than a standalone PDF — with domain diagrams instead of equations. |
| 9 | Understanding the PYTH Tokenomics | Pyth Network | https://www.pyth.network/blog/understanding-the-pyth-tokenomics | 2023 | The tokenomics half of a litepaper spun out as a standalone post — hard numbers (10B fixed supply, 85% locked, 6/18/30/42-month unlocks) plus governance scope. |

## Spec-as-code / no-paper protocols (docs + GitHub + blog)

| # | Title | Author / Org | URL | Year | Why it exemplifies the form + structural note |
|---|-------|--------------|-----|------|-----------------------------------------------|
| 10 | Jito — MEV docs + jito-solana client | Jito Labs / Foundation | https://docs.jito.wtf/ · https://github.com/jito-foundation/jito-solana | 2022–ongoing | A high-value protocol with **no classic whitepaper**: bundles, tip auctions, and TipRouter/NCN tip distribution are specified in docs + the validator-client repo — the Solana norm of docs-as-spec. |
| 11 | Firedancer | Jump Crypto / Firedancer team | https://github.com/firedancer-io/firedancer · https://jumpcrypto.com/build/firedancer | 2022–ongoing | A ground-up C validator client whose "spec" is the **codebase + a build page**, never a whitepaper — the extreme of Solana's spec-as-code convention (tile message-passing architecture, AF_XDP kernel bypass). |
| 12 | Jupiter — developer & tokenomics hub | Jupiter Exchange | https://dev.jup.ag/ · https://station.jup.ag/ | 2021–ongoing | Solana's largest DEX aggregator documents mechanism via a dev portal and its **tokenomics via a running series of DAO/blog posts** (Jupuary airdrops, the Castanbul supply burn) rather than a single litepaper. |
| 13 | Wormhole — protocol docs | Wormhole | https://wormhole.com/docs/ | ongoing | Cross-chain messaging protocol used heavily on Solana; canonical design lives in structured docs (guardian/VAA model) — an interoperability example of the docs-spec pattern. |

## The explainer layer (blogs that popularize a paper — how the form is actually distributed)

| # | Title | Author / Org | URL | Year | Why it belongs here + note |
|---|-------|--------------|-----|------|----------------------------|
| 14 | Alpenglow: Solana's Great Consensus Rewrite | Helius (Ryan/Helius team) | https://www.helius.dev/blog/alpenglow | 2025 | The prototypical **whitepaper→explainer**: turns the formal Votor/Rotor paper into an accessible deep-dive — the real distribution channel for a dense spec. |
| 15 | What is Firedancer? | Helius | https://www.helius.dev/blog/what-is-firedancer | 2023 | Explains a *codebase-only* spec (Firedancer's tile architecture) for a general dev audience — shows how the ecosystem substitutes explainers when there is no paper. |
| 16 | Jito Explained: Bundles, Tips & MEV on Solana | Chainstack | https://chainstack.com/jito-explained-bundles-tips-mev-solana/ | 2024 | Infra-vendor explainer standing in for Jito's absent whitepaper — documents bundle auctions and tip flow narratively. |
| 17 | Proof of History: A Clock for Blockchain | Anatoly Yakovenko | https://solana.com/news/proof-of-history | 2017 | The founder's own popularization of the whitepaper's core primitive — the canonical example of pairing a formal paper with a plain-language companion. |
