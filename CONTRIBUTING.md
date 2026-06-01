# Contributing

This repo lives or dies by **discipline about naming and documentation**. The whole point is to be able to look at any run a year later and reproduce it.

## How to add a new print run

1. Make a folder: `runs/YYYY-MM-DD_<lowercase_underscore_description>/`
2. Inside it, make subfolders: `settings/`, `photos/`.
3. Copy the **exact** INI files you used into `settings/` (don't link, copy — files on disk get overwritten).
4. Take photos of the print and drop them in `photos/`.
5. Write `notes.md` using the template below.
6. Commit. Push.

### `notes.md` template

```markdown
# Run: <short title>

**Date:** YYYY-MM-DD
**Operator:** <your name>
**Goal:** One sentence — what were you testing?

## Setup

- **STL:** <which one, link to `gcode/<part>/source.stl`>
- **Material loaded in syringe:** <ink composition, supplier, batch>
- **Reservoir head:** SDS-10 / EMO / VOL / Hot End
- **Nozzle gauge / diameter:** <e.g. 24G, 311 µm>
- **Print profile used:** `configs/prusaslicer/print/<file>.ini`
- **Filament profile used:** `configs/prusaslicer/filament/<file>.ini`
- **Printer profile used:** `configs/prusaslicer/printer/<file>.ini`
- **Settings snapshot:** `settings/` (this run's folder)

## Key parameters (TL;DR)

| Parameter | Value |
|---|---|
| Layer height | __ mm |
| Print speed | __ mm/s |
| Travel speed | __ mm/s |
| Extruder temp | __ °C |
| Bed temp | __ °C |
| Extrusion multiplier | __ |
| Retraction length / speed | __ mm @ __ mm/s |
| Z-hop | __ mm |

## Result

- [ ] Clean print
- [ ] Stringing between paths
- [ ] Blobs at perimeter start/end
- [ ] Inconsistent line width
- [ ] Gaps in perimeters
- [ ] First-layer adhesion issue
- [ ] Other: ______

**Photos:** `photos/` in this folder.

## Diagnosis / interpretation

What's the symptom telling you? What did Nick / the team think?

## Next change to try

One variable at a time. Be specific.
```

---

## How to add a new ink / material

1. Decide on a clean code name: `<polymer>_<solvent>_<conc>` (e.g., `PCL_DCM_15`, `PCLPEO_DCM_7p5`).
2. Create a new filament profile in `configs/prusaslicer/filament/<code_name>.ini`.
3. Update the file's first comment line with: ink composition, solvent system, polymer concentration (% w/w), supplier, batch / date prepared.
4. If the ink needs different print speeds, also create a print profile: `configs/prusaslicer/print/<code_name>_<settings>.ini`.
5. Document the rheology of the ink in `docs/inks/<code_name>.md` (template below).

### `docs/inks/<code_name>.md` template

```markdown
# Ink: <code_name>

**Date formulated:** YYYY-MM-DD
**Formulated by:** <name>
**Goal:** What is this ink for?

## Composition

| Component | Amount |
|---|---|
| Polymer A (PCL) | __ % w/w |
| Polymer B (PEO, if any) | __ % w/w |
| Solvent (DCM / ACE / other) | __ |
| Additive (if any) | __ |

## Preparation procedure

Step-by-step. Stirring rate, temperature, time.

## Rheology (Zhang protocol)

| Property | Value | Notes |
|---|---|---|
| Power-law index n | __ | n < 1 = shear-thinning |
| Consistency index m | __ Pa·sⁿ | |
| Yield stress | __ Pa | |
| Recovery at 90 s | __ % | should be ≥ 80 % |

## Print parameters that work

| Parameter | Range |
|---|---|
| Nozzle gauge | __ |
| Print speed | __ mm/s |
| Travel speed | __ mm/s |
| Pressure / extrusion mult | __ |

## Print parameters that DON'T work

(Bound the printable window — useful negative data.)

## References

Which papers / prior runs informed this formulation.
```

---

## How to add a new geometry / part

1. Make a folder: `gcode/<lowercase_underscore_part_name>/`
2. Drop the STL in as `source.stl`. Optional: drop the original CAD file (.f3d, .step) as `source.<ext>` if it's small.
3. Slice with whichever configs you'd recommend. Save the resulting G-code as `original_<short_descriptor>.gcode` (e.g., `original_25print_60travel.gcode`).
4. Write `gcode/<part>/notes.md` describing the part and any quirks.

---

## How to commit a G-code patch

If you patched a G-code with one of the scripts:

1. Keep the original file. Don't overwrite it.
2. Save the patched file in the **same folder** with a suffix: `_travel_fixed`, `_retract_added`, etc.
3. Add a header comment block at the top of the patched file explaining: what was changed, why, when, by whom.
4. Update the part's `notes.md` to reference the patch.
5. If the patch script is reusable, save it in `scripts/`.

---

## Commit message style

Use the standard prefix conventions:

| Prefix | Meaning |
|---|---|
| `config:` | Changes to a slicer profile (.ini) |
| `gcode:` | Adds or modifies a G-code file |
| `script:` | Changes to scripts |
| `docs:` | Markdown docs only |
| `run:` | A new print run added under `runs/` |
| `fix:` | Bug fix |
| `wip:` | Work in progress |

Examples:
- `config: bump travel_speed 25 → 60 in PCL_DIW print profile`
- `run: 2026-06-01 day-1 travel-speed diagnosis`
- `docs: add Zhang 2021 to papers.md`
- `script: patch_travel_speed.py supports custom F values`

---

## What NOT to commit

- **PDFs** — they're copyrighted (papers). Reference them in `docs/papers.md` by citation only.
- **Large RAW photo files** — convert to JPEG first. The `.gitignore` blocks the common RAW extensions.
- **Anything with a personal email, phone number, or AAMU/UNCG credentials in the file.**
- **Lab safety data sheets you don't have permission to redistribute.**

---

## Questions

If you're not sure where to put something, open an issue or ask Nick / Nengi.
