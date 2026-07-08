# Content Form Analysis: The Walkthrough (Solana)

*A guided tour of something that already exists — a repo, a program, a protocol flow, a
transaction — where the reader builds nothing but comes out able to navigate and reason
about the artifact. Original analysis for a writer producing one. Evidence base: 42
open-licensed `solana-foundation/program-examples` READMEs saved under `exemplars/`
(measured), plus a cataloged set of external walkthroughs (see `catalog.md`).*

---

## 1. Definition & scope

A **walkthrough** takes an existing artifact and walks a reader *through* it along a chosen
thread. The reader does not build; they learn to **read**. The deliverable is
understanding-of-a-thing, not a working-thing. Contrast the adjacent forms:

- **Walkthrough vs tutorial.** A tutorial hands you an empty folder and ends with a program
  you built. A walkthrough hands you a program that already exists and ends with you able to
  navigate it. `exemplars/tokens/escrow/anchor/README.md` never says "type this" — it tours
  Dean Little's escrow and explains *why each account and name is what it is*. That is a
  walkthrough. `exemplars/basics/hello-solana/README.md` sits on the boundary: it explains an
  existing minimal program's transaction anatomy (walkthrough) inside a repo you can also run
  (tutorial scaffolding).
- **Walkthrough vs cookbook-recipe.** A recipe is a copy-pasteable snippet answering "how do
  I do X" (Solana Cookbook style). A walkthrough is longer-arc and *explanatory* — it answers
  "how does this X work and why is it built this way," tracing structure rather than handing
  you a paste.
- **Walkthrough vs reference / API docs.** Reference is exhaustive and unordered (every field,
  every method). A walkthrough is selective and *ordered by a vantage* — it drops the 80% that
  doesn't serve the thread.
- **The two subtypes that matter in Solana.** (a) **Repo/annotated-code walkthrough** — lives
  as a README or inline comments *next to* the code, assumes the reader has the repo open, runs
  short (see §3). (b) **Standalone article walkthrough** — a self-contained blog post or wiki
  page (Umbra "Lifecycle of a Solana Transaction," Helius "Hitchhiker's Guide to Program
  Security") that must *quote* the pinned artifact because the reader isn't looking at it.

**Choose the walkthrough when** the artifact already exists and its value is in being *read*:
a canonical reference implementation (escrow, AMM), a protocol flow the reader will integrate
against (Pyth price feeds, a CPI chain), a transaction whose bytes you want decoded, or an
attack path through vulnerable code. If the reader's win-state is "I built it," write a
tutorial instead.

---

## 2. Structural anatomy

Two skeletons appear in the corpus. Use them as templates.

### Skeleton A — Repo/annotated walkthrough (the dominant `program-examples` shape)

```
# <Artifact name>                         ← H1 = the subject, named plainly
<1-3 sentence what-it-is + why-it-matters> ← the hook is usually a problem, not a teaser
## <Concept or Design section>            ← the "why": design decisions, constraints, trade-offs
   - real code/config quoted or permalinked
## Usage / Quick start                    ← how to run it (`anchor test`, `just build`)
## Notes / Changes / Credit               ← variant caveats, provenance, follow-the-thread links
```

Observed instances:
- **Problem-framed opener.** `tokens/escrow/anchor/README.md` opens with Alice/Bob and "what
  if Bob took the USDC and ran?" — the hook is a failure mode, not marketing.
- **Design-decision core.** The same escrow README is *almost entirely* a "Changes from
  original" list: `deposit` → `token_a_offered_amount`, `Escrow` (the offer) → `Offer`. Every
  entry names a *why* (ambiguity, verb/noun collision). This is the walkthrough's beating heart:
  **why it's this way**, not just what it is.
- **Motivating sequence.** `basics/cross-program-invocation/README.md` motivates CPI with a
  numbered 4-step token-mint sequence ("we can't create metadata without first creating a
  mint") before showing any code — vantage first, code second.
- **Layout table + inventory.** `games/world-cup/pinocchio/README.md` uses a `| Path | What |`
  table, a Quick-start block, and an explicit **Accounts** + **Instructions** inventory
  (`init_config`, `submit_bracket`, `lock`, …) — the map of the tour.

### Skeleton B — Standalone article walkthrough (the skill's target shape)

1. **Hook** — why open this hood (a fee, a bug, an exploit, a design rumor).
2. **The map** — the *vantage* in one paragraph + the ordered stops. This is where a dataflow
   diagram earns its keep.
3. **Waypoints** — one section per stop. Show the real, **pinned** code/data; say what it does;
   say **why it's this way** (the design decision or constraint).
4. **The trade-off** — what the design buys and what it costs; what you'd do differently.
5. **Where to go next** — 2-3 concrete pointers deeper into the subject.

The clearest corpus approximation of Skeleton B is `tokens/token-swap/README.md` (3,561 words):
intro (what/why AMMs) → **Design** → **Principals** (explicit trade-offs) → **Code Examples**
walked instruction-by-instruction via **commit-pinned GitHub permalinks**
(`blob/419cb6b6…/instructions/swap_exact_tokens_for_tokens.rs#L33-L56`). The permalink *is* the
`subject_ref` — the tour survives even as `main` moves.

**Required parts:** named subject (H1), a vantage/what-it-is opener, at least one pinned real
artifact reference, at least one *why*. **Optional:** quick-start, layout table, provenance/
credit, variant notes, follow-the-thread links, diagram.

---

## 3. Length, density & format

Measured across all 42 exemplar READMEs (`wc -w`):

| Metric | Value |
|---|---|
| Count | 42 READMEs |
| Total words | 11,603 |
| Mean | 276 words |
| Median | ~150 words |
| Min | 5 words (framework-variant stubs that only point to the parent) |
| Max | 3,561 words (`tokens/token-swap`) |

The distribution is **bimodal and heavily short-tailed**. Most repo walkthroughs are
**50-300 words** — a title, a couple of framing sentences, a why-note, a run command. Two
outliers (`token-swap` 3,561; `token-2022/nft-meta-data-pointer` 2,258) behave like Skeleton-B
articles. The `asm/` variants (5 words each) are pure redirects to a canonical README — a real
convention: *don't re-explain per language variant; point back*.

- **Code-to-prose ratio.** For the README subtype it is *low inline* but *high by reference*:
  the prose does the explaining and the **repo itself** is the code. `token-swap` inlines almost
  no Rust — it links commit-pinned line ranges and narrates each. Standalone article
  walkthroughs invert this: they must embed the quoted snippet because the reader has no repo.
- **Format furniture.** Markdown H1/H2, fenced blocks for **commands** (`anchor test`, `just
  setup`), config (`Cargo.toml` `[features]`), and small wire-format sketches
  (`hello-solana` sketches a transaction as `signatures / message / instructions`). Tables for
  layout inventories (`world-cup`). GitHub `> [!NOTE]` / `> [!WARNING]` callouts and `:key:`
  emoji markers appear in the root README and `hello-solana`.
- **Diagrams are rare in this corpus.** The `program-examples` READMEs lean on *tables and code
  fences*, not dataflow diagrams (one CPI README embeds a decorative lever image). Standalone
  article walkthroughs (Umbra, AlmostEfficient's Excalidraw diagrams) are where real diagrams
  live — and where they pay off most.
- **Heading style.** Plain and noun-y: `## Introduction`, `## Design`, `## Usage`, `## Layout`,
  `## The program`. No clickbait.

---

## 4. Voice, framing & conventions

- **Register.** Second-person, present tense, peer-to-peer engineer. Warm but terse. The AMM
  README's "Let the exploration begin!" is at the effusive end; most are flatter
  ("This example demonstrates how to use a PDA to pay the rent…").
- **Opening convention.** Name the artifact, then state what-it-is in one sentence, then (best
  practice) a *problem*: escrow opens on counterparty risk, CPI on an ordering constraint, Pyth
  on "use prices from real-life assets in your programs." Marketing hooks are absent; the hook
  is a use-case or failure mode.
- **How Solana primitives get introduced.** Concretely and by address/type, not abstractly:
  - **Accounts** as typed state containers, often with an explicit byte-size accounting
    (`token-swap` walks `Amm::LEN` = 32 + 32 + 2, `Pool::LEN` = 8 padding + 3×32 = 104).
  - **PDAs** introduced *with their seed recipe and the reason for it* — `token-swap`'s
    "Simplicity in Seeds" advises parent-seed-then-alphabetical-identifiers.
  - **CPIs** motivated by dependency ("we can't create metadata without a mint first"), then
    shown with `CpiContext` / signer seeds.
  - **Addresses** pinned inline: Pyth's SOL/USD feed is quoted as
    `H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG`.
  - **CU / rent** framed as the cost side of a trade-off, not a footnote ("this may increase
    account rent slightly, but…").
- **Code presentation norm.** Two idioms: (a) **commit-pinned permalinks** to line ranges
  (`token-swap`) so the tour can't rot; (b) short inline fences for commands/config only.
- **Citation/link norm.** Link generously to canonical docs (Solana docs, Pyth docs, the Rust
  Book's features chapter) and **credit the upstream** when touring someone's code — escrow
  explicitly credits Dean Little's `anchor-escrow-2024` and lists its deviations.

One illustrative quote (open-licensed exemplar, `tokens/escrow/anchor/README.md`):

> "One of the challenges when teaching is avoiding ambiguity — names have to be carefully
> chosen to be clear and not possible to confuse with other times."

That sentence *is* the walkthrough ethos: the tour exists to remove ambiguity from an artifact
the reader will otherwise misread.

---

## 5. Cadence & distribution

- **Where it lives.** Repo subtype: in-repo `README.md` per example, shipped with the code and
  CI-tested (the `program-examples` root carries Anchor/Pinocchio/Native CI badges — the tour is
  *verified to still run*). Standalone subtype: engineering blogs (Helius, Anza, Jito Labs,
  QuickNode, Chainstack, Neodyme/OtterSec for security), protocol docs, personal dev blogs
  (apfitzge.github.io), and GitHub "deep-dive" repos (AlmostEfficient/transaction-deep-dive),
  often paired with a video and Excalidraw diagrams.
- **Cadence.** Repo walkthroughs grow with the codebase (contribution-driven; "if an example is
  missing, send a PR"). Article walkthroughs are episodic — commonly **series**: Sec3 "Solana
  Internals" (4 parts), Umbra "Solana Fees" (Part 1…), Neodyme's Security Workshop (levels 0-4).
- **How a series is built.** By vantage tiling: pick one thread (the transaction lifecycle,
  native programs, a vulnerability taxonomy) and split it into ordered stops, each its own post.
- **Promotion.** X threads summarizing the tour, cross-links from `awesome`-style indexes, and
  inclusion in official docs sidebars.
- **Evergreen vs timely.** Structurally evergreen *if pinned* — a commit-pinned code tour or a
  tx-signature decode stays valid. Runtime/scheduler tours (Agave banking stage, versioned
  transactions) are **timely** and rot on version bumps; they must state the version they toured.

---

## 6. Solana-specific conventions

- **Pin the subject.** The single most important convention. `token-swap` pins a commit hash
  (`419cb6b6…`) in every permalink; the skill calls this `subject_ref`. For tx walkthroughs,
  pin the **signature**; for protocol tours, pin the **program id** and cluster; for runtime
  tours, pin the **Agave/Anchor version**. Walkthroughs rot when the subject moves.
- **Framework variants are first-class.** The corpus tours the *same* artifact across
  **Anchor / Native / Pinocchio**, and the READMEs explain the deltas (`repository-layout`:
  native adds a `processor.rs` Anchor abstracts away; Pinocchio is `#![no_std]` and logs via
  `pinocchio-log`). Name the framework and version up front.
- **Devnet vs mainnet framing.** State the cluster for any pinned address — Pyth's feed is
  quoted as *mainnet*; example programs default to local/devnet test runs.
- **Program IDs & addresses quoted verbatim**, not paraphrased.
- **Test harness is part of the tour.** These READMEs name the harness as a navigation aid:
  Native/Pinocchio examples test via **LiteSVM**, Anchor via `pnpm test`; the ecosystem's
  companion harnesses are **Mollusk** and **Surfpool**. A code tour that points at the tests is
  pointing at executable documentation.
- **Security caveats belong in the tour.** The security subtype (Neodyme Workshop, Helius
  Hitchhiker's Guide, Coral `sealevel-attacks`) tours *vulnerable* code and names the fix —
  owner checks, signer checks, `has_one`, checked arithmetic, the `init_if_needed` reinit risk.
  Even non-security tours flag invariants (the AMM README walks the `xy = K` invariant re-check
  after a swap).

---

## 7. What good looks like — checklist

A writer can grade a draft against these:

- [ ] **Subject named and pinned** — commit/version/program-id/signature in the first screen.
- [ ] **One vantage stated** — a single thread (a user action, a lifecycle, an attack path)
      that orders the whole tour.
- [ ] **The map is visible early** — the ordered stops listed (table, inventory, or a diagram).
- [ ] **Every waypoint quotes something real** — pinned line range, address, or byte layout;
      no hand-waving.
- [ ] **Every waypoint names a *why*** — the design decision or constraint, not just the *what*.
- [ ] **The vantage thread survives to the end** — no detour that drops the through-line.
- [ ] **At least one explicit trade-off** — what this design buys and what it costs.
- [ ] **Cluster/framework/version disclosed** — reader knows which world this tour is valid in.
- [ ] **Provenance credited** — if you tour someone's code, link and credit the upstream.
- [ ] **Reader can rerun/verify** — a run command, test-harness pointer, or explorer link.
- [ ] **Right length for the subtype** — 50-300 words if it rides next to the repo; 1,000-3,000
      if it's standalone and must quote the artifact.
- [ ] **"Where to go next"** — 2-3 concrete follow-the-thread pointers, not a generic outro.
- [ ] **Reader builds nothing** — if there are "now type this" steps, it drifted into a tutorial.

---

## 8. Alignment with the edu-content skill

A skill form **exists**: `skills/edu-content/forms/walkthrough.md`. Real practice broadly
**confirms** its model, with one clear divergence and one gap.

**Confirms:**
- **`subject_ref` pinning.** Directly validated — `token-swap`'s commit-pinned permalinks and
  `world-cup`'s versioned layout are exactly the "pin it; walkthroughs rot when the subject
  moves" instinct.
- **Waypoints show real code + *why*.** The escrow "Changes from original" list is nothing but
  why-per-waypoint; `token-swap` walks each instruction against a pinned line range.
- **Vantage thread.** `cross-program-invocation` (hand pulls lever) and `world-cup` (submit →
  score → claim) trace a single action end-to-end, matching the `vantage` extra.
- **The trade-off beat.** `token-swap`'s "Principals" section explicitly names costs (storing
  keys raises rent; minimizing instruction scope raises LOC) — the skill's step 4, in the wild.
- **Where to go next.** `transfer-tokens` ends by pointing to `spl-token-minter` / `nft-minter`.
- **Visuals default `light`.** Matches: the corpus prefers tables + code fences, with true
  diagrams reserved for standalone tours (Umbra, AlmostEfficient) where they pay off.

**Diverges:**
- **Length band.** The skill sets **1,000-3,000 words**. That fits the *standalone article*
  subtype well, but the *dominant real practice* — the repo/README walkthrough — has a **median
  ~150 words** and clusters at 50-300. The skill's band would mis-grade a perfectly good
  annotated README as "too short."
- **Mandatory Hook.** The skill makes the Hook step 1. Many strong README exemplars open with a
  plain definition, not a hook. The hook is a blog-post convention; enforce it for Skeleton B,
  relax it for Skeleton A.

**Gap to close:** the skill treats "walkthrough" as one shape. Practice shows **two**: the
short, code-adjacent **repo/annotated** walkthrough and the long, self-contained **article**
walkthrough. Recommend the skill add a `subtype: repo | article` toggle that flexes the length
band (50-400 vs 1,000-3,000), the visuals default (tables/code vs diagram-anchored), and whether
Hook is required. Everything else in the skill's recipe holds for both.

Verdict: **confirms** (form exists and the recipe is validated), with a documented length/hook
divergence for the README subtype.

---

## 9. Takeaways for a writer

1. **Lead with the artifact and pin it.** First screen: name the thing and a commit hash /
   program id / tx signature / version. An unpinned walkthrough is a future 404 of meaning.
2. **Pick one vantage and never drop it.** A user action traced end-to-end, a lifecycle, or an
   attack path. The vantage is what makes a tour a tour instead of a reference dump.
3. **Every stop earns a *why*.** The `what` is in the code; your job is the design decision or
   constraint behind it. If a waypoint has no why, cut it or find the why.
4. **Match length to subtype, not to a target.** Riding next to the repo? 50-300 words and lean
   on the code. Standalone? 1,000-3,000 words and *quote the pinned lines* so the reader who
   isn't looking at the repo can still follow.
5. **Name at least one trade-off.** "This buys X, costs Y, and here's when I'd choose
   differently." It's the fastest signal that you understand the artifact, not just describe it.
6. **Don't drift into a tutorial.** No "now create a new folder." The moment the reader is
   building, you've changed forms. Keep them reading and reasoning.
7. **Point at the tests and the explorer.** The harness (LiteSVM/Mollusk/Surfpool) and a
   commit-pinned permalink or explorer link turn your tour into something the reader can verify.
8. **Credit the upstream.** Touring someone's code is a gift to them; link it, name your
   deviations (escrow does this well), and you inherit their credibility instead of borrowing it.
9. **Close with a thread, not a summary.** 2-3 concrete "go read this next" pointers deeper into
   the subject beat any recap paragraph.
</content>
</invoke>
