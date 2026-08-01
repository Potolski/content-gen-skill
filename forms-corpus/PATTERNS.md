# PATTERNS — Cross-form synthesis (Solana content-forms corpus)

> Reads across all eight FORM.md analyses (tutorials, walkthroughs, blog-posts, essays,
> litepapers-whitepapers, tweets, threads, slides) and pulls out what separates the forms,
> how to choose between them, what they share, and where they map onto the edu-content
> skill's six forms. For a WRITER picking a form and for the course/content skill routing a
> request. Each per-form FORM.md is the deep dive; this is the map.

---

## The form spectrum (at a glance)

One row per form. "Proof/goal" = the single test of *what the reader can now do*.

| Form | Typical length | Code density | Primary channel | Cadence | Proof / goal (reader can now…) | edu-content skill form |
|---|---|---|---|---|---|---|
| **Tutorial** (guide) | ~1,390 w median (800–2,500) | High — code:prose ~1.5–2.1:1 | solana.com/developers/guides; Helius, QuickNode | Evergreen, version-maintained; vendor series | **Run** a working artifact (deployed program, minted token, confirmed tx) | `tutorial` — confirms |
| **Tutorial** (cookbook recipe) | ~235 w median (90–520) | Very high — ~10:1, near-zero prose | solana.com/developers/cookbook | Evergreen lookup | **Paste** the exact snippet for one task | `tutorial` — partial (recipe unmodeled) |
| **Walkthrough** (repo/README) | ~150 w median (50–300) | Low inline, high *by reference* (pinned repo) | In-repo `README.md` (CI-verified) | Grows with the codebase | **Navigate** an existing artifact along one thread | `walkthrough` — partial (length/hook) |
| **Walkthrough** (article) | 1,000–3,000 w | Quoted pinned snippets | Helius, Anza, Jito, Neodyme, OtterSec | Episodic / series | **Reason about** a repo/tx/protocol/vuln (builds nothing) | `walkthrough` — confirms |
| **Blog-post** (explainer) | 1,500–4,000 w (6,000+ compendia) | 0% (protocol, diagram-carried) → 45% (how-to) | helius.dev, anza.xyz, jito.wtf, quicknode, chainstack | Editorial calendar; evergreen + release notes | **Understand** a mechanism/subsystem | **GAP** → add `explainer` |
| **Essay** (thesis) | 1,000–3,500 w | Rare — prose-dominant | Research blogs, Umbra, Syncracy, personal, X longform | Episodic / release-tracking series | **Argue/defend** a falsifiable claim | `essay` — confirms |
| **Essay** (expository) | 2,000–4,000 w | Light–moderate | Helius/Anza deep-dives, Umbra | Episodic | **Explain** a mechanism (mental model) | `essay` — partial (no thesis/steelman) |
| **Litepaper / whitepaper** | LP ~2–8 pp / one docs page · WP ~10–40 pp PDF | Pseudocode + schemas, **no app code** | Protocol PDF, Anza/university, docs, GitHub SIMD | Versioned in place, not serialized | **Cite** a canonical design-of-record; justify mechanism + tokenomics | **GAP** → add `litepaper`; formal WP out of scope |
| **Tweet** | ≤280 chars (~40–55 w); longform ~150–500 w | Code = image/link (X has no code blocks) | X (near-exclusive) | Event-driven; decays hours–days | **Grab** one high-signal idea | `post` (short end) — confirms |
| **Thread** | 5–15 units (mega 20–42); ~400–1,200 w; long-post ≤25k chars | Low; code = screenshots, 1 diagram / 2–3 units | X; threadreader unrolls; Discord/TG | Release-driven; launch-thread pairing | **Follow** a sequenced explainer → funnel to depth | `post` (long end) — confirms |
| **Slides / talk** | Talk 15–25 slides (~1.5 min/slide); workshop 10–20 + repo | Low on-slide — 1–3 code slides, 5–15 elided lines | Recorded video (YouTube, Solana Compass) + paired repo | Event-driven (Breakpoint, Accelerate); workshops reused | **Watch** one takeaway land live, with a demo climax | `slides` — confirms (gaps) |

Read the table top-to-bottom and it is roughly an axis of its own: **immediacy and reach
fall, permanence and rigor rise** — tweet → thread → blog-post/essay → whitepaper — while
the tutorial↔walkthrough↔recipe cluster sits orthogonal (all code-facing, differing on
*who builds*).

---

## Axes that separate the forms

Seven axes do almost all the discriminating. A form is a *point in this space*, not a genre
label.

**1. Length — two orders of magnitude.** From a ≤280-char tweet to a 40-page whitepaper. The
ordering that matters: tweet (~50 w) < cookbook recipe (~235 w) < README walkthrough (~150 w)
< thread (~400–1,200 w) < guide-tutorial (~1,390 w) < essay / blog-post (1,500–4,000 w) <
whitepaper (3,000–8,000+ w typeset). Length is *downstream of payload*, not a dial you set —
a thread that needs 4,000 words wanted to be a blog-post; a tutorial padded to essay length
lost its arc.

**2. Payload orientation — the master axis.** *What can the reader DO afterward?*
- **Run a thing** → tutorial (task-first; breaks if a step is reordered).
- **Paste a thing** → cookbook recipe (reference snippet, no arc).
- **Navigate a thing** → walkthrough (reference-by-vantage over an *existing* artifact).
- **Understand a thing** → blog-post explainer / expository essay (expository).
- **Argue a thing** → thesis essay (argument-first; breaks if a *claim* is removed).
- **Cite a thing** → whitepaper/litepaper (canonical spec).
- Tweets/threads/slides are *channels* that can carry any of the above at their own length.
This is the litmus every FORM.md returns to: tutorial vs essay is "run it" vs "argue/explain
it"; walkthrough vs tutorial is "read it" vs "build it"; explainer vs essay is "describe" vs
"defend a contestable claim."

**3. Code-to-prose ratio — inverts across the spectrum.** Highest in the cookbook recipe
(~10:1) and framework how-to explainers (25–45%); moderate in guide-tutorials (~1.5–2:1);
near-zero in thesis/expository essays and protocol explainers (diagram-carried); *zero
inline* on X (code is a carbon/ray.so screenshot or a link — the single biggest invisible
constraint on tweets and threads) and on slides (elided to load-bearing lines, full code in
the repo/demo). Whitepapers show **pseudocode and account/instruction schemas, never Rust**.
Rule of thumb repeated across essays and blog-posts: *if code outweighs prose you've drifted
into a tutorial.*

**4. Distribution channel — sets register and cadence.** Docs site (tutorials, evergreen,
community-editable), in-repo README shipped and CI-verified (repo walkthroughs), first-party
company blog (blog-posts/essays, SEO + reputation), protocol PDF / GitHub SIMD (whitepapers,
citable primary source), X (tweets/threads, discovery-native and ephemeral), recorded video +
paired repo (slides, where the *recording* is the durable artifact, not the deck). The channel
is not incidental — it dictates formality, half-life, and whether links can even be clicked.

**5. Evergreen vs timely.** Evergreen: mechanism explainers (Turbine, slots/blocks/epochs),
protocol-internal essays, quickstart tutorials, pinned README walkthroughs, workshop decks,
whitepapers (revised in place with a version bump). Timely: announcements/tweets, "All You
Need to Know About Agave vX" posts, release threads, conference keynotes, incident
post-mortems. The corpus splits cleanly, and the discipline is identical everywhere: **pin the
version and date the number so the rot is visible.**

**6. Single-author vs org — a voice axis.** Founder tweets/threads and personal-blog essays
run first-person, lowercase, opinionated (toly, febo, hana's "ok so what the fuck is the deal
with solana anyway"). Company blogs and docs run first-person-plural or neutral, authoritative,
evergreen. The whitepaper is the extreme: impersonal, third-person, declarative ("the protocol
finalizes…"), named byline but neutral body. Tweet is the most personal point on the axis;
whitepaper the least.

**7. Formality / register.** Whitepaper (academic, decimal-numbered, impersonal) → blog-post /
essay (engineer-to-engineer, precise, lightly informal, allergic to marketing gloss) → tutorial
(second-person imperative, encouraging, celebratory checkpoints) → thread/tweet (terse, punchy,
peer-to-peer) → slides (written *for the ear* — the cue-vs-substance split, where the bullet is
a pointer and the speaker note is the payload). Two openers are banned in every reading form:
"In this article/tutorial we will…" and "I'm excited to announce" / "a thread on…".

---

## Choose-the-form decision guide

Start from payload, then let channel + permanence pick the vehicle.

```
Q1. What can the reader DO afterward?

  RUN / build a working artifact ........................... → TUTORIAL
      └─ needs a learning arc (hook, one-concept-per-step, exercise)? → guide-tutorial
      └─ already knows the concept, just needs the 15 lines?         → cookbook recipe

  NAVIGATE / reason about an artifact that already exists ... → WALKTHROUGH
      (a repo, a program, a tx signature, a protocol flow, a vuln class)
      └─ rides next to the code, reader has repo open? → repo/README subtype (50–300 w)
      └─ standalone, reader has no repo?               → article subtype (1,000–3,000 w)

  UNDERSTAND a mechanism / subsystem ....................... → BLOG-POST EXPLAINER
      (or expository ESSAY on a research blog; same payload, pick by venue)

  ARGUE / defend a contestable, falsifiable claim .......... → ESSAY (thesis mode)

  CITE a canonical design (mechanism correctness or token) . → WHITE/LITEPAPER
      └─ correctness IS the pitch (consensus, oracle, AMM invariants)? → whitepaper + proofs
      └─ value + token is the pitch?                                   → litepaper, no proofs
      └─ neither novel mechanism nor token?  Solana default →  docs + a SIMD/repo, not a PDF

  Then choose the CHANNEL/length by immediacy vs permanence:
      one idea, timely, max reach ................ → TWEET
      one idea + 3–15 supporting moves, social ... → THREAD (trailer → funnel to the long form)
      live audience + a clock + a demo ........... → SLIDES
      hosted, durable, SEO, evergreen ............ → BLOG-POST / ESSAY
      canonical, citable, permanent .............. → WHITEPAPER
```

**The escalation ladder (tweet → thread → blog-post → essay → whitepaper).** Same idea, more
moves, more permanence, more rigor, less immediacy at each rung. Count logical *moves*: one
move (a number, a shipped noun, a claim) is a **tweet**; two-plus (setup → mechanism →
implication → CTA) is a **thread**; a sectioned deep-dive with an internal link web and pinned
versions is a **blog-post**; a defended thesis with a real steelman is an **essay**; a spec
whose correctness must survive an auditor is a **whitepaper**. Escalate the moment the current
rung strains: a tweet that wants headings → essay; a thread that crams the whole blog into
280-char cards → mis-scoped, write the blog and *launch it with the thread*. The healthy
Solana pattern is a **pair**, not a choice — the thread/tweet is the ad, the blog/essay/paper
is the product.

**The tutorial ↔ walkthrough ↔ cookbook triangle.** All three are code-facing; two questions
separate them. **Does the reader type it?** Tutorial *yes* (empty folder → built artifact);
walkthrough *no* (the code exists, you tour it — the instant there's a "now create a folder,"
it drifted into a tutorial). **Is there a learning arc?** Guide-tutorial *yes* (hook →
one-concept-per-step → run it → exercise); cookbook recipe *no* (zero preamble, the exact
snippet, done). `basics/hello-solana` sits on the boundary — it *explains* an existing minimal
program's tx anatomy (walkthrough) inside a repo you can also run (tutorial scaffolding); pick
the vantage by the win-state you're writing toward.

**Secondary routing note.** "Understand a mechanism" is the one payload with four legitimate
vehicles — blog-post (hosted, evergreen, SEO), expository essay (research-blog register),
thread (social trailer), slides (live). Choose by permanence and audience, not by payload;
they share a spine (mental-model-before-mechanism, one-concept-per-unit, diagram-carried).

---

## Shared building blocks

A handful of primitives recur across all eight forms; mastering them ports everywhere.

**The hook.** A felt problem, a hard number, an EVM contrast, or a war story — never
throat-clearing. Present in *all eight*. `local-rust-hello-world` names the thing and starts;
the Turbine essay opens on "how does a block reach 2,000 validators fast?"; the Hitchhiker's
Guide opens on the attacker model; a tweet spends its *entire budget* on line one (toly's "20x
average-vs-median fee gap"); a thread's hook is the whole ballgame; Dean Little's optimization
deck opens on wasted CU. Banned openers ("In this article we will…", "excited to announce",
"🧵 a thread on…") appear in weak examples and never in the best.

**The worked example / runnable checkpoint.** The concrete thing the prose orbits. Tutorial's
earned "Run it" moment with literal output (`Program Id: EFH95f…`); walkthrough's commit-pinned
line range (`token-swap` `blob/419cb6b6…/swap_..rs#L33-L56`); blog-post's production-safe
snippet (readers copy it into prod); slides' live demo climax ("switch to the terminal"); the
tweet's phone-legible code image. Essays and whitepapers are the exception — one illustrative
struct/formula, not a runnable build.

**The diagram-of-the-mental-model.** Carries the no-code sections. The Helius house-style
custom diagram is the signature of protocol explainers; essays lean on a single "hero" diagram
the whole piece references (Turbine fanout tree, Banking Stage pipeline); threads run one image
per 2–3 units with a cover card on the hook; slides default to `visuals: rich` (account boxes,
CU bar charts); whitepapers carry a figure per 1–2 pages. It is *rare* in cookbook recipes and
repo READMEs, which substitute tables and code fences — a real signal that those subtypes are
lookup-density, not teaching-density.

**The "gotcha" / security callout.** The same canonical footgun set surfaces in every form,
placed differently. Tutorial: inline `<Callout type="caution">` *at the step where it bites*
(init_if_needed reinit, unchecked math, missing owner/signer). Walkthrough: the whole security
subtype (Neodyme workshop, Coral `sealevel-attacks`). Blog-post: the compendium genre
(Hitchhiker's Guide, Neodyme Common Pitfalls, OtterSec). Essay: name the footgun on every
recommendation. Whitepaper: a real *attacks/risks* section with stated trust assumptions
(Alpenglow's 80%/60% liveness modes). Tweet/thread: an honest "unaudited / devnet-only"
caveat. Slides: the spoken "don't ship this in prod." The recurring canon — stored canonical
bumps, checked arithmetic, reload-after-CPI, validated CPI targets, no `unwrap()` in program
code — is load-bearing everywhere code appears.

**The version/cluster pin.** Anchor + Agave/client version, devnet vs mainnet, `SIMD-####`.
The universal anti-rot device — mandatory in tutorials (`cargo add …@"=2.0.3"`), blog-posts,
essays, tweets, threads, slides, and whitepapers (protocol era). The one convention no form
skips; an unpinned Solana artifact has a shelf life measured in weeks.

**The CTA / where-to-go-next.** How each form closes. Tutorial: "Next steps" doc links.
Walkthrough: 2–3 follow-the-thread pointers (not a recap). Blog-post: further-reading +
deliberate internal link web. Essay: a "so what / what to watch" close, never a summary
restatement. Tweet/thread: exactly one deferred canonical link, no hashtag pileup. Slides: a
closing *ask that answers the hook* (not "Thank you / Questions?") plus a resources slide
(repo, docs, program IDs — the only clickable artifact on a recording). Whitepaper: future-work
+ a paired reference implementation / SIMD.

**The trade-off beat** (secondary but high-leverage). Named cost-of-the-approach. The skill
*requires* it in tutorials though Foundation guides skip it; the walkthrough exemplar nails it
(`token-swap`'s "Principals" section); essays demand it on every recommendation; whitepapers
carry it as limits/risks. Cheapest single upgrade from "describes the thing" to "understands
the thing."

---

## Mapping to the edu-content skill's forms

The skill ships six forms: `course`, `tutorial`, `walkthrough`, `essay`, `slides`, `post`
(`skills/edu-content/forms/FORMS.md`). Mapping the eight corpus forms onto them:

| Corpus form | Skill form | Status | Why |
|---|---|---|---|
| Tutorial (guide) | `tutorial` | **Covered** | Definition matches beat-for-beat (hook → build → run it → trade-off → exercise). Skill is rightly *more* demanding (requires trade-off + DIY exercise the corpus omits). |
| Tutorial (cookbook recipe) | `tutorial` | **Partial** | ~235-word, ~10:1, arc-less "how do I X?" lookup doesn't fit the tutorial recipe — no hook, no artifact framing, no exercise to bolt onto a 15-line keypair snippet. |
| Walkthrough (article) | `walkthrough` | **Covered** | `subject_ref` pinning, why-per-waypoint, single vantage, trade-off beat all validated by `token-swap` / escrow. |
| Walkthrough (repo/README) | `walkthrough` | **Partial** | Skill's 1,000–3,000-word band mis-grades a perfectly good ~150-word annotated README; mandatory Hook is a blog convention many strong READMEs skip. |
| Blog-post (expository explainer) | — | **GAP** | Maps to *none*: not `tutorial` (no artifact), not `essay` (no thesis/steelman), not `walkthrough` (a concept, not one artifact), too long/sectioned for `post`. The single most common Solana blog output. |
| Essay (thesis) | `essay` | **Covered** | Hook → thesis → argument chain → steelman → so-what matches the best argument pieces; `thesis`/`steelman`/`evidence_plan` extras name exactly what weak essays skip. |
| Essay (expository deep-dive) | `essay` | **Partial** | The Solana *majority* (Turbine, Gulf Stream, tx lifecycle) has no contestable thesis and no natural steelman; force-routing grades it against a steelman it shouldn't have. |
| Litepaper / whitepaper | — | **GAP** | Closest is `essay` and it diverges hard: canonical/impersonal/exhaustive, proofs + attacks section vs thesis + steelman, 10–40 pp PDF outside every band. |
| Tweet | `post` (short end) | **Covered** | Hook rule, one-takeaway discipline, grounding-because-quoted-out-of-context all confirm. Omits the code-as-image constraint and the longform-single boundary. |
| Thread | `post` (long end) | **Covered** | In scope and structurally matched — but `post`'s 50–300-word / 3–8-unit band and `visuals: none` default actively mis-fit real 9–42-unit, media-first threads; funnel pattern unmodeled. |
| Slides / talk | `slides` | **Covered** | Notes-carry-substance, hook-not-agenda / ask-not-thanks, `visuals: rich`, `slide_budget = min ÷ 1.5` all confirm. Under-covers the workshop sub-mode and the live-demo beat. |
| *(none — composite)* | `course` | **N/A** | No single corpus form *is* a course; a course sequences tutorials/walkthroughs/essays/slides with assessment. It's the skill's meta-form. |

**Opinionated recommendation — what to ADD and what to split, in priority order:**

1. **ADD `explainer` (highest value).** The expository mechanism deep-dive is the single
   biggest slice of real Solana writing and routes to none of the six. Add it *between*
   `tutorial` and `essay`: expository not argumentative, understanding not artifact. Aliases:
   "primer," "deep-dive," "how X works." Minimum brief extras: `mechanism`, `mental_model` (the
   scaffolding laid first, usually an EVM contrast), `grounding_set` (numbers/CU/versions/IDs to
   freeze), `code_or_diagram` (which carries the no-prose sections), `version_targets`,
   `evergreen|timely`. This is the clearest gap in the corpus and the cleanest fix.

2. **Give `post` a thread sub-profile — do NOT split into `tweet`/`thread`.** The shared
   principles (hook, one-idea-per-unit, grounding, no hashtag pileup) dominate, so a top-level
   split is wrong. Instead branch `post` by `platform`: a `units` count (band 3–20, not a single
   word cap), `visuals: light|medium` when `platform: thread` (media is load-bearing, not
   decoration), a `funnels_to` key so the writer designs the last-unit CTA, and a note that on X
   *code and benchmarks are images or links by necessity*. Second-highest value: today `post`
   mis-grades the most common distribution wrapper in the ecosystem.

3. **ADD a lightweight `litepaper` authoring form; keep formal whitepapers out of scope.**
   Writers genuinely need (a) to author a litepaper at token/protocol launch (abstract → problem
   → mechanism → tokenomics → risks/disclaimer, docs-page to ~8 pp, explicitly *not*
   proof-bearing) and (b) a "paper → explainer" derivation that routes popularization to
   `explainer`/`walkthrough`. Leave proof-bearing whitepapers (Solana, Alpenglow) as **source
   documents the skill's other forms cite**, not deliverables it produces — writing machine-
   checked proofs isn't teaching.

4. **Add sub-modes to three existing forms (refinements, not new forms):**
   - `essay` → an **expository sub-mode**: replace `thesis` with a `mental_model_promise`, make
     `steelman` optional, and substitute a **required diagram for any multi-hop mechanism +
     required trade-offs/limitations** as the rigor anchor. Keeps one form, stops demanding a
     fake argument.
   - `walkthrough` → a **`subtype: repo | article` toggle** that flexes the length band (50–400
     vs 1,000–3,000), the visuals default (tables/code vs diagram-anchored), and whether Hook is
     required.
   - `tutorial` → a **recipe mode** that relaxes Hook / Trade-off / Exercise for lookup snippets;
     and surface **version-pinning + SDK-duality (`<Tabs>` v1/kit)** as explicit conventions.
   - `slides` → a **workshop mode** (decouple `slide_budget` from minutes, require a paired repo)
     and a first-class **`demo` beat with a mandatory fallback-screenshot visual**.

Net: two new forms (`explainer`, `litepaper`), one sub-profile (`post`→thread), and four
sub-mode refinements. `explainer` and the thread sub-profile are the two that move the most
real volume; do those first.

---

## What to steal, per form

The single highest-leverage structural move from each form's exemplars.

- **Tutorial — the earned "Run it" moment with literal on-chain output.**
  `local-rust-hello-world` shows the actual `Program Id: EFH95f…` line and an explorer link. The
  whole form lives or dies on the reader reaching a *confirmed* result fast; get to a runnable
  checkpoint early, then layer complexity. Corollary to steal: make every step independently
  testable so a stuck reader knows *which* step broke.

- **Walkthrough — pin the subject so the tour can't rot.** `token-swap` puts a commit hash
  (`419cb6b6…`) in every permalink; the pin *is* the `subject_ref`. Steal the discipline (pin a
  commit / program ID / tx signature / version on the first screen) and its partner move: give
  every waypoint a **why**, not just a what — escrow's "Changes from original" list is nothing
  *but* why-per-waypoint.

- **Blog-post — one concept per H2 + a fixed repeatable micro-template for catalog sections.**
  The Hitchhiker's Guide repeats an identical *Vulnerability → Example Scenario → Recommended
  Mitigation* triplet ×20; the eBPF VM post builds strictly bottom-up (rBPF → BPF → ISA → loaders
  → execution). Structure *is* the teaching — and lay the mental model (account model / EVM
  contrast) before the mechanism.

- **Essay — the steelman engaged at full strength.** Resnick's *Issuance from First Principles*
  answers the best counter-argument in the piece; it's the single most-skipped beat and the
  clearest quality signal (on Solana X the strongest counter lands in the replies within an hour
  — put it in the essay). For the expository sub-mode, steal instead the **one "hero" diagram**
  the whole piece references.

- **Litepaper / whitepaper — a real attacks section with stated trust assumptions, shipped with
  the code.** Alpenglow pairs prose with machine-checked proofs *and* a Rust reference impl and
  names its 80%/60% liveness thresholds. Steal: lead the abstract with the result and a hard
  number (finality ms, TPS, confidence interval), write the adversarial section for real, and
  never ship a lonely PDF — attach a SIMD / reference impl / documented program IDs.

- **Tweet — spend the whole budget on line one and make the payload survive
  decontextualization.** toly's "20x average-vs-median fee gap" is one number that travels;
  assume it gets screenshotted with zero surrounding context and still lands. Steal the ruthless
  first-line economy and the exactness (a wrong CU/percent/SIMD number in a short form travels
  farthest and does the most damage).

- **Thread — be a trailer, not the movie.** The dominant Solana move is thread-as-companion:
  land the payoff, then funnel to the blog/docs/repo in the *last* unit (priority-fees thread →
  fee-markets long-form; APE thread → the "APE-och" blog). Steal the blog↔thread pairing and the
  one-idea-per-unit rule (each post quotable standalone), with a diagram every 2–3 units.

- **Slides — write the speaker notes first, the slides second.** The deck ships as a *recording*
  (Solana Compass, YouTube), so the spoken track is the real deliverable; the slide is a cue, the
  note is the payload (bullet: `Store the canonical bump`; note: *recomputing find_program_address
  burns ~1,500 CU, so persist `ctx.bumps.vault` once*). Steal the cue-vs-substance split and the
  demo-as-climax staging with a mandatory fallback screenshot — a failed devnet demo with no
  backup kills a good talk.
