#!/usr/bin/env python3
"""
patch_travel_speed.py — fix the "sticky F" problem in PrusaSlicer/Slic3r G-code.

THE PROBLEM
-----------
When every speed in the print-settings INI is identical (e.g., all 25 mm/s),
PrusaSlicer only emits an `F` value once on the first move, because the
feedrate never changes. Result: every subsequent move — including long
travel repositionings — inherits the same speed, causing ink to ooze
during travel.

THIS SCRIPT
-----------
Walks through a G-code file and:
  - Adds an explicit `F<travel_f>` to every TRAVEL move (G0, or G1 with X/Y
    but no E).
  - Adds an explicit `F<print_f>` to the FIRST PRINT move after each travel
    (so print speed gets restored cleanly).

PROPER FIX
----------
The right fix is to set `travel_speed = 60` (or wherever) in the print
profile and re-slice. This script is the hand-patch backup when re-slicing
isn't an option (no PrusaSlicer on the lab machine, etc.).

USAGE
-----
    python3 patch_travel_speed.py input.gcode output.gcode
    python3 patch_travel_speed.py input.gcode output.gcode --travel-f 4800
    python3 patch_travel_speed.py input.gcode output.gcode --travel-f 3600 --print-f 1500

F values are in mm/min. Divide by 60 for mm/s.
    F1500 = 25 mm/s
    F3600 = 60 mm/s
    F4800 = 80 mm/s
"""

import argparse
import re
import sys
from datetime import date

DEFAULT_TRAVEL_F = 3600   # mm/min = 60 mm/s
DEFAULT_PRINT_F  = 1500   # mm/min = 25 mm/s


def has_extrusion(line: str) -> bool:
    """G1/G0 line with an explicit positive-or-negative E parameter."""
    return re.search(r'\sE[\-0-9.]', line) is not None


def has_xy(line: str) -> bool:
    return (re.search(r'\sX[\-0-9.]', line) is not None
            and re.search(r'\sY[\-0-9.]', line) is not None)


def is_g0_or_g1(line: str) -> bool:
    s = line.lstrip()
    return s.startswith('G0 ') or s.startswith('G0\t') \
        or s.startswith('G1 ') or s.startswith('G1\t')


def ensure_f(line: str, target_f: int) -> str:
    """Return the line with F<target_f> guaranteed. Strips any existing F first."""
    # Split off the comment if any
    if ';' in line:
        idx = line.index(';')
        body, comment = line[:idx].rstrip(), ' ' + line[idx:]
    else:
        body = line.rstrip('\n').rstrip()
        comment = ''
    # Remove any existing F<num>
    body = re.sub(r'\s*F[0-9.]+', '', body).rstrip()
    body = f'{body} F{target_f}'
    return body + comment + '\n'


def patch(in_path: str, out_path: str, travel_f: int, print_f: int) -> dict:
    with open(in_path) as f:
        lines = f.readlines()

    new_lines = []
    last_was_travel = None  # None / True / False
    n_travel_patched = 0
    n_print_patched = 0

    for ln in lines:
        if is_g0_or_g1(ln) and has_xy(ln):
            if has_extrusion(ln):
                # Print move
                if last_was_travel in (None, True):
                    # First print move after a travel — explicitly stamp print speed
                    new_lines.append(ensure_f(ln, print_f))
                    n_print_patched += 1
                else:
                    # Continuing a print sequence — leave F implicit (sticky from previous print move)
                    new_lines.append(ln)
                last_was_travel = False
            else:
                # Travel move — always explicit
                new_lines.append(ensure_f(ln, travel_f))
                n_travel_patched += 1
                last_was_travel = True
        else:
            new_lines.append(ln)

    header = [
        f'; ============================================================\n',
        f'; PATCHED by patch_travel_speed.py on {date.today().isoformat()}\n',
        f'; \n',
        f'; Original issue: sticky F values caused travel and print to\n',
        f';                 share the same speed.\n',
        f'; \n',
        f'; This patch:     adds F{travel_f} (={travel_f/60:.0f} mm/s) to {n_travel_patched} travel moves,\n',
        f';                 and F{print_f} (={print_f/60:.0f} mm/s) to {n_print_patched} re-entry print moves.\n',
        f'; \n',
        f'; Source file:    {in_path}\n',
        f'; ============================================================\n',
        f'\n',
    ]

    with open(out_path, 'w') as f:
        f.writelines(header + new_lines)

    return {
        'in_path': in_path,
        'out_path': out_path,
        'travel_f': travel_f,
        'print_f': print_f,
        'travel_patched': n_travel_patched,
        'print_patched': n_print_patched,
        'total_in_lines': len(lines),
        'total_out_lines': len(new_lines) + len(header),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('input', help='Input .gcode file')
    p.add_argument('output', help='Output .gcode file')
    p.add_argument('--travel-f', type=int, default=DEFAULT_TRAVEL_F,
                   help=f'Feedrate for travel moves (mm/min). Default {DEFAULT_TRAVEL_F} (={DEFAULT_TRAVEL_F/60:.0f} mm/s).')
    p.add_argument('--print-f', type=int, default=DEFAULT_PRINT_F,
                   help=f'Feedrate for print moves (mm/min). Default {DEFAULT_PRINT_F} (={DEFAULT_PRINT_F/60:.0f} mm/s).')
    args = p.parse_args()

    stats = patch(args.input, args.output, args.travel_f, args.print_f)
    print(f"Patched {stats['in_path']}")
    print(f"  → {stats['out_path']}")
    print(f"Travel moves rewritten with F{args.travel_f} ({args.travel_f/60:.0f} mm/s): {stats['travel_patched']}")
    print(f"Print re-entry moves rewritten with F{args.print_f} ({args.print_f/60:.0f} mm/s): {stats['print_patched']}")
    print(f"Lines in: {stats['total_in_lines']}, Lines out: {stats['total_out_lines']}")


if __name__ == '__main__':
    main()
