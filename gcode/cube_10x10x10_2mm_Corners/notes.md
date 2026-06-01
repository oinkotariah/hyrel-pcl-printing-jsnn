# Part: cube_10x10x10_2mm_Corners

A 10×10×10 mm cube with reinforced corners (2 mm chamfers / fillets). Calibration geometry.

## Source

- **STL:** `source.stl` (original from lab, dated October 2024)
- CAD source (.f3d / .step) not yet committed — TODO: ask Nick for it.

## Files in this folder

| File | What it is |
|---|---|
| `source.stl` | Original 3D mesh |
| `original_BROKEN.gcode` | PrusaSlicer 2.9.2 output from 2026-06-01. Has the sticky-F bug (only F1500 in entire file → travel = print = 25 mm/s). Kept for reference. |
| `travel_fixed.gcode` | Hand-patched by `scripts/patch_travel_speed.py`. Travel moves now at F3600 (60 mm/s), print moves at F1500 (25 mm/s). |
| `notes.md` | This file. |

## Print info (PrusaSlicer 2.9.2)

- **Profile used:** `configs/prusaslicer/print/PCL_DIW_25print_25travel_BROKEN.ini` (original) → `PCL_DIW_25print_60travel_FIXED.ini` (corrected)
- **Filament profile:** `ABS-30M_240C_80Cbed.ini` — note this is mismatched with PCL DIW (see repo README "Known issues")
- **Printer profile:** `30M-ESR_T1_Heated.ini`
- **Layer height:** 0.25 mm
- **Extrusion width:** 0.38 mm
- **Perimeters:** 4
- **Infill:** 100%
- **First-layer Z-offset:** Default (TBD — possibly needs tuning per Day 1 beading observation)

## Observations

- 2026-06-01 (Day 1): Print exhibited stringing during travel between separated paths. Diagnosed as sticky-F bug. See `runs/2026-06-01_day1_travel_speed_diagnosis/notes.md`.

## TODOs

- [ ] Print with `travel_fixed.gcode` and compare visual quality side-by-side with original.
- [ ] Tune first-layer Z-offset for beading (Nick's Day 1 fix #1).
- [ ] Replace ABS filament profile with PCL-appropriate one.
- [ ] Consider adding 1–3 mm retraction (currently `retract_length = 0`).
