# Reference papers

PDFs are not committed (copyright). Citations only here. Lab members access PDFs via institutional library or the lab shared drive.

---

## Zhang et al. 2021 — *the most directly relevant*

**Citation:** Zhang, B., Chung, S. H., Barker, S., Craig, D., Narayan, R. J., & Huang, J. (2021). Direct ink writing of polycaprolactone / polyethylene oxide based 3D constructs. *Progress in Natural Science: Materials International*, **31**(2), 180–191. https://doi.org/10.1016/j.pnsc.2020.10.001

**Why it matters here:** The closest published method to what this lab does. Demonstrates that PCL (a hydrophobic polymer) can be DIW-printed by dissolving in DCM or acetone and using solvent evaporation as the "set" step.

**Key results to use:**
- DIW travel speed range: 30–80 mm/s (vs. print 2.5–12.5 mm/s).
- DCM beats acetone for shape fidelity due to better viscosity recovery (93% vs ~30% at 100 s).
- The three rheology tests every ink should pass: shear viscosity sweep, oscillatory yield-stress sweep, creep recovery test.
- ≥ 80% viscosity recovery within ~90 s is the working rule.
- Power-law index n < 1 is required for extrusion.

---

## Teixeira et al. 2026

**Citation:** Teixeira et al. (2026). A simple method to assess the optimum 3D printing parameters, using agarose hydrogel. *MRS Communications*, **16**, 212–218.

**Why it matters here:** The methodology backbone for parameter sweeps. Once an ink is loaded, this is the workflow for finding the best print speed × pressure × nozzle combination.

**Key results to use:**
- Best line accuracy 97.3% at 2 %w/v agarose, 25G, 6 mm/s, 40 kPa (the sweet-spot example).
- Adding a 3 %w/v thickener (laponite) lifted grid accuracy from 60% → 83%. PEO plays the same rescue role for PCL inks.
- Accuracy formula: `Accuracy(%) = (1 − |A_exp − A_CAD| / A_CAD) × 100`
- Pore printability for square pores: `Pr = L² / (16·A)`. Pr = 1 is perfect.

---

## Yuk et al. 2020 — *the long-game vision*

**Citation:** Yuk, H., Lu, B., Lin, S., Qu, K., Xu, J., Luo, J., & Zhao, X. (2020). 3D printing of conducting polymers. *Nature Communications*, **11**, 1604. https://doi.org/10.1038/s41467-020-15316-7

**Why it matters here:** The endpoint the lab is heading toward — conductive polymer 3D printing. Demonstrates a 9-channel soft neural probe printed from PEDOT:PSS in PDMS, implanted in mouse hippocampus.

**Key results to use:**
- Printable PEDOT:PSS nanofibril concentration window: 5–7 wt%.
- Dry conductivity: 155 S/cm. Hydrogel state: 28 S/cm.
- Bending durability: < 5% conductivity drop over 10,000 cycles.
- Multi-material strategy: conductive electrodes printed *inside* a PDMS encapsulation in one continuous job.

---

## Suggested reading order

1. **Zhang first** — that's your week-1 workflow.
2. **Teixeira second** — for the optimization protocol once you have a stable ink.
3. **Yuk third** — for vision and where the project might publish in a year or two.
