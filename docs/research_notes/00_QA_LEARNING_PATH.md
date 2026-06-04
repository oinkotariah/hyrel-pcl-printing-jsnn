# Q&A Learning Path — what we worked through (and the answers)

*Companion to `00_PROJECT_HANDOFF.md`. The handoff captures the project **state**; this captures the **path** — the questions Nengi actually worked through and the key answers — so the new chat knows what's already understood and doesn't re-explain it. Paste **both** into the co-op chat.*

---

## Phase 1 — G-code & the travel-speed bug
- **Q: What does F mean?** → F = **feedrate** (toolhead speed, mm/min), *not* filament/extrusion speed. It's **sticky** — only re-written when the speed changes. ÷60 for mm/s.
- **The Day-1 bug:** slicer wrote only one F (F1500 = 25 mm/s) because every speed in the INI was 25 → **travel ran at print speed → ooze/stringing.** Fix: `travel_speed` → 60 (F3600), or patch the G-code.
- **Q: Why does the E value steadily increase?** → **Absolute extrusion (M82):** E is a cumulative odometer, not per-move. Per-move amount = subtract consecutive E's. Volumetric (`M229`) → E in mm³.
- **Consequence:** in absolute mode you **can't** hand-insert `G1 E-1.5` to retract (it's an absolute target, not a pullback). Use Hyrel **M729 / M727 (unprime / prime)** — they don't touch the E odometer — or re-slice with retraction on.
- **Where unprime goes:** at the **E↔no-E boundaries** (last print move → travel → first print move). The "snail line" between circles = the **travel move** curling around because *avoid-crossing-perimeters* is enabled.
- **Q: Control unprime from PrusaSlicer?** → set `retract_length` > 0, but PrusaSlicer emits **E-retraction (`G1 E…`), not M729** — so if the lab wants M729, that's a hand-edit/post-process. Gotcha: *"only retract when crossing perimeters"* can skip retraction on clean hops. Also flagged the **240 °C temp commands** (ABS-profile leftover) to neutralize before running PCL.

## Phase 2 — Printer hardware failure
- **Q: Printer shows 1000, head won't heat, some heads missing.** → "1000" = a **temperature-sensor fault** (open thermistor reads garbage; firmware cuts heat as a *protection*, so the cold head is the safety working). Check the **E-Stop**, press the front **RESET**, check head **LEDs** (flashing = communicating), **reseat** heads; USB/COM if total comms loss. **Multiple heads down = stop and get Nick** (controller/CANBUS/power, not a setting).

## Phase 3 — PrusaSlicer learning
- Workflow: load STL → pick 3 profiles → Slice → preview → Export G-code. **Beginner mode hides travel speed & retraction → switch to Expert.** Four tabs (Plater / Print Settings / Filament / Printers); left-side gizmos (move / scale / rotate / place-on-face / measure). Sliced a test box to see the loop.

## Phase 4 — The pivot
- **Bone scaffolds → flexible electronics.** PCL becomes the flexible *substrate*; add a conductor. Learned conducting-polymer basics: **conjugation** (alternating bonds → delocalized "electron cloud"), **doping** (conceptually like doping silicon — adds carriers), **PANI** oxidation states + the **acid on/off switch** (emeraldine base → salt).

## Phase 5 — Materials understanding
- PCL fundamentals (Tg −60 °C, Tm ~60 °C, MW↔crystallinity, solubility, degradation). **Solvent casting vs melt processing.** **Percolation threshold** (enough graphite to form a connected network; target just above it to keep flexibility). **Sonication** for dispersion.

## Phase 6 — The brittleness diagnosis (a clean worked path)
- **Q: Printed PCL is brittle but the notes say "rubbery" — is it a thermoset that changed on heating?** → **No — PCL is a thermoplastic** (melts reversibly, doesn't cure/crosslink). "Rubbery" was an oversimplification: PCL is **semi-crystalline** (amorphous part = rubbery, crystalline part = rigid).
- Candidate causes weighed: printing-induced crystallinity (Liu), thin-geometry/weak fusion, or **thermal degradation**.
- **Printed at 60 °C onto a room-temp plate** → rules out degradation (60 °C is safe). With **14k → then 8k** PCL, the brittleness is mostly the **low MW itself** (few chain entanglements = brittle, and more crystalline) plus cold-plate quench → poor inter-bead fusion. ("PCL 300" flagged to confirm.)

## Phase 7 — Process / the pressure question
- **Q: Extrude (pressured) vs mould-cast (no pressure) — how does pressure affect results?** → Pressure/shear **aligns** crystals *and* graphite flakes → **anisotropic** conductivity (extrude) vs **isotropic** (cast); pressure **compacts** the network (can lower resistance); different **void** behavior (weld-lines vs trapped bubbles); the screw **mixes**. **Rule: use one route for all 5 ratios.** Cast = cleaner intrinsic baseline; extrude = closer to the real device.

## Phase 8 — Measurement & pitfalls (max-depth, all papers)
- Decided: measure **intrinsic** conductivity via multimeter on dog-bones (R → σ).
- 9 pitfalls surfaced (full detail in handoff §6): contact resistance / 4-point probe, dog-bone **geometry** (measure actual cross-section), **range** ("OL" = below percolation, not failure), graphite **settling**, **aging** drift, 8k **brittleness** handling, **nozzle size as a confound**, **clogging** at small-nozzle/high-graphite, **combinatorial blowup**.
- Key decision (handoff §7): for **intrinsic** conductivity, fix one nozzle / cast and sweep **graphite % only**; nozzle×graphite is a separate *process* study.

## Phase 9 — Papers
- Built: `abstracts_and_materials` (5 papers, PDF page locations), `source_referenced_facts` (cited), `05_liu_section3` crystallography decoder. Roles: **Yuk** = north star, **Zhang** = PCL-DIW how-to, **Teixeira** = optimization method, **Liu** = crystallinity, **Woodruff** = background.

---

## Also exists / threads
- **GitHub repo** `oinkotariah/hyrel-pcl-printing-jsnn` (gcode, configs, scripts, docs). **Nick added as collaborator.**
- **Non-research:** flight changed to go retrieve the car; **CEE&I / Shawn Johnson** + the **Dr. Curry email** action item (warm draft already written). (Dr. Curry also drew a doodle "balance the equation" puzzle — a stoichiometry gag, not project-relevant.)
