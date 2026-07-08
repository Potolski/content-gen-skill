# Audit Solana Programs: Exploit, Harden, Fuzz

> By the end you can take an unfamiliar Solana program, find the planted vulnerabilities, ship the fixes, and prove it with a fuzz harness — the way an auditor does.

A hands-on course for **developers already building on Solana**. Already builds and tests Anchor/native programs (accounts, PDAs, CPIs, SPL tokens). Wants the security tier.

**Format:** self-paced · **Length:** ~8h across 3 weeks, 6 lessons · **Status:** draft · **Version:** 0.1.0

**Prerequisites:** has shipped a PDA + CPI program; comfortable reading Rust and running anchor test.

## Terminal outcomes

- **analyze**: identify and fix the common Solana program vulnerabilities (signer/owner, PDA/bump, arithmetic, arbitrary CPI) in an unfamiliar codebase
- **evaluate**: audit an unfamiliar Solana program end-to-end: find the planted bugs, ship fixes, and add a fuzz test that catches a regression

## Modules & lessons

| # | Lesson | Module | Job | Difficulty |
|---|---|---|---|---|
| 1 | Break it before you defend it | Think like an attacker first | `show-how` | 2 |
| 2 | Signer and owner checks: the cheap fixes that matter most | The checks that stop most exploits | `show-how` | 2 |
| 3 | Canonical bumps and seed hygiene | The checks that stop most exploits | `derive-why` | 2 |
| 4 | Overflow and the programs you call | Arithmetic and the programs you call | `show-how` | 3 |
| 5 | Find the bug you didn't think of: fuzzing | Prove it: fuzz and audit | `show-how` | 3 |
| 6 | Audit an unfamiliar program (the CTF) | Prove it: fuzz and audit | `motivate` | 3 |

You build a running toolkit as you go: `a working exploit against a vulnerable program`, `the same program, hardened`, `checked arithmetic + validated CPI targets`, `a fuzz harness + a full audit report`.

## How this course was generated

Produced by **ContentGen** (`content-gen-skill`): the course is designed backward from a measurable capstone into `manifest.json` (a `course` object, a prerequisite DAG, modules, and per-lesson briefs), validated by deterministic gates (`validate_course.py`: DAG, briefs, ladder, capstone, outcomes), then each lesson is written from its brief through the `writer-style` voice router, finished with a visual-placeholder pass, and checked by the runnable-code verifier (`verify_code.py`). This README is generated from the manifest.

## Layout

```
solana-program-security-audit/
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

