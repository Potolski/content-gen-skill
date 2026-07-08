# Cyfrin Updraft — Solana: Curriculum Analysis (META)

> Pedagogical teardown for a course *designer*. Not a content summary. Every structural
> claim below is grounded in files under `content/` that were actually opened.

## 1. Snapshot

- **Provenance:** https://updraft.cyfrin.io/courses/solana — source transcripts mirrored from the
  Cyfrin `solana-course` monorepo (exercise links throughout point to
  `github.com/Cyfrin/solana-course/blob/main/apps/...`).
- **Delivery format:** **Video-first**, with these `+page.md` files as the written companion /
  transcript layer. Tell-tale signs: every "lesson" is a SvelteKit route (`<n>-<slug>/+page.md`);
  interstitial and quiz slots exist as **stub routes** with no markdown body (see §5), which only
  makes sense if the real payload is a video + an interactive quiz component rendered by the
  Updraft platform, not the markdown.
- **Scale (verified counts):**
  - **9 modules** (`1-course-intro` … `9-common-bugs`) — the brief said 8; there is a 9th,
    `9-common-bugs`, a security/CTF tier.
  - **48 `+page.md` files total.** Of those: **9 inter-module interstitial stubs** (2-line
    placeholders, no instructional body), **8 quiz stubs** (literally the 3 bytes `---`), leaving
    **31 real content lessons**.
  - Real lessons decompose into **15 concept/theory lessons**, **12 exercise READMEs**
    (6 projects × native + Anchor), and **4 CTF exploit challenges**.
  - **6 dual-track build projects:** `hello`, `oracle`, `piggy` (piggy-bank), `auction`
    (dutch-auction), `amm`, `cpi`. Each is built **twice** — once native, once Anchor.
  - **4 CTF challenges** in module 9 (signer, authorization, pda, rent).
  - **Hours:** not encoded in the corpus (video runtimes aren't in the markdown); do not infer.
- **Target audience (stated in `1-course-intro/2-course-intro`):** three named personas —
  (1) aspiring Solana developers who found other resources too dense, (2) Rust practitioners
  sharpening skills "in a high-stakes setting," (3) **security auditors / bug hunters** (the native
  track exists partly to serve them).
- **Prerequisites (stated):** working knowledge of **Rust**; blockchain fundamentals;
  **EVM experience "highly recommended"** — the course "frequently use[s] EVM concepts as a
  comparative baseline."

## 2. Structural architecture

**Decomposition:** `course → modules (9) → lessons (numbered dirs) → +page.md`. There is exactly
one leaf content file per lesson (`+page.md`), the SvelteKit page convention.

**Ordering scheme:** purely **numeric directory prefixes** — `2-core-concepts/5-pda/+page.md`.
There is **no sidecar metadata file** (no JSON/YAML/frontmatter index); the only non-`+page.md`
file in the whole tree is `LICENSE`. Sequence is therefore encoded entirely in folder names, and
lesson frontmatter is absent (concept lessons open directly on an `#`/`##` H1). Ordering is
strict, linear, prerequisite-driven — not priority-field or metadata-driven.

**Module taxonomy (real names):**

| # | Module | Role | Build project | Tracks |
|---|--------|------|---------------|--------|
| 1 | `1-course-intro` | Framing + env setup | — | — |
| 2 | `2-core-concepts` | Concept spine | — | — |
| 3 | `3-hello-program` | First program | `hello` | native + anchor |
| 4 | `4-oracle` | Program state | `oracle` | native + anchor |
| 5 | `5-piggy-bank` | PDAs + SOL transfer | `piggy` | native + anchor |
| 6 | `6-dutch-auction` | SPL tokens | `auction` | native + anchor |
| 7 | `7-amm` | DeFi / token math | `amm` | native + anchor |
| 8 | `8-cpi-idl` | Composition | `cpi` (factory→counter) | native + anchor |
| 9 | `9-common-bugs` | Security / CTF | 4 exploits | native only |

**Sequencing logic / prereq graph.** Two backbones run in series:

1. **Concept spine (module 2)** walks the Solana DAG in dependency order:
   `ethereum-and-solana → accounts → programs-transactions-and-instructions → pda → cpi → idl`.
   This is the classic *Accounts → Programs → PDAs → CPIs* prerequisite chain
   (cf. `references/solana-syllabus-dag.md`), preceded by an EVM-anchored map-from-known lesson.
2. **Artifact ladder (modules 3–8)** escalates the *build*:
   `hello (empty program) → oracle (single-account state + auth) → piggy (PDA that holds & releases
   SOL) → auction (SPL token transfers, ATAs, time-based pricing) → amm (multi-account DeFi, LP
   shares, swap math) → cpi (program-invokes-program + IDL import)`.
   Each rung introduces exactly one new mechanism, and each new concept is *pre-taught* by a short
   theory lesson at the top of the module (e.g. `5-piggy-bank/2-transfer-sol` before the piggy
   exercises; `6-dutch-auction/2-spl-token` + `3-spl-token-cli` before the auction exercises).

Module 9 is a distinct late tier that depends on build fluency (you cannot exploit code you can't
read/write) — it reuses the `oracle` and `piggy` programs as vulnerable targets.

## 3. Lesson anatomy

There are **two distinct lesson templates**, not one. This is the single most important structural
fact for a designer to copy.

**Template A — Concept lesson** (e.g. `2-core-concepts/3-accounts`, `.../5-pda`,
`2-ethereum-and-solana`, `3-hello-program/2-program-id`):

```
# Single H1 title (no frontmatter, no objectives block)
Intro paragraph — states the "golden rule" / one-sentence thesis
## Anatomy / mechanism        — the struct, the formula, the fields, broken down field-by-field
## Why it matters / benefits  — enumerated (Security / Hashmap / Determinism …)
## Worked concrete example(s) — Alice/Bob scenarios with literal Rust structs & byte values
## Technical deep dive        — optional; the "bump & Ed25519 curve" layer for PDA
## Summary / Key Takeaways     — bulleted recap
(Frequently) a Markdown comparison table (Ethereum | Solana) as the closing artifact
```

Always present: thesis → mechanism → summary. Optional: deep-dive section, comparison table,
`> Developer Note` callouts. These lessons are read-only — no in-page code-along.

**Template B — Exercise README** (e.g. `3-hello-program/4-native-exercises`,
`5-piggy-bank/3-native-exercises`, `7-amm/3-anchor-exercises`):

```
# <Project> (<Native|Anchor>)
1-3 sentence spec of what the program must do
"Complete all tasks below" checklist (Build · Test locally · Deploy local · Deploy Devnet)
# Task 1 - Implement `instructions::<x>` (LINK to the exact file in the Cyfrin repo)
   - bulleted acceptance criteria ("Check dst signed", "Check amt > 0", …)
   - fenced code SNIPPETS for the load-bearing lines (invoke_signed, require!, borrow_mut_lamports)
# Task 2 … (same shape)
# Build   → `cargo build-sbf` / `anchor build`
# Test    → `cargo test -- --nocapture` / `anchor test`
# Test with script → run validator, deploy, `cargo run --example demo $KEYPAIR $RPC $PROGRAM_ID`
# Deploy to Devnet (native only for hello) + `solana program close` to reclaim SOL
```

The README is a **spec + partial-scaffold pointer**, not a worked example: the actual starter code
(with TODOs) and reference `solution/` live in the external monorepo (`apps/<name>/native/exercise`
vs `.../solution`, structure diagrammed in `1-course-intro/3-course-setup`). The code snippets in
the README are the *hint layer* — enough to unblock, not the whole file.

**Template C — CTF lesson** (module 9, all four ~22 lines, e.g. `2-missing-signer-check`):

```
# <bug name>
2-3 sentences: the program's intended invariant + "there is a bug… find it and <exploit goal>"
# Task 1 - Write your exploit  (link to apps/ctf/<class>/exercise/tests/test.rs)
# Build / # Test — "Your exploit is successful if the test passes."
```

## 4. Content sequencing & pacing

- **Strictly linear, prerequisite-ordered.** Progression is the numeric directory ordering; each
  lesson presupposes the previous one. No per-lesson time budget or duration is encoded anywhere in
  the corpus — pacing is expressed through content **grain** (below), not a clock.
- **The only explicit "loop" prescribed is a learning *method*, not a schedule** — the
  **"Verify and Fix" AI workflow** in `2-course-intro`: Prompt AI → expect broken/deprecated code →
  ask it to fix → *"The actual learning occurs in step 4"* when you fix its hallucination against
  official docs. This is Cyfrin's pacing philosophy in miniature: friction is the feature.
- **Pacing is enforced by artifact difficulty, not by time.** Exercise scope ramps sharply:
  `hello` has 0 implementation tasks (just build/deploy the given program); `oracle` has 2 tasks;
  `piggy` 2 tasks but with PDA creation + manual lamport math; `auction` (native) has **3 tasks
  with ~10 acceptance checks each**; `amm` has 4 instructions (init_pool/add/remove/swap).
- **Scaffolding fades across the ladder.** Early READMEs paste near-complete code blocks
  (piggy native shows the full `invoke_signed`); later ones (`amm`) drop to bullet specs with **no
  code** ("Calculate user shares to mint", "Transfer amount_a from user into pool_a"). Classic
  fade.

## 5. Learning artifacts & practice

Practice is embedded as **runnable test-passing and deployment tasks**, escalated in tiers — the
exercises make the learner *build, run, and pass* code, never answer multiple-choice in the markdown.

1. **Unit tests (LiteSVM)** — native exercises say "Test locally with LiteSVM"; `cargo test --
   --nocapture` must pass.
2. **Localnet integration** — deploy the `.so` to `solana-test-validator`, then run a provided
   **Rust demo script** (`cargo run --example demo $KEYPAIR $RPC $PROGRAM_ID`) that drives the
   program end-to-end.
3. **Devnet deploy** — `hello` explicitly goes to Devnet and checks the tx on Solana Explorer,
   then `solana program close` to reclaim rent. A real on-chain "run it for yourself" task.
4. **Anchor track** — `anchor test` (Rust test template, `anchor init --test-template rust`).
5. **CTF exploit challenge (module 9)** — inverted: *"Your exploit is successful if the test
   passes."* You write an attack in `tests/test.rs`; a green test = you broke the program.
6. **Quizzes** — a quiz slot exists per module (`*/N-quiz/+page.md`) but is an empty `---` stub in
   this corpus; the actual quiz is an interactive platform component, not present in these files.

No autograder is embedded in the markdown — **the test *is* the grader, run by the student.** Every
artifact is a runnable task (build, test, deploy, exploit), not a passive checkpoint.

## 6. Pedagogical devices

Mapped onto the house pattern vocabulary (`patterns/*.md`):

- **build-it-twice — the defining signature, applied at ladder scale.** Every one of the 6 build
  projects is implemented in *both* native `solana-program` and Anchor
  (`*-native-exercises` + `*-anchor-exercises` dirs). `2-course-intro` states the rationale
  verbatim: native is *superior for education* (see what Anchor hides), Anchor is *superior for
  shipping*. **Note the deliberate deviation:** `patterns/build-it-twice.md` warns to apply the
  twice-build to only *1–2 artifacts*; Cyfrin applies it to **all 6 rungs**. That is a bet that the
  audit-oriented audience wants the low-level contrast every single time.
- **concept-spine** — module 2 is a textbook dependency-ordered backbone
  (accounts→programs→pda→cpi→idl), each concept grounded with literal structs/byte-values and a
  closing recap.
- **map-from-known** — `2-ethereum-and-solana` opens the spine with a 5-axis EVM↔Solana comparison
  (language, coupled-vs-decoupled state, sequential-vs-parallel, gas-vs-rent, immutable-vs-upgrade),
  and EVM analogies recur ("Anchor ≈ Hardhat/Foundry", "lamports ≈ wei", "compute budget ≈ gas").
  EVM experience is a stated prereq specifically to power this device.
- **challenge-ladder** — modules 3–8 are escalating self-contained builds on a shared monorepo
  scaffold, one new mechanism per rung, `solution/` provided as a resource.
- **security-epoch** — module 9 is the late, distinct, offense-first hardening tier: vulnerable
  program → write exploit → (patch implied) → named class. Classes covered: **missing signer,
  missing authorization, missing PDA check, missing rent cleanup** — a direct subset of the syllabus
  DAG's vuln list.
- **overview-lab-challenge** — present but *thin*. The concept lesson is the "overview," the
  exercise README is the "challenge," but the guided middle ("lab") is outsourced to the video +
  the pasted hint-snippets rather than an in-text code-along.

**Named devices not fully covered by the house patterns:**

- **Adversarial-AI loop ("AI as a broken pair-programmer")** — the "Verify and Fix" workflow that
  *expects* the LLM to emit broken/deprecated code and makes fixing-against-docs the learning
  event. A deliberate meta-skill device rarely seen in other courses.
- **README-as-lesson / repo-tethered exercise** — the written unit is a task checklist that *links
  into* an external monorepo (`exercise/` + `solution/` + per-app `README.md`), rather than
  embedding the full artifact. The transcript is intentionally incomplete without the repo.
- **Proof-escalation ladder** — LiteSVM unit test → localnet + demo script → Devnet deploy, a
  graduated authenticity ramp within a single exercise.

## 7. Scaffolding & tooling

- **Env setup (`1-course-intro/3-course-setup`)** pins exact versions: **Rust 1.87.0, Solana CLI
  3.0.10/3.0.13, Anchor 0.31.1** (note: **Anchor 0.31**, *not* the Anchor 1.0 the repo's own
  `.claude/rules/anchor.md` describes — the course predates that). Setup covers `solana config`,
  file-system wallet (`solana-keygen new`), `solana airdrop`, and running `solana-test-validator`.
- **Monorepo layout (diagrammed in setup):**
  `repo/apps/<app>/{anchor,native}/{exercise/,solution/,README.md}` — students write in
  `exercise/`, compare against `solution/`, follow the per-app `README.md`.
- **Test harnesses, per track:**
  - Native unit tests: **LiteSVM** (`cargo test -- --nocapture`) — in-process, no validator.
  - Native integration: **`solana-test-validator`** + Rust `examples/demo` script.
  - Anchor: **`anchor test`** with the **Rust test template** (`--test-template rust`), plus
    `anchor keys sync` / `anchor clean` for the "sometimes tests fail, reset it" foot-gun.
  - Module 6 adds the **SPL Token CLI** (`spl-token create-token / create-account / mint`) taught
    hands-on before the token program is built.
- **Build:** `cargo build-sbf` (native) vs `anchor build` (Anchor). Deploy: `solana program deploy`
  vs `anchor deploy`. Cleanup: `solana program close` to reclaim SOL is taught as routine hygiene.
- **In-browser:** none. Everything is local CLI. No embedded autograder — the test *is* the grader,
  run by the student.
- **AI is explicitly part of the toolchain** (ChatGPT/Claude), framed as an unreliable assistant to
  be corrected against official docs — not banned, not trusted.

## 8. Voice & framing

Register: **plain-spoken, engineering-mentor, EVM-translator.** Concepts are introduced thesis-first
("**All data on Solana is stored in accounts**"), then dismantled field-by-field with literal values,
then re-summarized. Heavy use of Alice/Bob concrete scenarios showing real struct contents. The
motivation is repeatedly *"learn the hard way so you understand what the framework hides"* — pain is
positioned as pedagogy.

Illustrative (one sentence): *"While Anchor is superior for shipping products, the Native approach is
superior for education."*

## 9. Distinctive signatures

What this course does that the others don't:

1. **Twice-build on *every* rung.** Not a one-off "look under the hood" detour — a parallel native
   track and Anchor track for all 6 projects, a structural commitment most courses avoid for cost.
2. **Audit-first justification of the native track.** The stated reason to suffer raw
   `solana-program` is to serve **security auditors / bug hunters**, and the course pays that off
   with a dedicated **CTF module 9** where you *write exploits*, not patches.
3. **Proof-by-exploit inversion.** "Your exploit is successful if the test passes" flips the normal
   green-test-means-correct convention.
4. **Repo-tethered, deliberately-incomplete transcripts.** The written lessons link into
   `github.com/Cyfrin/solana-course` rather than embedding full code; the markdown is a companion,
   not a standalone book. Exercise READMEs are spec + hint-snippet, with `solution/` as a safety net.
5. **The "Verify and Fix" AI doctrine** as an explicit, named learning method — a stance on LLMs
   baked into lesson 1.
6. **Full DeFi payoff rung.** The ladder culminates in a real **constant-sum AMM** with LP-share
   minting/burning and fee'd swaps (`7-amm`), and a **program-composition** rung using
   `declare_program!` to import a counter's IDL and CPI into it (`8-cpi-idl`).

## 10. Takeaways for a course designer

1. **Steal the dual-track for an audit audience — but scope it deliberately.** Native+Anchor on
   every rung is powerful *only* because the stated outcome is "understand what Anchor hides / be
   able to audit." If your outcome is "ship fast," follow `build-it-twice.md`'s advice and twice-build
   only 1–2 artifacts; Cyfrin's all-rungs bet is expensive and beginner-hostile.
2. **Steal the two-template split.** Read-only **concept lessons** (thesis → field-by-field
   mechanism → Alice/Bob values → recap) cleanly separated from **exercise READMEs** (spec → linked
   TODO tasks → hint-snippets → tiered proof) is a clean, repeatable shell. Keep concept and build in
   different lesson *types*, not mashed together.
3. **Steal the proof-escalation ladder.** LiteSVM unit test → localnet + demo script → Devnet deploy
   gives graduated authenticity and a real "it's on-chain" moment cheaply. Bake `program close`
   (reclaim rent) in as hygiene.
4. **Steal the offense-first security capstone.** A late CTF tier where the learner *writes the
   exploit* (green test = you broke it) is more memorable than a checklist and directly serves
   the audit persona. Gate it behind build fluency (module 9, not module 2).
5. **Steal map-from-known as the on-ramp.** One EVM↔Solana comparison lesson up front, then recurring
   analogies, is a high-ROI accelerant *when EVM is a real prereq* — and Cyfrin makes it a prereq on
   purpose. Don't force it on true beginners.
6. **Steal the "AI as broken pair-programmer" doctrine.** Naming a Verify-and-Fix loop turns the
   inevitable LLM usage into a debugging exercise instead of a copy-paste crutch.
7. **Avoid the transcript-repo gap for self-study.** The markdown is unusable without the external
   monorepo and the video; if you want a *standalone* written course, embed the starter code and
   expected output inline rather than linking out.
8. **Avoid empty scaffolding slots masquerading as content.** Quiz routes here are 3-byte `---`
   stubs and inter-module interstitials are 2-line placeholders — fine for a video platform, but if
   the written artifact must stand alone, either fill those slots or drop them.
