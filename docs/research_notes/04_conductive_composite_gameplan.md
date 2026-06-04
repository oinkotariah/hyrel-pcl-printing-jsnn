# Conductive PCL–Graphite Composite — Project Gameplan & Process Notes

*Living doc. **[confirm w/ Nick]** = fuzzy/unstated detail.*

> **Citation note:** this gameplan is mostly **Nick's plan + general concepts** (percolation, the composite logic), so most of it carries no paper citation. Paper citations appear only where a step mirrors a **published method** — Teixeira's parameter optimization and Zhang's DIW rheology rules.

---

## The goal (one sentence)
Make a **flexible conductive composite** by loading **graphite into PCL**, find the **percolation threshold**, print/cast **dog-bone** specimens, and **test conductivity** — enough for a **poster now**, **paper later**.

## The core concept: percolation threshold *(general concept — cite your graphite-composite paper, not yet in the set)*
- Too little graphite → isolated particles → insulator.
- At threshold → connected network spans the part → conductivity jumps orders of magnitude.
- More than needed → conducts well but stiff/brittle.
- Target: **minimum graphite that still conducts** (keep flexibility).

## The experiment: 5 compositions
- **Range:** **10 → 30%** graphite, **5 points** (likely 10/15/20/25/30%) **[confirm: spacing, wt% vs vol%]**.
- **Why 5 points:** map conductivity vs loading, locate the percolation jump.
- This one-variable-at-a-time sweep to find the parameter window mirrors the published optimization approach in **Teixeira 2026** (sweep parameters, measure an outcome, find the usable window — Teixeira 2026, Sect."Materials and methods" & Discussion, p.3, p.6).

## ROUTE A — Primary (printer working): melt-compound + 3D print
1. **Melt** PCL in the heated head (replaces solvent dissolution).
2. **Mix in graphite** (melt compounding); disperse well (sonication). Good dispersion = consistent conductivity.
3. **Extrude / 3D print** into the dog-bone; solidifies on cooling.
4. **Test conductivity.**
- *If using a DIW/solvent ink instead, the ink must obey the rheology rules: shear-thinning + >80% viscosity recovery (Zhang 2021, Intro, p.2), and DCM outperforms acetone (Zhang 2021, Sect.3.1.2, p.6).*

## ROUTE B — Fallback (printer down): melt in beaker + mould-cast
1. **Melt PCL in a beaker.**
2. **Mix in graphite.**
3. **[confirm — order]** sonicate and/or let cool.
4. **Blend** **[confirm — homogenize vs granulate]**.
5. **Cast into dog-bone moulds.**
6. **Test conductivity.**
> Either route yields composites + dog-bones + conductivity data → **the poster works with or without the printer.**

## Characterization
- **Conductivity** across the dog-bone gauge length (4-point probe is the standard method — cf. Yuk 2020, Methods, p.7).
- Dog-bone = standard tensile specimen; mechanical testing possible too **[confirm if in scope]**.
- **Key figure: conductivity vs graphite %** (the percolation plot).

## Deliverable timeline
- **Now → poster:** 5 compositions, dog-bones, conductivity-vs-loading + percolation plot.
- **Later → paper.**

## Open questions for Nick
1. Exact ratios + wt% vs vol%.
2. Conductor: graphite only, or graphite + PANI?
3. Fallback step order (melt / mix / sonicate / cool / blend).
4. What the blender step is for.
5. Mechanical (tensile) testing in scope?

## Vocabulary
- **Solvent casting · melt compounding · percolation threshold · sonication · dog-bone.**
