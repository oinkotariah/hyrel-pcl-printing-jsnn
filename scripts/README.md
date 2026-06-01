# scripts/

Small Python utilities for G-code work on the Hyrel.

## `analyze_gcode.py`

Diagnostic. Tells you what's actually in a G-code file: travel-vs-print move counts, every unique `F` value, and warnings for common problems (like the "only one F value in the whole file" sticky-F bug).

```bash
python3 scripts/analyze_gcode.py gcode/cube_10x10x10_2mm_Corners/original_BROKEN.gcode
```

Output for our broken cube:
```
=== ...original_BROKEN.gcode ===
Total lines:         7013
Travel moves:         242
Print moves:         5732

Unique F values (any move):
  F1500.0   →  25.00 mm/s   (appears 40×)

⚠️  Only ONE F value (F1500.0 = 25 mm/s) appears in the whole file.
   Travel and print are running at the same speed — likely the 'sticky F' bug.
```

## `patch_travel_speed.py`

Hand-patches a G-code to set explicit feedrates on travel and re-entry print moves. The fix-of-last-resort when re-slicing isn't possible.

```bash
# Default: travel = F3600 (60 mm/s), print = F1500 (25 mm/s)
python3 scripts/patch_travel_speed.py input.gcode output.gcode

# Custom travel speed (e.g., 80 mm/s = F4800)
python3 scripts/patch_travel_speed.py input.gcode output.gcode --travel-f 4800
```

The script adds a header comment block to the output file explaining what changed.

**The right way to fix the sticky-F problem is still to re-slice with `travel_speed > print_speed` in the print profile.** This script exists for the cases where you can't.

## Requirements

Python 3.8+. No external libraries.

## Adding new scripts

If you write a script and it's likely to be reused:

1. Put it here as `scripts/<verb>_<noun>.py` (e.g. `scripts/strip_layer_change_commands.py`).
2. Module docstring at the top explaining what it does and a USAGE block.
3. Use `argparse` for CLI args, no positional magic.
4. Update this README with a one-paragraph blurb and an example invocation.
