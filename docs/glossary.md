# Glossary

Short definitions only. The full keyword/reference doc lives at `docs/keywords.md`. This one is the "I need to recall a single term" lookup.

## G-code

| Term | Meaning |
|---|---|
| F | Feedrate — toolhead motion speed in mm/min. Sticky. |
| E | Extruder amount — mm of filament, OR mm³ if M229 volumetric mode is enabled. |
| G0 | Rapid (travel) move. No extrusion. |
| G1 | Controlled move. Print if E is present; travel if not. |
| G28 | Home all axes. |
| G92 | Set current position. Used for Z-offset. |
| M104 / M109 | Set extruder temp, no wait / with wait. |
| M140 / M190 | Set bed temp, no wait / with wait. |
| M229 E1 D1 | Enable volumetric E (Hyrel always uses this). |
| M756 S[h] | Hyrel: set layer height. |
| M727 / M729 | Hyrel: prime / un-prime head. |
| T0 / T1 / T12 | Tool slot select on Hyrel. |

## Slicer settings

| Term | Meaning |
|---|---|
| travel_speed | Feedrate when not extruding. Should be 3–10× print speed for DIW. |
| perimeter_speed | Print speed for outer walls. |
| extrusion_multiplier | Scales E values. 0.95–1.05 normal range. |
| retract_length | mm of filament pulled back before travel. |
| retract_lift / Z-hop | Lift nozzle during travel to clear print. |
| wipe | Sideways nozzle wipe during retraction. |

## Materials

| Term | Meaning |
|---|---|
| PCL | Polycaprolactone. Biodegradable polyester, melts ~60 °C. |
| PEO | Polyethylene oxide. Water-soluble. Blended 1:1 with PCL for wettability. |
| PEDOT:PSS | Most-used conducting polymer. Watery dispersion as sold. |
| PANI | Polyaniline. Conducting polymer. Lab's eventual target. |
| PDMS | Silicone elastomer. Soft, biocompatible, insulating. |
| DCM | Dichloromethane. PCL solvent. Toxic, fume hood required. |
| ACE | Acetone. Alternative PCL solvent. Inferior viscosity recovery vs DCM. |

## Rheology

| Term | Meaning |
|---|---|
| Shear-thinning | Viscosity drops as shear rate rises. Required for DIW. |
| Yield stress | Minimum stress to initiate flow. |
| Power-law index (n) | < 1 = shear-thinning. n = 1 = Newtonian. |
| Recovery (%) | Viscosity returned after shear stops. ≥ 80% in 90 s. |
| Thixotropy | Shear-thinning + recovery combined. |
| Filament fidelity | Printed line width ÷ nozzle diameter. ~1.0 ideal. |
| Pore printability (Pr) | L²/(16·A). Pr = 1 = perfect square pore. |

## Hyrel hardware

| Term | Meaning |
|---|---|
| SDS-10 | Smooth Driven Syringe, 10 cc reservoir. The DIW workhorse. |
| EMO | Emulator Motor Output. Heated melt extruder. |
| VOL | Volumetric head. High-precision flow control. |
| Repetrel | Hyrel's proprietary printer-control program. NOT a slicer. |
| ESR | Engineering Solutions Researcher. A Hyrel SYSTEM 30M variant. |
| T1 / T12 | Tool slot positions on the Hyrel. |

## Software

| Term | Meaning |
|---|---|
| Slic3r | Original open-source slicer (MIT). |
| PrusaSlicer | Slic3r fork. The slicer this lab uses. |
| Repetrel | Hyrel's printer controller (not a slicer). |
| STL | 3D mesh file format (slicer input). |
| G-code | Plain-text printer instructions (slicer output). |
| ImageJ | Free image analysis (used in Teixeira for line measurements). |
