# Tutorial — curated catalog

Real, currently-reachable (verified July 2026) exemplars of the **tutorial** form in the
Solana ecosystem. Each entry: title — author/org — URL — (year) — one original sentence on
why it exemplifies the form + a structural note. Mix of verbatim open-licensed exemplars
(Solana Foundation guides/cookbook, saved under `exemplars/`) and external tutorials
catalogued as metadata only.

Verbatim provenance: guides & cookbook from `solana-foundation/developer-content` (open
repo). External sources are proprietary — metadata + one characterizing sentence only, no
body text.

## Guide-tutorials (verbatim exemplars, Solana Foundation)

1. **Setup, build, and deploy a Solana program locally in Rust** — Solana Foundation —
   https://solana.com/developers/guides/getstarted/local-rust-hello-world — (2024) —
   The archetypal zero-to-deployed native-Rust quickstart, and the corpus's cleanest step
   model. Structure: hook → `## What you will learn` → verb-first steps (install → validator
   → cargo lib → write entrypoint → build → deploy) → literal `Program Id:` output →
   promote to devnet → Next steps; heavy shell+rust, five callouts. (`exemplars/guides/local-rust-hello-world.md`, ~1,442 words)

2. **How to CPI in a Solana program** — Solana Foundation —
   https://solana.com/developers/guides/getstarted/how-to-cpi — (2024) —
   Shows one task three functionally-equivalent ways (CpiContext → invoke helper → manual
   Instruction), teaching depth by progressive expansion. Structure: Playground starter →
   `## How to CPI with Anchor` with three `###` variants, each a runnable diff with
   line/regex highlights; ~2:1 code-to-prose. (`exemplars/guides/how-to-cpi.md`, ~826 words)

3. **How to Create a Token on Solana** — Solana Foundation —
   https://solana.com/developers/guides/getstarted/how-to-create-a-token — (2024) —
   A CLI-first build that ends with a real SPL mint plus uploaded metadata, artifact you can
   see in a wallet. Structure: ten short verb-first `##` steps (install → keypair → devnet
   SOL → mint address → create mint → upload image/metadata → mint tokens) → further
   reading. (`exemplars/guides/how-to-create-a-token.md`, ~1,612 words)

4. **Full-stack Solana Development with React and Anchor** — Solana Foundation —
   https://solana.com/developers/guides/getstarted/full-stack-solana-development — (2024) —
   A two-artifact build (Anchor counter program + React client) that models nested-section
   scaffolding for longer tutorials. Structure: `## Project overview` → `## Write and deploy
   a Solana program` (Anchor project → Rust → test → PDA → devnet) → `## Build a React
   client` → `## What now?`; ~6,805 words, borders on a mini-course. (`exemplars/guides/full-stack-solana-development.md`)

5. **How to add transfer fees to a token (Token Extensions)** — Solana Foundation —
   https://solana.com/developers/guides/token-extensions/transfer-fee — (2024) —
   Best template for a feature-family cadence: one tight tutorial per token extension.
   Structure: Getting Started → Add Dependencies → Mint Setup → Build Instructions → Send
   Transaction → per-operation steps → Conclusion; very code-heavy (~2:1). (`exemplars/guides/transfer-fee.md`, ~2,067 words)

6. **How to create a CRUD dApp (Journal) on Solana** — Solana Foundation —
   https://solana.com/developers/guides/dapps/journal — (2024) —
   A create/read/update/delete journal program that teaches account lifecycle end-to-end via
   one coherent artifact. Structure: Anchor program with init/update/delete instructions,
   PDA-per-entry, tests, then client. (`exemplars/guides/journal.md`, ~2,167 words)

7. **Hello World in your browser (Solana Playground)** — Solana Foundation —
   https://solana.com/developers/guides/getstarted/hello-world-in-your-browser — (2024) —
   The zero-install on-ramp exemplar: build and deploy entirely in Solana Playground before
   touching a local toolchain. Structure: `## What you will learn` → Using Solana Playground
   → Create a program → Interact with it → Next steps. (`exemplars/guides/hello-world-in-your-browser.md`, ~1,615 words)

8. **Creating Compressed NFTs with JavaScript** — Solana Foundation —
   https://solana.com/developers/guides/javascript/compressed-nfts — (2023) —
   A long JS/TS build covering Merkle-tree creation, minting, reading, and transferring
   cNFTs — a heavier "advanced artifact" tutorial. Structure: env setup → create tree → mint
   → read → transfer; JS-first, ~4,200 words. (`exemplars/guides/compressed-nfts.md`)

## Cookbook-recipes (verbatim exemplars, Solana Foundation)

9. **How to Create a Keypair** — Solana Foundation —
   https://solana.com/developers/cookbook/wallets/create-keypair — (2024) —
   The minimal recipe: one paragraph of context and a `<Tabs>` v2/v1 snippet, no learning
   arc — the pure "how do I X?" reference shape. Structure: framing sentence → two SDK tabs;
   ~109 words, code-first. (`exemplars/cookbook/wallets__create-keypair.md`)

10. **How to Create a PDA's Account** — Solana Foundation —
    https://solana.com/developers/cookbook/accounts/create-pda-account — (2024) —
    Shows the `## Program` / `## Client` split standard for on-chain recipes, with the Rust
    `invoke_signed` create + the web3.js caller. Structure: framing → Generating a PDA →
    Program (rust) → Client (ts); ~369 words. (`exemplars/cookbook/accounts__create-pda-account.md`)

11. **How to do Cross Program Invocation** — Solana Foundation —
    https://solana.com/developers/cookbook/programs/cpi — (2024) —
    A larger recipe (no H2s at all) carrying the full SPL-transfer-via-CPI code with an
    EVM/Uniswap analogy for framing. Structure: prose framing + numbered account list → two
    long rust blocks; ~1,302 words, ~13:1 code-to-prose. (`exemplars/cookbook/programs__cross-program-invocation.md`)

## External tutorials (catalog metadata only)

12. **Deploy Your First Solana Program / Quick Start** — Solana (official docs) —
    https://solana.com/docs/intro/quick-start — (2025) —
    The canonical browser-based first build (program → accounts → transactions → PDAs/CPIs)
    with no local install required. Structure: sequential Playground steps, each ending in a
    confirmed on-chain action.

13. **An Introduction to Anchor: A Beginner's Guide to Building Solana Programs** — Helius
    (0xIchigo) — https://www.helius.dev/blog/an-introduction-to-anchor-a-beginners-guide-to-building-solana-programs — (2024) —
    A tutorial-plus-reference hybrid that deploys a Hello-World in Playground then annotates
    every Anchor primitive it uses. Structure: prereqs → install → Playground → Hello World
    → deep dives (IDLs/macros, account types/constraints/space, errors, CPIs, PDAs) →
    conclusion; deploys to devnet.

14. **How to Write Your First Anchor Program in Solana — Part 1** — QuickNode (Aaron Milano)
    — https://www.quicknode.com/guides/solana-development/anchor/how-to-write-your-first-anchor-program-in-solana-part-1 — (2024) —
    A vendor-blog quickstart that ships a deployable Anchor program and a TS client, part of
    a numbered series. Structure: Overview/prereqs → init project → wallet + devnet SOL →
    Hello World → compile & deploy → call from client → Wrap Up.

15. **How to Create and Mint Fungible SPL Tokens Using Anchor** — QuickNode —
    https://www.quicknode.com/guides/solana-development/anchor/create-tokens — (2024) —
    Builds a two-instruction (`init_token`, `mint_tokens`) Anchor program with tests to a
    working mint. Structure: setup → program instructions → tests → run; program + test code
    interleaved with prose.

16. **How to Build a Solana Portfolio Viewer with Next.js** — Helius —
    https://www.helius.dev/blog/build-a-solana-portfolio-viewer — (2024) —
    A client-side app tutorial (RPC/DAS + Next.js) whose artifact is a running wallet-balance
    UI rather than a program. Structure: setup → fetch balances/assets → render → deploy;
    TS/React-first.

17. **How to Start Building with the Solana Web3.js 2.0 SDK** — Helius —
    https://www.helius.dev/blog/how-to-start-building-with-the-solana-web3-js-2-0-sdk —
    (2024) — A migration-flavored build that walks the new `@solana/kit` primitives
    (createSolanaRpc, pipe, functional transactions) with runnable snippets. Structure:
    what's new → install → RPC → build/sign/send a tx → patterns.

18. **Solana Anchor: Accounts, PDAs, Seeds, Bumps Explained** — Chainstack —
    https://chainstack.com/solana-anchor-accounts-pdas-seeds-bumps/ — (2024) —
    A concept-anchored tutorial that builds small Anchor programs to make PDAs/seeds/bumps
    concrete rather than abstract. Structure: concept → minimal program per concept →
    derive/verify; code-forward.

19. **Create a Solana dApp from scratch** — Loris Leiva —
    https://lorisleiva.com/create-a-solana-dapp-from-scratch — (2023) —
    A multi-part indie tutorial building a simplified on-chain Twitter, the canonical
    long-form learn-by-building dApp series. Structure: chaptered program + client build with
    per-chapter runnable checkpoints.

20. **60 Days of Solana** — RareSkills — https://www.rareskills.io/solana-tutorial —
    (2024) — An EVM-developer-oriented course-length tutorial series that maps Ethereum
    mental models onto Solana one buildable day at a time. Structure: sequenced daily
    lessons, each a small self-contained build with exercises.

21. **The Anchor Book** — Coral / Anchor maintainers — https://book.anchor-lang.com/ —
    (2024) — The framework's own tutorial-plus-reference, whose milestone project walks a
    complete Anchor program from `init` to tested. Structure: intro → basics → milestone
    build → references; canonical, version-tracked.
