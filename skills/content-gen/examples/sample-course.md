# Worked example — a course architecture produced by this skill

Proves the skill *generates*, not just describes. It runs the full `SKILL.md` procedure on one realistic
brief and ends in two complete, voice-ready lesson briefs. Use it as a template.

> **Note:** this is a *structural* artifact. The Solana technical details are illustrative; a real run pairs
> the build steps with a grounding/verification pass (see `../references/quality-bar.md` §5).

---

## Intake (the user's request)
*"Make a course that gets Solidity devs productive on Solana fast — they should walk away having shipped a
few real programs. Self-paced. They already know EVM/Solidity well."*

- **Audience / prior model:** EVM developers; strong Solidity/EVM mental model.
- **Desired outcome:** ship real programs, fast.
- **Format:** self-paced. **Credential:** on-chain (deployed-artifact / verify).

## Step 2 — Backward design (outcome + capstone FIRST)
- **Terminal outcome (Bloom: create):** *The learner can build, test, and deploy a PDA-backed SPL-token
  vault on devnet with correct signer/owner checks, and can explain how Solana's account model differs from
  EVM storage.*
- **Capstone:** ship an original small program (their choice) that uses an account/PDA + an SPL-token CPI,
  deployed to devnet, with a passing test suite. **Gated on the deploy + tests, not on watching.**

## Step 3 — Prerequisite DAG (entry point chosen by prior model)
EVM devs already have the state-machine model, so we **enter via 1:1 mappings** and defer the account model
for a couple of early wins (RareSkills inversion), then walk the hard chain:
`compute≈gas / errors≈revert (early wins) → account model → programs/instructions → PDAs → CPIs → SPL
tokens → (inline Footguns)`. Hard edges respected (accounts→programs→PDAs→CPIs→tokens).

## Step 4 — Routing decision
- **Backbone:** `map-from-known` opener → `challenge-ladder` (build outcome, motivated independent devs).
- **Guest (1):** `build-it-twice` on the **accounts/vault** artifact — the single biggest EVM divergence,
  where the native↔Anchor contrast teaches the most.
- **Lesson template:** `overview-lab-challenge`.
- **Security:** inline **Footguns** (not a full `security-epoch` — outcome is "ship," not "audit").
- Stacking budget: 1 backbone + 1 opener + 1 guest = within budget. ✓

## Step 5 — Module sequence (up the DAG, threading the artifact ladder)

| # | Module (driving question) | Artifact (ladder rung) | Pattern(s) | Diff | dominant_job(s) |
|---|---|---|---|---|---|
| 0 | "What maps 1:1 from Solidity — and what doesn't?" | toolchain + deploy hello | map-from-known + completion-loop | 1 | motivate / show-how |
| 1 | "Where did gas and revert go?" | add compute budget + custom errors | map-from-known | 1 | derive-why |
| 2 | "There are no storage variables — so where does state live?" | counter (account state) | concept-spine + overview-lab-challenge | 2 | derive-why |
| 3 | "Solidity had mappings; Solana doesn't. Now what?" | per-user PDA vault | challenge-ladder + **build-it-twice** | 2 | derive-why / show-how |
| 4 | "How do programs call other programs and move tokens?" | SPL-token deposit via CPI | challenge-ladder | 3 | show-how |
| 5 | "Ship your own." | freeform capstone | challenge-ladder | 3 | motivate |

Retrieval/interleaving: Module 4 reuses the PDA + account validation from Module 3; a cumulative checkpoint
precedes the capstone. Fading: worked examples in M0–M2, completion problems in M3, near-blank scaffold by
M4–M5.

## Step 6 — Two full lesson briefs (the handoff units)

### Brief 1 — Module 2, Lesson "Where state lives: accounts vs storage"
```yaml
lesson:
  id: state-lives-in-accounts
  title: "Where state lives: accounts, not storage variables"
  objectives:
    - {bloom: explain, statement: "explain why Solana programs are stateless and where their state lives"}
    - {bloom: implement, statement: "create and write to a data account from a program"}
  prerequisites: [hello-and-toolchain, compute-and-errors]
  hook: "In Solidity, `uint public count;` just... persists. You wrote to storage and forgot about it. Your first Solana program has nowhere to put `count`. Where did storage go?"
  concept_spec: "Programs are stateless code; state lives in separate accounts the caller passes in. Teach by building a counter whose value lives in a data account. One new element: the data account (defer PDAs to next lesson)."
  artifact_spec: "A counter program with an `initialize` and `increment`; the count stored in a plain data account."
  exercise_spec: "Completion: fill in the account's space/size (TODO). Solo: add a `decrement`. Accept: value persists across two separate transactions; test passes."
  the_tradeoff: "Separating code from state buys Solana parallelism (txs touching different accounts run concurrently) — BUT you must pass every account a program will touch, and size/rent it yourself up front."
  just_in_time:
    define: [account, data-account, rent, account-space]
    footguns: ["under-sizing the account", "forgetting the account is not auto-created"]
  assessment: "anchor test: increment persists across txs; reading back returns the new value."
  difficulty: 2
  fading: "fully worked counter shown; completion problem for sizing; solo for decrement"
  dominant_job: derive-why
  voice_notes: "contested 'why is it built this way' — Vitalik craft over Kaue's spine; the parallelism payoff is a great order-of-magnitude seam. Map from Solidity storage explicitly (map-from-known framing)."
  est_length: "1300 words / ~13 min"
```

### Brief 2 — Module 4, Lesson "Deposit a token: your first CPI"
```yaml
lesson:
  id: token-deposit-cpi
  title: "Deposit an SPL token: your first CPI"
  objectives:
    - {bloom: implement, statement: "transfer SPL tokens into a program-controlled account via a CPI"}
  prerequisites: [state-lives-in-accounts, per-user-pda-vault, spl-token-basics]
  hook: "Your vault holds SOL. Real protocols hold tokens. To move a user's USDC, your program has to call another program — the Token Program. How does one program call another?"
  concept_spec: "Cross-Program Invocation: invoke / invoke_signed; the vault PDA signs for itself. One new element: the CPI (token mechanics already taught)."
  artifact_spec: "Add a `deposit_token` instruction that CPIs into the Token Program to move tokens from the user's ATA into the vault's ATA."
  exercise_spec: "Completion: fill the CPI accounts struct (TODO). Solo: add `withdraw_token` with an owner check. Accept: deposit moves the balance; unauthorized withdraw fails."
  the_tradeoff: "CPIs make programs composable (your vault works with any SPL token) — BUT each adds compute cost and a trust surface; signing as a PDA means the seeds must match exactly or the CPI fails."
  just_in_time:
    define: [cross-program-invocation, invoke_signed, associated-token-account]
    footguns: ["wrong PDA seeds in invoke_signed", "missing owner check on withdraw", "unchecked token mint"]
  assessment: "anchor test: token balance moves on deposit; withdraw by non-owner reverts."
  difficulty: 3
  fading: "CPI accounts shown once; completion problem for the struct; solo for withdraw"
  dominant_job: show-how
  voice_notes: "documented mechanism → Helius expository craft; flag security footguns inline (Footguns dose, not a full epoch)."
  est_length: "1400 words / ~14 min"
```

## Step 8 — Quality-bar spot check
Outcome measurable + capstone proves it ✓ · DAG respected (accounts→PDA→CPI→tokens) ✓ · every concept in an
artifact ✓ · load managed (one new element/lesson, JIT) ✓ · fading visible (worked→completion→solo across
M0–M5) ✓ · gated on deploy+tests ✓ · trade-offs named in both briefs ✓ · both briefs carry hook +
trade-off + `dominant_job` ✓ · 1 backbone + 1 opener + 1 guest ✓ · tight (6 modules, ship-focused) ✓.

## Step 9 — Handoff
The course spec + the six modules' briefs go to `writer-style`. Brief 1 routes **Vitalik craft over
Kaue's spine** (`derive-why`); Brief 2 routes **Helius** (`show-how`). The writer adds the prose, the
pain-first hooks in Kaue's register, the LATAM stakes, and the sign-offs — structure already decided.
