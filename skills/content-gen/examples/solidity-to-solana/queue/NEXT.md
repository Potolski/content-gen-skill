# NEXT TO WRITE — hello-and-toolchain  (module: module-mappings)

Status: {'briefed': 6, 'researched': 0, 'drafted': 0, 'verified': 0, 'published': 0} · paste the block below into `/write-in-voice` (default pack: kaue).
The dominant_job (motivate) routes the voice. Frozen facts follow — you may shortcut Pass A.

```yaml
lesson:
  id: hello-and-toolchain
  title: "Your Solidity instincts, mapped onto Solana"
  objectives:
    - bloom: implement
      statement: "build and deploy a hello-world program and name its EVM equivalents"
  prerequisites: []
  hook: "You can read Solidity in your sleep. Most of that intuition transfers to Solana — until it suddenly, expensively doesn't. Let's get a program deployed and find the seams."
  concept_spec: "The 1:1 map: program≈deployed contract, instruction≈function, signer≈msg.sender, compute≈gas. Worked example: deploy hello-world and read the log. One new element: the build/deploy/invoke loop."
  artifact_spec: "Build and deploy hello-world to a local validator; invoke it; see the greeting in the logs."
  exercise_spec: "Completion: change the logged message (TODO) and redeploy. Solo: add a second instruction. Accept: both messages appear in the logs."
  the_tradeoff: "Leading with EVM mappings gets you productive fast, BUT a few of those mappings are traps — the account model (next modules) is where the analogy breaks."
  just_in_time:
    define:
      - program
      - instruction
      - signer
    footguns:
      - "assuming a contract holds its own state"
      - "wrong cluster in the CLI"
  assessment: "deploy hello-world and show a changed log line"
  difficulty: 1
  fading: worked
  dominant_job: motivate
  voice_notes: "course opener; spine carries it; the 'until it expensively doesn't' line is the hook."
  est_length: "1000 words / ~10 min"
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
