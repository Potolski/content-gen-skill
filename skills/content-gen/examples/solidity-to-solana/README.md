# Solana for Solidity Devs: Ship Four Programs

> By the end you can build, test, and deploy a PDA-backed SPL-token vault on Solana devnet, and explain exactly how the account model differs from EVM storage.

A hands-on course for **developers with EVM / Solidity experience**. Strong Solidity/EVM model: contracts, storage variables, mappings, gas, revert.

**Format:** self-paced · **Length:** ~6h across 3 weeks, 6 lessons · **Status:** draft · **Version:** 0.1.0

**Prerequisites:** comfortable with TypeScript; has shipped at least one Solidity contract.

## Terminal outcomes

- **create**: build, test, and deploy a PDA-backed SPL-token vault on devnet with correct signer/owner checks
- **explain**: explain how Solana's account model differs from EVM storage

## Modules & lessons

| # | Lesson | Module | Job | Difficulty |
|---|---|---|---|---|
| 1 | Your Solidity instincts, mapped onto Solana | What maps 1:1 from Solidity — and what doesn't? | `motivate` | 1 |
| 2 | Where gas and revert went | Where did gas and revert go? | `derive-why` | 1 |
| 3 | Where state lives: accounts, not storage variables | There are no storage variables — so where does state live? | `derive-why` | 2 |
| 4 | Per-user state with a PDA (the mapping you don't have) | Solidity had mappings; Solana doesn't. Now what? | `derive-why` | 2 |
| 5 | Deposit an SPL token: your first CPI | How do programs call other programs and move tokens? | `show-how` | 3 |
| 6 | Ship your own program | Ship your own. | `motivate` | 3 |

You build a running toolkit as you go: `toolchain + deployed hello`, `compute budget + custom errors`, `a counter in a data account`, `per-user PDA vault`, `SPL-token deposit via CPI`, `freeform capstone`.

## How this course was generated

Produced by **ContentGen** (`content-gen-skill`): the course is designed backward from a measurable capstone into `manifest.json` (a `course` object, a prerequisite DAG, modules, and per-lesson briefs), validated by deterministic gates (`validate_course.py`: DAG, briefs, ladder, capstone, outcomes), then each lesson is written from its brief through the `writer-style` voice router, finished with a visual-placeholder pass, and checked by the runnable-code verifier (`verify_code.py`). This README is generated from the manifest.

## Layout

```
solana-for-solidity-devs/
|- manifest.json   design of record: course, DAG, modules, lessons, capstone
|- README.md       this file (generated)
|- lessons/
|  |- drafts/      the written lessons + 000-cover.md
|  |- briefs/      per-lesson structured briefs
|  \- facts/       per-lesson atomic frozen-facts
\- _state.yaml     progress ledger
```

---
_(Generated from manifest.json; do not hand-edit the sections above, re-emit to refresh. A course-specific narrative may be appended below by hand.)_

