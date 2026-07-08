# Ackee — School of Solana — Pedagogical Analysis (META)

> Analysis for a course *designer*. Characterizes the STRUCTURE, SEQUENCING, and PEDAGOGY of the course content — what is taught, in what order, how it is chunked, and how a lesson is built.
> Every claim grounded in files under `courses-corpus/ackee/content/`.

## 1. Snapshot

- **Provenance / authorship**: https://ackee.xyz/school-of-solana ; source mirror `Ackee-Blockchain/school-of-solana`. Companion textbook at https://ackee.xyz/solana/book/latest/. Authored by Ackee — a blockchain-security audit firm (also builds Wake + Trident) — whose auditor DNA visibly shapes the content lens (a full security unit, taught exploit-first).
- **Delivery format**: **Primarily VIDEO-led** with a written substrate. The corpus captures only the written layer, which splits into three media:
  1. **Per-lecture READMEs** (`N.lesson/README.md`) — supplementary reference/cheatsheet to a recorded lecture, not the primary teaching medium.
  2. **Solana Handbook** (`Solana-Handbook/docs/...`) — an evergreen, open MkDocs-Material theory textbook, explicitly the "main learning material" for early lessons (`1.lesson/README.md:41`).
  3. **Code example repos** (`hello_world`, `calculator`, `ticket-registry`, `test-examples`, `token-example`, `escrow-example`) — pulled in as git submodules; the corpus retains only their thin how-to READMEs (`yarn install` → `anchor test`).
- **Scale (verified in corpus)**:
  - **7 numbered lessons** (`1.lesson` … `7.lesson`), one per lecture-unit.
  - **3 bonus lectures present** (`Bonus-Pinocchio`, `Bonus-Tokens`, `Bonus-Trident`); the root README lecture table advertises more bonus slots (SPL Tokens, Token-2022, Trident, Gaming/Unity guest lecture).
  - **5 Tasks (hands-on assignments, Task 1–5)** + **1 capstone** ("final Solana program").
  - **Solana Handbook = 4 chapters + 2 appendices, ~40 topic pages**: ch1 Solana Basics (8 topics), ch2 Core Concepts (8), ch3 Programming Model (7), ch4 Solana Program Library (5), Appendix A (ecosystem/wallets/mobile, 3), Appendix B (NFTs/Metaplex/compression, 9).
  - Written depth is **front-loaded**: lessons 2–5 are 12–25 KB of prose; lessons 1/6/7 and all bonuses are 0.6–3.7 KB stubs that defer to video, external repos, and the handbook.
- **Topic scope**: from blockchain fundamentals → Rust → the Anchor programming model (accounts, PDAs, errors, CPI) → testing/debugging → a Solana frontend → program security → (bonus) tokens, fuzzing, and Pinocchio.
- **Target audience**: Programmers new to Solana/Rust who "already have previous knowledge in any programming language" (`README.md:16`). Aimed at devs, and — given Ackee's audit DNA — future auditors.
- **Prerequisites**: Prior programming experience in any language; Git familiarity; an IDE. No Rust or blockchain assumed (lesson 2 is a "gentle introduction to Rust").

## 2. Structural architecture

**Decomposition**: `lecture-unit` → `lesson README + Handbook chapter(s) + code example repo` → `Task`. There is no path/track layer; the sequence is linear.

**Ordering scheme**: **Numbered directories** (`1.lesson` … `7.lesson`) with the **canonical order encoded in a single Markdown table** in the root `content/README.md` (lines 30–44). That table is the ordering-metadata file — a `|Week|Lecture|Description|Task|` grid mapping each numbered lesson to a sequence position and a Task. There is **no YAML frontmatter, no priority field, no manifest JSON** in the lesson tree. The Handbook, by contrast, is ordered by MkDocs `index.md` "grid cards" nav pages (`Solana-Handbook/docs/index.md`, and per-chapter `index.md`), with `hide: [navigation, toc]` frontmatter — a separate ordering system from the lessons.

**Module taxonomy (real names, from `README.md` lecture table)**:
| Unit | Lesson dir | Title | Task |
|------|-----------|-------|------|
| 1 | `1.lesson` | Introduction to Solana and Blockchain | Task 1 |
| 2 | `2.lesson` | Introduction to Rust | Task 2 |
| 3 | `3.lesson` | Solana programming model I | Task 3 |
| 4 | `4.lesson` | Solana programming model II | Task 4 |
| 5 | `5.lesson` | Best development practices and debugging | "Solana Program" (capstone begins) |
| 6 | `6.lesson` | Front-end for Solana Programs | — |
| 7 | `7.lesson` | Security | Task 5 |
| bonus | `Bonus-Tokens` / `Bonus-Trident` / `Bonus-Pinocchio` | SPL Tokens · Token-2022 · Trident Fuzzing · Pinocchio | — |
| 8 | — | Build capstone (integrative program) | — |
| — | — | Guest Gaming (Unity) lecture | — |

**Sequencing logic / prereq graph**: A clean dependency chain — *blockchain concepts → Rust language → Anchor programming model I (accounts, errors) → programming model II (CPI, PDA) → testing/debugging → frontend → security*. The Handbook mirrors this DAG one level deeper: ch1 basics → ch2 the "eight core concepts" (PoH, Tower BFT, Turbine, Gulf Stream, Sealevel, Pipelining, Cloudbreak, Archivers) → ch3 programming model, whose own page order is **Interacting → Transaction Lifecycle → Transaction Anatomy → Account Anatomy → Runtime Policy → PDA → CPI** (`chapter3/index.md`) — i.e. transactions/accounts before PDA before CPI, the correct prerequisite spine.

## 3. Lesson anatomy

A lecture README is a **reference sheet wrapped around a recorded lecture**, not a self-contained lab. Recurring skeleton (grounded in `3.lesson/README.md`, `4.lesson/README.md`, `5.lesson/README.md`):

```
# N. Lecture — <Title>                     ← H1, always
[one-line framing sentence]                 ← "Hackers away! This lecture will…" (optional, motivational)
## Table of Contents  <!-- no toc -->       ← hand-maintained anchor list, always for the heavy lessons
---                                          ← hr separator
# / ## Theory sections                       ← nested headers; prose adapted from canonical docs
   ```rust / ```bash / ```typescript ```     ← inline code blocks (concept → minimal example)
   > [!NOTE] / [!TIP] / [!IMPORTANT] / [!WARNING]   ← GitHub-alert callouts, very frequent
   > [!TIP] [Account Reference](https://docs.rs/…)  ← "reference-relay" links out to docs.rs / anchor-lang
# Additional Resources                        ← optional; curated external reading (Helius, Solana docs)
-----
### Need help?                               ← ALWAYS the final section (a persistent help-pointer footer)
```

Companion artifacts hang off the same dir: `Setup.md`/`Docker.md` (lesson 1 only), and a **code example subdir** (`hello_world/`, `calculator/`, `ticket-registry/`, `test-examples/`) whose README is a 2-line `yarn install` → `anchor test` runner.

**Always present**: H1 title; the "Need help?" footer. **Present on the heavy lessons (2–5)**: hand-written TOC, extensive callouts, worked code snippets. **Optional/absent**: TOC and deep prose vanish on the thin lessons — `6.lesson/README.md` is 15 lines (just links to `create-solana-dapp` + Codama), `7.lesson/README.md` is 70 lines that mostly point to an external "Common Attack Vectors" repo, and `Bonus-Pinocchio/README.md` / `Bonus-Trident/README.md` are **single-line title stubs** (the teaching lives entirely in video).

## 4. Content sequencing & pacing

- **Grain = the lecture-unit.** Content is chunked into 7 sequential lecture-units, each pairing one lecture (video + README + Handbook chapter(s) + a code-example repo) with one hands-on Task. The intended cadence is a lockstep *read/watch → run the example → ship the Task* rhythm, one unit per sitting; there is no branching.
- **The sequence grid is the ordering mechanism** (`README.md:30-44`): units 1–7 each carry a lecture and (mostly) a Task, followed by a dedicated capstone-build unit and a guest Gaming/Unity lecture. Ordering is explicit and linear.
- **Environment setup is front-loaded as unit-1 pre-work**: lesson 1 pushes learners to *"set up your development environment in advance"* (`1.lesson/README.md:3`) and pins exact versions (Rust 1.86.0, Solana 2.2.12, Anchor 0.31.1) so everyone builds on one reproducible toolchain before any code lesson.
- **Handbook as spaced / parallel prep**: lesson 1 frames the Handbook as *"the main learning material for the first lecture… Getting comfortable with it will help you pass the first task!"* (`1.lesson/README.md:41`) — durable theory read *around* the lectures that feeds each unit's Task, a spiral where book concepts resurface in lecture practice.
- **Written depth front-loaded across the sequence**: lessons 2–5 carry 12–25 KB of prose (the conceptual heavy-lifting), while lessons 1/6/7 and all bonuses shrink to 0.6–3.7 KB dispatcher stubs that defer to video/repos/Handbook — scaffold-dense early, faded to thin pointers late.
- **No per-lesson time budgets or micro-goal tiers**: the pacing unit is the lecture-unit, and progress advances by completing each unit's Task rather than by auto-checkpoints.

## 5. Learning artifacts & practice

- **5 Tasks (Task 1–5)**, one hands-on assignment per lecture unit (units 1–4 and 7). The Task specs live off-corpus, but each lecture is tied to its Task in the sequence grid — the required practice artifact that turns a unit's reading/watching into a build.
- **Capstone — an integrative original program**: learners *"build and submit your final Solana program"* (`README.md:72-78`), worked across unit 5 and the dedicated build unit. It is the culminating artifact that forces integration of accounts/PDA/CPI/testing/security into one shipped program.
- **`anchor test` as the local practice harness**: every code-example repo is exercised by `yarn install && anchor test` (`hello_world/README.md`, `calculator/README.md`) — the learner runs a real test suite on their own machine as the built-in verification step.
- **Security practiced adversarially**: lesson 7 hands off to the external **Common Attack Vectors** repo, which ships *"example programs with proof-of-concept tests to demonstrate the attack vectors"* (`7.lesson/README.md:22-26`) — an exploit-then-patch lab, not a quiz.
- **No multiple-choice quizzes anywhere in the corpus.** Practice is entirely artifact-based: per-unit Tasks + one capstone + passing test suites. Every practice item makes the learner write or run code, never just recall.

## 6. Pedagogical devices

Mapped onto the house pattern vocabulary (`course-skill-draft/patterns/*.md`):

- **concept-spine** *(strong — the Handbook)*: The Solana Handbook is a textbook-grade concept-spine — dependency-ordered chapters, each topic a card with a diagram and one concrete instance, stating reading order and *why* (ch3 orders accounts/transactions before PDA before CPI). It is the "understand why it works" layer, deliberately split out from the lectures.
- **security-epoch** *(strong)*: The security unit (lesson 7) is a distinct, late hardening tier taught offense→defense — attack vectors with PoC exploits, then mitigation, then the `Bonus-Trident` **fuzzing** capstone tool. Textbook security-epoch shape.
- **overview-lab-challenge** *(structural, at unit grain)*: The per-unit loop is *read Handbook/watch lecture → run the guided code example (`hello_world`, `calculator`, `ticket-registry`) → ship the unit's Task*. Three exposures at rising autonomy, but stretched across a lecture-unit rather than nested inside one lesson file.
- **client-integration** *(single-lesson slice)*: Lesson 6 is a self-contained client-integration lesson — `create-solana-dapp` scaffold + **Codama** IDL client to wire a UI to the ticket-registry program.
- **map-from-known** *(weak/implicit)*: Routes by generic "you already know some programming language" and eases in with a "gentle introduction to Rust" (lesson 2) — but it is **not** an EVM/web2 1:1 mapping; no false-friend table.
- **build-it-twice** *(nascent, bonus only)*: `Bonus-Pinocchio` gestures at the Anchor→Pinocchio contrast (strip the framework to see the machinery), but it is a one-line video stub, not a first-class twin build.

**New devices to name (not in the house vocabulary):**

- **Companion-textbook split (dual-medium spine)**: the defining device — an **open, evergreen, versioned theory textbook** (Handbook, MkDocs, `/latest/` URL) runs *parallel* to a **code-heavy lecture track**. Concepts live in the durable book; toolchain-specific how-to lives in the disposable lecture READMEs. Cleanly separates "why" (stable) from "how" (churns with Anchor versions).
- **Reference-relay**: instead of reproducing canonical material, lessons *relay* to it via `> [!TIP]` callouts linking docs.rs / anchor-lang / Solana docs (e.g. `3.lesson/README.md` links the Account, Context, and Constraints references inline). The lesson curates and sequences the canon rather than rewriting it — prose is often adapted near-verbatim from Anchor's own docs.
- **Task-portfolio → capstone**: practice is distributed across several small per-unit Tasks that then converge on a single integrative capstone build — many small artifacts to build momentum, one large one to force synthesis of the whole course.
- **Vendor-tool interludes**: bonus lectures double as onboarding to Ackee's own products — **Trident** (fuzzer) and **Pinocchio**/Token-2022 — folding the toolchain into the curriculum as advanced electives.

## 7. Scaffolding & tooling

- **Dev-env setup**: Two supported on-ramps — a **manual guide** (`1.lesson/Setup.md`: WSL 2.0 + Ubuntu 22.04, pinned Rust 1.86.0 / Solana 2.2.12 / Anchor 0.31.1 via `avm`) and a **pre-built Docker image** (`1.lesson/Docker.md`) "with everything ready to go." Version pinning keeps the toolchain reproducible across learners.
- **Starter repos**: per-lesson Anchor projects delivered as **git submodules** (`hello_world`, `calculator`, `ticket-registry`, `token-example`, `escrow-example`, `test-examples`); each is run identically with `yarn install` → `anchor test`.
- **Test harness philosophy** (from `5.lesson/README.md`, the testing lecture): teaches a **layered testing pyramid** — **unit tests** via Rust's native `cargo test` for pure functions/arithmetic/access-control; **integration tests** via `solana-program-test` (in-process runtime) and the **Anchor testing environment** (IDL-aware, PDA-auto-deriving); **client tests** via `@solana/web3.js` / **Solana Kit**. Includes a decision table for choosing between them. *(Note: this corpus predates a LiteSVM/Mollusk migration; it teaches `solana-program-test` + `solana-test-validator`, and `Common Issues/README.md` troubleshoots the validator directly.)*
- **Frontend tooling** (lesson 6): `create-solana-dapp` (full-stack template) + **Codama** (IDL→TypeScript client generator).
- **Fuzzing** (Bonus): **Trident** — "the first Solana Fuzzer for Anchor programs," Ackee's own tool — as the advanced security testing layer.
- **In-browser vs local**: **fully local** (WSL/Docker). No hosted IDE, no in-browser autograder; the built-in check is `anchor test` on the learner's machine, plus `anchor keys list` for the classic program-ID mismatch (`Common Issues/README.md`).
- **A dedicated `Common Issues` doc** acts as a shared troubleshooting harness (insufficient funds, rustc mismatch, program-ID mismatch, WSL cwd) with a contribution template — friction-removal treated as first-class scaffolding.

## 8. Voice & framing

- **Register**: warm, encouraging, lightly exclamatory instructor voice for the lecture READMEs — hooks like *"Hackers away!"* (lesson 7), *"Make your program alive!"* (lesson 6), *"Develop like a pro!"* (lesson 5). The Handbook is calmer and textbook-formal ("written for developers, auditors and anyone interested in how Solana works… **Good luck, and enjoy the journey!**").
- **Motivation devices**: a persistent "Need help?" footer on every page; framing Ackee's audit credibility ("created with love by Solana Auditors and Developers of Ackee").
- **Concept introduction**: definition → minimal Rust snippet → escalate constraints → callout of the gotcha. Heavy use of GitHub-alert callouts (`[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`) to separate the happy path from footguns (e.g. "use `require_keys_eq` not `require_eq` for pubkeys — comparing with `require_eq` is very expensive," `3.lesson/README.md:393`).

## 9. Distinctive signatures

- **A real, open, evergreen textbook** (the Solana Handbook) shipped *alongside* the lectures — most Solana courses have lessons only; Ackee maintains a versioned `/latest/` MkDocs book with its own DAG, diagrams, and appendices that outlive any single season of the course.
- **The "eight core concepts" framing** (ch2): infrastructure internals (PoH, Tower BFT, Turbine, Gulf Stream, Sealevel, Pipelining, Cloudbreak, Archivers) are taught as first-class curriculum, not hand-waved — reflecting the auditor's why-it's-fast lens.
- **Auditor-firm DNA end-to-end**: security is a full unit taught exploit-first via a PoC repo, then fuzzed with **Trident** (their own tool) — the content is oriented toward producing developers who think like auditors.
- **Reference-relay over reproduction**: lessons deliberately curate-and-link the canonical docs (docs.rs, anchor-lang) rather than re-teaching them, keeping the written layer thin and the video + book as the real payload.
- **Version-pinned, dual on-ramp (manual + Docker)** so every learner shares one exact toolchain — infrastructure treated as pedagogy.

## 10. Takeaways for a course designer

1. **Split "why" from "how" into two media.** Steal the companion-textbook pattern: put durable conceptual theory in an evergreen, versioned book (its own prereq DAG + diagrams) and keep toolchain-specific how-to in disposable, dated lesson notes. The book survives framework churn; the notes get rewritten each iteration.
2. **Encode ordering in one human-readable table, not scattered frontmatter.** Ackee's entire sequence lives in a single `|Lecture|Task|` grid in the root README — trivially auditable and editable. Fine for a linear course; add a manifest only when you need branching/paths.
3. **Distribute practice across per-unit Tasks that culminate in one integrative capstone.** Several small hands-on Tasks build momentum unit by unit; a single real capstone forces the learner to synthesize the whole course into one shipped program.
4. **Make security a late, distinct, offense-first epoch.** Don't sprinkle security into every lesson — concentrate it (the security unit + fuzzing bonus), teach exploit→patch with PoC tests, and assess with adversarial artifacts, not quizzes.
5. **Pin the toolchain and offer a Docker escape hatch.** Exact versions (Rust/Solana/Anchor) + a prebuilt image + a `Common Issues` troubleshooting doc eliminate the "works on my machine" tax that silently stalls learners.
6. **Relay to canon; don't reproduce it.** Curate and sequence the official docs with callout links instead of rewriting them — cheaper to maintain and keeps learners in the real reference habitat. Reserve your prose for the connective tissue and gotchas.
7. **Front-load environment setup as explicit pre-work.** "Set up before lesson 1" plus a version table gets every learner building from the first lecture instead of debugging installs.
8. **Watch the failure mode: thin READMEs are dead weight without the video.** Lessons 6/7 and the bonus stubs are near-empty on their own — if you adopt a video-primary model, either accept that the written layer is a cheatsheet *or* invest to make it self-contained; don't ship one-line "READMEs" and call it a lesson.
