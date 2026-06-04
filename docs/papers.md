# Reference papers

**PDFs are not committed (copyright).** Citations + links only here. Access PDFs via
the AAMU library or the lab shared drive. Open-access ones are linked directly below.

---

## Zhang et al. 2021 — *the most directly relevant (method)*

**Citation:** Zhang, B., Chung, S. H., Barker, S., Craig, D., Narayan, R. J., & Huang, J. (2021). Direct ink writing of polycaprolactone / polyethylene oxide based 3D constructs. *Progress in Natural Science: Materials International*, **31**(2), 180–191. https://doi.org/10.1016/j.pnsc.2020.10.001
**Access:** OPEN ACCESS (CC BY-NC-ND). Free PDF: https://bura.brunel.ac.uk/handle/2438/27125

**Why it matters here:** The closest published method to what this lab does. PCL (hydrophobic) is DIW-printed by dissolving in DCM or acetone and using solvent evaporation as the "set" step.

**Key results to use:**
- DIW travel speed range: 30–80 mm/s (vs. print 2.5–12.5 mm/s).
- DCM beats acetone for shape fidelity due to better viscosity recovery (93% vs ~30% at 100 s).
- The three rheology tests every ink should pass: shear viscosity sweep, oscillatory yield-stress sweep, creep recovery test.
- ≥ 80% viscosity recovery within ~90 s is the working rule.
- Power-law index n < 1 is required for extrusion.

---

## Teixeira et al. 2026 — *parameter-sweep method*

**Citation:** Teixeira et al. (2026). A simple method to assess the optimum 3D printing parameters, using agarose hydrogel. *MRS Communications*, **16**, 212–218.
**Access:** PAYWALLED (Springer). Get via AAMU library proxy. Do NOT commit the PDF.

**Why it matters here:** The methodology backbone for parameter sweeps — the workflow for finding the best print speed × pressure × nozzle once an ink is loaded.

**Key results to use:**
- Best line accuracy 97.3% at 2 %w/v agarose, 25G, 6 mm/s, 40 kPa.
- A 3 %w/v thickener (laponite) lifted grid accuracy 60% → 83%. PEO plays the same role for PCL inks.
- Accuracy: `Accuracy(%) = (1 − |A_exp − A_CAD| / A_CAD) × 100`
- Square-pore printability: `Pr = L² / (16·A)`. Pr = 1 is perfect.

---

## Yuk et al. 2020 — *the long-game vision*

**Citation:** Yuk, H., Lu, B., Lin, S., Qu, K., Xu, J., Luo, J., & Zhao, X. (2020). 3D printing of conducting polymers. *Nature Communications*, **11**, 1604. https://doi.org/10.1038/s41467-020-15316-7
**Access:** OPEN ACCESS. Free at nature.com; PMC7105462.

**Why it matters here:** The endpoint the lab heads toward — conductive polymer 3D printing (9-channel soft neural probe from PEDOT:PSS).

**Key results to use:**
- Printable PEDOT:PSS nanofibril window: 5–7 wt%.
- Dry conductivity 155 S/cm; hydrogel state 28 S/cm.
- < 5% conductivity drop over 10,000 bending cycles.
- Multi-material: conductive electrodes printed *inside* a PDMS encapsulation in one job.

---

## Bone composite — *your actual end goal (NEW)*

These are the references that match where the project is headed: a PCL + mineral
scaffold that mimics bone. The "ground bone / calcium carbonate" you're adding is the
same idea as **hydroxyapatite (HAp)** in the literature.

**Zhang et al. 2022.** Direct ink writing of vancomycin-loaded polycaprolactone / polyethylene oxide / hydroxyapatite 3D scaffolds. *Journal of the American Ceramic Society*. https://doi.org/10.1111/jace.18048
- HAp added at 55–85% w/w to mimic bone mineral; **65% w/w ≈ the inorganic content of natural bone** and gave the best viscosity recovery + mechanical properties. This is the direct precedent for your composite.

**Kolan et al. 2018.** Solvent and melt-based extrusion 3D printing of polycaprolactone bioactive glass composite for tissue engineering. *Pro-AM 2018*, 176–182. https://doi.org/10.25341/D4B018
- Both melt and solvent routes for a PCL + mineral (bioactive glass) composite scaffold. Cited by the Hampton PREM poster.

**Varntanian, S. 2017.** 3D Printing of Polycaprolactone Scaffolds. https://doi.org/10.13140/RG.2.2.27949.28645

**Prior work (context, not a journal ref):** Horton, G. & Dumas, J. *3D Printing Polycaprolactone with Bone Composite.* PREM poster, Hampton University (NSF-DMR 1827820). Heated melt extrusion of PCL (Mw 14k → 80k), 60–95 °C, 20G→26G needles. — *Reference the approach; do not host the PDF (not ours).*

---

## Suggested reading order

1. **Zhang 2021** — your core DIW workflow.
2. **Zhang 2022 + Kolan 2018** — the bone-composite precedent; this is your poster's "why."
3. **Teixeira 2026** — the optimization protocol once you have a stable ink/composite.
4. **Yuk 2020** — long-term vision.
