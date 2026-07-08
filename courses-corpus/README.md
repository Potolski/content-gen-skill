# Solana Course Corpus

A study corpus of the major Solana developer courses, gathered to analyze
**how effective technical courses are structured** — sequencing, lesson anatomy,
cadence, and proof-of-learning. It feeds pattern analysis for the
`edu-content-skill` course architect.

Two artifacts per course:
- **verbatim/structural source** — the actual course material (open-source repos)
  or a captured outline (proprietary courses).
- **`META.md`** — original pedagogical analysis of that course (see
  [`PATTERNS.md`](./PATTERNS.md) for the cross-course synthesis).

## The seven courses

| # | Course | Dir | Source | Fidelity | License |
|---|--------|-----|--------|----------|---------|
| 1 | **Blueshift** | [`blueshift/`](./blueshift) | [learn.blueshift.gg](https://learn.blueshift.gg) · [repo](https://github.com/blueshift-gg/blueshift-dashboard) | Verbatim (EN) | MIT |
| 2 | **Solana Foundation Developer Courses** | [`solana-foundation/`](./solana-foundation) | [solana.com/developers/courses](https://solana.com/developers/courses) · [repo](https://github.com/solana-foundation/developer-content) | Verbatim | Open repo (archived, read-only; no root LICENSE file) |
| 3 | **Cyfrin Updraft — Solana** | [`cyfrin-updraft/`](./cyfrin-updraft) | [updraft.cyfrin.io](https://updraft.cyfrin.io/courses/solana) · [repo](https://github.com/Cyfrin/Updraft) | Verbatim (transcripts) | AGPL-3.0 |
| 4 | **freeCodeCamp — Solana Curriculum** | [`freecodecamp/`](./freecodecamp) | [web3.freecodecamp.org/solana](https://web3.freecodecamp.org/solana) · [repo](https://github.com/freeCodeCamp/solana-curriculum) | Verbatim | BSD-3-Clause |
| 5 | **Ackee — School of Solana** | [`ackee/`](./ackee) | [ackee.xyz/school-of-solana](https://ackee.xyz/school-of-solana) · [repo](https://github.com/Ackee-Blockchain/school-of-solana) | Verbatim | Open repo (no root LICENSE file) |
| 6 | **RareSkills — 60 Days of Solana** | [`rareskills/`](./rareskills) | [rareskills.io/solana-tutorial](https://rareskills.io/solana-tutorial) | **Structural only** | Proprietary (public blog) |
| 7 | **Risein — Build on Solana** | [`risein/`](./risein) | [risein.com/courses/build-on-solana](https://www.risein.com/courses/build-on-solana) | **Structural only** | Proprietary (login-gated video) |

## Scale captured

| Course | Content units | Notes |
|--------|---------------|-------|
| Blueshift | 28 courses · 174 lessons · 15 challenges · 2 paths | multilingual repo; EN extracted |
| Solana Foundation | 12 courses · 63 lessons | each course = `metadata.yml` + `.md` lessons |
| Cyfrin Updraft | 1 course · 8 modules · 48 pages | dual-track (native + Anchor) |
| freeCodeCamp | 15 project-lessons | interactive, test-gated |
| Ackee | 7 lessons + 3 bonus + Solana Handbook | cohort course + companion textbook |
| RareSkills | 8 modules · 60 lessons | outline + framing only |
| Risein | 5 sections · 22 lessons · ~6h video | outline + framing only |

## Layout

```
courses-corpus/
├── README.md            ← this index
├── PATTERNS.md          ← cross-course comparative synthesis (the payoff)
├── <course>/
│   ├── META.md          ← per-course pedagogical analysis
│   ├── content/         ← verbatim source (open-source courses)
│   ├── structure.md     ← captured outline (proprietary courses)
│   └── LICENSE          ← upstream license, where the repo ships one
```

## How it was gathered

- **Open-source courses (1–5)** were `git clone`d from their public repositories
  (shallow/sparse) and the course material copied verbatim into `content/`.
  Blueshift ships nine languages; only English (`en.mdx`) was extracted. Ordering
  metadata (`courses.meta.ts`, `paths.meta.ts`, `metadata.yml`, numbered dirs) was
  preserved because sequencing is itself a pattern under study.
- **Proprietary courses (6–7)** are not open-source. Their **public course
  outlines and stated pedagogy** were captured into `structure.md`; lesson body
  text was **not** reproduced. The `META.md` analysis for these is structural.

## Provenance & fidelity notes

- This corpus is for **studying course-design patterns**, not for republishing
  course content. Open-source material retains its upstream license (see table and
  per-dir `LICENSE`); attribution is preserved via source URLs above.
- `META.md` / `PATTERNS.md` are **original analysis** produced for this project.
- Where a repo shipped no root LICENSE file, that is stated rather than guessed;
  consult the upstream repo for exact terms before any reuse.
- Non-English Blueshift translations and course code-scaffolding beyond what is
  needed to read structure were intentionally omitted to keep the corpus focused.

## Start here

Read [`PATTERNS.md`](./PATTERNS.md) first for the comparative playbook, then dive
into any course's `META.md` for the detail.
