# Pattern: client-integration
> Shape a course around the **off-chain side** — wallet, RPC, IDL-typed client, and dApp/mobile UI — that
> wires real users to on-chain programs.

## Signature strength
Owns the half of Solana the program-centric patterns ignore: **connecting a user to a program.** It
sequences the client journey (connect wallet → read state → build & send a transaction → confirm/handle
errors → subscribe to updates) and treats the **IDL as the program↔client contract**. Without it, "build a
dApp" courses have no shaping pattern and no rungs to climb.

## Route for (triggers)
- Outcomes that are a working **dApp / mobile app / frontend / SDK**, not (only) a program.
- **Mobile** (Mobile Wallet Adapter, React Native), **web** (wallet-adapter, `@solana/web3.js` or `kit`),
  or **integration/SDK** courses.
- The **client half** of a full-stack course (pairs with an on-chain backbone).

## Anti-triggers (don't lead with this when…)
- **Pure on-chain program** courses with no UI — use challenge-ladder.
- Learners with **no JS/TS/mobile base** — the client language is a prerequisite, not taught here.
- **Non-technical** courses (no code).

## The structure it produces
```
Client artifact sub-ladder (the program is given, or built in a paired on-chain module):
  connect a wallet → read an account/state → build & send a transaction →
  confirm + handle errors → subscribe to account changes → IDL-typed client → full dApp/mobile UI → ship
each rung = an overview-lab-challenge lesson; difficulty ramps; scaffold fades (given client → blank)
```

## Why it works (mechanism)
Whole-task practice on the *integration* skill (4C/ID) + concrete-before-abstract (a real wallet connect
before the RPC abstraction) + just-in-time (introduce the IDL when the client needs typed calls) + the
scaffold removing UI boilerplate so each rung isolates one client concept.

## Stacks with
The **on-chain backbone** (challenge-ladder / build-it-twice supplies the program; this wires the client);
**concept-spine** for the transaction-lifecycle / RPC model. Often the **second track** of a full-stack
course. Lessons use **overview-lab-challenge**.

## Voice handoff
Mostly `show-how` (Helius). Wallet-UX / "why non-custodial" framing can be `derive-why` (Vitalik) or
`frame` (Balaji); the **mobile-access / LATAM** stakes angle is a strong `motivate`/`sustain` seam for
Kaue's spine.

## Worked micro-illustration (Solana)
> Mobile dApp course. Ladder: connect via **Mobile Wallet Adapter** → read a user's token balance → send a
> transfer → handle confirm + the "insufficient funds" error → subscribe to balance changes → typed client
> from the program **IDL** → ship a React Native app. Trade-off named: MWA gives native UX but ties you to
> Android session-token flows. `dominant_job: show-how`.

## What this pattern deliberately EXCLUDES
It does **not teach program/on-chain logic** (pair with an on-chain backbone) and is **not for
non-technical or pure-program** courses. The client language (TS / React / React Native) is assumed.

## Pulled from
Blueshift Mobile track (MWA, embedded wallets, dApp-store publishing) · Solana Foundation "Frontend" /
Mobile course · Ackee "Front-end for Solana Programs" lecture · Solana docs Frontend + Cookbook wallet /
transaction recipes.
