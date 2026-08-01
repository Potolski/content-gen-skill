# Pattern: map-from-known
> Route by the learner's **prior model**: lead with 1:1 mappings from what they already know, bank early
> wins, then hit the genuinely different parts.

## Signature strength
**Turns existing expertise into a springboard.** For a learner who already knows an adjacent system (EVM,
web2), the fastest path is "you know how to do X over there — here's X here," sequenced so the easy
mappings come first (momentum) and the genuinely alien parts come once they have traction. It also
**defuses false friends** by naming them explicitly.

## Route for (triggers)
- Audiences with **strong adjacent priors**: **EVM devs**, **web2 devs**, devs from another chain.
- **Fast-track / transition** courses ("Solana for Solidity engineers").
- Any course where the audience keeps asking "but how do I do \<thing I know\> here?"

## Anti-triggers (don't lead with this when…)
- **Absolute beginners** — there's no prior model to map from, and forced analogies mislead.
- The prior model is **too weak or too distant** to carry real transfer.
- Over-mapping risk is high (e.g., "Solidity ≈ JavaScript" lulls learners into ignoring the account model).

## The structure it produces
```
Opener / framing layer (not a whole backbone):
  open on "I know X in <prior>; how in Solana?"
  sequence by MAPPING STRENGTH, not topic logic:
     lead with 1:1 maps (compute units ≈ gas, custom errors ≈ revert, signer ≈ msg.sender-ish)
     → then partial maps (storage ≈ accounts, but...) → then the genuinely different (PDAs, rent, parallelism)
  flag FALSE FRIENDS explicitly ("looks like a mapping; Solana has none — here's why")
  bank early wins before the hard, unfamiliar parts (RareSkills inversion)
```

## Why it works (mechanism)
Prior-knowledge activation (Merrill's activation principle) + transfer + momentum from early wins. "Leverage
past experience as a springboard" (RareSkills) — it's far easier to attach the new to an existing schema
than to build one from nothing.

## Stacks with
The **opener / framing** on a **concept-spine** or **challenge-ladder** (it is rarely the whole course). It
also recurs **inside lesson briefs** as a framing device (the `hook` "in Solidity you'd…"). For EVM devs it
typically *replaces* the generic concept-spine opener.

## Voice handoff
"Why Solana differs" is `derive-why` (Vitalik); the mappings themselves are `show-how` (Helius); collapsing
a *feared* difference is `demystify` (Hotz — "a PDA is just a deterministic address the program can sign
for"). Course opener stays `motivate` (spine).

## Worked micro-illustration (Solana)
> "Solana for Solidity devs" opener. Day 1 leads with **compute units (≈ gas)** and **custom errors
> (≈ require/revert)** — concepts that map almost 1:1, for instant traction — and *defers* storage. Day 4,
> with momentum banked, hits the real divergence: "there are no storage variables; state lives in accounts
> you pass in, and there are no mappings." False friend flagged: "Anchor's `#[account]` is not a Solidity
> contract." `dominant_job: derive-why` for the divergence lessons.

## What this pattern deliberately EXCLUDES
**Not for beginners**, and **not a full course structure** — it's a framing/opener that hands off to a real
backbone. Beware **false-friend over-mapping**; every analogy must be bounded where it breaks (the
trade-off-naming rule applied to analogies).

## Pulled from
RareSkills "60 Days of Solana" (the entire "I know X in Ethereum, how in Solana?" pedagogy + the
lead-with-equivalents inversion) · Cyfrin's explicit EVM↔Solana contrast framing.
