# PCL Review — Summary & Notes

**Paper:** Woodruff, M. A. & Hutmacher, D. W. (2010). *The return of a forgotten polymer — Polycaprolactone in the 21st century.* Progress in Polymer Science, 35, 1217–1256.
**Why you're reading it:** foundational "what is PCL and why do we use it" — feeds your polymer class and your poster. The *paper* frames PCL for tissue engineering, but for **your** project the takeaway is PCL's **flexibility + processability** as a substrate for **flexible electronics**. (The bone/scaffold content is background — your live application is a flexible *conductive* composite.)

*Citations below: (Woodruff 2010, location) unless noted. Page numbers are the journal page on the PDF.*

---

## The story in one paragraph
PCL was synthesized way back (Carothers group, ~1930s) and was popular for drug delivery in the 1970s–80s. It got **"forgotten" for ~two decades** because faster-degrading polymers (PLA, PGA, PLGA) were preferred — PCL's slow 2–4 year degradation looked like a disadvantage. It came *back* with **tissue engineering** in the 1990s–2000s, thanks to easy processing, low cost, and FDA approval (Woodruff 2010, Abstract & Intro, p.1218). *(For your project, the inheritance isn't the degradation — it's that PCL is cheap, processable, and flexible.)*

---

## Key properties — the numbers to actually know *(all from Woodruff 2010, Sect.2, p.3 unless noted)*
- **Made by:** ring-opening polymerization (ROP) of ε-caprolactone (Woodruff 2010, Sect.2, p.1218).
- **Type:** hydrophobic, **semi-crystalline** aliphatic polyester (Woodruff 2010, p.3).
- **Glass transition (Tg): −60 °C** → at room temp PCL is above Tg, so it's **soft/rubbery, not glassy** ← *the key property for your project* (Woodruff 2010, p.3).
- **Melting point (Tm): ~59–64 °C** (Woodruff 2010, p.3). *(Liu 2018 lists 58–60 °C for Mw 50k — Liu 2018, Sect.2.2, p.2.)*
- **Molecular weight range:** ~**3,000 to 80,000 g/mol**; **crystallinity decreases as MW increases** (Woodruff 2010, p.3).
- **Solubility:** dissolves well in **chloroform, DCM**; **poor in acetone**; insoluble in alcohols (Woodruff 2010, p.3). *(Borne out in DIW: DCM ink works, acetone underperforms — Zhang 2021, Sect.3.1.2, p.6.)*
- **Blend-friendly:** mixes/copolymerizes easily and accepts fillers (Woodruff 2010, p.3–4).

---

## How and why it degrades *(core PCL knowledge; less central to electronics)*
- **Total degradation 2–4 years**, slower at higher MW (Woodruff 2010, Sect.3, p.4).
- **Two stages:** hydrolysis of ester bonds → MW drops; then intracellular uptake once MW < ~3,000 (Woodruff 2010, Sect.3, p.5).
- **Mass loss begins ~MW 5,000** (~9 months in vivo) (Woodruff 2010, Fig.4, p.7).
- Final product **6-hydroxylcaproic acid** enters the citric acid cycle (Woodruff 2010, Fig.5, p.8).
- **Degrades without an acidic burst** (unlike PLA/PGA) → low inflammation (Woodruff 2010, Sect.3, p.4).

---

## Why PCL — and why you composite it (the core of your project)
- PCL is **flexible and easy to process** (above its Tg of −60 °C at room temp; melts/dissolves easily) — ideal for a *flexible* electronic substrate.
- **BUT pure PCL is an electrical insulator** — all single bonds, electrons locked. *(General polymer fact, not from a specific paper in your set.)*
- **Fix: composite it.** Add a conductor — **graphite/carbon** filler, or an intrinsically conducting polymer like **polyaniline (PANI)**. The conductor brings conductivity; PCL brings flexibility + processability. *(PEDOT:PSS is the published parallel — Yuk 2020.)*
- Same composite logic as the old bone plan (add a mineral for stiffness/osteoconductivity, e.g. mPCL + 20 wt% β-TCP — Woodruff 2010, Sect.8.2, p.24–25); here you add a conductor instead.

## What makes a good flexible conductor (criteria — straight into your poster)
1. **A percolating conductive network** — enough conductor, connected, for a continuous current path. *(General concept — cite the graphite-composite paper, not in this set.)*
2. **Flexibility retained** — enough PCL matrix that it stays bendable, not brittle.
3. **Uniform filler dispersion** — even spread (sonication) for consistent conductivity.
4. **Stable conductivity under flexing** — keeps conducting when bent/cycled, doesn't crack the network. (Cf. **Yuk 2020, p.4, Fig.3b–c**: <5% conductivity drop over 10,000 bends.)
> Golden rule: target just above the percolation threshold — minimum conductor for maximum flexibility/printability.

## Where YOUR method fits
- Fabrication menu (solvent casting, melt extrusion, direct writing) is material-agnostic (Woodruff 2010, Sect.8.1, Fig.9 — see note 03).
- Your routes: melt-compound + extrude/3D-print, or solvent-cast / mould-cast.
- **Key flip from the scaffold version:** a scaffold *wants* porosity; a **conductor wants a dense, continuous composite** — pores break the network. Aim for dense, well-dispersed dog-bones.

---

## ✍️ Things to write down (the keepers)

**For the polymers class (Drakes):**
- PCL = semi-crystalline aliphatic polyester via **ROP of ε-caprolactone**; **Tg −60 °C, Tm ≈ 60 °C**; crystallinity drops as MW rises (Woodruff 2010, Sect.2, p.3).
- Higher MW → higher viscosity, harder to melt, slower degradation.
- PCL alone is an **insulator**; conduction needs an added filler or conjugated polymer.

**For the poster Intro / Significance:**
- "PCL is flexible, processable, biocompatible, FDA-familiar — a strong substrate for flexible devices" (Woodruff 2010, Abstract).
- "Pure PCL is an insulator, so a conductor (graphite and/or PANI) is added → a flexible conductive composite."

**For your research understanding:**
- Solubility (chloroform/DCM yes, acetone weak) → the solvent-cast route (Woodruff 2010, p.3; Zhang 2021, Sect.3.1.2, p.6).
- The percolation threshold is the variable your experiment maps *(cite the composite paper)*.
- PCL's flexibility (Tg −60 °C) is why it's the substrate.

---

## Parked for later
- **Liu et al. 2018 (PCL melt-extrusion crystallinity / XRD)** — revisit after the polymers session with Drakes (crystals align in flow, volume fraction rises down the nozzle — Liu 2018, Sect.3, p.4–5).
