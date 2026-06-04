# PROJECT HANDOFF — JSNN / IMPACT Lab Co-op

*Paste this into a fresh chat to restore full context. The new (co-op) chat already has most of the paper PDFs, so this is **context + decisions + plan**, not a re-dump of the papers.*

**How to use:** paste this whole file + a one-liner about what you need right now (e.g., "standing at the bench, about to mix the first composite batch — walk me through it"). The 5 PDFs are already attached in the co-op chat.

---

## 0. Snapshot
- **Nengi (Onengiyeofori Inko-Tariah)** — EE sophomore (AAMU), on an **NSF REU at the IMPACT Lab, JSNN** (NC A&T + UNCG). Mentor: **Nick Ricks**.
- **Current project:** a **flexible conductive polymer composite** — polycaprolactone (PCL) loaded with **graphite** — formed into **dog-bone specimens** to find the **percolation threshold** (conductivity vs graphite loading). Poster now, paper later.

## 1. The pivot (read first)
- Started as **PCL for bone-tissue-engineering scaffolds**.
- **Pivoted to flexible electronics:** Nick isn't pursuing bone; the goal is flexible electronics using **PCL as a flexible substrate + a conductor** (graphite filler, possibly **polyaniline/PANI** later).
- So all bone/scaffold material in the notes is **background**; the live application is a flexible *conductive* composite.

## 2. Goal
- Make **PCL + graphite** composites and **measure the sample's intrinsic conductivity** (multimeter → resistance → conductivity) across graphite loadings → **percolation plot** (conductivity vs graphite %) for the poster.

## 3. Materials
- **PCL 8,000 MW** for the composite (low-MW → low viscosity, easy to mix; but **brittle + more crystalline**).
- Earlier work used **PCL 14,000** (also brittle/low-MW).
- A **"PCL 300"** was called "the flexible one" — **CONFIRM with Nick** (its MW + whether it's the matrix or a plasticizer; low MW alone = *more* brittle, so "flexible" only makes sense if it's a soft additive).
- **Graphite** = conductive filler. Possibly **PANI** as an intrinsic conductor later.

## 4. Equipment & fabrication routes
- **Hyrel SYSTEM 30M** (DIW/melt extrusion), run via **Repetrel**. **Printer is currently down** — heads/nozzles reordered, Nick emailing Hyrel.
- Two fabrication routes:
  - **A. Extrude/print** dog-bones via the heated head (pressured + sheared).
  - **B. Melt in a beaker (no pressure) → pour into dog-bone moulds** (fallback if printer stays down).
- Either route yields composites + conductivity data → **the poster works with or without the printer.**

## 5. Experiment plan
- **5 graphite loadings**, ~**10–30%** (likely 10/15/20/25/30% — confirm spacing & wt% vs vol%).
- Form dog-bones, measure conductivity, plot vs loading → percolation threshold.
- **Replicates (n≈3)** per condition for credibility.

## 6. Critical pitfalls / cautions (from a full read of the 5 papers)
1. **Contact resistance** — 2-point multimeter includes probe/lead resistance, worst on the **conductive (high-graphite)** samples. Yuk used a **4-point probe**; at minimum use fixed **silver-paste contacts**, not hand-pressed tips.
2. **Geometry** — dog-bone cross-section isn't uniform; probe the **straight gauge** and **measure the actual cross-section** (don't assume nozzle/CAD size). σ = L/(R·A).
3. **Range** — insulating (low-graphite) samples may read **"OL"** on a handheld meter — expected (below percolation), not a failure. Use an instrument spanning the range.
4. **Graphite settling** — in low-viscosity 8k melt (esp. no-pressure cast), graphite sinks → conductivity gradient. Stir right before pouring; thin parts / short melt time.
5. **Aging** — PCL keeps crystallizing for hours-days → conductivity & brittleness drift. **Measure every sample at the same age.**
6. **8k brittleness** — samples crack on handling/clamping → broken network → erratic readings.
7. **Nozzle size is a confound, not a neutral knob** — smaller nozzle → more shear → aligns particles → higher/anisotropic conductivity (Yuk). Varying nozzle measures a *process* effect, not intrinsic material conductivity.
8. **Unprintable corner** — small nozzle + high graphite % → clogs.
9. **Combinatorial blowup** — full nozzle×graphite×replicate grid = dozens of samples (the "days"). **Screen the printable window first** (Teixeira), don't brute-force.

## 7. The key strategic decision (raise with Nick)
- Goal = **intrinsic** conductivity → **fix one nozzle (or cast), sweep graphite % only.** ~15 samples, clean curve.
- If instead studying **how print settings change the printed part** → nozzle×graphite is the right (bigger) *process* study, but it describes the printed part, not the material.
- Nozzle size is the crux; the two goals are in tension.

## 8. The 5 papers & roles (PDFs already in the co-op chat)
- **Yuk et al. 2020** (Nat. Commun. 11, 1604) — ***north star***: 3D printing a conductor (PEDOT:PSS); <5% conductivity drop over 10,000 bends; percolation via dry-annealing; 4-point conductivity.
- **Zhang et al. 2021** (Prog. Nat. Sci. Mater. Int. 31, 180–191) — PCL DIW how-to; ink rules (shear-thinning + >80% recovery); **DCM beats acetone**.
- **Teixeira et al. 2026** (MRS Commun. 16, 212–218) — parameter-optimization method (sweep, measure accuracy by area, find printable window). Directly applicable.
- **Liu et al. 2018** (Macromol. Mater. Eng. 303, 1700494) — melt extrusion changes PCL crystallinity/orientation; why printed PCL came out brittle. (Crystallography deep-dive parked for the "Drakes" polymer class.)
- **Woodruff & Hutmacher 2010** (Prog. Polym. Sci. 35, 1217–1256) — broad PCL review; now background.

## 9. Open questions for Nick
1. Graphite ratios + **wt% vs vol%**.
2. Conductor: graphite only, or graphite + PANI?
3. What **"PCL 300"** is (MW + role).
4. Fallback (mould) route step order; what the **blender** step is for.
5. **Mechanical** (tensile) testing in scope, or electrical only?
6. Intrinsic-conductivity **vs** process-study question (§7) — decides whether to sweep nozzle.
7. Repo notes — keep bone framing as background?

## 10. File manifest (everything produced)
**Canonical notes — use these (`research_notes/`):**
- `00_README.md` — index / reading order
- `01_PCL_fundamentals_review.md` — PCL fundamentals (cited)
- `02_conducting_polymers_PANI_primer.md` — conducting polymers & PANI (cited)
- `03_printing_and_preparation.md` — fabrication methods (cited)
- `04_conductive_composite_gameplan.md` — the experiment plan (cited)
- `05_liu_section3_crystallography_decoder.md` — plain-English XRD/crystallography decoder

**Other current files (top level):**
- `abstracts_and_materials.md` — all 5 papers' abstracts + materials, with PDF page locations
- `source_referenced_facts.md` — poster-ready facts, each with page/figure citation
- `papers.md` — reference list (has bone-composite refs; some framing now background)
- `print_run_log.md` — one-row-per-attempt experiment log template (still useful for the composite runs)

**Pre-pivot / historical (from the Day-1 travel-speed fix; keep for the record):**
- `mock_paper_PCL_DIW_travel_fix.md` — early mock paper
- `travel_fixed_ANNOTATED_READING_COPY.gcode` — annotated G-code

**Superseded (replaced by the `research_notes/` versions — kept for completeness):**
- `PCL_review_summary_notes.md` → use `research_notes/01`
- `conducting_polymers_PANI_primer.md` → use `research_notes/02`
- `printing_and_preparation_summaries.md` → use `research_notes/03`
- `conductive_composite_gameplan.md` → use `research_notes/04`

## 11. How I've been helping (so the new chat matches the style)
- Paper claims get **inline citations with page/figure** (e.g., "(Yuk 2020, p.4, Fig.3)"); general/textbook facts are **left uncited rather than faking a source**.
- **Honest flags** when something could undermine the experiment or doesn't match the stated goal — with mitigations.
- Step-by-step, structured deliverables; explanations tied to actual files/photos.

## Other threads (non-research, low priority)
- **Entrepreneurship / CEE&I at NC A&T:** met director **Shawn Johnson** (brief pitch coaching). Action item — email **Dr. Curry** to get on CEE&I updates (a warm draft was already written).
