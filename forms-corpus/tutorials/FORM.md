# Form: Tutorial (Solana ecosystem)

Original pattern analysis for a writer who wants to produce one. Grounded in 51 Solana
Foundation **guides** and 54 **cookbook recipes** captured verbatim under
`exemplars/`, plus a curated catalog of external tutorials (see `catalog.md`).

---

## 1. Definition & scope

A **tutorial** drives a reader from zero to a **working artifact** via ordered, testable
steps, in one sitting. The defining test: at the end the reader has *run the thing* — a
deployed program, a minted token, a transaction confirmed on an explorer. Remove the
artifact and you have an essay; stretch it across modules and you have a course.

In Solana practice the form splits into two clearly different sub-forms, both captured here:

- **Guide-tutorial** (the 51 `guides/`): a narrative build. Prose scaffolds each step,
  one new concept is introduced where it bites, and the piece usually ends deployed to
  devnet with an explorer link. Median ~1,390 words. Examples:
  `guides/local-rust-hello-world.md`, `guides/how-to-create-a-token.md`,
  `guides/full-stack-solana-development.md`.
- **Cookbook-recipe** (the 54 `cookbook/`): a single-task reference answer to "how do I
  X?" — near-zero preamble, one or two copy-paste code blocks, minimal prose. Median ~235
  words, code-to-prose ~10:1. Examples: `cookbook/wallets__create-keypair.md`,
  `cookbook/tokens__transfer-tokens.md`, `cookbook/accounts__create-pda-account.md`.

**How it differs from adjacent forms.** vs **walkthrough**: a walkthrough tours an *already
finished* reference repo (the code exists; you explain it); a tutorial has the reader
*build* it step by step. vs **cookbook-recipe**: a recipe is a lookup snippet with no
learning arc — no "what you'll build," no trade-off, no exercise. vs **blog-post/essay**:
those argue or explain a concept and can end with the reader merely *understanding*; a
tutorial fails if nothing runs. vs **course**: a course sequences many tutorials with
assessment; a tutorial is a single self-contained sitting.

**When a writer should choose it.** Pick a guide-tutorial when a developer needs to *learn
by building* a concrete thing (a token, a PDA vault, a wallet-connected dApp) and you can
get them to a runnable checkpoint. Pick a cookbook-recipe when the reader already knows the
concept and just needs the exact 15 lines to do one task. If the reader needs to understand
*why* before *how*, write an essay/post and link the tutorial from it.

---

## 2. Structural anatomy

### Guide-tutorial skeleton (recurring, in order)

1. **Frontmatter** *(required)* — YAML: `title`, `description`, `difficulty`
   (`intro | beginner | intermediate | advanced`), `tags[]`, usually `date`, sometimes
   `keywords[]`, `altRoutes[]`. Grounded in `guides/how-to-cpi.md`,
   `guides/local-rust-hello-world.md`.
2. **Context hook** *(required)* — 1–3 sentences of felt problem or plain framing, never
   "In this tutorial…". `local-rust-hello-world.md` opens "Rust is the most common
   programming language to write Solana programs with." `how-to-cpi.md` opens by naming
   three equivalent implementations you'll meet in the wild.
3. **What you'll build / what you need** *(recommended)* — an artifact-in-one-sentence and
   honest prereqs. Often a `## What you will learn` bullet list (used literally in only 4
   of 51, e.g. `hello-world-in-your-browser.md`, `full-stack-solana-development.md`) and/or
   a prerequisite `<Callout type="caution">` linking the install guide.
4. **Starter / environment** *(optional)* — a Solana Playground link or a repo to fork so
   the reader starts from a known-good state (`how-to-cpi.md` links a `beta.solpg.io`
   starter). Zero-install on-ramp is a strong Solana convention.
5. **Numbered / imperative step sections** *(required, the spine)* — 4–11 `##` headings
   that are **verb-first task names**, not concept names: "Install Rust and Cargo", "Run
   your localhost validator", "Create a new Rust library with Cargo", "Build your Rust
   program", "Deploy your Solana program". Each step: short prose → one code/command block →
   what to expect. Footguns flagged inline with `<Callout>`.
6. **Run it / expected output** *(required)* — the moment it works, with the literal output
   shown. `local-rust-hello-world.md` shows the `Program Id: EFH95f…` line and a
   Congratulations callout with an explorer link.
7. **Deploy to devnet** *(common)* — promote from localhost to a public cluster so others
   can see it. Nearly universal in program guides.
8. **Next steps / further reading / conclusion** *(recommended)* — 18 of 51 guides carry a
   `## Next steps`, `## Conclusion`, or `## Further reading` list of doc links.

Skill's own recipe adds two beats the exemplars *underuse*: an explicit **trade-off**
("what this costs, when not to use it") and a **do-it-yourself exercise**. Foundation
guides rarely include either (see §8).

### Cookbook-recipe skeleton (recurring, in order)

1. **Frontmatter** — `title`, `sidebarSortOrder`, `description`. No `date`, no `difficulty`,
   no `tags`.
2. **One-paragraph framing** — what the task is and when you'd need it
   (`accounts__create-pda-account.md`: PDAs "can only be created on-chain…").
3. **Code block(s)** — often split by a `## Program` / `## Client` pair for on-chain
   examples, or a `<Tabs>` toggle for `web3.js v2` vs `v1`. Frequently *just the code* with
   no `##` headings at all (`tokens__transfer-tokens.md`,
   `programs__cross-program-invocation.md` have zero H2s).
4. **Optional inline comment output** — expected values shown as `// ...` comments rather
   than a prose "Run it".

### Reusable guide template

```markdown
---
title: "How to <verb> <artifact> on Solana"
description: "One sentence: what the reader builds and why."
difficulty: beginner
tags: [rust, anchor, spl-token]
---

<1–3 sentence hook: the felt problem — NOT "In this tutorial…">

## What you will learn
- <bullet>  - <bullet>  - <bullet>

<Callout type="caution" title="Prerequisites">Toolchain + versions + zero-install link.</Callout>

## <Verb-first step 1>
<why> ```shell / ```rust filename="lib.rs"
<expected result of this step, testable before step 2>

## <Verb-first step 2>
… (one new concept per step)

## Run it
```shell …```    <literal expected output>

## Deploy to devnet
```shell solana program deploy … --url devnet```

## The trade-off        <!-- skill wants this; add it -->
## Do it yourself       <!-- unguided extension + acceptance check -->
## Next steps
- <doc link>  - <doc link>
```

---

## 3. Length, density & format

Measured over the captured exemplars:

| Metric | Guide-tutorial (n=51) | Cookbook-recipe (n=54) |
|---|---|---|
| Word count median | ~1,390 | ~235 |
| Typical band | 800–2,500 | 90–520 |
| Range | 55 – 8,877 | 89 – 1,302 |
| `##` step sections | 4–11 | 0–3 |
| Code : prose (non-blank lines) | ~1.5–2.1 : 1 | ~10–13 : 1 |

- **Guide band matches the skill's 800–2,500.** The core buildable guides cluster
  1,200–2,200 words (`how-to-create-a-token.md` 1,612; `hello-world.md` 2,028;
  `transfer-fee.md` 2,067). Outliers are multi-part builds: `full-stack-solana-development.md`
  6,805 and `cash-app.md` 8,877 read more like mini-courses.
- **Code presentation.** Fenced blocks carry a language *and* a filename:
  ` ```rust filename="lib.rs" `, ` ```ts filename="cpi.test.ts" `. Line-highlighting
  (`{14}`, `{24-37}`) and regex highlights (`/sender/ /recipient/`) draw the eye to the
  diff that matters — a Foundation-docs house style worth copying.
- **Language mix.** Guides: `shell` (153 blocks), `rust` (138), `javascript`/`js` (180
  combined), `ts`/`tsx`/`typescript` (91), `toml` (11). Cookbook: `typescript` dominates
  (66 blocks) with `rust` (14) for on-chain snippets. Client-side Solana content is
  TypeScript-first; program content is Rust.
- **Visuals are light** (matches skill default). Screenshots are rare and purposeful — e.g.
  `how-to-cpi.md` embeds one transaction-details PNG. No architecture diagrams in the step
  body; the "diagram" is the code and the explorer screenshot of the result.
- **Callouts** are the main texture device: `<Callout type="caution|success|...">` for
  footguns/wins, `<Tabs>/<Tab>` for SDK-version splits. Heading style is sentence-case,
  imperative, `##` for steps and `###` for sub-steps.

---

## 4. Voice, framing & conventions

- **Register:** second person, imperative, present tense. "Add the `solana-program`
  crate…", "Open your `src/lib.rs`…". Encouraging but terse; celebratory beats at
  checkpoints ("Congratulations! You have successfully…").
- **Hook convention:** state the problem or plain context in one or two sentences and move.
  The exemplars almost never write "In this tutorial we will…"; they name the thing and
  start (`how-to-cpi.md`, `local-rust-hello-world.md`).
- **Concepts introduced at point of use.** PDAs, CPIs, accounts, bumps, CU are defined the
  moment the step needs them, usually with an inline doc link, not front-loaded. A CPI
  guide explains "calling another program's instruction inside our program" *right before*
  the `invoke` call, with an analogy (`cross-program-invocation.md` uses Uniswap's `swap`).
  EVM-relative framing is common for onboarding devs.
- **Addresses & IDs** are shown as literal base58 in code (`declare_id!("9AvUN…")`), and the
  reader is told to swap in their own (`YOUR_PROGRAM_ID`). Program IDs are pinned in the
  snippet, never hand-waved.
- **Code norms:** every command/API is grounded and runnable; expected output is shown
  after it; blocks carry filenames so the reader knows *where* code goes; version-pinning is
  called out explicitly (see §6).
- **Citation/link norms:** inline links to `/docs/...`, to the live explorer
  (`explorer.solana.com`, `solana.fm`), and to a Solana Playground starter/reference. A
  "Next steps / Further reading" list of doc links is the standard closer.

Illustrative open-licensed quote (from `guides/local-rust-hello-world.md`, Solana Foundation
developer-content, open repo):

> "It is highly recommended to keep your `solana-program` and other Solana Rust dependencies
> in-line with your installed version of the Solana CLI."

---

## 5. Cadence & distribution

- **Primary home:** the docs site. Guides render at
  `solana.com/developers/guides/<category>/<slug>` (categories: `getstarted`, `dapps`,
  `token-extensions`, `games`, `javascript`); recipes at
  `solana.com/developers/cookbook/<area>/<slug>`. Source lives in the (now archived)
  `solana-foundation/developer-content` repo — community-editable via PR.
- **Third-party homes:** developer-relations blogs run the same form as marketing +
  education — **Helius** (`helius.dev/blog`), **QuickNode Guides**
  (`quicknode.com/guides`), **Chainstack**, plus independent sites (RareSkills, Loris
  Leiva, the Anchor Book). These pin an RPC/tooling vendor and often ship a companion repo.
- **Cadence & series.** Docs guides are evergreen and version-maintained rather than dated
  drops; vendor blogs publish weekly-ish and build **numbered series** ("…Part 1 / Part 2",
  QuickNode's Anchor series; RareSkills' "60 Days of Solana"). Token-extension guides form a
  natural family (one guide per extension: transfer-fee, transfer-hook, metadata-pointer,
  non-transferable…) — a good template for building a cadence: pick a surface area, ship one
  tight tutorial per feature.
- **Promotion:** X threads and newsletters point at the long-form; the tutorial is the
  destination, the thread is the teaser. Timely tutorials (a new Agave/Anchor release, a new
  token extension) get a launch push; evergreen quickstarts get steady search traffic.

---

## 6. Solana-specific conventions

- **Version pinning is a first-class step.** Guides tell readers to match
  `solana-program`/`anchor-lang` to the installed CLI (`cargo add solana-program@"=2.0.3"`)
  and call out breakage across versions. State the Anchor/Agave versions you wrote against —
  Solana's toolchain moves fast enough that an unpinned tutorial rots in months.
- **Cluster framing: localhost → devnet → (rarely) mainnet.** The standard arc runs
  `solana-test-validator` + `solana config set --url localhost`, then a `--url devnet`
  redeploy so the artifact is publicly viewable. Mainnet is gated behind explicit warnings;
  tutorials default to devnet and airdrop test SOL (`requestAirdrop`, faucets).
- **Zero-install on-ramp: Solana Playground** (`beta.solpg.io`). Browser-based build/deploy
  and prebuilt starter/reference links let a reader run everything before installing a
  toolchain — the ecosystem's answer to setup friction.
- **SDK-version duality.** Client tutorials must handle `@solana/web3.js` v1 vs
  `@solana/kit`/web3.js 2.0. The house pattern is a `<Tabs>` toggle showing both
  (`cookbook/wallets__create-keypair.md`). New tutorials should lead with kit/2.0 and keep
  v1 as the compatibility tab.
- **Program IDs & PDAs.** Show `declare_id!` literally; derive PDAs with
  `findProgramAddressSync`/`PublicKey.findProgramAddress` and explain the bump; where the
  project's own rules apply, store the canonical bump rather than recomputing.
- **Test-harness mentions.** The modern convention names in-process harnesses —
  **LiteSVM**, **Mollusk**, **Bankrun** (`guides/testing-with-jest-and-bankrun.md`) — over
  the slow `solana-test-validator` for unit tests, and **Surfpool** for mainnet-fork
  integration. A tutorial that ships tests signals production-readiness.
- **Security caveats inline.** Flag reinit risks (`init_if_needed`), unchecked arithmetic,
  missing owner/signer checks, and airdrop/mainnet confusion *at the step where they bite*,
  via a `<Callout type="caution">`, not in a trailing disclaimer.

---

## 7. What good looks like — checklist

- [ ] **Hook, not preamble** — opens on the felt problem/artifact; no "In this tutorial…".
- [ ] **Artifact named in one sentence** early, plus honest prerequisites and toolchain.
- [ ] **Every step is verifiable before the next** — a stuck reader knows exactly *where*.
- [ ] **One new concept per step**, defined at point of use; nothing front-loaded.
- [ ] **Run it moment** with the literal expected output shown (program ID, tx sig, logs).
- [ ] **Every command/API/version grounded** and runnable as written.
- [ ] **Versions pinned** (Anchor/Agave/CLI) and stated up front.
- [ ] **Cluster path explicit** — localhost/devnet default, mainnet gated with a warning.
- [ ] **Footguns flagged inline** where they bite (callouts), not in a trailing note.
- [ ] **Code blocks carry filenames**; the reader always knows where code goes.
- [ ] **Zero-install on-ramp offered** (Playground or fork) when feasible.
- [ ] **Trade-off named** — what this approach costs, when not to use it. *(often missing)*
- [ ] **Do-it-yourself extension** with an acceptance check. *(often missing)*
- [ ] **Next steps / further reading** links to deepen or continue.
- [ ] **Tests or a verification method** shown, ideally LiteSVM/Mollusk/Bankrun.

---

## 8. Alignment with the edu-content skill

Skill definition read: `skills/edu-content/forms/tutorial.md`.

**Where practice CONFIRMS the skill:**
- The core definition — "one sitting, one buildable artifact, from zero to working" — is
  exactly the guide-tutorials' contract. The essay/course boundary the skill draws matches
  the corpus (no artifact → essay; multi-module → course).
- The 800–2,500-word band and **light** visuals default match measured guide reality
  (median ~1,390; screenshots rare).
- Structure beats 1–4 (Hook → What you'll build + need → testable numbered Steps → Run it)
  are the dominant real skeleton, including "never 'In this tutorial…'" and one-concept-
  per-step. The skill's checklist ("every step verifiable before the next," "expected output
  shown after Run it," "version grounded") is precisely what the strong exemplars do.

**Where practice DIVERGES / the skill has a gap:**
- **The two Foundation-omitted beats.** The skill *requires* a `## The trade-off` and a
  `## Do it yourself` exercise (`exercise_spec`). Real Foundation guides almost never include
  either — they close on "Next steps" doc-links. This is a place the skill is **more
  demanding than the corpus**, and rightly so: adding a trade-off + unguided extension is a
  cheap, high-leverage upgrade. Writers should follow the skill here, not the corpus.
- **The cookbook-recipe sub-form is unmodeled.** ~235-word, ~10:1-code, arc-less "how do I
  X?" lookups are a huge, distinct slice of Solana tutorial content and don't fit the
  skill's tutorial recipe (no hook, no artifact framing, no exercise). Recommendation: the
  skill should recognize **recipe** as either a lightweight tutorial variant (a "reference
  snippet" mode that relaxes Hook/Trade-off/Exercise) or a documented non-goal, so a writer
  isn't told to bolt a Do-it-yourself onto a 15-line keypair snippet.
- **Version pinning and SDK-duality (`<Tabs>` v1/kit) aren't surfaced** in the skill's
  Solana extras beyond `prereq_toolchain`. Given how fast the toolchain rots, "state the
  versions and offer both SDK tabs" deserves to be an explicit skill convention.

Net: **confirms** the model's spine; **diverges** by (a) demanding trade-off + exercise the
corpus skips (keep the skill's bar) and (b) not covering the recipe sub-form (add a note).

---

## 9. Takeaways for a writer

- **Earn the "Run it" fast.** The whole form lives or dies on the reader reaching a
  confirmed on-chain result. Get to a checkpoint that *runs* as early as possible, then
  layer complexity.
- **Make every step independently testable.** If a reader gets stuck, the structure should
  tell them *which* step failed. One command → one expected output → next step.
- **One concept per step, defined where it bites.** Don't front-load a "background" section
  on PDAs/CPIs/accounts; introduce each the moment the code needs it, with an inline link.
- **Pin versions and say so up front.** Name your Anchor/Agave/CLI versions; use
  `@"=x.y.z"`. An unpinned Solana tutorial has a shelf life measured in weeks.
- **Default to devnet, gate mainnet, offer Playground.** Localhost → devnet with an explorer
  link is the safe, demonstrable arc; a zero-install on-ramp beats a setup wall.
- **Show code with filenames and highlight the diff.** ` ```rust filename="lib.rs" ` plus
  line/regex highlights tells the reader *where* and *what changed* — copy the Foundation
  house style.
- **Add the two beats the corpus skips:** a one-line trade-off ("costs X, don't use when Y")
  and one unguided "now add Z yourself" extension with an acceptance check. Cheapest way to
  turn a decent tutorial into a great one.
- **Know which sub-form you're writing.** A learning build wants a hook, an arc, and an
  exercise; a lookup recipe wants zero preamble and the exact snippet. Don't pad a recipe or
  strip an arc from a tutorial.
- **Ship tests.** A LiteSVM/Mollusk/Bankrun test (not `solana-test-validator`) signals the
  artifact is real and gives the reader a verification method beyond eyeballing logs.
