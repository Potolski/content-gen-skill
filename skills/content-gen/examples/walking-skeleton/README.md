# Ship a Per-User Counter on Solana

> By the end you can build, test, and deploy a per-user PDA counter program to Solana devnet — even if you've never touched a blockchain.

A hands-on course for **developers coming from web2 / traditional software**. Backend web2: functions, a database, REST handlers. No blockchain.

**Format:** self-paced · **Length:** ~2h across 1 weeks, 3 lessons · **Status:** draft · **Version:** 0.1.0

**Prerequisites:** comfortable with the command line; some TypeScript or Rust exposure helps.

## Terminal outcomes

- **create**: build, test, and deploy a per-user PDA counter program to Solana devnet

## Modules & lessons

| # | Lesson | Module | Job | Difficulty |
|---|---|---|---|---|
| 1 | Get a program on-chain in ten minutes | Your first program: state lives in accounts | `motivate` | 1 |
| 2 | Store a number that survives | Your first program: state lives in accounts | `show-how` | 1 |
| 3 | Give every user their own counter | One counter per user, with PDAs | `derive-why` | 2 |

You build a running toolkit as you go: `a single-counter program`, `a per-user PDA counter`.

## How this course was generated

Produced by **ContentGen** (`content-gen-skill`): the course is designed backward from a measurable capstone into `manifest.json` (a `course` object, a prerequisite DAG, modules, and per-lesson briefs), validated by deterministic gates (`validate_course.py`: DAG, briefs, ladder, capstone, outcomes), then each lesson is written from its brief through the `writer-style` voice router, finished with a visual-placeholder pass, and checked by the runnable-code verifier (`verify_code.py`). This README is generated from the manifest.

## Layout

```
solana-pda-counter-for-web2-devs/
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

