# NEXT TO WRITE — hello-and-toolchain  (module: module-first-program)

Status: {'briefed': 3, 'researched': 0, 'drafted': 0, 'verified': 0, 'published': 0} · paste the block below into `/write-in-voice` (default pack: kaue).
The dominant_job (motivate) routes the voice. Frozen facts follow — you may shortcut Pass A.

```yaml
lesson:
  id: hello-and-toolchain
  title: "Get a program on-chain in ten minutes"
  objectives:
    - bloom: implement
      statement: "deploy a hello-world program to a local validator and read its log"
  prerequisites: []
  hook: "You've shipped web2 services for years. Today you'll put real code on a public computer that no one — not even you — can quietly change. That shift is the whole game."
  concept_spec: "What a Solana program is (a stateless, deployed function) and the dev loop: build, deploy, invoke, read logs. Worked example: the default hello-world."
  artifact_spec: "Build and deploy the hello-world program to a local validator; invoke it; see the greeting in the logs."
  exercise_spec: "Completion: change the logged message and redeploy. Solo: add a second log line. Accept: the new message shows in the validator logs."
  the_tradeoff: "A local validator is instant and free but throws away state on restart — great for the loop, useless as a record. We move to devnet once the program is real."
  just_in_time:
    define:
      - program
      - validator
      - log
    footguns:
      - "forgetting to rebuild before redeploy"
      - "pointing the CLI at the wrong cluster"
  assessment: "deploy hello-world locally and show the changed log line"
  difficulty: 1
  fading: worked
  dominant_job: motivate
  voice_notes: "course opener; spine carries it; the felt 'no one can change it' shift is the hook."
  est_length: "900 words / ~9 min"
```

## Frozen facts (verified — do NOT change these numbers/identifiers)
_(no pre-verified facts — writer runs full Pass A)_

## After the writer returns
1. Save the prose to: `lessons/drafts/m00-l1-hello-and-toolchain.md`
2. Validate with writer-style's own tools (set $WRITER to the writer-style skill dir):
   `python3 "$WRITER/tools/validate_voice.py" diff  --facts lessons/facts/m00-l1-hello-and-toolchain.facts.md --styled lessons/drafts/m00-l1-hello-and-toolchain.md`
   `python3 "$WRITER/tools/validate_voice.py" tells --file lessons/drafts/m00-l1-hello-and-toolchain.md --card "$WRITER/profiles/kaue/kaue.card.yaml"`
3. Set `hello-and-toolchain` → `drafted` in `_state.yaml` (then `verified` once diff passes).
4. Re-run `scaffold_course.py emit` (or re-render this file) for the next lesson.
   Batch check after several drafts: `python3 "$WRITER/tools/validate_voice.py" audit --lessons lessons/drafts/`
