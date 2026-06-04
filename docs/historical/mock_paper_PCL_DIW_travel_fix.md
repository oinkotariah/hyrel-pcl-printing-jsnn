# MOCK PAPER — annotated draft

*This is a practice fill of a research paper, built from your actual JSNN work. Each
section starts with* ***▸ What it's for*** *(plain English, so you learn the anatomy),
then the* ***Draft*** *(real text from your project). Anything in `[BRACKETS]` is a hole
you fill in later — most of them after you actually print. Don't delete the brackets
until you've replaced them with something true.*

---

## The 4-question skeleton (read this first)

A paper answers four questions, in this order. Everything else just supports them:

1. **What's the problem, and why care?** → Introduction
2. **What did you do about it?** → Methods
3. **What happened?** → Results
4. **What does it mean?** → Discussion

A poster is the *same four questions* with the words cut and the figures enlarged. So if
you can fill these, you can build the poster. Right now you can fully answer 1 and 2.
3 and 4 are waiting on your next print — and seeing that gap clearly is the job of this exercise.

---

## Title

***▸ What it's for:*** *One sentence a stranger can scan to know exactly what you did.
Specific beats clever. Name the material, the method, the machine or the finding.*

**Draft:**
> Diagnosing and Correcting Travel-Move Stringing in Direct Ink Writing of
> Polycaprolactone on a Hyrel SYSTEM 30M

*Alternatives to consider once you have results — a title can advertise the finding:*
> *A Single-Parameter Feedrate Correction Eliminates Travel Stringing in PCL Direct Ink Writing*

---

## Authors & Affiliation

***▸ What it's for:*** *Who did the work and where. Order matters — first author did the
most hands-on work; this is the authorship conversation to have with Nick.*

**Draft:**
> Onengiyeofori Inko-Tariah¹, Nick Ricks¹
> ¹IMPACT Lab, Joint School of Nanoscience and Nanoengineering (JSNN),
> North Carolina A&T State University & UNC Greensboro

---

## Abstract

***▸ What it's for:*** *A ~150–200 word miniature of the whole paper: problem → what you
did → key result → why it matters. People decide whether to read on from this alone.
Write it LAST, because you can't summarize results you don't have yet.*

**Draft (with the result left blank on purpose):**
> Direct ink writing (DIW) of polycaprolactone (PCL) enables fabrication of biodegradable
> scaffolds, but print fidelity suffers when process parameters are mismatched. During
> calibration printing on a Hyrel SYSTEM 30M, we observed persistent stringing during
> non-extruding travel moves. Analysis of the G-code revealed that the slicer
> (PrusaSlicer 2.9.2) emitted only a single feedrate (F1500, 25 mm/s) for the entire job,
> because every speed parameter was set identically; as a result, travel moves executed at
> printing speed and ink oozed between separated paths. We raised the travel speed to
> 60 mm/s (F3600) as an isolated change and evaluated its effect on stringing.
> `[RESULT — fill after printing: e.g., "stringing was reduced/eliminated, measured as ___"]`.
> `[ONE-SENTENCE SIGNIFICANCE — what this means for the lab/for PCL DIW]`. All slicer
> configurations and analysis scripts are openly released to support reproducibility.

---

## 1. Introduction

***▸ What it's for:*** *Funnel from broad to narrow: the field → the specific problem →
the gap nobody's filled → your objective (one sentence). This is where your references live.*

**Draft:**
> Direct ink writing (DIW) is an extrusion-based additive manufacturing technique in which
> a paste-like material is deposited layer by layer through a fine nozzle. It is well suited
> to soft and shear-thinning materials that cannot be processed by conventional
> melt-based 3D printing. Polycaprolactone (PCL) — a biocompatible, biodegradable,
> low-melting-point polyester — is a common DIW feedstock for tissue-engineering scaffolds
> (Zhang et al., 2021).
>
> A central challenge in DIW is **print fidelity**: keeping deposited material exactly where
> it was placed. A frequent fidelity defect is *stringing*, where ink trails across the gap
> between two separated features. Stringing is governed largely by what happens during
> *travel moves* — the non-extruding repositioning moves between printed paths — and is
> influenced by travel speed and nozzle retraction.
>
> `[GAP — state it plainly: the lab had no documented, reproducible parameter set for PCL
> DIW on the SYSTEM 30M, and a calibration print exhibited stringing of unknown cause.]`
>
> **Objective:** to diagnose the source of stringing in the calibration G-code and implement
> a minimal, reproducible correction that establishes a clean baseline for subsequent ink and
> geometry studies.

---

## 2. Materials and Methods

***▸ What it's for:*** *Enough detail that a competent stranger could repeat your work and
get the same result. This is your strongest section — be concrete. Past tense, "we did X."*

**Draft:**
>
> **2.1 Equipment.** Printing was performed on a Hyrel SYSTEM 30M equipped with a
> `[SDS-10 syringe — CONFIRM head model with Nick]` extruder in tool position T1, using a
> `[24G — CONFIRM]` nozzle. The machine was controlled via Repetrel.
>
> **2.2 Material.** `[INK FORMULATION — the real gap: PCL in which solvent (DCM/acetone)?
> what concentration? any PEO? ASK NICK what is actually in the syringe.]`
>
> **2.3 Test geometry and slicing.** A 10 × 10 × 10 mm calibration cube (`source.stl`) was
> sliced in PrusaSlicer 2.9.2 with a layer height of 0.25 mm, extrusion width 0.38 mm, and a
> nominal print speed of 25 mm/s. The Hyrel header places extrusion values in volumetric
> mode (`M229 E1 D1`), so extrusion is expressed in mm³.
>
> **2.4 G-code diagnosis.** The generated G-code (7,013 lines) was analyzed with a custom
> Python script (`analyze_gcode.py`) that counts travel moves (G1 with no E) versus print
> moves (G1 with E) and enumerates every unique feedrate (F) value. The analysis found
> 242 travel moves, 5,732 print moves, and **only one feedrate value in the entire file
> (F1500 = 25 mm/s).** Because G-code feedrate is "sticky" — once set, it carries to all
> later moves until changed — and because every speed parameter in the print profile was
> identical (25 mm/s), the slicer never emitted a second F value. Travel moves therefore
> ran at printing speed, giving ink time to ooze during repositioning.
>
> **2.5 Correction.** The travel speed was changed from 25 to 60 mm/s (a single parameter,
> `travel_speed`, in the print profile), yielding explicit F3600 on all travel moves while
> print moves remained at F1500. A hand-patch script (`patch_travel_speed.py`) reproduced
> the same result on the existing G-code without re-slicing. Following a one-variable-at-a-time
> methodology (Teixeira et al., 2026), retraction was deliberately left unchanged in this
> experiment so the effect of travel speed could be isolated.
>
> **2.6 Characterization.** `[HOW YOU'LL JUDGE THE RESULT — e.g., printed cubes were
> photographed and inter-path stringing assessed qualitatively; line width and visible
> strands quantified in ImageJ.]`
>
> **2.7 Rheological context.** PCL inks are shear-thinning: viscosity drops under the shear
> of extrusion and recovers at rest. Recovery rate controls how well a deposited line holds
> its shape (Zhang et al., 2021). `[Optional: note the qualitative vaseline demonstration of
> shear-thinning and recovery observed in the lab.]`

---

## 3. Results

***▸ What it's for:*** *What happened — facts and figures only, no interpretation yet.
Each figure gets a number and a one-line caption. THIS IS YOUR EMPTY BOX. You fill it
after you print travel_fixed. Do not write anything here you haven't observed.*

**Draft (structure only — fill after the print):**
>
> **Figure 1.** `[Side-by-side photo: original (F1500-only) cube vs. travel_fixed cube,
> same region, same scale.]`
>
> `[SENTENCE 1 — the observation, neutral: e.g., "The original print showed N visible
> strands across the gap between concentric paths; the travel-fixed print showed M."]`
>
> `[SENTENCE 2 — any measurement: line width, strand count, or "no measurable strings."]`
>
> `[If you also test retraction later, that becomes Figure 2 and its own result.]`
>
> *(Note to self: a single clean before/after photo with a scale bar is enough to make this
> section real. A number is better. Either one turns this from a plan into a finding.)*

---

## 4. Discussion

***▸ What it's for:*** *What the results MEAN. Interpret, compare to the literature, admit
limitations. This is where you're allowed to reason — but every claim must trace to a
result in Section 3.*

**Draft (conditional skeleton — fill once Results exist):**
>
> `[IF stringing dropped:]` Raising travel speed reduced the time the nozzle lingered over
> each inter-path gap, lowering ooze — consistent with travel speed being a primary lever
> for stringing in DIW. The recommended DIW travel range (≈30–80 mm/s; Zhang et al., 2021)
> brackets our 60 mm/s value.
>
> `[IF stringing persisted:]` Travel speed alone did not eliminate stringing, which is
> consistent with residual nozzle pressure: with zero retraction, ink can continue to weep
> regardless of how fast the head moves. This motivates retraction as the next variable.
>
> **Limitations.** `[e.g., single geometry; ink formulation not yet characterized; stringing
> assessed by photograph rather than quantitative rheology.]`

---

## 5. Conclusion & Future Work

***▸ What it's for:*** *One short paragraph: what you established, and the obvious next steps.
Future work is honest, not filler — it shows you know where this goes.*

**Draft:**
> We identified the cause of travel-move stringing in a PCL DIW calibration print as a
> single sticky feedrate produced by uniform speed settings, and corrected it with an
> isolated travel-speed change. `[ONE LINE ON THE OUTCOME once you have it.]` Future work
> includes adding nozzle retraction as a second stringing control, developing a
> PCL-specific (and PCL/PEO) ink profile, printing a representative scaffold geometry rather
> than a calibration cube, and — longer term — extending the workflow toward conductive
> DIW inks (Yuk et al., 2020).

---

## References

***▸ What it's for:*** *Every source you cited, in a consistent format. These three are
already in your repo's `docs/papers.md`.*

1. Zhang, J. et al. (2021). Direct ink writing of polycaprolactone / polyethylene oxide based
   3D constructs. *Progress in Natural Science: Materials International*, 31, 180–191.
2. Teixeira, M. et al. (2026). A simple method to assess the optimum 3D printing parameters,
   using agarose hydrogel. *MRS Communications*, 16, 212–218.
3. Yuk, H. et al. (2020). 3D printing of conducting polymers. *Nature Communications*, 11, 1604.

---

## Acknowledgments

***▸ What it's for:*** *Thank the funding and the people who helped but aren't authors.*

**Draft:**
> This work was supported by the National Science Foundation REU program at the IMPACT Lab,
> JSNN. The author thanks Nick Ricks for mentorship and guidance.

---

## What this mock just told you (the takeaway)

- **Sections 1, 2, 5, References, Acknowledgments:** essentially done. You could fill these tonight.
- **Sections 3 and 4 (Results, Discussion):** blocked on one thing — printing travel_fixed and photographing it.
- **The one real data gap in Methods:** what's actually in the syringe (Section 2.2). That's a question for Nick, not something you can write your way around.

So the poster's missing piece is exactly one figure: the before/after print. Everything else is reading-and-typing you already have the material for.
