# Catalog: Solana technical talk decks & workshop presentations

Real, currently-reachable exemplars of the *slide deck / talk* form in the Solana
ecosystem (verified reachable July 2026). Each entry: **Title** — Author/Org — URL —
(year) — one original sentence on why it exemplifies the form + a structural note.

IP note: entries are metadata + one original characterizing sentence. No third-party slide
or transcript text is reproduced. Where a deck ships only as a recording, that is noted —
it is the ecosystem's dominant distribution reality for this form.

---

## Open-licensed instructor decks & workshops (source available)

1. **Solana Professional Education** — Solana Foundation / solana-developers — https://github.com/solana-developers/professional-education — (2023–24, CC-BY-SA-4.0) — The canonical open-licensed instructor deck: a multi-day course delivered as Keynote decks with an `AGENDA.md`, instructor notes, and lab solutions. *Structure: 4-day / 12-day arc — cryptography → accounts & transactions → tokens & metadata → Anchor → escrow; one-idea-per-slide with hands-on labs between beats.*

2. **Build your first DeFi app in 30 minutes** — solana-developers (same repo) — https://github.com/solana-developers/professional-education/tree/main/presentations — (2023, CC-BY-SA-4.0) — A condensed conference-talk deck distilling the course into a single 30-minute demo-led session. *Structure: hook → minimal concept beats → live build → recap; the short-talk counterpart to the full course.*

3. **Solana 101** — Joe Caulfield / Solana-Workshops — https://github.com/Solana-Workshops/solana-101 — (2023) — A reusable Hacker House opener deck (Google Slides, delivered at Melbourne and Ho Chi Minh City) covering Solana basics for newcomers. *Structure: distributed-systems framing → accounts → transactions → programs; thin deck paired with recorded walkthroughs.*

4. **Solana Developer Workshops (11 workshops)** — solana-developers — https://github.com/solana-developers/workshops — (2022–24, MIT) — A workshop collection where each README is the talk scaffold and the repo is the live-demo target (NFT Minter, Solana Twitter, Token Swap, Solana Pay storefront, xNFT, and more). *Structure per workshop: objectives → prerequisites → guided build steps → deploy; the deck is thin, the terminal does the work.*

5. **Neodyme Breakpoint Security Workshop** — Neodyme — https://github.com/neodyme-labs/neodyme-breakpoint-workshop (hosted: https://workshop.neodyme.io) — (2022–23) — An exploit-first security workshop where the audience breaks progressively harder programs before seeing the fix. *Structure: mdBook + `level0`→`level4` challenge folders, each a vulnerability class (signer/owner checks, math, PDA misuse) to break then patch.*

6. **Writing Optimized Solana Programs (Scale or Die / Accelerate 2025)** — Dean Little (Blueshift), transcription by Laugharne — https://github.com/Laugharne/solana_optimized_programs — (2025) — A CU-optimization talk preserved as a timestamped transcription with code, exemplifying the benchmark-driven dev talk. *Structure: problem (wasted CU) → framework comparison (Anchor vs Pinocchio vs assembly) → live-coded sBPF → size/CU metrics → takeaway.*

---

## Conference talks (distributed as recording; deck embedded in video)

7. **Breakpoint 2023: Firedancer Update** — Dan Albert (Jump) — https://youtu.be/hEEWMiMuEF8 — (2023) — The recurring flagship infra keynote: a status-and-vision talk on the second validator client. *Structure: where-we-were → what-shipped → benchmarks → roadmap; slides are backdrop to a spoken update.*

8. **Breakpoint 2024 Keynote: Fast Forward from Frankendancer to Firedancer** — Kevin Bowers (Jump) — https://solanacompass.com/learn/breakpoint-24/breakpoint-2024-keynote-fast-forward-from-frankendancer-to-firedancer-kevin-bowers — (2024) — A performance-reveal keynote culminating in a 1M-TPS-on-commodity-hardware demo, the archetypal "proof is the climax" talk. *Structure: ceiling problem → architecture → live throughput demo → what's next.*

9. **Breakpoint 2024: Fuzzing Comes to Solana (Trident)** — Viktor Fischer (Ackee/Aki) — https://solanacompass.com/learn/breakpoint-24/breakpoint-2024-technical-talk-fuzzing-comes-to-solana-viktor-fischer — (2024) — A tool-launch talk where the test harness *is* the subject, opening on Solana's share of hack losses. *Structure: threat framing → tool intro → integration steps → adoption CTA.*

10. **Breakpoint 2024: Efficient Solana Programs (Peregrine product keynote)** — Breakpoint 2024 — https://solanacompass.com/learn/breakpoint-24/breakpoint-2024-product-keynote-efficient-solana-programs — (2024) — A framework-launch keynote pitching a low-overhead program-building approach. *Structure: cost problem → framework reveal → benchmark comparison → try-it ask.*

11. **Breakpoint 2023: A Fireside Chat on Solana Security** — Anatoly Yakovenko & Thomas Lambertz (Neodyme) — https://solanacompass.com/learn/breakpoint-23/breakpoint-2023-a-fireside-chat-on-solana-security-with-anatoly-yakovenko-and-thomas-lambertz — (2023) — The (near) slide-less variant of the form: a fireside where the "deck" is the conversation, useful as a contrast case for when *not* to build slides. *Structure: theme prompts → discussion; no concept-beat slides.*

12. **Breakpoint 2023: Know Your Why — Demystifying Building on Solana** — Jeff Paul — https://solanacompass.com/learn/breakpoint-23/know-your-why-demystifying-building-on-solana — (2023) — A motivation-register talk aimed at onboarding builders rather than teaching an API. *Structure: why-build hook → ecosystem map → paths-in → CTA; concept-light, framing-heavy.*

13. **Breakpoint 2023: School of Solana by Ackee Blockchain** — Ackee Blockchain — https://solanacompass.com/learn/breakpoint-23/breakpoint-2023-school-of-solana-by-ackee-blockchain — (2023) — A talk *about* an education program (the full course lives elsewhere), showing how an org promotes an evergreen curriculum from a conference stage. *Structure: problem (dev shortage) → program overview → outcomes → enroll ask.*

14. **Breakpoint 2023: FPGA Working at 8M TPS** — Kaveh Aasaraai & Kevin Bowers (Jump) — https://youtu.be/1oQg2_b_gv8 — (2023) — A deep-tech research talk demonstrating an extreme throughput result on old hardware, the "surprising benchmark" sub-genre. *Structure: claim → method → live/recorded result → implications.*

---

## Standalone slide hosts (SpeakerDeck) & aggregators

15. **Getting Started with Solana Blockchain Development: A Developer's Roadmap in 2025** — ATH Infosys — https://speakerdeck.com/athinfosys/getting-started-with-solana-blockchain-development-a-developers-roadmap-in-2025 — (2025) — A thin marketing/roadmap deck (7 slides) showing the low-density, no-code end of the form's spectrum. *Structure: intro → why-Solana → architecture → tooling → setup → conclusion; one topic per slide, no code.*

16. **Solana Blockchain on Azure** — Asif Waquar — https://speakerdeck.com/asifwaquar/solana-blockchain-on-azure — (2023) — An integration/infra meetup deck hosted as standalone slides, illustrating SpeakerDeck as a (rarer) durable slide channel. *Structure: platform framing → deploy steps → wrap.*

17. **Solana Compass — Breakpoint 2023 learn hub** — Solana Compass — https://solanacompass.com/learn/breakpoint-23 — (2023–) — The de-facto archive: dozens of Breakpoint talks with recordings + AI transcripts + summaries, the primary place this form is *consumed* after the event. *Structure: indexed talk directory; each entry = video + generated notes.*

18. **solsec — Solana smart-contract security resources** — Sanny Kim (curated) — https://github.com/sannykim/solsec — (2022–, curated) — A resource hub linking many security *talks and slide decks*, useful for sourcing more exemplars of the security sub-genre. *Structure: curated link list grouped by topic (auditing, exploits, tooling).*

---

_Distribution reality worth flagging for the writer: entries 7–14 ship as **video first**;
the standalone deck (PDF/SpeakerDeck) is the exception, not the rule. The durable artifacts
are the recording, the paired repo (workshops), and the resources slide — which is why the
skill's emphasis on the speaker-notes track is well-aimed._
