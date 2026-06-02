# hyrel-pcl-printing-jsnn

PrusaSlicer configs, G-code, and patch scripts for **3D printing PCL (polycaprolactone) on the Hyrel SYSTEM 30M** by Direct Ink Writing (DIW), at the IMPACT Lab, JSNN (the Joint School of Nanoscience and Nanoengineering — NC A&T + UNCG).

The point of this repo is to **make the lab's settings reproducible** — so when we publish, the methods section can point here and anyone can re-slice the same STL with the same configs and get the same G-code.

---

## Quick start

If you just want to print our calibration cube:

1. Open PrusaSlicer 2.9.2 or newer.
2. Load these three profiles (under Print Settings, Filament Settings, Printer Settings):
   - **Print:** `configs/prusaslicer/print/PCL_DIW_25print_60travel_FIXED.ini`
   - **Filament:** `configs/prusaslicer/filament/ABS-30M_240C_80Cbed.ini` *(placeholder — will be replaced with a PCL-specific profile, see [Known issues](#known-issues))*
   - **Printer:** `configs/prusaslicer/printer/30M-ESR_T1_Heated.ini`
3. Import `gcode/cube_10x10x10_2mm_Corners/source.stl`.
4. Slice. The output should be ~7,000 lines and use **two F-values**: F1500 (25 mm/s, print) and F3600 (60 mm/s, travel).
5. Load the resulting G-code into Repetrel.
6. Print.

If PrusaSlicer isn't available, the pre-sliced fixed G-code is at `gcode/cube_10x10x10_2mm_Corners/travel_fixed.gcode`.

---

## What was actually fixed (the F1500 → F3600 story)

On 2026-06-01, the lab's calibration print of `cube_10x10x10_2mm_Corners` showed obvious stringing during travel moves between separated paths. We diagnosed the G-code and found:

| Measurement | Value |
|---|---|
| Travel-only moves (G1 X Y, no E) | 242 |
| Print moves (G1 X Y with E) | 5,732 |
| Unique F values in the entire 7,013-line file | **F1500 only** |

That meant every travel move was crawling at 25 mm/s (same as print speed), so the ink had time to ooze during each repositioning.

**Root cause:** In `PCL_DIW_25print_25travel_BROKEN.ini`, *every* speed setting was 25 mm/s — including `travel_speed`. PrusaSlicer only emits a new `F` value when the speed *changes* between moves, so it emitted F1500 once at the top of the file and never wrote another F.

**Fix:** Change one line — `travel_speed = 25` → `travel_speed = 60` — in the print-settings INI. Now PrusaSlicer differentiates between print and travel and writes F3600 on every travel move. The fixed profile is at `configs/prusaslicer/print/PCL_DIW_25print_60travel_FIXED.ini`.

**Why 60 mm/s:** Zhang 2021 and the DIW literature recommend travel = 3–10× print speed. With our 25 mm/s print, 60 mm/s (2.4×) is the conservative middle of the 30–80 mm/s DIW range. Bump higher once 60 is proven stable.

We also produced a hand-patched G-code at `gcode/cube_10x10x10_2mm_Corners/travel_fixed.gcode` using `scripts/patch_travel_speed.py` — useful for printing the fix without re-slicing.

---

## Repo layout

```
hyrel-pcl-printing-jsnn/
├── README.md                  ← this file
├── CONTRIBUTING.md            ← how to add a new ink, new geometry, new print run
├── LICENSE                    ← MIT
├── .gitignore
│
├── configs/
│   └── prusaslicer/
│       ├── printer/           ← Hyrel printer profile(s)
│       ├── filament/          ← material/temperature profile(s)
│       ├── print/             ← speed / extrusion / retraction profile(s)
│       └── recipes_naming_conventions.txt
│
├── gcode/
│   └── <part_name>/
│       ├── source.stl         ← CAD source
│       ├── original_*.gcode   ← sliced output, untouched
│       ├── *_fixed.gcode      ← any patched variants
│       └── notes.md           ← per-part observations
│
├── scripts/
│   ├── patch_travel_speed.py  ← adds F values for travel/print moves
│   ├── analyze_gcode.py       ← diagnostic: counts moves, lists unique Fs
│   └── README.md
│
├── docs/
│   ├── keywords.md            ← keyword/glossary cheat sheet
│   ├── papers.md              ← references (citations only, no PDFs)
│   └── glossary.md            ← short technical glossary
│
└── runs/
    └── YYYY-MM-DD_<short_description>/
        ├── notes.md           ← what we changed, what we observed
        ├── photos/            ← print result photos (gitignored if large)
        └── settings/          ← INI snapshot used for this run
```

### Naming conventions for files

**Print profiles:** `<material>_<process>_<print_speed>print_<travel_speed>travel_<status>.ini`
Examples:
- `PCL_DIW_25print_25travel_BROKEN.ini`
- `PCL_DIW_25print_60travel_FIXED.ini`
- `PCLPEO_DIW_5print_30travel_v1.ini`

**G-code variants:** Stored inside a `gcode/<part_name>/` folder. Always keep the **original** slicer output untouched as `original_<descriptor>.gcode`. Patched variants get a suffix like `_travel_fixed`, `_retract_added`, etc.

**Run folders:** `runs/YYYY-MM-DD_<lowercase_underscore_description>/`. One folder per session. Each has its own `notes.md`.

---

## Workflow

### To run a new test print

1. Decide what you want to test (new ink? new speed? new geometry?).
2. Make a new folder under `runs/` with today's date.
3. Choose existing config profiles in `configs/prusaslicer/` — or copy one to a new file with a clear name if you're changing settings.
4. Snapshot the exact INI(s) you used into `runs/<your_run>/settings/`.
5. Slice → load into Repetrel → print.
6. Photograph the result. Drop photos in `runs/<your_run>/photos/`.
7. Write up what you changed and what happened in `runs/<your_run>/notes.md` (template in `CONTRIBUTING.md`).
8. If you patched the G-code, commit both the original and the patched file under `gcode/<part_name>/`.
9. Commit. Push.

### To diagnose a G-code problem

```bash
python3 scripts/analyze_gcode.py path/to/file.gcode
```

It prints the count of travel vs. print moves, lists every unique `F` value, and flags suspicious patterns (like a file with only one F-value).

### To patch an existing G-code's travel speed

```bash
python3 scripts/patch_travel_speed.py input.gcode output.gcode --travel-f 3600 --print-f 1500
```

`--travel-f` and `--print-f` are in mm/min. Defaults are 3600 (60 mm/s) and 1500 (25 mm/s).

---

## Known issues / TODOs

- **Filament profile mismatch.** The current `ABS-30M_240C_80Cbed.ini` is set up for melt extrusion of ABS at 240 °C with an 80 °C bed. We're doing room-temperature DIW of PCL — the profile needs to be replaced with a PCL-DIW-appropriate one (likely with `temperature = 25` or similar, depending on Nick's heated vs. unheated head choice).
- **Retraction is 0.** `retract_length = 0,0,0,0,0` in the printer profile. For solvent-based DIW with stringing problems, 1–3 mm of retraction would likely help. Talk to Nick before changing.
- **No PCL/PEO ink profile yet.** Once we know the exact ink formulation (solvent system, concentration, ± PEO), we should add a print profile with that information in the filename.
- **No `runs/` history yet.** The first one is the 2026-06-01 diagnosis (under `runs/2026-06-01_day1_travel_speed_diagnosis/`).

---

## References

The methodology in this repo draws on three papers, all summarized in `docs/papers.md`:

1. **Zhang et al. 2021** — *Direct ink writing of polycaprolactone / polyethylene oxide based 3D constructs.* Progress in Natural Science: Materials International, 31, 180–191. (The closest published match to our workflow.)
2. **Teixeira et al. 2026** — *A simple method to assess the optimum 3D printing parameters, using agarose hydrogel.* MRS Communications, 16, 212–218. (Parameter sweep methodology.)
3. **Yuk et al. 2020** — *3D printing of conducting polymers.* Nature Communications, 11:1604. (The long-game endpoint.)

PDFs are NOT committed to this repo (copyright). Lab members can access them via the institutional library or the lab's shared drive.

---

## Authors / contributors

- **Onengiyeofori "Nengi" Inko-Tariah** — REU student, AAMU EE — initial diagnosis and patch (June 2026).
- **Nick Ricks** — graduate mentor, IMPACT Lab.


---

## License

MIT. See `LICENSE`. The configs are derivatives of PrusaSlicer's output (
