# NEXT TO WRITE — the-exploit-mindset  (module: module-offense)

Status: {'briefed': 6, 'researched': 0, 'drafted': 0, 'verified': 0, 'published': 0} · paste the block below into `/write-in-voice` (default pack: kaue).
The dominant_job (show-how) routes the voice. Frozen facts follow — you may shortcut Pass A.

```yaml
lesson:
  id: the-exploit-mindset
  title: "Break it before you defend it"
  objectives:
    - bloom: analyze
      statement: "find and trigger a planted vulnerability in a small Solana program"
  prerequisites: []
  hook: "You've shipped programs that 'worked.' Here's one that works too — and drains its vault in one transaction. Your job today isn't to fix it. It's to break it."
  concept_spec: "The auditor's mindset: assume every account and input is hostile. Worked example: an unguarded withdraw that anyone can call. One new element: reading a program adversarially."
  artifact_spec: "A vulnerable counter-vault program; the learner writes a test that drains it."
  exercise_spec: "Completion: finish the exploit test that calls withdraw as the wrong signer (TODO). Solo: find a second way to break it. Accept: the exploit test passes (the program is drained)."
  the_tradeoff: "Exploit-first teaches the why fast, BUT it's only safe on intentionally vulnerable code — never run these moves on programs you don't own."
  just_in_time:
    define:
      - threat-model
      - invariant
      - attacker-controlled-input
    footguns:
      - "assuming the happy path is the only path"
      - "trusting an account because it has the right shape"
  assessment: "the learner's exploit test drains the vulnerable program"
  difficulty: 2
  fading: worked
  dominant_job: show-how
  voice_notes: "security: be wary of Hotz reductive collapse — exploits are concrete, don't over-simplify the fix. Helius expository craft."
  est_length: "1300 words / ~13 min"
```

## Frozen facts (verified — do NOT change these numbers/identifiers)
_(no pre-verified facts — writer runs full Pass A)_

## After the writer returns
1. Save the prose to: `lessons/drafts/m00-l1-the-exploit-mindset.md`
2. Validate with writer-style's own tools (set $WRITER to the writer-style skill dir):
   `python3 "$WRITER/tools/validate_voice.py" diff  --facts lessons/facts/m00-l1-the-exploit-mindset.facts.md --styled lessons/drafts/m00-l1-the-exploit-mindset.md`
   `python3 "$WRITER/tools/validate_voice.py" tells --file lessons/drafts/m00-l1-the-exploit-mindset.md --card "$WRITER/profiles/kaue/kaue.card.yaml"`
3. Set `the-exploit-mindset` → `drafted` in `_state.yaml` (then `verified` once diff passes).
4. Re-run `scaffold_course.py emit` (or re-render this file) for the next lesson.
   Batch check after several drafts: `python3 "$WRITER/tools/validate_voice.py" audit --lessons lessons/drafts/`
