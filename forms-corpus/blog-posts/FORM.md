# FORM — Technical blog post (Solana engineering blog)

> Original pattern analysis for a writer producing a Solana **engineering blog post**:
> the long-form explainer/deep-dive published on a company or independent dev blog
> (Helius, Anza, Jito, Jump, QuickNode, Chainstack, Umbra, Neodyme, OtterSec, sec3).
> RESEARCH mode: no verbatim reproduction of proprietary sources. Exemplars are cited
> by title/org/URL; all analysis below is original. Seed:
> `../_seeds/solana-awesome.md`.

---

## 1. Definition & scope

The **technical blog post** is not one thing — it is a *delivery vehicle*. A blog is
a channel; what lands on it can be a tutorial, an essay, a walkthrough, a release
note, or an explainer. This FORM analyzes the **dominant subtype the Solana
ecosystem actually ships**: the **long-form expository explainer / mechanism
deep-dive** — the "how does X work" / "everything you need to know about Y" /
"primer on Z" article that is the backbone of the Helius and Anza blogs.

What it is, concretely in Solana:
- An **expository** piece: it *describes and explains* a protocol mechanism, a
  subsystem, a fee model, or a framework — it does not primarily argue a thesis, and
  it does not walk you to a single running artifact. Example: [Understanding Slots,
  Blocks, and Epochs on Solana — Helius](https://www.helius.dev/blog/solana-slots-blocks-and-epochs)
  or [The Solana eBPF Virtual Machine — Anza](https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine).
- Authored by an **infra/RPC/validator/security company** as top-of-funnel
  developer marketing, or by an **independent researcher** building reputation. The
  company byline matters: it sets register (authoritative, evergreen, SEO-shaped) and
  cadence.

How it differs from adjacent forms (the distinctions a writer must get right):

| Adjacent form | The line | Blog-post explainer sits where |
|---|---|---|
| **Tutorial** | Tutorial ends with one buildable artifact you ran ("clone, `anchor build`, deploy"). | Explainer may *contain* code but the takeaway is *understanding a mechanism*, not a shipped artifact. [Priority Fees — Helius](https://www.helius.dev/blog/priority-fees-understanding-solanas-transaction-fee-mechanics) explains the fee model AND shows how to set CU price — half explainer, half how-to. |
| **Walkthrough** | Walkthrough tours ONE existing artifact (a specific repo/tx/program). | Explainer tours a *concept or subsystem* generically, not one codebase. |
| **Cookbook recipe** | Recipe is a copy-pasteable snippet for one task, terse, no narrative. | Explainer is narrative, contextual, teaches the "why." |
| **Essay** | Essay defends a *contestable thesis* and must steelman the opposition. | Explainer is largely *uncontested description*: "here is how Turbine propagates blocks," not "Turbine is the wrong design." When a blog post argues (e.g. [The Truth about Solana Local Fee Markets — Helius](https://www.helius.dev/blog/solana-local-fee-markets)), it has crossed into **essay** territory. |
| **Litepaper/whitepaper** | Whitepaper is a first-party spec of a *new* system, authored by its builders, PDF/formal register. | Explainer is third-party or retrospective, HTML, teaching register, cites the whitepaper rather than being one. |

**When a writer should choose this form:** you want to make an existing Solana
mechanism legible to developers, the payload is *understanding* (not a build or an
argument), the topic is evergreen or tied to a release, and the venue is a blog with
SEO/reputation goals. If the payload is "reader ships X" → tutorial. If it is "reader
can defend claim Y" → essay. If it is "reader understands this one repo" →
walkthrough.

---

## 2. Structural anatomy

Strong Solana explainers converge on a recurring skeleton. Two grounded reference
shapes from measured exemplars:

- **Linear mechanism deep-dive** — [The Solana eBPF Virtual Machine — Anza](https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine):
  motivation hook → definitional sections building bottom-up (rBPF VM → BPF → ISA →
  loaders → execution) → a "tour" gateway section → pipeline walk → close on
  functional outcome. 11 sections, ~12–15 inline code blocks, no diagrams.
- **Compendium / catalog explainer** — [A Hitchhiker's Guide to Solana Program
  Security — Helius](https://www.helius.dev/blog/a-hitchhikers-guide-to-solana-program-security):
  problem hook → attacker-model framing section → ~20 topic sections each following
  an identical **Vulnerability → Example Scenario → Recommended Mitigation** triplet →
  Conclusion → Additional Resources. Repeating micro-structure is the whole design.

### Reusable template (the skeleton)

```
# <Title: noun-phrase or "What is X" / "Everything You Need to Know About X">

[Hook]                     REQUIRED. A felt problem, a number, a "you've hit this
                           error," or a why-this-matters framing. Not "In this post…".

[TL;DR / what you'll learn] OPTIONAL but common on company blogs. 2–4 bullets or a
                           short paragraph promising the payload (SEO + skim bait).

[Prerequisite grounding]   OPTIONAL. "This assumes you know the account model" +
                           one link back to a 101 explainer (internal link web).

## Background / the problem space   REQUIRED for deep-dives. Establishes the mental
                           model before the mechanism (e.g. "how Ethereum does it"
                           as a contrast anchor).

## Core mechanism, section per moving part   REQUIRED. Bottom-up or
                           pipeline-ordered. ONE concept per H2. Concrete before
                           abstract. Diagram or code per section as the topic demands.

## [Repeat sections]        The body. Compendiums use a fixed micro-template per
                           section (Problem/Example/Fix). Deep-dives escalate depth.

## Practical implications / how to use it   OPTIONAL. Bridges theory to the reader's
                           code (CU numbers, config flags, API calls).

## Conclusion / wrap        REQUIRED. Recaps the mental model in 3–5 lines. Often a
                           forward-look ("what's next for X") or soft CTA.

## Further reading / resources   COMMON. Curated links: whitepaper, docs, related
                           posts on the same blog (internal linking is deliberate).
```

**Required vs optional.** Required: title that states the payload, hook, at least one
background section, mechanism body with one-concept-per-heading, conclusion. Optional
but high-frequency: TL;DR bullets, prerequisite links, a "how this affects your code"
bridge, a resources list, author bio/date block. The **internal link web** (linking
to the blog's own 101 posts) is a near-universal convention on Helius/Anza/QuickNode
and worth treating as required for a series blog.

---

## 3. Length, density & format

Measured against the exemplar set (word counts approximate, from structure + reading):

- **Typical length:** 1,500–4,000 words for a standard deep-dive. Short primers /
  "version update" posts run 1,000–2,500 ([Agave v2.1 Update — Helius](https://www.helius.dev/blog/agave-v21-update-all-you-need-to-know)).
  Compendiums run long: the [Hitchhiker's Guide to Solana Program Security](https://www.helius.dev/blog/a-hitchhikers-guide-to-solana-program-security)
  is a ~20-section reference, well past 6,000 words — effectively a small book chapter.
- **Sections:** 6–12 H2s for a deep-dive; 20+ for a catalog compendium. Each H2 is a
  self-contained unit a reader can jump to.
- **Code-to-prose ratio — varies by subtype, and this is the key format decision:**
  - *Pure mechanism explainers* (Turbine, slots/blocks/epochs, consensus, Gulf
    Stream) are **near-zero code**; they lean on **diagrams and analogies**. Helius's
    protocol posts are famous for custom illustrative diagrams.
  - *Framework / how-to explainers* ([An Introduction to Anchor — Helius](https://www.helius.dev/blog/an-introduction-to-anchor-a-beginners-guide-to-building-solana-programs),
    [A Guide to Testing Solana Programs — Helius](https://www.helius.dev/blog/a-guide-to-testing-solana-programs))
    run **~25–45% code by volume**, with Rust/TypeScript blocks per concept.
  - *Systems deep-dives* ([Anza eBPF VM](https://www.anza.xyz/blog/the-solana-ebpf-virtual-machine))
    are code-heavy (12–15 blocks) with pseudo-code and macro definitions.
- **Visual assets:** diagrams (the Helius house style), sequence/pipeline figures,
  the occasional screenshot (explorer views, dashboards), and fenced command/code
  blocks with language tags. Tables are used for comparisons (fee tiers, version
  deltas, EVM-vs-Solana).
- **Heading style:** descriptive noun phrases ("The Transaction Pipeline",
  "Bump Seed Canonicalization"), not clickbait questions inside the body. Title-level
  often uses the "X: Everything You Need to Know" / "What is X?" / "A Primer on X"
  SEO patterns.

---

## 4. Voice, framing & conventions

**Register:** authoritative-but-friendly technical exposition. First-person plural or
neutral third person on company blogs ("we'll walk through…"); more personal and
irreverent on independent blogs (hana's [ok so what the fuck is the deal with solana
anyway](https://2501babe.github.io/posts/solana101.html) is the extreme of the
irreverent-but-rigorous end). The dominant company-blog voice is confident,
pedagogical, and evergreen — written to be linked for years, not to chase a moment.

**Hook conventions.** The strongest openers do one of: (a) name a *felt pain*
("your transaction keeps failing during congestion"), (b) drop a *concrete number or
claim* to be unpacked, (c) set an *EVM contrast* for the incoming mental model, or
(d) frame *why this matters now* (a release, an outage, a narrative). Avoid the dead
"In this article, we will…" open — it appears in weak posts and never in the best.

**How Solana concepts are introduced (the ecosystem norm):**
- **Accounts / account model** — introduced early as the foundational mental model,
  usually contrasted with the EVM's contract-storage model. Everything else is built
  on it; strong posts link to a dedicated account-model explainer rather than
  re-teaching it.
- **PDAs** — defined at point of use as program-controlled addresses off the ed25519
  curve; the canonical-bump nuance is flagged where relevant (and is itself a whole
  compendium section in security posts).
- **CPIs** — framed as "programs calling programs," with the privilege-escalation /
  signer-extension angle noted for security-flavored posts.
- **Addresses** — base58 pubkeys; program IDs given verbatim when a specific program
  is discussed.
- **Compute units (CU)** — introduced as the metering unit; strong posts cite
  *actual CU numbers* and the 200k-per-ix default / 1.4M-per-tx cap as anchors.

**Code presentation norms:** fenced blocks with a language tag; Rust for programs,
TypeScript for clients; short, runnable-in-spirit snippets rather than full files;
inline `code` for identifiers, account names, and CLI flags. Best practice mirrors
the project's own rules — checked arithmetic, no `unwrap()` in program snippets,
stored bumps — because readers copy blog code into production.

**Citation/link norms:** inline hyperlinks to primary sources (docs, SIMDs, the
whitepaper, GitHub source, the specific PR/commit for a release post). Company blogs
heavily **cross-link their own back-catalog** to build a topic cluster and keep
readers on-site. A "Further reading" list at the end is conventional.

(No verbatim quote is included here: this form's `exemplars/` directory holds no
open-licensed source, and all catalogued posts are proprietary. Per IP rules, their
text is not reproduced.)

---

## 5. Cadence & distribution

**Where it's published:** a first-party company blog on the marketing domain
(`helius.dev/blog`, `anza.xyz/blog`, `jito.wtf/blog`, `quicknode.com/guides` +
`blog.quicknode.com`, `chainstack.com/blog`), or an independent researcher's site
(`umbraresearch.xyz/writings`, `neodyme.io/blog`, `osec.io/blog`, personal domains).
Some also cross-post to Medium or a Substack.

**Cadence:** company blogs publish on a **regular editorial calendar** — Helius has
shipped a large, sustained body (dozens of posts indexed in the seed) mixing evergreen
explainers with timely "All You Need to Know About Solana's vX Update" release notes.
Independent research (Umbra, Neodyme) is **lower-frequency, higher-depth**, published
when there is something substantial to say.

**Promotion:** the launch is an **X (Twitter) thread** that teases the post and links
it — the thread is the ad, the post is the product. Reposts by the company account and
author, inclusion in ecosystem newsletters, and occasional Reddit/Discord shares.

**Series / cadence building:** two proven patterns — (1) a **numbered/named series**
(sec3's four-part [Solana Internals](https://www.sec3.dev/blog/solana-internals-part-1-what-are-the-native-on-chain-programs-and-why-do-they-matter),
Umbra's multi-part [Solana Fees](https://www.umbraresearch.xyz/writings/solana-fees-part-1));
and (2) a **recurring template** applied to each new release (the Helius
"vX.Y Update: All You Need to Know" cadence tracks the Agave version train). The
template turns a one-off into a franchise readers await.

**Evergreen vs timely:** the corpus splits cleanly. **Evergreen** — mechanism
explainers (Turbine, consensus, the account model, PDAs, testing) that are updated in
place as Solana evolves. **Timely** — version-update posts, incident post-mortems, and
narrative-of-the-moment pieces. A strong company blog runs mostly evergreen with a
steady drip of timely posts to catch search traffic on each release.

---

## 6. Solana-specific conventions

Domain norms a writer in this form is expected to honor:

- **Version pinning is mandatory and load-bearing.** State the **Anchor** version and
  the **Agave/validator client version** the post targets — Solana's toolchain moves
  fast and unpinned posts rot. The entire "All You Need to Know About Solana's
  v1.16/v1.17/v1.18 Update" and [Agave v2.x](https://www.helius.dev/blog/agave-v2-update)
  genre exists because version deltas are newsworthy. Note the Agave/Anza rename and
  the Firedancer client where relevant.
- **Devnet vs mainnet framing.** Say which cluster commands/examples target; devnet
  for anything a reader will run, mainnet-beta for economic/production claims. Airdrop
  and faucet caveats belong on devnet examples.
- **Program IDs given verbatim** when a specific native or SPL program is discussed
  (System, Token, Token-2022/Token Extensions, ATA, the loaders). Token Extensions
  posts ([Primer on Solana's Token Extensions — Superteam](https://blog.superteam.fun/p/primer-on-solanas-token-extensions))
  distinguish classic Token vs Token-2022 explicitly.
- **Test-harness mentions.** Modern posts name the current tooling — **LiteSVM** and
  **Mollusk** for in-process unit tests, **Surfpool** for mainnet-fork integration —
  and flag that `solana-test-validator` is the slow path. A testing explainer that
  omits LiteSVM/Mollusk now reads as dated.
- **Security caveats are a genre unto themselves.** Program posts flag the canonical
  footguns — unchecked arithmetic, missing owner/signer checks, `init_if_needed`
  reinit risk, arbitrary CPI, bump canonicalization, account reload after CPI. The
  security compendia ([Neodyme — Common Pitfalls](https://neodyme.io/en/blog/solana_common_pitfalls/),
  [OtterSec — An Auditor's Introduction](https://osec.io/blog/2022-03-14-solana-security-intro),
  [Helius — Hitchhiker's Guide](https://www.helius.dev/blog/a-hitchhikers-guide-to-solana-program-security))
  are the reference standard.
- **CU / performance numbers** are expected to be real and current; "saves ~1,500 CU
  by storing the bump" style claims should be grounded, not vibed.
- **EVM contrast** is the default on-ramp device, since much of the reader base
  arrives from Ethereum.

---

## 7. What good looks like — checklist

Grade a draft against these:

- [ ] **Payload is clear and correctly-formed** — it explains a mechanism
  (explainer), not secretly a tutorial or an argument wearing an explainer's clothes.
- [ ] **Hook earns the read** — a felt problem, a number, or an EVM contrast; never
  "In this article we will."
- [ ] **Title states the payload** and uses a discoverable pattern ("What is X",
  "Everything You Need to Know About X", "A Primer on X").
- [ ] **One concept per H2**, ordered bottom-up or pipeline-order; concrete before
  abstract.
- [ ] **Mental model established before mechanism** — the account-model / EVM-contrast
  scaffolding is laid before the deep part.
- [ ] **Versions pinned** (Anchor + Agave/client) and **cluster named** (devnet vs
  mainnet).
- [ ] **Every number, CU figure, API name, and program ID grounded** against a primary
  source and frozen before writing.
- [ ] **Code is production-safe** (checked math, no `unwrap()` in program snippets,
  stored bumps) — readers copy it.
- [ ] **Diagrams/analogies carry the no-code sections**; code carries the how-to
  sections; neither is decoration.
- [ ] **Internal + primary links** present: back-catalog cross-links and primary
  sources (docs/SIMD/whitepaper/source).
- [ ] **Conclusion recaps the mental model** in a few lines and points forward or to
  further reading.
- [ ] **Evergreen posts are datestamped/versioned** so rot is visible and fixable.
- [ ] **Security caveats present** where the post touches program code.
- [ ] **No filler / no throat-clearing** — every section advances the explanation.

---

## 8. Alignment with the edu-content skill

**There is no `blog-post` form in the skill.** The six forms are `course`,
`tutorial`, `walkthrough`, `essay`, `slides`, `post`
(`skills/edu-content/forms/FORMS.md`). The corpus README already flags blog-post as a
notable gap. My assessment, grounded in the exemplar set:

**Where practice is COVERED by existing forms (blog-post as vehicle):**
- A blog post that walks you to a running artifact → the skill's **`tutorial`** covers
  it exactly (hook → build → run it → trade-off → exercise).
- A blog post that argues a contestable thesis ([The Truth about Solana Local Fee
  Markets](https://www.helius.dev/blog/solana-local-fee-markets), Solana-thesis pieces)
  → the skill's **`essay`** covers it (thesis, steelman, evidence plan).
- A blog post touring one specific repo/tx → **`walkthrough`**.
So "blog post" as a *channel* is genuinely absorbed by tutorial/essay/walkthrough,
and the skill is right not to add a "channel" form.

**Where practice DIVERGES / reveals a gap (the dominant subtype is uncovered):**
The **expository mechanism explainer** — "What is Firedancer," "Understanding Slots,
Blocks, and Epochs," "The Solana eBPF Virtual Machine," "Turbine: Block Propagation,"
"An Introduction to Anchor" — is the single most common Solana blog output, and it
maps cleanly to **none** of the six:
- It is **not `tutorial`**: there is no single buildable artifact; the terminal
  takeaway is understanding, not a running thing. Forcing it into tutorial's
  "artifact_spec / exercise_spec" scaffolding distorts it.
- It is **not `essay`**: it defends no falsifiable thesis and has no real steelman —
  the skill's `essay` form explicitly requires both, so an honest explainer would fail
  the essay checklist while being excellent.
- It is **not `walkthrough`**: it tours a *concept*, not one existing artifact.
- It is **too long and sectioned for `post`.**

That expository/reference register — descriptive, multi-section, diagram- or
code-heavy, evergreen, one-concept-per-heading — is a distinct FORM with its own
quality bar (grounding, version-pinning, mental-model-before-mechanism, internal link
web) that the current six do not encode.

**Recommendation → `no-form-recommend-add`.** Add an **`explainer`** form (aliases:
"primer," "deep-dive," "how X works") to the skill, sitting between `tutorial` and
`essay`: expository not argumentative, understanding not artifact. Minimum brief
extras: `mechanism` (the one subsystem explained), `mental_model` (the scaffolding
laid first, usually an EVM contrast), `grounding_set` (numbers/CU/versions/program
IDs to freeze), `code_or_diagram` (which carries the no-prose sections),
`version_targets` (Anchor + Agave/client), `evergreen|timely`. If the maintainers
prefer not to add a seventh form, the minimal alternative is to **widen `essay`** to
admit a non-argumentative expository mode (drop the mandatory steelman when
`dominant_job` is `demystify`/`show-how` rather than `derive-why`) — but a dedicated
`explainer` form is the cleaner fit and matches where the ecosystem actually spends
its writing effort.

---

## 9. Takeaways for a writer

- **Decide the payload before the outline.** Understanding → explainer. A running
  thing → tutorial. A claim to defend → essay. One repo → walkthrough. Mixing two
  ("explain fees AND ship a CU-optimizer") is fine only if you sequence them; don't
  let an explainer secretly become a half-built tutorial.
- **Lay the mental model before the mechanism.** The best Solana posts spend the first
  third establishing the account model / EVM contrast, then go deep. Skipping the
  scaffolding loses the EVM-native reader in section two.
- **One concept per heading, bottom-up or pipeline-order.** The eBPF VM post builds
  rBPF → BPF → ISA → loaders → execution; the security compendium repeats a fixed
  Vulnerability/Example/Fix triplet. Structure is the teaching.
- **Pin versions and name the cluster — every time.** Unpinned Solana posts rot within
  a release cycle. State Anchor + Agave versions; say devnet vs mainnet. Datestamp
  evergreen posts so decay is visible.
- **Ground every number, CU figure, program ID, and API name** against a primary
  source and freeze it before writing. Blog posts get linked for years and copied into
  production — a wrong number does lasting damage.
- **Let diagrams carry the no-code sections and production-safe code carry the how-to
  sections.** Don't paste code into a Turbine explainer to look technical; don't
  explain Anchor constraints in prose when a 6-line snippet is clearer. Never ship
  program snippets with `unwrap()` or unchecked math.
- **Build a franchise, not a one-off.** A named series or a repeatable release-note
  template (the "vX Update: All You Need to Know" pattern) compounds; cross-link your
  back-catalog to build a topic cluster.
- **Write the launch thread as you write the post.** The X thread is the distribution;
  a strong post with no thread underperforms a mediocre post with a great one.
- **Avoid:** the "In this article we will…" open; unversioned toolchain claims;
  decorative code; survey padding that advances no concept; and burying the payload —
  the title and hook should tell a skimmer exactly what they'll walk away knowing.
