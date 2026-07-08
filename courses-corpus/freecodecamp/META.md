# freeCodeCamp — Solana Curriculum — META

Pedagogical teardown for a course designer. All claims are grounded in files under
`courses-corpus/freecodecamp/content/`, primarily the 15 lesson files in `content/curriculum/`
and `content/README.md`. This is analysis, not a content summary.

---

## 1. Snapshot

- **Provenance:** https://web3.freecodecamp.org/solana (source repo `freeCodeCamp/solana-curriculum`), listed in `content/README.md`.
- **Delivery format:** **interactive, local-first, terminal + real browser.** Not a video course, not an in-browser sandbox. Lessons run inside a dev-container / Gitpod-style workspace; the learner drives a real terminal, a real local Solana validator, and (later) a real Phantom extension in a real browser. Progress is checked by a `freeCodeCamp: Run Course` command that executes hidden JS test blocks against the workspace.
- **Scale (verified counts):**
  - **15 projects** = **10 guided `learn-*` courses** + **5 freeform `build-*` integrated projects**.
  - **528 numbered auto-graded steps** across the 10 guided courses (hello-world 56, interact 65, token 52, metaplex 51, tic-tac-toe-1 68, tic-tac-toe-2 67, deploy-to-devnet 17, client-side-1 62, client-side-2 35, mainnet 55).
  - Each `build-*` project = **1 freeform step** with a large user-story spec (5 total).
  - **1,576 hidden `js` assertion blocks** total (`grep -rF '```js'`) — the real "test surface."
  - `README.md` names only 12 projects + "More Coming Soon…"; **3 additional projects already exist** on disk (`learn-how-to-deploy-to-devnet`, `learn-how-to-build-for-mainnet`, `build-and-deploy-your-freeform-app`) — the README is stale relative to the corpus.
- **Time budget:** none published — no estimated-hours field anywhere in the files, so the step count, not a clock, is the only pacing signal.
- **Target audience:** early-intermediate developers with some Rust and JS/TS literacy who want end-to-end Solana. Not absolute-zero programmers (Rust/JS are used, not taught), but assumes no Solana knowledge.
- **Prerequisites:** basic Rust, basic JavaScript/Node, comfort in a terminal. Everything Solana-specific is taught in-course.
- **Topic scope:** the full end-to-end Solana developer path — CLI/keypairs, native `solana_program` on-chain programs, the web3.js client, SPL tokens, Metaplex NFTs, the Anchor framework (program + TS test suite), a Vite/Phantom client-side dApp, and deployment through devnet to mainnet.

---

## 2. Structural architecture

**Decomposition:** `curriculum → project → step → hidden test block`.
There is no "path/module" wrapper layer in the corpus — the 15 project files *are* the top level, and `content/README.md`'s ordered table is the syllabus.

**Two project archetypes, encoded in the filename prefix:**
- `learn-*` (10 files) — **guided, step-by-step.** A numbered sequence of `## 1 … ## N` steps, each a micro-lesson with hidden autograded tests. Heavy scaffolding.
- `build-*` (5 files) — **freeform integrated projects.** A single step containing a **User Stories** spec and one large `--tests--` battery. No step-by-step guidance; the learner architects the whole thing and the grader checks the finished artifact.

**Ordering scheme:**
- *Within a project:* strict integer step order — every step is an H2 heading that is a bare number (`## 5`, `## 6`…), terminated by a `## --fcc-end--` sentinel. Steps are **mastery-gated**: you cannot advance until the current step's tests pass.
- *Across projects:* dictated by the `README.md` project table (Section "Projects"), reinforced by explicit backward references in the prose ("Previously, you built and deployed a program … using the native `solana_program` crate. In this project, you will use the Anchor framework"). Ordering metadata proper (the platform's per-project `meta.json`) is not shipped in this corpus; the README table is the authoritative in-corpus ordering source. Tests read a `project.dashedName` variable that must equal the project directory, so each project is pinned to its own workspace folder.

**Module taxonomy (real names, in README order) — four "learn-pair → build-prove" epochs plus a deployment coda:**

| # | File | Type | Focus |
|---|------|------|-------|
| 1 | learn-how-to-set-up-solana-by-building-a-hello-world-smart-contract | learn | Solana CLI, keypairs, **native** `solana_program` on-chain program, `cargo build-sbf`, deploy to localnet |
| 2 | learn-how-to-interact-with-on-chain-programs | learn | `@solana/web3.js` client for the native program (heavily seeded: 53 seed blocks) |
| 3 | build-a-smart-contract | **build** | Freeform: native program + Node client, graded by native `cargo test` + on-chain state |
| 4 | learn-solanas-token-program-by-minting-a-fungible-token | learn | `@solana/spl-token`, mints, ATAs (37 seed blocks) |
| 5 | learn-the-metaplex-sdk-by-minting-an-nft | learn | `@metaplex-foundation/js`, NFT metadata |
| 6 | build-a-university-certification-nft | **build** | Freeform: NFT-issuance system, Token Metadata program on localnet |
| 7 | learn-anchor-by-building-tic-tac-toe-part-1 | learn | Anchor 0.28 via `avm`, accounts/constraints, program logic (68 steps) |
| 8 | learn-anchor-by-building-tic-tac-toe-part-2 | learn | Writing the Anchor TS/mocha test suite for the game (67 steps) |
| 9 | build-an-anchor-leaderboard | **build** | Freeform: Anchor program logic for a game leaderboard |
| 10 | learn-how-to-build-a-client-side-app-part-1 | learn | Vite dApp, `web3.js`, IDL-typed calls to the Anchor program (62 steps) |
| 11 | learn-how-to-build-a-client-side-app-part-2 | learn | Phantom wallet adapter, connect wallet, sign txs in-browser (35 steps, 25 manual gates) |
| 12 | build-a-client-side-app | **build** | Freeform: multiplayer messaging dApp |
| 13 | learn-how-to-deploy-to-devnet | learn | Devnet deploy, derivation-path wallet, airdrops, `anchor verify` (17 steps) |
| 14 | learn-how-to-build-for-mainnet | learn | Production build path (55 steps, 28 seed blocks) |
| 15 | build-and-deploy-your-freeform-app | **build** | Capstone: freeform — architect and ship any self-chosen Solana app end-to-end |

**Sequencing logic / prereq graph:** native program → its client → *prove* → tokens → NFTs → *prove* → Anchor program → Anchor tests → *prove* → dApp client → wallet → *prove* → devnet → mainnet → *capstone*. It walks the Solana DAG (CLI/keypairs → accounts/programs → serialization → tokens → NFTs → framework → client/wallet → deployment) but delivers concepts **just-in-time inside build steps**, not as an upfront concept module.

---

## 3. Lesson anatomy

There are **two templates** because there are two archetypes.

### 3a. Guided `learn-*` step (the atomic unit, repeated ~528×)

```
## N                              # bare integer heading = one step
### --description--               # ALWAYS. Instructions + 1 idea. May contain:
                                  #   - fenced command/code the learner runs or writes
                                  #   - <dfn title="…">term</dfn> inline glossary tooltips
                                  #   - explanatory tables (e.g. account-size byte math)
                                  #   - occasional inline image (Phantom screenshots)
### --tests--                     # ALWAYS. 1..k hidden blocks, each a human-readable
                                  #   sentence followed by a ```js assertion using __helpers
[### --seed--]                    # OPTIONAL. Canonical file injection:
    [#### --force--]              #   force = overwrite learner's file
    #### --"<path>"--             #   target path, then a code fence with full contents
[### --before-all--]              # OPTIONAL. JS setup: load a file into a global,
                                  #   normalize whitespace (e.g. global.__librs)
[### --after-all--]               # OPTIONAL. JS teardown: delete the global
...
## --fcc-end--                    # terminal sentinel closing the project
```

Always present: `## N`, `--description--`, `--tests--`. Optional: `--seed--`, `--before-all--`/`--after-all--`. **`--hints--` is never used (0 across all files)** — freeCodeCamp's hint block is absent; guidance lives entirely in the description prose.
Grounding: `learn-how-to-set-up-solana-by-building-a-hello-world-smart-contract.md` steps 1–27; `learn-anchor-by-building-tic-tac-toe-part-1.md` steps 31–34 (a full seed/before-all/after-all example).

### 3b. Freeform `build-*` project (the epoch capstone, 5×)

```
## 1
### --description--
   You need to build X.
   **User Stories**            # a numbered/bulleted executable spec — the whole assignment
   [inline data-shape snippets, e.g. struct MessageAccount { message: String }]
   **NOTES:** (paths relative to <project>/)
### --tests--                  # ONE large battery (dozens of assertions), each a labelled ```js
### --before-all--             # global.__loc = '<project-dir>'
### --after-all--              # delete global.__loc
## --fcc-end--
```

No steps, no seed, no scaffolding fade — the learner starts from a spec and a mostly empty
directory. Grounding: `build-a-smart-contract.md` (native program spec, 13-user-story battery),
`build-a-university-certification-nft.md` (client-brief framing).

---

## 4. Content sequencing & pacing

- **Grain is emergent from step count.** There is zero "week N / day N / ~X hours" framing anywhere; content advances at the learner's own pace, chunked into 528 guided micro-steps + 5 open builds. The step — one idea, one action — is the unit of progress, not a clock.
- **The gate is the pace mechanism.** Progress is **per-step mastery gating**: a step's tests must all pass before the next unlocks. The `freeCodeCamp: Run Course` command re-runs the current step's hidden tests on demand — the tightest possible feedback loop (read one idea → do one thing → run → pass → advance).
- **Macro-cadence = a repeated epoch unit.** The syllabus is four **{2 guided learn courses → 1 freeform build}** epochs (program, token/NFT, Anchor, client) followed by a **ship coda** (devnet → mainnet → freeform capstone). The freeform build is the recurring "prove it unaided" beat that closes each epoch.
- **Manual gates for un-assertable steps.** Browser/visual actions can't be auto-graded, so they gate on the learner typing `done` in the terminal. `learn-how-to-build-a-client-side-app-part-2.md` uses **25 such `done` gates** (Phantom is inherently manual); most other files use exactly 1 (the final "you're finished" step). The freeform capstone's only gate is `done`.
- **Deploy-time friction is deliberately paced in.** `learn-how-to-deploy-to-devnet.md` steps 9–11 script the real-world airdrop rate-limit dance (fail → temp-wallet workaround → transfer) as graded steps, so pacing includes waiting on the network.

---

## 5. Learning artifacts & practice

The practice embedded in every step is an **executable assertion run against the learner's real workspace and a real chain** — not a quiz. Each step's `--tests--` battery is the exercise's built-in check, and the learner's job is to make it pass. The `__helpers` API surface (usage counts across corpus) reveals five distinct assertion mechanics the exercises lean on:

1. **Filesystem/state checks** — `getFile` (385), `fileExists` (25), `getDirectory`, `readFile`: the right files exist with the right contents.
2. **Terminal-history matching** — `getLastCommand` (100), `getCWD`/`getLastCWD`, `getTerminalOutput` (31): asserts the learner *ran the exact command* (often via regex) and stood in the right directory.
3. **Source-code assertions** — regex on `getFile` output **and AST parsing via `__helpers.Babeliser` (225 uses)**. Babeliser parses JS/TS and asserts on structure — exact import specifiers, exported `const` shape, declaration presence — e.g. `learn-how-to-build-a-client-side-app-part-2.md` step 3 asserts `PhantomWalletAdapter` is imported from `@solana/wallet-adapter-phantom` and that `./wallet.js` is *not* imported. Rust is graded by regex over `lib.rs` (whitespace-normalized into globals).
4. **Live on-chain verification** — `establishConnection` + `getAccountInfo`, `getConfirmedSignaturesForAddress2`, raw `getHealth`/`getAccountInfo` curl. **13 of 15 files** assert against a running validator: program is deployed *and* `executable === true`, the program owns its data account, the deploy authority equals the learner's `wallet.json` key, at least N transactions landed. The pass condition is literally the ledger state — the on-chain verify is itself a graded learning task.
5. **Native Rust unit tests as grader** — `build-a-smart-contract.md` shells out to `cargo test <name>` (`owner_not_program_id`, `no_accounts`, `instruction_too_long`, `instruction_data_padded`, …) and asserts `test <name> ... ok`, delegating correctness checks to the program's own test suite.

**The artifacts are deliverables, not exams.** The token/NFT courses have the learner *build* real on-chain outputs — an SPL mint, a Metaplex NFT (the NFT project's output is a *simulated* university NFT the learner constructs, i.e. a built deliverable). The five `build-*` projects each yield a shippable artifact — native program, NFT-issuance system, Anchor leaderboard, messaging dApp, and a freeform capstone app — that *is* the assessment for that epoch, checked by its own `--tests--` battery rather than a separate rubric.

---

## 6. Pedagogical devices (mapped to house vocabulary + new coinages)

**Maps cleanly to house patterns:**
- **completion-loop** (`patterns/completion-loop.md`) — the dominant device. Every `learn-*` course is many tiny chapters, each = one idea + a near-complete artifact with one blank to fill, auto-checked and mastery-gated. The `--seed --force` block *is* the "pre-seeded near-complete code block"; the learner edits the signal, not the noise. This is the purest completion-loop in the corpus and it carries 528 of the ~533 steps.
- **build-it-twice** (`patterns/build-it-twice.md`) — at the **module level**, native `solana_program` (projects 1–3) vs Anchor (projects 7–9), explicitly narrated ("Previously … native … now … the Anchor framework"). The learner writes account validation and (de)serialization by hand, then watches Anchor's macros absorb it.
- **client-integration** (`patterns/client-integration.md`) — projects 2, 10, 11, 12 walk the client journey (IDL-typed calls → read state → build/send tx → Phantom connect → sign), treating the program↔client boundary as first-class. Project 11 is a textbook wallet-adapter arc.
- **overview-lab-challenge** (`patterns/overview-lab-challenge.md`) — visible at **macro grain**: the two guided courses of an epoch are the "overview + guided lab," and the `build-*` project is the "unguided challenge." The triad is stretched across whole projects rather than living inside one lesson.
- **challenge-ladder** (`patterns/challenge-ladder.md`) — the five `build-*` freeform projects form a coarse rung sequence (native program → NFT system → Anchor logic → dApp → anything), each a shippable artifact that *is* the assessment.

**Deliberately NOT used:**
- **concept-spine** — there is no upfront mental-model module. Concepts arrive just-in-time via `<dfn>` tooltips and inline tables (e.g. the account byte-size table in tic-tac-toe-1 step 32). A designer studying this course should note the bet: *momentum over model*, model back-filled by contrast (build-it-twice) rather than lecture.

**New device names to coin (not in house vocabulary):**
- **deliberate-failure step ("run it till it breaks").** The learner is *told* to run a command that will fail, and the grader asserts on the error string — `anchor test` → `assert.include(out, 'Error: failed to send transaction')` (tic-tac-toe-1 step 8); `anchor deploy` → `insufficient funds for fee`; airdrop → rate-limited (devnet steps 9–11). Teaches error-literacy and real deploy friction instead of hiding it.
- **force-seed checkpoint.** `--seed--`+`--force--` overwrites a workspace file with canonical contents. Dual purpose: (a) **divergence recovery** — a learner who broke earlier steps is silently put back on the rails; (b) **noise injection** — hand the learner 100 lines of "not relevant" game logic so they focus on the target concept (tic-tac-toe-1 step 33: "your `lib.rs` should have been seeded with all the game code … not relevant to Anchor … just a few things to fix"). Heaviest in the client/token/mainnet type-along courses (interact 53, token 37, mainnet 28 seed blocks).
- **grade-the-chain.** Assessments query a live validator for on-chain truth (executable flag, ownership, tx count) rather than trusting local files.
- **AST-structural grading (Babeliser).** Semantic code-shape assertions that survive formatting differences — stricter and less brittle than regex for JS/TS.
- **spec-story capstone.** The `build-*` "User Stories" brief as an executable assignment, often wrapped in a **client-brief frame** ("You have been contacted by Solana University to build …").
- **learn-pair → build-prove epoch.** The repeated macro unit: two guided courses then one unaided freeform build.

---

## 7. Scaffolding & tooling

- **Environment:** a pre-provisioned dev-container / Gitpod workspace with the toolchain baked in ("Solana is already installed in this environment"). One VS Code command, `freeCodeCamp: Run Course`, is the test runner and the whole UX. The task instructions call this a dev-container driven by that command; step 1 of most projects just has the learner `cd` into the project directory in a *new* terminal (the grader's own terminal is protected — "Do not change the existing terminal").
- **Starter repos:** each project is its own directory in the workspace, sometimes shipped with starter code and progressively `--seed--`ed. Later projects hand over the prior artifact ("You have been started out with the same Tic-Tac-Toe Anchor program as the last project").
- **Test harness:** a custom `__helpers` API (not a standard SVM harness). It combines filesystem access, terminal-command/-output introspection, a JS/TS AST parser (`Babeliser`), a `@solana/web3.js` RPC client (`establishConnection`), and shell-outs to `cargo test`. Assertions use `chai` (`assert.*`).
- **Real, not simulated, runtime.** The course grades against **`solana-test-validator`** (74 references) and `anchor test`, a live **Vite** dev server on `localhost:5173`, the real **Phantom** extension, and finally real **devnet + mainnet**. It does **not** use LiteSVM / Mollusk / Surfpool — a deliberate contrast to fast in-process SVM harnesses (worth flagging: builds and deploys are slow but authentic).
- **Pinned versions (dated):** Solana CLI `1.17.18`, Anchor `0.28.0` (installed via `avm`), `@solana/web3.js@1.78`, plus `@solana/spl-token` (90 refs), `@metaplex-foundation/js` (30), `@solana/wallet-adapter-phantom` (16), `yarn`. These pins are old — a designer reusing this material must re-pin.
- **Autograder location:** local/in-workspace, not in-browser. Grading is per-step and on-demand.

---

## 8. Voice & framing

- **Register:** direct, second-person, imperative-first ("Change into the … directory", "Run the `anchor test` command"). Concept is delivered in 2–5 sentence bursts immediately before the action.
- **Motivation devices:** emoji milestones at project boundaries (🚀 🧨 🌟 🎆), congratulatory closers, and a "camper" identity carried in the harness (`getCamperKeypair`).
- **Concept introduction:** just-in-time. New terms get an inline `<dfn title="…">` tooltip (e.g. *discriminator* = "a uniquely identifiable octet to help Anchor find an account") and hard facts get tables (byte-size math), never a standalone theory chapter.
- **Client-brief framing** for capstones puts the learner in a role: *"You have been contacted by Solana University to build an NFT that will be used to certify students…"* (`build-a-university-certification-nft.md`).

---

## 9. Distinctive signatures

What this course does that the others in the corpus do not:

1. **Grades against a live ledger.** 13/15 files assert on real on-chain state (deployed + `executable`, correct owner/authority, transaction counts). Proof-of-learning is the chain, not a quiz or a diff.
2. **AST-based code grading (Babeliser, 225 uses).** It can require an exact import specifier or an exported-const shape and shrug off whitespace — far beyond regex.
3. **Deliberate-failure steps.** It *assigns* commands that fail and grades the error message, teaching error-literacy and surfacing real deploy friction (airdrop rate limits, insufficient funds) as first-class curriculum.
4. **Force-seed checkpoints** that both recover divergent learners and inject "irrelevant" scaffolding so each step isolates one concept — an inverted scaffolding-fade (give the noise, edit the signal).
5. **Module-level build-it-twice** with explicit narration: hand-rolled native `solana_program` first, Anchor second, so the framework's value is felt by contrast.
6. **Ships to mainnet.** Uniquely carries the arc all the way through devnet (derivation-path wallets, `anchor verify`, airdrop workarounds) to a real mainnet build — most curricula stop at localnet/devnet.
7. **Filename-encoded pedagogy.** `learn-*` vs `build-*` is a load-bearing convention: guided-with-tests vs freeform-with-spec, alternating on a fixed rhythm.
8. **~528 mastery-gated micro-steps / 1,576 hidden assertions** — an unusually fine grain and an unusually large hidden test surface.

---

## 10. Takeaways for a course designer

1. **Steal the completion-loop grain for onboarding.** One-idea-per-step + a near-complete seed + one blank + instant auto-check is the lowest-cognitive-load on-ramp there is. It converts "where do I start" paralysis into a stream of small wins. Use it for CLI/syntax/framework-macro onboarding.
2. **Steal force-seed as a divergence airbag.** Periodically overwriting the learner's file with a canonical checkpoint means a mistake in step 12 doesn't brick step 40. It also lets you hand over boilerplate so a step teaches exactly one thing. Essential if your grader is stateful across steps.
3. **Steal grade-the-chain + deliberate-failure.** Asserting on live on-chain state makes "it works" unfakeable; assigning a command that *fails* and grading the error builds the debugging muscle every other course skips. Pair them.
4. **Steal the learn-pair → build-prove epoch.** Two guided courses then one unaided spec-driven build is a clean, repeatable macro-cadence that alternates scaffolding with transfer. The "User Stories" brief doubles as spec and rubric.
5. **Steal AST grading for client code.** For JS/TS, Babeliser-style structural assertions are more robust and more precise than regex — worth the harness investment if you grade real code.
6. **Avoid the stale-pins trap.** Hard-pinned tool versions (Solana 1.17.18, Anchor 0.28, web3.js 1.78) rot fast and quietly break the autograder. Centralize versions and budget for re-pinning; the on-chain assertions and manual `done` gates also silently rot when APIs move.
7. **Avoid over-relying on `done` gates.** 25 unverifiable "type `done`" gates in the Phantom course means a chunk of that project is honor-system, not graded. If a step can't be asserted, minimize it or find an indirect on-chain signal instead of trusting self-report.
8. **When this model fits:** a hands-on, tooling-heavy course for developers who already code, where authentic proof (real deploys) matters more than speed, and you can afford to build and maintain a custom autograder. **When it doesn't:** conceptual/non-technical courses (no concept-spine here to lean on), absolute beginners who need Rust/JS taught first, or anyone needing fast iteration (real validators/mainnet are slow — reach for LiteSVM/Mollusk instead).
