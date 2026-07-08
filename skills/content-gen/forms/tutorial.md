# Form: tutorial

One sitting, one buildable artifact, from zero to working. The reader follows steps
and ends with the thing running. If there is no artifact, it is an `essay`; if it
spans modules, it is a `course`.

**Length band:** 800–2500 words. **Visuals default:** `light`.

**Sub-mode: `recipe`** — the ~90–520-word cookbook lookup ("how do I make a
keypair"): near-zero prose, code:prose up to ~10:1, no hook, no exercise, no
trade-off required. Zero preamble, the exact snippet, expected output, done. Use
when the reader already has the concept and needs the 15 lines.

**Conventions (both modes):** pin every dependency version in the install command
(the universal anti-rot device); where an SDK has two live generations
(`@solana/web3.js` v1 vs `@solana/kit`), show tabs or pick one and say so.

## Brief extras (beyond §F core)
- `artifact_spec` — exactly what the reader has built and can run at the end.
- `exercise_spec` — one unguided extension ("now add X yourself") + acceptance check.
- `prereq_toolchain` — versions and the zero-install on-ramp if one exists.

## Structure recipe (the output IS)
1. **Hook** — the felt problem this build solves (never "In this tutorial…").
2. **What you'll build + what you need** — artifact in one sentence; prereqs, honest.
3. **Steps** — numbered, each one testable before the next begins; one new concept
   per step, defined at point of use; footguns flagged inline where they bite.
4. **Run it** — the moment it works, with expected output shown.
5. **The trade-off** — what this approach costs, when not to use it.
6. **Do it yourself** — the `exercise_spec` extension.

## Checklist
- [ ] Every step verifiable before the next (a reader stuck knows *where*).
- [ ] Every command/API/version grounded; expected output shown after `Run it`.
- [ ] One new concept per step; nothing front-loaded.
- [ ] Trade-off named; extension exercise present (both waived in `recipe` mode).
- [ ] Spine rules hold (`../design-spine.md` §§4–7 are the load-bearing ones here).
