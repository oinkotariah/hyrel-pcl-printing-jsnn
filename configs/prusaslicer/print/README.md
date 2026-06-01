# Print profiles

Naming convention: `<material>_<process>_<print_speed>print_<travel_speed>travel_<status>.ini`

| File | What it is | Status |
|---|---|---|
| `PCL_DIW_25print_25travel_BROKEN.ini` | Original lab profile from 2021. Every speed set to 25 mm/s, which triggers PrusaSlicer's sticky-F bug — only F1500 is emitted in the resulting G-code. **Kept here for reference, do NOT use for new prints.** |
| `PCL_DIW_25print_60travel_FIXED.ini` | Corrected version: `travel_speed = 60` (was 25). All other settings identical. Re-slice with this. | **Current default** |

## Why two profiles instead of one in-place fix?

Keeping the broken one preserves history. Anyone looking at the repo a year from now will see *both* the bug and the fix and understand what changed. The git log already shows the diff, but having both files explicitly named makes the "tribal knowledge" visible without having to read commits.

## When to make a new profile

Whenever you're going to change settings *in a way you want to be repeatable*. Don't edit a checked-in profile in-place except to fix an outright mistake. Copy it, rename it with the changed parameter in the filename, and commit.

Examples of new profiles you might add:
- `PCL_DIW_15print_60travel_FIXED.ini` — slower print speed for thicker ink
- `PCL_DIW_25print_80travel_FIXED.ini` — faster travel for stringy ink
- `PCLPEO_DIW_5print_30travel_v1.ini` — completely different ink, slower print
