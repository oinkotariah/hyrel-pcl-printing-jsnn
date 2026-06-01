#!/usr/bin/env python3
"""
analyze_gcode.py — quick diagnostic for a G-code file.

Prints:
  - Total line count
  - Number of travel moves (G0, or G1 with X/Y but no E)
  - Number of print moves (G1 with X/Y and E)
  - List of unique F values and where they appear
  - Flag if the file looks suspicious (e.g., only ONE F value in the whole file)

USAGE
-----
    python3 analyze_gcode.py path/to/file.gcode
"""

import argparse
import re
import sys
from collections import Counter


def has_extrusion(line):
    return re.search(r'\sE[\-0-9.]', line) is not None


def has_xy(line):
    return (re.search(r'\sX[\-0-9.]', line) is not None
            and re.search(r'\sY[\-0-9.]', line) is not None)


def is_g0_or_g1(line):
    s = line.lstrip()
    return s.startswith('G0 ') or s.startswith('G0\t') \
        or s.startswith('G1 ') or s.startswith('G1\t')


def analyze(path):
    with open(path) as f:
        lines = f.readlines()

    n_travel = 0
    n_print = 0
    travel_f = Counter()
    print_f = Counter()
    all_f = Counter()

    for ln in lines:
        fmatch = re.search(r'\sF([0-9.]+)', ln)
        if fmatch:
            all_f[float(fmatch.group(1))] += 1
        if is_g0_or_g1(ln) and has_xy(ln):
            if has_extrusion(ln):
                n_print += 1
                if fmatch:
                    print_f[float(fmatch.group(1))] += 1
            else:
                n_travel += 1
                if fmatch:
                    travel_f[float(fmatch.group(1))] += 1

    return {
        'total_lines': len(lines),
        'n_travel': n_travel,
        'n_print': n_print,
        'all_f': all_f,
        'travel_f': travel_f,
        'print_f': print_f,
    }


def report(path, stats):
    print(f"=== {path} ===")
    print(f"Total lines:        {stats['total_lines']:>6}")
    print(f"Travel moves:       {stats['n_travel']:>6}")
    print(f"Print moves:        {stats['n_print']:>6}")
    print()
    print("Unique F values (any move):")
    for f, count in sorted(stats['all_f'].items()):
        print(f"  F{f:<8}  → {f/60:>6.2f} mm/s   (appears {count}×)")
    print()
    print("F values that appear on TRAVEL moves:")
    if stats['travel_f']:
        for f, count in sorted(stats['travel_f'].items()):
            print(f"  F{f:<8}  → {f/60:>6.2f} mm/s   ×{count}")
    else:
        print("  (none explicitly written — travel inherits from previous F)")
    print()
    print("F values that appear on PRINT moves:")
    if stats['print_f']:
        for f, count in sorted(stats['print_f'].items()):
            print(f"  F{f:<8}  → {f/60:>6.2f} mm/s   ×{count}")
    else:
        print("  (none explicitly written — print inherits from previous F)")
    print()

    # Warning checks
    warnings = []
    if len(stats['all_f']) == 1 and (stats['n_travel'] > 0 and stats['n_print'] > 0):
        only_f = list(stats['all_f'].keys())[0]
        warnings.append(
            f"⚠️  Only ONE F value (F{only_f} = {only_f/60:.0f} mm/s) appears in the whole file. "
            f"Travel and print are running at the same speed — likely the 'sticky F' bug. "
            f"Fix the slicer profile (travel_speed ≠ print speed) or use patch_travel_speed.py."
        )
    if stats['n_travel'] == 0:
        warnings.append("⚠️  No travel-only moves detected. File may be incomplete or non-standard.")

    if warnings:
        print("=== WARNINGS ===")
        for w in warnings:
            print(w)
    else:
        print("No warnings.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('input', help='Path to .gcode file')
    args = p.parse_args()
    stats = analyze(args.input)
    report(args.input, stats)


if __name__ == '__main__':
    main()
