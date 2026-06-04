; #####################################################################
;  ANNOTATED READING COPY  -  travel_fixed.gcode
;  Hyrel SYSTEM 30M / PCL DIW / cube_10x10x10_2mm_Corners
; ---------------------------------------------------------------------
;  This is a SHORT, COMMENTED EXCERPT of the real file for eyeballing.
;  It is NOT the full 7,478-line print. The real one is in your repo:
;    gcode/cube_10x10x10_2mm_Corners/travel_fixed.gcode
;  Do NOT load THIS file into Repetrel - load the real one.
; ---------------------------------------------------------------------
;  My annotations are the lines starting with  ;>>   (added by me).
;  Everything else is verbatim from your actual file.
; #####################################################################


; ===== YOUR PATCH HEADER (verbatim, lines 1-20 of the real file) =====
; PATCHED: Travel-speed fix applied 2026-06-01 by Nengi + AI
; ORIGINAL ISSUE: F1500 written ONCE; every travel + print move inherited
;                 25 mm/s -> stringing during travel (ink oozed).
; PATCH:          travel moves (G1 X Y, no E)  -> F3600 (60 mm/s)
;                 first print move after travel -> F1500 (25 mm/s) re-stamped
; ROOT CAUSE:     print INI had travel_speed = 25 = perimeter_speed.


; ===== HYREL INIT (verbatim from real header) =====
M229 E1 D1        ; enable E-values (volumetric)
;>> VOLUMETRIC MODE. E is in cubic mm (mm^3), NOT mm of filament.
;>> So if you ever add retraction, "E-1.5" = 1.5 CUBIC mm of ink.


; ===== TEMP CONTROL (verbatim) -- READ THIS BEFORE YOU PRINT =====
M190 S80          ; bed temp     : set and wait
M109 T12 S240     ; head temp    : set and wait
;>> !!! FLAG !!! These are leftover from the ABS profile.
;>> "set and wait" = printer heats head to 240C + bed to 80C and
;>> WAITS before moving. PCL melts ~60C and degrades well below 240C.
;>> If PCL / solvent ink / vaseline is in the syringe, 240C is bad.
;>> ASK NICK: zero these, or set to a real value, before running.
;>> (Your travel patch was correct; it just didn't touch the header.)

T1                ; use SECOND tool position from the left


; #####################################################################
;  THE PATCH PATTERN  (verbatim lines 118-123, real coordinates)
;  Sequence: print -> travel -> print  (this repeats ~242 times)
; #####################################################################

G1 X128.918 Y105.321 E5.60981 ; skirt
;>> PRINT move (has E). Inherits F1500 = 25 mm/s. Correct.

G1 X129.199 Y105.495 F3600 ; move to first skirt point
;>> TRAVEL move (NO E). Patched to F3600 = 60 mm/s.
;>> Faster reposition = less linger = less ooze across the gap.
;>> NOTE: still no retraction here. Ink can still weep from the tip.
;>> That is the open Day-2 question (option C / ask Nick).

G1 X129.222 Y105.457 E5.61349 F1500 ; skirt
;>> PRINT resumes. F re-stamped to F1500 = 25 mm/s.
;>> Without this re-stamp the move would inherit F3600 and print
;>> too fast. This re-stamp is the "202 print re-entries" in your notes.

G1 X130.296 Y104.349 E5.74132 ; skirt
;>> more PRINT moves, all inherit F1500 until the next travel. Correct.


; #####################################################################
;  NOT IN THE FILE YET - retraction proposal (Day-2 option C)
;  Fully commented so it can't execute. Ask Nick BEFORE enabling.
; #####################################################################
; G1 E-1.5 F2400                     ;>> RETRACT 1.5 mm^3 at 40 mm/s
; G1 X129.199 Y105.495 F3600         ;>> travel with tip "empty" -> can't ooze
; G1 E1.5 F2400                      ;>> UN-RETRACT: push 1.5 mm^3 back to tip
; G1 X129.222 Y105.457 E5.61349 F1500 ;>> resume printing cleanly
;>> 1-2 mm^3 is a sane SDS-10 / 24G start. Too much pulls AIR into the
;>> line -> skips on next deposition. Confirm amount with Nick.


; #####################################################################
;  F <-> SPEED  (divide F by 60)
;    F1500 = 25 mm/s  <- print speed (leave alone)
;    F3600 = 60 mm/s  <- patched travel speed
;    F4800 = 80 mm/s  <- next bump if 60 prints clean
; #####################################################################
; Real file F counts: 243x F1500 (print) + 243x F3600 (travel). Clean.
