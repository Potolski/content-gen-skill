# Solana Syllabus DAG — the domain knowledge the architecture must respect

The one thing the corpus agrees on hardest is **order**. Solana concepts have a real dependency graph;
violating it is the most common way a course confuses people. This file is the architect's source of truth
for sequencing. (Distilled from Solana docs — which state the order in prose — plus RareSkills, Cyfrin,
Ackee, freeCodeCamp, Blueshift, the Anchor Book, and program-examples.)

---

## 1. The prerequisite DAG (developer track)

The Solana docs state it outright: *"Read Accounts, Programs, Instructions, Transactions, and Fees in that
order, as each builds on the previous. Read Accounts and Programs before PDAs. Read Programs, Instructions,
and PDAs before CPIs."* Consolidated with language + applied layers:

```
Foundations (mental model)
  blockchain-as-state-machine ─► why Solana (PoH, parallelism/Sealevel, fees)

Language
  Rust basics (ownership/borrowing, structs, enums, Result/Option,
               traits, macros-as-boilerplate-at-first)        ── can be JIT, not all up front

Core primitives  (THE hard dependency chain — do not reorder)
  Account model (accounts, data, owner, rent, executable)
        │
        ├─► Programs (the program account, instructions, handlers)
        │         │
        │         ├─► Transactions (signers, instruction composition, atomicity)
        │         └─► Fees / Compute units / priority fees
        │
        ▼
  PDAs (find_program_address, canonical bump, seeds)
        │
        ▼
  CPIs (invoke / invoke_signed, signing as a PDA, program composition)

Applied
  SPL Tokens (Token Program: mint/ATA/transfer)  ─►  Token-2022 extensions  ─► transfer hooks
  Clients (TS @solana/web3.js or kit; Rust client; IDL as the program↔client contract)
  Testing (LiteSVM / Mollusk / bankrun; anchor test)        ── introduce EARLY, not at the end

Hardening
  Security (signer/owner/PDA/rent checks → exploit → patch → fuzz/CTF)   ── late tier, after build fluency

Composites
  DeFi (vault, escrow, AMM/constant-product, auction, lending, oracle integration) → capstone
```

**Hard edges (never violate):** accounts before programs; programs+accounts before PDAs;
programs+instructions+PDAs before CPIs; CPIs before anything that composes programs; tokens before
token-extensions before transfer-hooks; build fluency before security.

**Soft edges (can move by audience):** Rust depth (teach just-in-time vs. up front); native vs. Anchor
first (see §4); how early the mental-model block sits.

---

## 2. The canonical artifact ladder (the spine of the builds)

Concepts ride on artifacts. This ladder recurs across nearly every source — use it as the build sequence,
slicing in only the rungs the course's outcome needs:

| Rung | Artifact | Teaches (primitive) | Difficulty |
|---|---|---|---|
| 0 | **hello-world** (log / greeting) | program entry, deploy, the toolchain | 1 |
| 1 | **counter** | account state, read/write, init | 1 |
| 2 | **SPL token**: create → mint → transfer | the Token Program, ATAs | 1–2 |
| 3 | **PDA app**: vault / escrow / review / leaderboard | PDAs, per-user state, ownership | 2 |
| 4 | **transfer / payment splitter** | SOL movement, signers, CPI to system program | 2 |
| 5 | **DeFi**: AMM (constant-product) / Dutch auction / fundraiser | math, composition, token CPIs | 3 |
| 6 | **CPI composition**: factory → child program | invoke_signed, cross-program design | 3 |
| 7 | **capstone** (freeform, learner's own) | integration, judgment | 3 |

A single **accreting** artifact (one project that grows rung to rung) compounds motivation; a set of
**discrete** challenge artifacts (one per rung) maximizes portfolio breadth. Pick per pattern
(`challenge-ladder` favors discrete; `concept-spine`+lab favors accreting).

**Client / frontend sub-ladder** (for dApp / mobile / integration courses — see
`../patterns/client-integration.md`): `connect a wallet → read an account/state → build & send a
transaction → confirm + handle errors → subscribe to account changes → IDL-typed client → full
dApp/mobile UI`. The program is given or built in a paired on-chain module; this ladder wires the user to
it. (The on-chain ladder above is program-only; client courses ride this one.)

## 3. The token progression (a sub-ladder, mirrored in program-examples & Anchor docs)
`create-token → mint → transfer → ATA management → escrow/swap → Token-2022 basics → an extension
(transfer-fee / interest-bearing / metadata / non-transferable) → transfer-hooks (hello → whitelist).`
Don't teach Token-2022 before SPL Token; don't teach transfer-hooks before a basic extension.

## 4. Native vs. Anchor — the abstraction-layering decision
The corpus shows three valid strategies; pick one per audience (see `patterns/build-it-twice.md`):
- **Anchor-first, native later** (Solana Foundation) — productivity first, reveal internals later. Best for
  app developers and beginners.
- **Native-first, Anchor later** (freeCodeCamp) — feel the raw mechanism, then appreciate the framework.
- **Both side-by-side** (Cyfrin "build it twice"; program-examples' tri-framework matrix) — deepest
  understanding; costs ~2× the build time. Best for intermediate→advanced "why the framework exists."
Default for a general course: **Anchor-first**, with one or two native "look under the hood" detours.

## 5. The security vulnerability-class checklist (the late tier)
When the course includes hardening, this is the canonical class list (Sealevel attacks / Ackee / Cyfrin
Common Bugs), taught **insecure → exploit → patch**:
signer authorization · owner checks · account-data matching · reinitialization (init_if_needed) · duplicate
mutable accounts · type cosplay · arbitrary CPI · bump-seed canonicalization · closing accounts (revival) ·
PDA sharing · missing rent/cleanup · arithmetic overflow. Add **fuzzing** (Trident) and/or a **CTF** as the
applied assessment.

## 6. Audience entry-points (where to open the same DAG)
| Audience | Open on… | Lean pattern | Note |
|---|---|---|---|
| Absolute beginner | the account model, concretely; toolchain win first | completion-loop + overview-lab-challenge | Rust just-in-time; biggest scaffold |
| Web2 dev | "a program is a stateless function; state lives in accounts you pass in" | concept-spine + challenge-ladder | map from functions/DBs |
| EVM dev | the 1:1 mappings (compute≈gas, errors≈revert), defer storage/accounts | map-from-known | RareSkills inversion: early wins, then the different parts |
| Rust dev, new to blockchain | the account model + runtime (they have the language, not the chain model); skip Rust onboarding | concept-spine + challenge-ladder | map Rust ownership → account ownership; don't spend time on syntax |
| Solana dev leveling up | the specific gap (Token-2022, security, sBPF, optimization) | build-it-twice / security-epoch | skip foundations; gate on the prereq skill |
| Non-technical | concept-spine only (no builds); analogies + diagrams | concept-spine | outcome is *understanding*, proof is explain-it-back |

## 7. Toolchain & scaffold notes (to remove extraneous load)
Zero-install on-ramps the architect can specify: **Solana Playground** (browser, no install),
**Docker images** (Ackee-style), a **scaffold repo** (create-solana-dapp / Scaffold-ETH analog).
Testing tools to introduce early: **LiteSVM / Mollusk / bankrun**, `anchor test`. Naming convention for
builds: outcome-led, "Build a \<artifact\>" / "Learn \<primitive\> by building \<artifact\>."

**Testing is a thread, not a module** — introduce `anchor test` early and reuse it as the acceptance gate
on every build (overview-lab-challenge lessons), escalating to **fuzzing** (Trident) in the security tier;
tag generic test lessons `show-how`. This is the **`testing-thread`** pattern (`../patterns/testing-thread.md`).
**Optimization (compute units)** is a late **measure → optimize → re-measure** diagnostic loop (the
security-epoch loop shape), with before/after CU numbers as the proof — not a build-it-twice contrast. This
is the **`optimization-loop`** pattern (`../patterns/optimization-loop.md`). *(Both are now formalized
dedicated patterns — route them via `../routing/ROUTING.md`.)*
