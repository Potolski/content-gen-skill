# Form: litepaper

The canonical design-of-record a protocol/token ships at launch: abstract →
problem → mechanism → tokenomics → risks. The reader comes out able to **cite the
design**. Register is the corpus's most impersonal — third-person, declarative,
versioned in place (never serialized). Pseudocode and account/instruction schemas
only; **never application code**.

**Scope guard:** this form authors *litepapers* (one docs page to ~8pp, not
proof-bearing). Formal **whitepapers** (machine-checked proofs, 10–40pp academic
PDFs) are out of scope as deliverables — they are *source documents* the other
forms cite. If correctness itself is the pitch (consensus, oracle, AMM
invariants), the ask needs auditors, not this skill; offer a litepaper + an
`explainer` derivation instead. And if there is neither a novel mechanism nor a
token, the Solana-native answer is docs + a SIMD/repo, not a paper.

**Length band:** 1500–5000 words. **Visuals default:** `light` (one architecture
figure + one value-flow figure earn their keep; decoration doesn't).

## Brief extras (beyond §F core)
- `protocol_ref` — name, cluster, program IDs / repo if deployed; version of this
  paper (`v0.x`, revised in place).
- `mechanism_claims` — the 3–7 load-bearing design claims, each grounded.
- `tokenomics` — supply, allocation, emission, the value-flow loop (or explicitly
  `none` — then justify why a paper at all).
- `risk_register` — real attacks/failure modes + stated trust assumptions
  (thresholds, honest-majority requirements); a risks section that names nothing
  is marketing.
- `paired_artifact` — the SIMD / reference implementation / docs the paper ships
  with. Never a lonely PDF.

## Structure recipe (the output IS)
1. **Abstract** — the result first, with a hard number where one exists.
2. **Problem** — the gap, grounded; no market-size hand-waving.
3. **Mechanism** — the design, schema-and-pseudocode level, one subsection per
   `mechanism_claims` entry.
4. **Tokenomics** — the value flow, with the emission math shown, not asserted.
5. **Risks & trust assumptions** — the adversarial section, written for real.
6. **Roadmap + paired artifact** — future work and where the code/spec lives.
7. **Disclaimer** — the standard non-solicitation boilerplate, dated.

## Checklist
- [ ] Abstract leads with the result + a number; impersonal register throughout.
- [ ] No application code; schemas/pseudocode only.
- [ ] Risk section names specific attacks and thresholds — not platitudes.
- [ ] Every mechanism/tokenomics number grounded; paper versioned + dated.
- [ ] `paired_artifact` present; popularization routed to `explainer`, not inlined.
