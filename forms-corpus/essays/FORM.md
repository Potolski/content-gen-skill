# FORM: Technical essay (Solana ecosystem)

Original pattern analysis for a writer who wants to produce a Solana technical essay.
Scope note: this covers the RESEARCH mode of the form — thesis-driven "why X" pieces
and the expository "how X works" deep-dive that dominates Solana long-form. All
verbatim-source rules observed: no external body text is reproduced here; every named
piece is a metadata catalog reference (see `catalog.md`). This document is my analysis.

---

## 1. Definition & scope

A Solana technical essay is a **standalone long-form prose argument or explanation**
whose payload is *understanding*, not a built artifact. The reader finishes able to
**defend, attack, or reason about a claim or a mechanism** — not to run a command.
That single test ("can they now argue a position / explain a mechanism?" vs "can they
now run the thing?") is what separates it from every adjacent form.

Two live sub-modes exist in the wild, and a writer must pick one deliberately:

- **Thesis essay (argument-first).** A falsifiable claim, built and defended. E.g.
  Max Resnick's *Solana Issuance from First Principles* (Anza), Helius's *The Truth
  about Solana Local Fee Markets*, Syncracy's *Solana Thesis*, Toly's *What is the
  State Growth Problem on Solana* (X longform). The spine is a chain of reasoning.
- **Expository deep-dive (concept-first).** No contestable thesis; the payload is a
  correct mental model of a mechanism. E.g. Helius's *Turbine: Block Propagation on
  Solana* and *Consensus on Solana*, Umbra Research's *Lifecycle of a Solana
  Transaction*, Anza's *The Solana eBPF Virtual Machine*. The spine is the mechanism,
  usually walked from ingress to egress.

Both are "essays" in the skill's routing sense (long-form prose, not steps, not an
artifact tour). The skill's `essay.md` models only the first sub-mode well; the second
is the majority of Solana output and needs a lighter contract (see §8).

**How it differs from adjacent forms:**

- **essay vs tutorial** — Tutorial's spine is *steps toward a buildable outcome* ("add
  priority fees to a transaction"). Essay's spine is *reasoning*. If the reader's win
  is a working thing, route tutorial. A litmus: a tutorial breaks if a step is
  reordered; an essay breaks if a *claim* is removed.
- **essay vs walkthrough** — Walkthrough tours a *specific existing artifact* (this
  repo, this program, this transaction signature) in its own order. An essay about
  the *scheduler design* is an essay; a line-by-line tour of the scheduler *source
  file* is a walkthrough. Expository essays generalize; walkthroughs particularize.
- **essay vs blog-post** — "Blog post" is a **publishing vehicle, not a form**. A
  Helius or Anza blog post can *be* an essay, a tutorial, or a walkthrough. Route by
  payload, not by the URL living on `/blog/`. The skill correctly has no "blog-post"
  form; do not invent one.
- **thread/tweet vs essay** — A tweet is a `post`. A *thread* is a `post` when it's
  3–8 self-contained units around one takeaway; it becomes an essay only when it
  carries a sustained multi-section argument (Toly's X "articles" and long research
  threads sit on this boundary — treat as essay when they have a defended thesis and
  sections' worth of evidence).
- **litepaper/whitepaper vs essay** — A whitepaper (Solana's PoH whitepaper;
  *Compressing Digital Assets with Concurrent Merkle Trees*) is an **argument+spec
  hybrid serving as a canonical primary source**: formal protocol/math sections, a
  reference role, and permanence. It shares the essay's thesis-and-evidence spine but
  adds normative spec. It's closer to a primary artifact than to educational content;
  the skill has no form for it and probably shouldn't grow one (see §8).

**When to choose it.** Choose essay when the win is a *changed mind or a built mental
model*: a contestable "why/should/what-is", a mechanism people keep getting wrong, an
economic or design trade-off, a state-of-the-network argument, a post-mortem's
lessons. Do **not** choose it when the win is a runnable result (tutorial) or a tour
of one concrete artifact (walkthrough).

---

## 2. Structural anatomy

Two skeletons, one per sub-mode. Strong pieces follow them tightly; weak ones pad.

### 2a. Thesis essay skeleton (the skill's target)

1. **Hook — the tension.** A price, an outage, a migration, a fight, a number that
   shouldn't be true. Earns the read in the first screen. (Resnick opens on issuance
   being a first-principles question nobody re-derives; Helius local-fee-markets opens
   on the gap between the promise and the lived experience.)
2. **Thesis, stated plainly and early.** One falsifiable sentence by the end of the
   first section. "X matters" is not a thesis; "X will replace Y for workload Z
   because W" is.
3. **The argument chain.** Each section advances *one link*, concrete before abstract,
   with its grounded evidence (a chart, a measured number, a code path). No section
   that doesn't move the chain.
4. **The steelman.** The best opposing case at full strength, then why the thesis
   survives — or an honest scoping of where it doesn't. This is the single most
   skipped beat and the clearest quality signal.
5. **So what.** What the reader should now do, watch, or measure differently.
6. **(Optional) Further reading / primary sources.** SIMDs, source, prior posts.

### 2b. Expository deep-dive skeleton (the Solana majority)

1. **Hook — the problem the mechanism solves.** Often a comparison ("how does a block
   reach 2,000 validators fast?") or an Ethereum contrast.
2. **Promise / roadmap.** One line on the mental model the reader will leave with.
   Optional TOC on long pieces (Helius/Umbra anchor-link their H2s).
3. **Primer / prerequisites.** Define or link the load-bearing primitives (accounts,
   leaders, slots) before using them. Explainers link to a canonical primer; they
   don't re-teach the whole account model.
4. **The mechanism, walked in causal order.** Ingress → transform → egress, each stage
   with a **diagram** for anything multi-hop (the Turbine tree, the Gulf Stream flow,
   the transaction lifecycle). This is the body.
5. **Comparison / trade-offs / limitations.** Versus Ethereum or the prior design;
   what it costs; open problems and future-research pathways (Helius pieces routinely
   close on "future research").
6. **Conclusion + Further reading.**

### Reusable template (thesis mode)

```
# {Claim as a title, or a question the title answers}

{Hook: the tension in 2–4 sentences — a number, an outage, a fight.}

## The claim
{Thesis in one falsifiable sentence. Scope it: for workload/timeframe Z.}

## {Link 1 of the argument}
{Concrete evidence first — chart/number/code path — then the inference.}

## {Link 2 …}
{Each section = one link. Cut anything that only surveys.}

## The strongest case against
{Steelman at full strength. Then: why the thesis survives, or where it narrows.}

## So what
{What to do / watch / measure now. Trade-offs named on any recommendation.}

## Further reading
{SIMDs, source, docs, prior posts — primary sources, not just other blogs.}
```

**Required vs optional.** Required in both modes: a hook that isn't throat-clearing; a
plainly stated thesis-or-promise up front; grounded evidence; named trade-offs on any
recommendation; a "so what" close. Required in thesis mode specifically: the steelman.
Optional: TOC, footnotes, appendices, "further reading" — scale to length.

---

## 3. Length, density & format

Measured against the exemplars in `catalog.md` (word counts are estimates from the
live pages):

| Sub-form / venue | Typical length | Sections | Visual density | Code |
|---|---|---|---|---|
| Thesis essay (skill band) | 1,000–3,500 words | 4–7 H2 | 1–4 load-bearing charts | rare |
| Helius expository deep-dive | 2,000–4,000 words | 6–10 H2/H3 | hero + 3–8 diagrams | light–moderate |
| Anza protocol essay | 1,500–3,500 words | 5–9 H2 | austere; charts only when load-bearing | some (VM/runtime pieces) |
| Umbra Research piece | 2,000–4,500 words | numbered sections | diagrams + footnotes | light |
| X longform (Toly/Resnick) | 300–1,200 words | no headers; paragraph beats | inline images/replies | none |
| Substack narrative (Not Boring, ry.sh) | 3,000–6,000+ words | many, story-driven | images, embeds | none |
| Whitepaper/litepaper | 3,000–8,000 words + math | formal numbered | figures, equations | pseudocode |

**Code-to-prose ratio.** Protocol/economics essays are **prose-dominant**; code is the
exception (a struct, an instruction discriminator, a fee formula). This is the inverse
of a tutorial. Security and "how to think about X" essays (Neodyme pitfalls, testing
guides) carry more code but still lead with prose reasoning. Rule of thumb: if code
blocks outweigh prose, you've drifted into tutorial territory.

**Diagrams are the essay's primary visual**, not screenshots. Any mechanism with more
than two hops earns a diagram (Turbine's fanout tree, the Banking Stage pipeline). A
single "hero" diagram near the top that the whole piece references is a common,
effective pattern. Command blocks and terminal screenshots belong to tutorials.

**Heading style.** Sentence-case or title-case H2/H3; explainer titles trend
descriptive-and-SEO ("Everything You Need to Know", "A Primer on…", "Understanding
X"); thesis titles trend claim-or-provocation ("Solana Issuance from First
Principles", "The Truth about…"). Long pieces use anchor-linked H2s as a de facto TOC.

---

## 4. Voice, framing & conventions

**Register.** Authoritative but accessible; first-person-plural "we/let's" in
explainers, first-person-singular opinion in thesis/manifesto pieces. The dominant
Solana house style (Helius, Anza, Umbra) is *engineer-to-engineer*: precise,
lightly informal, comfortable naming trade-offs, allergic to marketing gloss. Irreverent
outliers exist and land (hana's "ok so what the fuck is the deal with solana anyway").

**Hook conventions that recur:**
- The Ethereum contrast ("on Ethereum X works like this; Solana can't/doesn't").
- The surprising number or the outage ("the network stalled on date; here's the
  mechanism that failed").
- The first-principles reset ("everyone cites this parameter; nobody re-derives it").
- The named fight (a governance debate, an issuance argument, a SIMD).
Avoid: "In this article, we will explore…" and "I'm excited to share".

**Introducing Solana concepts.** Explainers **define on first use or link to a
canonical primer** — accounts, PDAs, CPIs, compute units (CU), leaders, slots/epochs.
The convention is to link the account-model / programming-model primer rather than
re-teach it, then spend the budget on the piece's actual subject. Thesis essays assume
the primitives and spend their budget on the argument. Spell out an acronym once (CU =
compute units; PDA = program-derived address) then use freely. Frame CU as the real
scarce resource behind fees; frame accounts as the unit of parallelism when relevant.

**Code presentation.** Fenced blocks with language tags; minimal and illustrative, not
runnable-end-to-end (that's a tutorial). Pin versions in prose around the block (Anchor
/ Agave version) because APIs move. Prefer a fee formula or a struct layout over a full
program.

**Citation/link norms.** Inline hyperlinks are the norm, not a bibliography.
High-signal essays link **primary sources**: SIMDs (by number), GitHub source lines,
`docs.anza.xyz`, the whitepaper PDF — not only other blog posts. Helius cross-links its
own catalog heavily (a deliberate internal-link web). Academic-leaning venues (Umbra,
Neodyme, OtterSec) add footnotes. Always date or version-stamp a load-bearing number so
it doesn't silently rot.

Register example (paraphrased, not a quote): a strong opener states the tension and the
claim in the same breath, then earns every subsequent section as a link in that chain.

---

## 5. Cadence & distribution

**Where it's published:**
- **Company research blogs** — Helius (`helius.dev/blog`, very high cadence,
  SEO-titled), Anza (`anza.xyz/blog`, lower cadence, protocol-authoritative), Jito
  (`jito.wtf/blog`), Neodyme / OtterSec (`osec.io/blog`) for security.
- **Independent research shops** — Umbra Research (`umbraresearch.xyz/writings`),
  Syncracy, Delphi.
- **Personal sites / GitHub Pages** — apfitzge.github.io, 2501babe.github.io,
  writing.ry.sh, shinobi-systems.com. Often the deepest, least-polished, highest-trust.
- **Substack / Mirror** — Not Boring, Superteam, individual authors; narrative and
  timely.
- **X longform + threads** — Toly, Mert, Max Resnick publish thesis-grade arguments
  natively on X; these are essays that happen to live in a thread/article widget.
- **PDF** — whitepapers/litepapers (`solana.com/solana-whitepaper.pdf`).

**Promotion pattern.** The essay ships, then an **X thread summarizing it** (the `post`
form doing distribution duty), author quote-tweets, reshare by the org account, often a
newsletter slot and r/solana. The thread is a teaser, not a replacement — a healthy
essay/thread pair is complementary, not duplicative.

**Series & cadence.** Recurring templated series are a Solana signature: Helius's *All
You Need to Know About Agave vX.Y* release-tracking series (timely, expires), Umbra's
*Solana Fees Part 1/2*, Sec3's *Solana Internals Part 1–4*. Building a cadence means
either (a) a release calendar (every client version) or (b) a concept ladder (fees →
fee markets → priority fees).

**Evergreen vs timely.** Evergreen: mechanism explainers (Turbine, accounts model,
transaction lifecycle, VM) — these accrue links for years. Timely: version updates,
issuance/governance debates, outage post-mortems, market-thesis pieces. Version-stamp
the timely ones so readers know the frame date.

---

## 6. Solana-specific conventions

- **Version pinning.** Name the client and version (Agave 2.x, formerly "Solana Labs
  1.x") and the framework (Anchor 0.31 vs 1.0) whenever a claim depends on it. The
  ecosystem renamed Solana Labs → Agave and moved Anchor's TS client to
  `@anchor-lang/core`; stale essays that don't pin dates read as wrong. Reference SIMDs
  by number for anything protocol-level.
- **devnet vs mainnet framing.** Less central to protocol essays; essential when the
  piece makes an economic claim (mainnet fee/issuance data) or includes code (say which
  cluster). Economic arguments should be explicit that they describe mainnet-beta.
- **Program IDs & native programs.** Cite native programs by role (Vote, System, Stake,
  BPF Loader) and, where load-bearing, by ID. Essays about scheduling/consensus lean on
  the Vote program; fee essays on the compute-budget program.
- **Test-harness mentions.** Pure protocol essays rarely touch harnesses. Essays that
  shade into "how to reason about testing/security" name **LiteSVM / Mollusk** (fast
  in-process SVM) and **Surfpool** (mainnet-fork) — and explicitly *not*
  `solana-test-validator` for unit work. If your essay recommends a testing stance,
  use current harness names or it dates instantly.
- **Security caveats.** When an essay recommends a pattern, name the footgun: avoid
  `init_if_needed` (reinit attacks), store canonical PDA bumps, checked arithmetic,
  reload accounts after CPIs, validate CPI target program IDs. Security essays
  (Neodyme, OtterSec) are structured as *pitfall → why it bites → mitigation* and
  carry an audit-not-guaranteed disclaimer. Never present an unaudited pattern as
  production-safe without saying so.

---

## 7. What good looks like — checklist

- [ ] **Thesis or promise on the first screen.** Argument mode: one falsifiable
      sentence. Expository mode: one crisp "what mental model you'll leave with".
- [ ] **Hook is a real tension** (number, outage, fight, first-principles reset) — not
      "In this article we will".
- [ ] **Every load-bearing number is grounded and dated/version-pinned** and frozen
      before writing.
- [ ] **Steelman engaged at full strength** (argument mode) — the opposing case isn't a
      strawman, and the thesis is scoped where it doesn't survive.
- [ ] **Concrete before abstract**, and a **diagram for any multi-hop mechanism**.
- [ ] **Every section advances the spine** — no survey padding, no "background" that
      isn't load-bearing.
- [ ] **Comparisons earn their place** (Ethereum/prior design) and aren't filler.
- [ ] **Primary sources linked** (SIMD numbers, source, docs) — not only other blogs.
- [ ] **Trade-offs named on every recommendation.**
- [ ] **Scope stated honestly** ("holds for workload/timeframe Z").
- [ ] **Prose-dominant** — code/diagram support the argument, don't replace it (else
      it's a tutorial/walkthrough).
- [ ] **A "so what / what to watch" close**, not a summary restatement.
- [ ] **Version- and date-stamped** so timely claims don't silently rot.
- [ ] **Human voice** — no engagement-bait scaffolds, no LLM throat-clearing.

---

## 8. Alignment with the edu-content skill

Skill form file read: `skills/edu-content/forms/essay.md` (a form DOES exist).

**Where practice CONFIRMS the skill.** The skill models the *thesis essay* sub-mode
almost exactly, and its opinionated demands are the real quality separators:
- Its structure recipe (hook → thesis → argument chain → steelman → so-what) matches
  the best argument pieces beat-for-beat (Resnick's issuance essay, Syncracy's thesis,
  Helius's local-fee-markets, Toly's state-growth thread).
- Its brief extras — **`thesis` (falsifiable)**, **`steelman` (real, not decorative)**,
  **`evidence_plan` (3–5 frozen facts)** — name precisely what weak Solana essays skip.
  Requiring a real steelman and pre-frozen numbers would raise the median piece.
- Its 1,000–3,500-word band and "light" visual default fit the thesis-essay column in
  §3 well.

**Where practice DIVERGES / a gap.** The skill's essay is defined as "thesis-driven
long-form argument… able to defend or attack a position." But the **majority of Solana
long-form is expository deep-dive** (Turbine, Gulf Stream, Consensus, Transaction
Lifecycle, eBPF VM) — concept-first, with *no contestable thesis and no natural
steelman*. Under the current model these get force-routed to `essay` (and would be
graded against a steelman they shouldn't have) or to `walkthrough` (which expects a
concrete artifact, not a generalized mechanism). Neither fits cleanly. This is the
single highest-value gap.
- **Recommendation:** add an **expository sub-mode to the essay form** — a lighter
  contract where `thesis` is replaced by a `mental_model_promise`, `steelman` becomes
  optional, and a **required diagram for any multi-hop mechanism** plus **required
  trade-offs/limitations** substitute for the steelman as the rigor anchor. Keep
  grounding/dating requirements identical. This preserves one form while stopping the
  skill from demanding a fake argument.

**Vehicles and hybrids the skill correctly does NOT form-ify:**
- **Blog post** is a vehicle; the skill rightly routes by payload. Keep it that way.
- **Thread** splits cleanly between `post` (self-contained units, one takeaway) and
  `essay` (sustained multi-section argument). The routing note in `FORMS.md` handles
  this; no change needed beyond an example on the thread↔essay boundary.
- **Whitepaper / litepaper** is an argument+spec canonical primary source, closer to a
  produced *artifact* than to educational content. **Do not add a form**; if a user
  asks for one, route the argument portion to `essay` and treat the spec as
  out-of-scope. Flag it as `no-form-covered-elsewhere`.

Net: `essay` **confirms** for the thesis sub-mode and **diverges** for the expository
sub-mode; the actionable fix is a documented expository sub-mode, not a new top-level
form.

---

## 9. Takeaways for a writer

- **Decide sub-mode before the first sentence.** Argument or explanation? The two have
  different spines (chain-of-reasoning vs mechanism-in-causal-order) and different
  required beats (steelman vs diagram+limitations). Mixing them muddies both.
- **State the thesis or the promise on the first screen, and scope it.** "X will
  replace Y for workload Z" beats "X is important". Narrow claims survive; broad ones
  get dunked in the quote-tweets.
- **Steelman for real, or you'll be steelmanned in the replies.** On Solana X the
  strongest counter-argument WILL arrive within an hour; put it in the piece and answer
  it. Skipping it is the most common failure.
- **Freeze your numbers and version-stamp them.** Grab the fee/issuance/CU figures,
  cite the SIMD, name the Agave/Anchor version, and date the frame — before you write.
  A wrong or undated number is the fastest credibility loss in this ecosystem.
- **Diagram the mechanism; don't code-dump it.** Essays are prose-dominant. If your
  code blocks outweigh your prose, you're writing a tutorial — either commit to that or
  cut the code to one illustrative snippet.
- **Link primary sources, not a blog daisy-chain.** SIMD numbers, Agave source, Anza
  docs, the whitepaper. Cross-linking only other essays reads as thin.
- **Earn the Ethereum comparison.** It's the default hook and it works — but only when
  it clarifies a real design difference, not as reflexive tribal filler.
- **Close on "so what", then ship the thread.** End with what to watch/measure/do, not
  a summary. Then distribute with a teaser thread that complements — never duplicates —
  the essay.
- **Name every trade-off on every recommendation.** The house style rewards honesty
  about costs; unqualified "just do X" recommendations read as marketing.
