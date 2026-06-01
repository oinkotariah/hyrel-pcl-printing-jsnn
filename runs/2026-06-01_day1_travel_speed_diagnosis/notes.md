# Run: Day 1 — travel speed diagnosis

**Date:** 2026-06-01
**Operator:** Nengi
**Goal:** Diagnose why the lab's calibration cube print showed stringing/oozing during travel moves.

## Setup

- **STL:** `gcode/cube_10x10x10_2mm_Corners/source.stl`
- **Material loaded in syringe:** TBD (asked Nick to confirm — probably PCL solution or vaseline-like test ink, not actual ABS despite the filament profile)
- **Reservoir head:** TBD (likely SDS-10 for DIW)
- **Nozzle gauge / diameter:** TBD — slicer profile says 0.5 mm nozzle diameter
- **Print profile used:** `Print settings_0.35w, 0.25z, 25f, 100%.ini` (saved as `settings/print_25travel_BROKEN.ini`)
- **Filament profile used:** `filament settings_240°C, 25%Fan, 80°CBed (ABS-30M).ini` (saved as `settings/filament_ABS-30M_240C.ini`)
- **Printer profile used:** `30M-ESR_T1_Heated.ini` (saved as `settings/printer_30M-ESR_T1_Heated.ini`)
- **Settings snapshot:** `settings/` (this folder)

## Key parameters (TL;DR)

| Parameter | Value |
|---|---|
| Layer height | 0.25 mm |
| Print speed | 25 mm/s (F1500) |
| **Travel speed** | **25 mm/s (F1500) — BUG** |
| Extruder temp | 240 °C (profile mismatch — see Observations) |
| Bed temp | 80 °C (profile mismatch) |
| Extrusion multiplier | 1.0 |
| Retraction length / speed | 0 mm @ 40 mm/s (effectively no retraction) |
| Z-hop | 0 mm |

## Result

- [x] Stringing between paths
- [ ] Clean print
- [ ] Blobs at perimeter start/end
- [ ] Inconsistent line width
- [ ] Gaps in perimeters

**Photos:** `photos/` — empty for now, planned for Day 2 once we run the fixed file alongside.

## Diagnosis / interpretation

Ran `scripts/analyze_gcode.py` on `original_BROKEN.gcode`:

| Measurement | Value |
|---|---|
| Total lines | 7,013 |
| Travel-only moves (G1 X Y, no E) | 242 |
| Print moves (G1 X Y with E) | 5,732 |
| Unique F values | **F1500 only** (= 25 mm/s) |

**Root cause:** The print profile has every speed set to 25 mm/s. PrusaSlicer only emits a new `F` value when the speed actually changes between moves, so it wrote F1500 once on the very first move and never wrote another F. Every subsequent move — print and travel alike — inherited that 25 mm/s.

Conclusion: travel was crawling at the same speed as print, giving the ink plenty of time to ooze during repositioning.

**Fix:** Change `travel_speed = 25` → `travel_speed = 60` in the print profile (saved as `configs/prusaslicer/print/PCL_DIW_25print_60travel_FIXED.ini`) and re-slice. As a backup, hand-patched the existing G-code using `scripts/patch_travel_speed.py` (242 travel moves now F3600 = 60 mm/s, 202 print re-entries restamped F1500 = 25 mm/s). The patched file is at `gcode/cube_10x10x10_2mm_Corners/travel_fixed.gcode`.

**Why 60 mm/s:** Zhang 2021 and the DIW literature recommend travel = 3–10× print speed. With 25 mm/s print, 60 mm/s is the conservative middle of the recommended 30–80 mm/s range.

## Side observations (didn't act on these yet)

1. The **filament profile is for ABS at 240 °C with an 80 °C bed.** We're doing PCL via DIW at room temperature — the temps in the profile are meaningless for our actual setup, or the configs need to be updated. Need to confirm with Nick.
2. **Retraction is 0** on all five extruders in the printer profile. After we run the travel-speed-fixed print, if there's still any stringing, that's the next thing to tune (1–3 mm typical).
3. There's an `M756 S0.25` command emitted at every single layer change. Not wrong, just chatty — could be stripped if it bothers Repetrel.

## Next change to try

Print the `travel_fixed.gcode` (or re-slice with the fixed INI) and compare result side-by-side with the original print. If still stringing → add `retract_length = 1.5` to the printer profile. If clean → bump `travel_speed` to 80 mm/s and re-test.
