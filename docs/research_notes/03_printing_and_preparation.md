# Printing & Preparation — Separate Summaries

Two papers, kept separate, focused on the **printing / preparation** content. Methods apply whether printing a scaffold or a flexible PCL/PANI substrate.

*Citations: (Author Year, location).*

---

# PAPER 1 — "Return of a forgotten polymer" (Woodruff & Hutmacher 2010)
### → the printing/preparation portion = **Section 8.1, "Scaffold fabrication"** (Woodruff 2010, p.15–24)

"Printing" isn't in the heading, which is why it's hard to find. Methods are grouped as:

**8.1.1 Conventional** *(Woodruff 2010, Sect.8.1.1)*
- **Porogen / particulate leaching** — template dissolved out to leave pores; ~5–100 µm, porosity <90%; random connectivity (Woodruff 2010, Fig.9).
- **Phase separation (TIPS)** — cool a polymer solution to split into solid + pore regions; porosity <70% (Woodruff 2010, Fig.9).
- **Gas foaming / supercritical CO₂** — solvent-free pores.

**8.1.2 Textile / fiber** *(Woodruff 2010, Sect.8.1.2)*
- **Electrospinning** — high-voltage sub-micron fibers; porosity 90–95%; PCL is the most common polymer here.

**8.1.3 Solid Free-Form Fabrication = the 3D-printing family** *(Woodruff 2010, Sect.8.1.3)* ← *your part*
- **SLA / SLS / 3DP** — laser/binder methods.
- **8.1.3.2 Extrusion / Direct Writing** *(Woodruff 2010, Sect.8.1.3.2)* — closest to your work:
  - **FDM:** heated liquefier extrudes melt layer-by-layer; pore ~100–2000 µm (Woodruff 2010, Fig.9).
  - **PED:** extrudes **pellets directly**, no filament prep.
  - **Direct Writing (DIW):** extrudes **pastes/inks**; pore ~5–100 µm (Woodruff 2010, Fig.9).
  - **Limitation:** single extrusion head → pore openings differ in z vs x–y (Woodruff 2010, Sect.8.1.3.2).

**Solvent note:** in solvent-based 3DP, **warping scales with solvent vapor pressure** — chloroform (low) → little warping; DCM → more (Woodruff 2010, Sect.8.1.3.1.4 / 3DP).

**4 scaffold-design criteria:** interconnected porosity · matched biodegradation · cell-friendly surface · matched mechanics (Woodruff 2010, Sect.8, p.15–16).

---

# PAPER 2 — "Structural Evolution of PCL during Melt Extrusion 3D Printing" (Liu et al. 2018)
### → this paper *is* the printing/preparation paper

**What it's about:** 3D-printed PCL by **screw-assisted melt extrusion**, watched with **in-situ synchrotron XRD** as it printed (Liu 2018, Abstract & Sect.2.3).

**The printing setup (the "preparation" part) — (Liu 2018, Sect.2.1, p.2):**
- Screw-assisted extruder (PABS): PCL melts in a heated chamber, **compressed air (~6 bar)** feeds a stepper-driven screw, **0.5 mm nozzle**.
- Conditions: **10 rpm screw / 110 °C → 0.1 mm/s** print speed.
- Material: PCL **CAPA6500, Mw ≈ 50,000**; Tm 58–60 °C, Tg −60 °C, density 1.1 g/cm³ (Liu 2018, Sect.2.2, p.2).
- Spherulite size: **~40 µm (pellet) → <4 µm (printed)** (Liu 2018, Fig.2, p.2–3).

**Key finding (crystallinity — save the deep dive for Drakes):**
- Shear flow **aligns PCL crystals in the flow direction** (anisotropy) (Liu 2018, Sect.3.1, p.4).
- **Crystal volume fraction increases** down the nozzle (y = 0 → 1.8 mm), driven by **undercooling + shear** (Liu 2018, Sect.3.2 & Fig.5, p.5).
- More crystallization after exit, as it cools/stretches (Liu 2018, Sect.3.2, p.5).

**One-line takeaway:** how you print changes the polymer's internal structure — temp, screw speed, nozzle size set crystallinity/orientation, which set mechanical properties (Liu 2018, Conclusions, p.5).

---

## TL;DR
- **Woodruff** = a *menu* of fabrication methods (your slice: 8.1.3.2 extrusion / direct writing).
- **Liu** = a *deep look at melt extrusion*, showing print parameters reshape crystallinity.
- **Parked:** Liu's detailed crystallography (crystal axes, XRD patterns) until after Drakes.
