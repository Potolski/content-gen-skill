# Solana Content-Forms Corpus

A companion to [`../courses-corpus`](../courses-corpus). Where that corpus studies
**how courses are structured**, this one studies the **individual content forms** a
Solana educator/writer produces: tutorials, walkthroughs, blog posts, essays,
litepapers/whitepapers, tweets, threads, and slide decks.

Purpose: give the `edu-content-skill` a grounded, per-form pattern library — the
anatomy, length, voice, cadence, and quality bar of each form as actually practiced
in the Solana ecosystem — plus a map of where the skill's current six forms
(tutorial / walkthrough / essay / slides / post / course) cover the real landscape
and where they have gaps.

Two-tier capture, per form:
- **Verbatim exemplars** — only where a clean open-licensed source exists
  (tutorials, walkthroughs). Stored under `<form>/exemplars/`.
- **Curated catalog + original analysis** — for forms that live on proprietary
  blogs or social platforms (blog posts, essays, whitepapers, tweets, threads,
  slides). Real exemplars are indexed by title/author/URL with structural notes;
  their body text is **not** reproduced.

## The eight forms

| Form | Dir | Capture | Verbatim source |
|------|-----|---------|-----------------|
| **Tutorial** | [`tutorials/`](./tutorials) | Verbatim + catalog | Solana Foundation **guides** (51) + **cookbook** recipes (61) |
| **Walkthrough** | [`walkthroughs/`](./walkthroughs) | Verbatim + catalog | `solana-developers/program-examples` READMEs (42) |
| **Technical blog post** | [`blog-posts/`](./blog-posts) | Catalog + analysis | — (proprietary blogs) |
| **Technical essay** | [`essays/`](./essays) | Catalog + analysis | — |
| **Litepaper / whitepaper** | [`litepapers-whitepapers/`](./litepapers-whitepapers) | Structure + analysis | — (outline only) |
| **Tweet** | [`tweets/`](./tweets) | Catalog + analysis | — (social) |
| **Thread** | [`threads/`](./threads) | Catalog + analysis | — (social) |
| **Slide deck / talk** | [`slides/`](./slides) | Catalog + analysis | — |

Each form dir contains:
- **`FORM.md`** — original 9-section pattern analysis (definition, anatomy, length,
  voice, cadence, Solana conventions, quality checklist, skill-alignment, takeaways).
- **`catalog.md`** — curated real exemplars with links + structural notes.
- **`exemplars/`** — verbatim open-licensed examples (tutorials & walkthroughs only).

[`PATTERNS.md`](./PATTERNS.md) is the cross-form synthesis: the form spectrum, a
choose-the-form decision guide, shared building blocks, and a mapping of all eight
forms onto the edu-content skill's six — flagging **blog-post**,
**litepaper/whitepaper**, and the **tweet-vs-thread** split as the notable gaps.

## Verbatim exemplar provenance

| Source | Repo | License |
|--------|------|---------|
| Guides & cookbook | [solana-foundation/developer-content](https://github.com/solana-foundation/developer-content) (archived) | Open repo (see repo) |
| Program walkthroughs | [solana-developers/program-examples](https://github.com/solana-developers/program-examples) | Open repo (see repo) |
| Curated link seed | [helius-labs/solana-awesome](https://github.com/helius-labs/solana-awesome) → `_seeds/solana-awesome.md` | Open repo |

## Method & IP notes

- Verbatim material is limited to open-licensed repositories and retains its
  upstream license; sources are attributed above and in each `FORM.md`.
- For proprietary or social-platform forms, this corpus captures **structure,
  conventions, and a curated index of real exemplars** — not their text.
  `FORM.md`/`catalog.md`/`PATTERNS.md` are original analysis produced for this
  project.
- Whitepapers are captured as **section outlines + analysis only**, never full text.

## Relationship to the skill

The skill's form definitions live in
`skills/edu-content/forms/` (`tutorial.md`, `walkthrough.md`, `essay.md`,
`slides.md`, `post.md`, `FORMS.md`). Each `FORM.md` here reads its corresponding
skill definition (where one exists) and reports **confirms / diverges / gap** in its
"Alignment with the edu-content skill" section, feeding concrete recommendations in
`PATTERNS.md`.
