# Instructional-design canon — the load-bearing frameworks (with Solana implications)

The evidence base under the design spine. Read this when you need the *why* behind a spine rule, or when a
course is unusual enough that the defaults don't obviously apply. Each entry: the idea in a sentence or two,
then the concrete implication for a Solana course.

---

**Backward design — Understanding by Design (Wiggins & McTighe).** Design in three stages from the end:
desired results → acceptable evidence → learning activities. → Start every course from a measurable
terminal outcome and its capstone; derive modules from it. Never topic-list first. (Spine §1.)

**Bloom's taxonomy + measurable objectives.** Six rising levels — Remember, Understand, Apply, Analyze,
Evaluate, Create — each with action verbs that make objectives testable. → Tag every objective with a Bloom
verb and target level; the course should climb (define → implement → analyze → design). Ban
"know/understand" as objective verbs.

**Cognitive Load Theory (Sweller) — intrinsic / extraneous / germane.** Working memory is tiny; cut
extraneous load, manage intrinsic, protect germane. → Provide a scaffold/toolchain (kills extraneous load);
one new element at a time; diagrams next to code; never Rust lifetimes + Anchor macros + on-chain semantics
at once. (Spine §4.)

**Worked-example effect + faded examples + completion problems (Sweller, Renkl, Kalyuga).** Novices learn
more from studying complete worked examples than from unguided problem-solving; fade support step-by-step;
worked examples *hurt* once learners are proficient (expertise reversal). → worked example → completion
problem (TODOs) → from-scratch, faded across the module; drop worked examples in advanced modules.
(Spine §5; the `completion-loop` and `overview-lab-challenge` patterns.)

**Scaffolding & Zone of Proximal Development (Vygotsky; Wood/Bruner/Ross); fading.** Target tasks just
beyond independent ability; give temporary, contingent support; withdraw it as competence grows. → The
difficulty curve *is* a fading schedule; pitch each exercise just above current ability. (Spine §5, §10.)

**Spaced repetition, retrieval practice (testing effect), interleaving.** Retrieval beats rereading; spacing
and interleaving beat massing. → End modules with retrieval (not rereading); reuse earlier concepts in
later projects; interleave problem types; add a cumulative checkpoint. (Spine §9; the 101/201 spiral.)

**Project-/problem-based learning; constructivism.** Learners construct knowledge by solving authentic
tasks; PjBL produces a learner-directed artifact, PBL solves a posed problem. → Anchor every module in a
real, shippable artifact + a driving question. (Spine §3; the `challenge-ladder` pattern.)

**Merrill's First Principles of Instruction.** Learning is promoted when instruction is task-centered and
cycles Activation → Demonstration → Application → Integration. → Per-module template: real task → activate
prior (link web2/Rust/earlier module) → demonstrate (worked program) → apply (build, fading) → integrate
(extend / use in capstone).

**Gagné's Nine Events of Instruction.** A nine-step lesson sequence: gain attention → state objectives →
recall prior → present content → provide guidance → elicit performance → give feedback → assess → enhance
retention/transfer. → The lesson-level checklist behind `overview-lab-challenge`.

**4C/ID (van Merriënboer) — for complex skills.** Complex skills need Learning Tasks (authentic, whole,
easy→hard with diminishing support), Supportive Information, Procedural Information (just-in-time), and
Part-Task Practice. → Whole-task projects from the start, graduated; concept info and CLI/Anchor steps
just-in-time; part-task drills for error-prone routines (account constraints, PDA seeds). The master frame
for sequencing a *whole* developer curriculum.

**Productive failure (Kapur).** Attempting (and often failing) a hard problem *before* instruction deepens
understanding and transfer. → Occasionally pose the challenge before the clean solution ("try to stop this
double-spend"); pairs with exploit-first security. (Spine §8; the `security-epoch` pattern.)

**Concrete-before-abstract / concreteness fading; examples-first; just-in-time.** Start concrete, fade
toward the general/abstract; introduce concepts exactly when needed. → A specific token transfer before the
general CPI/account model; don't front-load rent/BPF/Sealevel before there's a program to attach them to.
(Spine §4.)

**Prerequisite mapping / learning hierarchies (Gagné).** Mastering a capability requires first mastering its
subordinate skills; sequence up the hierarchy. → Build the Solana prerequisite DAG first
(`solana-syllabus-dag.md`); ensure no module depends on an un-taught skill; gate advanced tracks.
(Spine §2.)

---

### The one-paragraph mandate
Architect backward from a Bloom-tagged terminal outcome + capstone; map the prerequisite DAG and gate on
it; structure as graduated whole-task projects with diminishing support; run each module through
Merrill/Gagné; manage cognitive load via a scaffold and one-concept-at-a-time, concrete-first,
just-in-time; teach via worked-example → completion → solo that fades; invert occasionally with
productive-failure/attack-first; and bake in spaced retrieval, interleaving, and a spiral for retention.
