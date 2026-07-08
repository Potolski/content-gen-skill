# RareSkills — "60 Days of Solana" — Structural Capture

> **Provenance:** https://rareskills.io/solana-tutorial (publicly readable blog series).
> This file is a **structural + pedagogical capture** (table of contents, ordering,
> stated approach), not a verbatim copy of lesson prose. It exists so the pattern
> analysis in `META.md` has a stable, inspectable artifact. Facts below were read
> from the public course index and framing page.

## Format
- **Delivery:** written blog-article lessons (free, no login), reachable individually.
- **Scale:** 60 lessons across 8 modules. The "60 Days" title frames a sustained
  daily-ish cadence; exact per-day pacing is not prescribed.
- **Companion:** code snippets inline; assumes local Anchor/Rust toolchain.

## Stated audience & prerequisites
- Target: engineers with **beginner–intermediate Ethereum/Solidity** experience.
- No prior Rust required. Learners without Solidity are pointed at RareSkills'
  free Solidity tutorial first.
- Thesis: a competent EVM dev learns Solana faster than a blockchain novice
  (analogy used: frontend→mobile transitions faster than backend→mobile).

## Pedagogical signature
- **Map-from-known:** every unit framed as "I know how to do X in Ethereum — how
  do I do X in Solana?" One-to-one concept mappings are the primary scaffold.
- **Deliberate inversion of the usual order:** intermediate EVM-familiar topics
  (compute units/gas, clock/block vars, msg.sender analogues) are frontloaded
  *before* Solana fundamentals like storage, because they map cleanly and build
  momentum through early wins.
- **Bite-sized active learning:** short exercises per lesson; "early victories"
  before the hard mental-model shift (accounts/ownership).
- **Spaced reinforcement:** the accounts module (18 lessons) revisits the same
  model repeatedly, explicitly acknowledging "it doesn't all stick right away."
- **Ends in raw metal:** closes with native (no-Anchor) programs and hand-written
  sBPF assembly — a rare depth ceiling for an intro course.

## Table of contents (8 modules, 60 lessons)

### Module 1 — Introductory Topics (5)
1. Solana Hello World (installation & troubleshooting)
2. Arithmetic and basic types in Solana and Rust
3. Solana Anchor program IDL
4. Require, revert, and custom errors in Solana
5. Solana programs are upgradeable and do not have constructors

### Module 2 — The Minimum Rust You Need to Know (5)
1. Basic Rust for Solidity developers
2. The unusual syntax of Rust
3. Rust function-like procedural macros
4. Rust structs and attribute-like / custom derive macros
5. Visibility and "inheritance" in Rust and Solana

### Module 3 — Important System-level Information in Solana (5)
1. The Solana clock and other "block" variables
2. Solana sysvars explained
3. Solana logs, "events," and transaction history
4. Tx.origin, msg.sender, and onlyOwner in Solana: identifying the caller
5. Introduction to Solana compute units and transaction fees

### Module 4 — Accounts and Storage in Solana (18)  ← the spine
1. Initializing accounts in Solana and Anchor
2. Solana counter tutorial: reading and writing data to accounts
3. Read account data with Solana web3 js and Anchor
4. Creating "mappings" and "nested mappings" in Solana
5. Cost of storage, maximum storage size, and account resizing
6. Reading an account balance in Anchor (address(account).balance analogue)
7. Function modifiers (view/pure/payable) & fallback functions: why they don't exist
8. Transferring SOL and building a payment splitter ("msg.value" in Solana)
9. Modifying accounts using different signers
10. PDA vs Keypair account in Solana
11. Understanding account ownership: transferring SOL out of a PDA
12. Init_if_needed in Anchor and the reinitialization attack
13. Multicall in Solana: batching transactions and transaction size limit
14. Owner vs authority in Solana
15. Deleting and closing accounts and programs in Solana
16. #[derive(Accounts)] in Anchor: different kinds of accounts
17. Reading another Anchor program's account data on chain
18. Cross-program invocation in Anchor

### Module 5 — Tokens on Solana (10)
1. How the SPL Token works
2. Transferring SPL tokens with Anchor and web3.js
3. Token sale with total supply tutorial
4. Basic bank tutorial with SPL tokens and Anchor
5. How Metaplex metadata for tokens works
6. Implementing token metadata with Metaplex
7. Time travel testing with LiteSVM
8. The Solana Token-2022 specification
9. Interest bearing token — part 1
10. Interest bearing token — part 2

### Module 6 — Advanced Topics in Solana Development (3)
1. Solana instruction introspection
2. Ed25519 signature verification in Solana
3. Switchboard

### Module 7 — Native Solana Programs (8)
1. Native Solana: program entry and execution
2. Native Solana: reading account data
3. Native Solana: Borsh serialization
4. Native Solana: CPI with invoke and invoke_signed
5. Native Solana: creating accounts for storage I
6. Native Solana: creating accounts for storage II
7. Native Solana: function dispatching
8. Native Solana: essential security checks

### Module 8 — Solana Assembly (sBPF) (8)
1. Rust program to SBF compilation
2. Introduction to sBPF virtual machine and instruction set
3. Tracing SBF instruction execution and compute costs
4. Solana program execution and input serialization
5. Instruction processor and runtime setup
6. sBPF memory layout and register conventions
7. Reading Solana instruction inputs using sBPF assembly
8. Solana syscalls: logging in sBPF assembly
