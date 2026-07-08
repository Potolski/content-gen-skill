# Form: Litepaper / Whitepaper (Solana ecosystem)

Original pattern analysis for a writer producing a protocol design document on Solana.
Structure-only study: no whitepaper prose is reproduced. Grounded in the section
skeletons of real papers (Solana, Alpenglow, Drift, Pyth) read for their outlines,
plus the docs/GitHub-native "spec" style that much of the Solana ecosystem now uses.

> Scope note: `exemplars/` for this form is intentionally empty — every source here is
> proprietary or externally hosted, so this file and `catalog.md` carry **metadata +
> original analysis only**. No verbatim body text, no illustrative quote (none is
> open-licensed).

---

## 1. Definition & scope

A **whitepaper** is a protocol's canonical design-of-record: a self-contained, citable
artifact that states a problem, proposes a mechanism, and *justifies* it with math,
algorithms, a security/adversarial analysis, and (for token protocols) an economic
model. A **litepaper** is the condensed, accessible cousin — same problem→mechanism
spine, but proofs and formal references are dropped in favour of the value proposition,
a high-level mechanism sketch, and tokenomics.

In Solana specifically the form lives on a **spectrum**, and where a project lands on it
is itself a signal:

- **Formal academic whitepaper (PDF/LaTeX).** The Solana whitepaper (Yakovenko, 2017 —
  Proof of History as a verifiable clock), **Alpenglow v1.1** (Kniep/Sliwinski/
  Wattenhofer, 2025 — Votor + Rotor, with machine-checked safety proofs), **Drift v0
  Devnet Feature Paper** (2021 — vAMM, funding, liquidations), and the **Pyth Network
  whitepaper v2.0** (2022 — pull-oracle aggregation + tokenomics). Numbered sections,
  equations, figures, a bibliography.
- **Litepaper (docs-embedded, HTML).** Marinade and Meteora publish "litepaper"-grade
  material *inside their docs sites* rather than as a standalone PDF — mechanism +
  token utility at docs-page length, few or no equations.
- **No paper at all — spec-as-code.** A large share of Solana infrastructure skips the
  PDF entirely and documents through **docs + GitHub + SIMDs + explainer blogs**: Jito
  (MEV bundles, TipRouter/NCN) lives in `docs.jito.wtf` and the `jito-solana` repo;
  **Firedancer** is a C codebase + Jump Crypto build page, never a whitepaper; Jupiter's
  "tokenomics" is a sequence of DAO/blog posts. On Solana the **SIMD** (Solana
  Improvement Document, Markdown in a GitHub repo) is the true canonical spec for
  protocol-level changes — Alpenglow is both a whitepaper *and* SIMD-0326.

**Whitepaper vs litepaper — the operational difference:**

| | Whitepaper | Litepaper |
|---|---|---|
| Job | be the reference; survive an auditor/researcher | sell the mechanism + token to users/integrators |
| Rigor | proofs, invariants, adversarial analysis | high-level, mostly prose |
| Length | ~10–40 pp | ~2–8 pp (or one docs page) |
| Refs | numbered academic bibliography | links, or none |
| Author | often named researchers | protocol/foundation, impersonal |
| Legal | disclaimer for token papers | disclaimer for token papers |

**How it differs from adjacent forms:**
- **vs essay / blog-post.** An essay argues a *falsifiable thesis* and may be
  provisional and opinionated; a whitepaper is a canonical, impersonal, exhaustive
  spec — it is the thing an essay *cites*. A blog post (Helius "What is Firedancer",
  Chainstack "Jito Explained") *popularizes* a paper; the paper is the primary source.
- **vs tutorial / walkthrough / cookbook-recipe.** No build steps, no "run this."
  It describes a system's *design and why it is safe*, not how to use it. A walkthrough
  tours an existing artifact for a learner; a whitepaper defines the artifact for a peer.
- **vs docs.** Docs are living, versioned, task-oriented ("how to stake mSOL"); a
  whitepaper is a snapshot of *rationale* ("why the delegation strategy is incentive-
  compatible"). Marinade/Meteora deliberately blur this by nesting a "litepaper" inside
  living docs.

**Choose this form when** you are launching a protocol or token and need (a) a citable
design-of-record for auditors, integrators, and sophisticated investors; (b) to justify
a *novel* mechanism whose safety is the product (consensus, oracle aggregation, AMM
invariants, liquidation engine); or (c) to anchor tokenomics and governance. Pick a
**litepaper** when accessibility and the token narrative matter more than proofs; pick a
**whitepaper** when the mechanism's correctness *is* the pitch. If you have neither novel
mechanism nor token, the Solana-native default is **docs + a SIMD or repo**, not a PDF.

---

## 2. Structural anatomy

The recurring skeleton, in order. Grounded in the read outlines of the Solana whitepaper
(§1 Introduction · §2 **Outline** · §3 Network Design · §4 Proof of History · §5 Proof of
Stake Consensus · §6 Streaming Proof of Replication · §7 System Architecture ·
References), the Drift v0 paper (Abstract · 1 Technical Overview · 2 vAMM · 3 Trading &
Order Specs · 4 Margin Methodology · 5 Funding Rates · 6 Dynamic Trading Fees · 7
Liquidations · 8 Risks · 9 Conclusion · 10 Disclaimer · 11 References), and Pyth v2.0
(mechanism → update fees → pull-vs-push → tokenomics → governance).

**Reusable template**

```
Title — "<Protocol>: <one-line claim about what it is/achieves>"
Authors · affiliation · version + date        [REQUIRED — version is load-bearing]

Abstract                    the entire paper in one paragraph; lead with the result
1. Introduction / Motivation the problem + why prior art is insufficient   [REQUIRED]
2. Outline / Roadmap         optional map of the paper (Solana §2 does this literally)
3. Background / Prior art    PBFT, constant-product AMMs, Filecoin PoRep, VDFs…
4. Core mechanism            one section PER subsystem — the meat              [REQUIRED]
   4.1 Description
   4.2 Algorithm / construction
   4.3 Verification
   4.4 Consistency / edge cases
   4.x Attacks               adversarial analysis of THIS subsystem  [WP: REQUIRED]
5. (repeat §4 per subsystem: PoH → PoS → PoRep; vAMM → Margin → Funding → Liquidations)
6. System architecture       components, instructions, account/data structures
7. Math / proofs             equations, invariants, safety & liveness theorems [WP]
8. Economic design / tokenomics  supply, distribution, vesting, fees, incentives [token papers]
9. Governance                what token holders decide
10. Security analysis / Risks  global adversarial section + trust assumptions  [WP: REQUIRED]
11. Performance / limits     network / compute / memory bounds (Solana §7.2–7.5)
12. Conclusion / Future work "current implementation" vs "future implementation"
13. Disclaimer               legal — for any token/investment-adjacent paper   [token papers]
References                   numbered [1]…[n] bibliography                     [REQUIRED-WP]
+ Figures throughout         architecture / sequence / curve / bin diagrams
```

**Required vs optional.** Universally required: **abstract**, **problem/introduction**,
**core mechanism**, and (for whitepapers) **references**. Whitepaper-required and the
thing that separates it from a litepaper: **math/proofs + a security/attacks section**.
Token papers require **tokenomics + a disclaimer**. Optional/mode-dependent: outline,
background, governance, performance-limits, future-work. Litepapers legitimately keep
only abstract → problem → mechanism → tokenomics.

**Grounding note.** The Solana whitepaper is unusual in giving a literal §2 *Outline* and
in attaching a per-subsystem *Attacks* subsection (under both PoH §4.7 and PoS §5.13).
Drift v0 shows the modern app-layer pattern: a **Technical Overview** that enumerates
on-chain **Components / Instructions / Data Structures** before the economics, and a
per-section **"Current Implementation" vs "Future Implementation"** split — a devnet-era
honesty convention. Alpenglow shows the frontier: the prose paper is backed by
**machine-checked proofs and a Rust reference implementation** in its repo.

---

## 3. Length, density & format

Measured from the read exemplars:

| Paper | Length | Sections | Figures | Refs | Math density |
|---|---|---|---|---|---|
| Solana whitepaper | ~10pp original (32pp in current re-typeset hosted PDF) | 7 top-level + ~30 subsections | 8 | 9 | heavy (hash-rate, timing, verification, network/compute/memory limits) |
| Drift v0 Feature Paper | 18pp, ToC with page numbers | 11 numbered + subsections | several (architecture) | yes | medium-heavy (funding, margin, liquidation formulas) |
| Pyth Network whitepaper v2.0 | 6pp | ~3–4 + subsections | few | yes | light–medium (aggregation, confidence intervals) |
| Alpenglow v1.1 | full academic paper (tens of pp) w/ formal proofs | many + appendices | yes | very heavy (safety/liveness theorems) |
| Marinade / Meteora litepaper | one–few docs pages | docs sections | diagrams | links | light (few or no equations) |

Patterns:
- **Format.** Whitepapers = **PDF, typeset (LaTeX/academic)**, hosted on the protocol
  domain or a university/Anza host. Litepapers = **HTML docs pages**. Protocol-level
  specs = **Markdown SIMDs** in GitHub.
- **Prose-to-math ratio.** Whitepapers carry real notation and numbered equations;
  litepapers are ~90% prose with the occasional formula. **Neither shows application
  code** — whitepapers show *pseudocode/algorithms* and *account/instruction schemas*
  (Drift lists its instruction set and data structures), not Rust.
- **Diagrams are non-negotiable.** Architecture diagrams, sequence/flow diagrams, and
  domain charts (AMM curves, Meteora liquidity **bins**, PoH sequence figures). The
  Solana paper references 8 figures; expect a figure roughly every 1–2 pages.
- **Heading style.** Academic **decimal numbering** (`1`, `1.1`, `1.1.1`). A **ToC with
  page numbers** for anything ≥ ~12pp (Drift v0 has one). An **abstract** always leads.

---

## 4. Voice, framing & conventions

- **Register.** Impersonal, third-person, declarative, present tense for mechanism:
  "the protocol finalizes…", "the AMM re-pegs when…". No "we think this is exciting."
  Named researchers appear on the byline (Yakovenko; Wattenhofer/Kniep/Sliwinski) but the
  *body* stays neutral. This is the sharpest voice contrast with the essay/blog form.
- **Opening convention.** The **abstract leads with the result/claim**, usually with a
  headline number (throughput, finality latency, confidence interval). The introduction
  then frames the problem and the prior-art gap before any mechanism.
- **How Solana concepts are introduced.** Base-layer papers *define their primitives from
  scratch* (PoH explained as a delay-function clock; Rotor explained against Turbine).
  App-layer papers *assume Solana* and reference the account model, PDAs, CPIs, and the
  **compute-unit (CU) budget** tersely, as constraints on feasibility — a DeFi paper will
  name its **oracle source (Pyth)** and justify that a mechanism fits on-chain within CU
  limits rather than re-explaining the runtime. Program IDs and account/instruction
  layouts may be listed as an appendix or an on-chain "components" section.
- **Code presentation norms.** Algorithms as pseudocode; state as struct/field tables;
  the real implementation is *pointed to* (GitHub, a SIMD), not pasted. Firedancer and
  the SIMD process are the extreme of this: the spec *is* the code + Markdown.
- **Citation/link norms.** Numbered **[n] bibliography** with cross-references to prior
  work (the Solana paper cites PBFT, Filecoin PoRep, Casper, hashgraph, etc.); internal
  cross-refs by section number ("described in Section 6"). Litepapers substitute inline
  hyperlinks.

> No illustrative quote is included: none of these papers is open-licensed, and this
> form's `exemplars/` dir holds no clean-licensed source. Characterize, never paste.

---

## 5. Cadence & distribution

- **Where it's published.** PDF on the protocol domain (`solana.com/solana-whitepaper.pdf`,
  `pythdataassociation.com/whitepaper.pdf`); an Anza/university host for research papers
  (`anza.xyz/alpenglow-1-1`, ETH Zurich disco lab); a **docs site** for litepapers
  (`docs.marinade.finance`, `docs.meteora.ag`); **GitHub** for code-native specs
  (`firedancer-io/firedancer`, `solana-foundation/solana-improvement-documents`,
  `anza-xyz/alpenglow`).
- **Versioned, not serialized.** A whitepaper is **evergreen but revised in place** with a
  version bump — Pyth v1→v2, Alpenglow v1.0→v1.1, Drift "Revision 1.1", Solana v0.8.13.
  There is no weekly cadence; you ship one per major protocol epoch.
- **Promotion pattern.** Launch = an **announcement blog + X thread** (Anza's Alpenglow
  post; Drift "Introducing v2"), then the ecosystem's **explainer layer** does the
  popularizing: Helius, Chainstack, QuickNode, Blockdaemon deep-dives, plus community
  "Whitepaper Reading Club" sessions at conferences (SBC). The paper is the seed; the
  explainers are the distribution.
- **Series/cadence.** Not a series. The closest thing to cadence is the
  **whitepaper → SIMD → reference-impl → audit → mainnet** pipeline for a single upgrade,
  and the version lineage of a single paper over years.

---

## 6. Solana-specific conventions

- **Version pinning.** Papers pin the protocol era: Solana v0.8.13; Alpenglow v1.1;
  Drift "Revision". App-layer papers implicitly target the **Agave/Anza** client era;
  Anchor is an implementation detail, usually unmentioned in the paper (it surfaces in
  the repo, not the spec).
- **devnet vs mainnet framing.** Explicitly labeled — Drift's was a **"Devnet Feature
  Paper."** Papers commonly carry a per-section **"Current implementation" vs "Future
  implementation"** split so readers can tell shipped mechanism from roadmap.
- **Program IDs & on-chain layout.** Spec-as-code is the Solana norm: papers may enumerate
  **program IDs, instruction sets, and account/data structures** (Drift §1) so the paper
  doubles as an integration reference. For protocol-level changes the **SIMD** (Markdown
  in `solana-improvement-documents`) is the canonical spec, sometimes paired with the PDF.
- **Test harness & formal verification.** The frontier convention: pair the prose with a
  **reference implementation and machine-checked proofs** (Alpenglow ships a Rust ref impl
  + formal safety proofs; consensus papers increasingly use TLA+/Stateright). Program
  papers that mention testing name the modern in-process harnesses (LiteSVM/Mollusk) and
  fork-testing (Surfpool), not `solana-test-validator`.
- **Security caveats & audits.** Whitepapers carry an explicit **attacks/risks** section
  and state **trust assumptions** (stake thresholds — Alpenglow's 80%/60% liveness modes;
  oracle-trust for DeFi). Token papers append a **legal disclaimer**. External **audits**
  are referenced from the paper or its docs.

---

## 7. What good looks like — checklist

- [ ] Title states the claim; **version + date** present and the paper is revised in
      place, not re-slugged.
- [ ] **Abstract leads with the result** (a number: TPS, finality ms, confidence interval)
      and summarizes the whole paper in one paragraph.
- [ ] Introduction names the **problem and the specific prior-art gap** before any solution.
- [ ] Each **core subsystem gets its own section** (description → construction →
      verification → edge cases), concrete before abstract.
- [ ] **Math/algorithms are explicit** (whitepaper) — invariants stated, key claims proved
      or referenced; litepaper may omit but must still be internally consistent.
- [ ] A real **adversarial/attacks section** with stated **trust assumptions** and
      failure modes — not a decorative "Security" paragraph.
- [ ] **Tokenomics** (if any) give hard numbers: total supply, distribution, vesting/unlock
      schedule, fee flows, and the incentive argument — plus a **disclaimer**.
- [ ] **Architecture and on-chain surface** documented: components, instructions,
      account/data layouts, program IDs where relevant.
- [ ] **Figures** carry load (architecture, sequence, curve/bin) — roughly one per 1–2 pp.
- [ ] **Decimal-numbered headings**, ToC with page numbers for long papers, abstract first.
- [ ] **Numbered references**; internal cross-refs by section number.
- [ ] **devnet/mainnet stage** and **current vs future** clearly separated; no roadmap
      dressed up as shipped.
- [ ] Solana specifics correct: CU/compute feasibility argued, oracle source named,
      version-era pinned, harness/audit references modern.
- [ ] Impersonal, declarative register throughout; the paper reads as a reference, not a take.
- [ ] Paired with a **reference implementation / SIMD** where the mechanism is protocol-level.

---

## 8. Alignment with the edu-content skill

**There is no edu-content skill form for litepapers/whitepapers.** The skill defines six
forms — `course`, `tutorial`, `walkthrough`, `essay`, `slides`, `post`
(`skills/edu-content/forms/FORMS.md`) — and none matches this artifact.

- **Closest neighbour is `essay`, and it diverges hard.** The essay form
  (`forms/essay.md`) is built around a **falsifiable thesis + a steelman + an
  evidence plan**, 1000–3500 words, deliberately opinionated. A whitepaper is the
  opposite job: **canonical, impersonal, exhaustive**, math- and proof-bearing, with a
  *security/attacks* section rather than a *steelman*, and no single falsifiable thesis.
  Length (10–40pp) and format (typeset PDF with a bibliography and figures) sit outside
  every existing form's band.
- **It also leaks into `slides` and `post`** at distribution time (the Alpenglow
  presentation deck; the launch X thread) but those are downstream artifacts, not the paper.

**Recommendation: `no-form-recommend-add`, but scoped.** Two things are true:

1. A whitepaper is a **primary/canonical artifact, not a lesson** — which is arguably
   out of an *edu-content* skill's core remit. Producing rigorous proofs is not teaching.
2. Yet writers in this ecosystem *constantly* need the two jobs the skill currently can't
   route: **(a) authoring a litepaper** (protocol/token launch — mechanism + tokenomics,
   accessible, no proofs) and **(b) turning a whitepaper into an explainer** (the Helius/
   Chainstack "What is X" deep-dive that is the actual distribution channel).

Concretely, add a lightweight **`litepaper` authoring form** (abstract → problem →
mechanism → tokenomics → risks/disclaimer; docs-page to ~8pp; explicitly *not*
proof-bearing), and register a **"paper → explainer" derivation pattern** that routes to
`walkthrough`/`essay` for popularizing an existing spec. Leave *formal proof-bearing
whitepapers* (Solana, Alpenglow) explicitly **out of scope** — flag them as source
documents the skill's other forms cite, not deliverables the skill produces. This mirrors
the corpus README's finding that blog-posts, whitepapers, and the tweet-vs-thread split
are the skill's real gaps.

---

## 9. Takeaways for a writer

- **Decide litepaper vs whitepaper on one axis: is the mechanism's correctness the
  pitch?** If yes (consensus, oracle aggregation, AMM/liquidation invariants), write a
  whitepaper with proofs and an attacks section. If the pitch is value + token, write a
  litepaper and skip the proofs — don't fake rigor you don't have.
- **Lead the abstract with the result and a number.** Finality ms, TPS, confidence
  interval, capital-efficiency gain. The reader should know your claim in three sentences.
- **One section per subsystem, description-before-proof, concrete-before-abstract.**
  Mirror Solana (PoH → PoS → PoRep) and Drift (vAMM → margin → funding → liquidations).
- **Write the attacks section for real.** State trust assumptions (stake thresholds,
  oracle trust) and failure modes explicitly. A missing or decorative security section is
  the fastest way to lose an auditor or serious integrator.
- **On Solana, ship the paper *with* the code.** A reference implementation, a SIMD, or
  at minimum documented program IDs / instruction / account layouts. Alpenglow's
  paper+proofs+Rust-impl bundle is the standard to aim at; a lonely PDF reads as vapor.
- **Separate "current" from "future" and label the deployment stage** (devnet/mainnet).
  Drift's per-section current-vs-future split is the honest, trust-building convention.
- **Version in place, then let the ecosystem distribute.** Bump the version, publish an
  announcement thread, and expect Helius/Anza/Chainstack explainers to be your real
  reach — write the paper to be *citable and explainable*, not viral.
- **Give hard tokenomics or none.** Total supply, distribution, unlock schedule, fee
  flows, incentive argument, disclaimer. Vague token narratives age badly (see the
  supply changes and burns that followed several launches).
- **Keep the register impersonal.** It's a reference, not an essay. Save the thesis, the
  steelman, and the "why this matters" voice for the blog post that popularizes it.
