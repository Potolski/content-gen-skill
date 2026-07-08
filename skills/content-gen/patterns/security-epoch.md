# Pattern: security-epoch
> A late, distinct hardening tier taught **offense → defense**: insecure → exploit → patch → fuzz/CTF.

## Signature strength
Teaches security the only way it sticks: by **breaking things first.** Each vulnerability class is shown as
a working exploit against vulnerable code, then patched, then re-tested — and the tier is assessed with
**authentic adversarial work** (fuzzing, CTF levels), not multiple choice. Produces builders who can both
ship and audit.

## Route for (triggers)
- **Audit / security tracks**; the **pre-mainnet hardening module** of any serious dev course.
- **Solana devs leveling up** into security.
- Any course whose terminal outcome includes "build *secure* / production-ready programs."

## Anti-triggers (don't lead with this when…)
- **Before build fluency** — you cannot find bugs in code you can't yet write. It is always a **late** tier.
- **Beginner intro courses** — a light, named **"Footguns"** treatment inline (per `design-spine.md` §8) is
  the right dose, not a full epoch.

## The structure it produces
```
Its own module/track, gated behind dev fluency. Per vulnerability class:
  show vulnerable handler → write an exploit test that drains/breaks it →
  patch (the check) → re-test (exploit now fails) → name the class
Class list (see solana-syllabus-dag.md §5): signer · owner · data-matching · reinit ·
  duplicate-mutable · type-cosplay · arbitrary-CPI · bump-seed · close/revival · PDA-sharing · arithmetic
Tiering: 101 (introduce the class) → 201 (subtle variants)
Applied assessment: Trident fuzzing a real program AND/OR CTF levels; optional recurring timed quiz.
```

## Why it works (mechanism)
Productive failure / exploit-first (Kapur) + contrastive insecure-vs-secure cases + authentic assessment
(CTF/fuzz) + spaced competitive retrieval (Secureum RACE-style). Feeling the exploit creates the "why this
check exists" that a warning never could.

## Stacks with
A **late tier** on any backbone; pairs with **build-it-twice** (audit both native and Anchor versions); can
itself be a **challenge-ladder** of attack challenges. Often the capstone gate for a "secure developer"
outcome.

## Voice handoff
Walkthroughs are `show-how` (Helius); "why the check is necessary" is `derive-why` (Vitalik). **Critical
`voice_notes` flag:** *"security — be wary of Hotz reductive collapse; a clean 'X is just Y' can ship an
exploit"* (this mirrors the voice router's explicit security caution). Keep the offense framing
**constructive / defensive**, never a how-to-grief.

## Worked micro-illustration (Solana)
> Hardening module, signer-authorization class. **Insecure:** a `withdraw` that never checks the signer.
> **Exploit:** a test where attacker drains the vault. **Patch:** add the `Signer` + `has_one` constraint.
> **Re-test:** attacker's tx now fails; owner's succeeds. **Apply:** fuzz the patched program with Trident
> for unexpected inputs. `dominant_job: show-how`; `voice_notes: security — Vitalik guest for "why".`

## What this pattern deliberately EXCLUDES
**Not an early-course pattern** and **not a substitute for the build fluency it depends on.** It does not
replace a real audit/professional review. The offense content must remain defensive in intent — exclude
anything that reads as enabling attacks on live protocols.

## Pulled from
Ackee School of Solana (security lecture + Trident fuzzing) & Solana Auditors Bootcamp (CTF) · Secureum
epochs / RACE / CARE · Cyfrin "Common Bugs" CTF · Solana Foundation Sealevel insecure→secure refactors.
