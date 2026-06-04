# Conducting Polymers & Polyaniline (PANI) — Primer

*Background for the flexible-electronics pivot, built on your EE intuition.*

> **Citation note:** the conducting-polymer fundamentals here (conjugation, doping, PANI's oxidation states) are **general/textbook knowledge** — they are *not* from any one paper in your set, so they don't carry a paper citation. The only paper-specific citations are to **Yuk 2020** for the PEDOT:PSS numbers, since that's the conducting-polymer paper you actually have.

---

## 1. Why most polymers insulate, but some conduct
- **Normal polymers (PCL):** all single (sigma) bonds → electrons locked → **insulator.**
- **Conducting (conjugated) polymers:** **alternating single and double bonds** along the backbone — that alternation is the key. *(General.)*

## 2. Conjugation = the "electron cloud"
- Double bonds carry **pi electrons**; when bonds alternate, the p-orbitals overlap continuously and the pi electrons **delocalize into a continuous cloud** along the chain. That's the "electron cloud." *(General.)*

## 3. Conjugation isn't enough — you DOPE it
- A bare conjugated polymer behaves like a **semiconductor** (has a band gap), like silicon.
- **Doping** adds carriers — like doping silicon. Carriers are **polarons/bipolarons** moving along the chain. Conductivity can jump ~10 orders of magnitude. *(General.)*

## 4. Polyaniline (PANI) specifically *(general/textbook)*
**Structure:** benzene rings linked by nitrogen — the single/double-bond diagram your mentor showed.

| State | Oxidation | Conducts? |
|---|---|---|
| Leucoemeraldine | fully **reduced** | no |
| **Emeraldine** | **half-oxidized** | **only when doped** ← the useful one |
| Pernigraniline | fully **oxidized** | no |

**PANI's special trick — acid doping:** protonate **emeraldine base** (insulating) with acid → **emeraldine salt** (conductive). Add base → off again. A reversible acid/base ON–OFF switch.

## 5. Why not PANI alone — why PCL or graphite
- PANI alone is **brittle and hard to process** (intractable). *(General.)*
- **PCL is flexible + processable** but insulating. Combine → flexible conductive composite. *(PEDOT:PSS is the published demonstration of this combine-conductor-with-processability idea — Yuk 2020.)*

## 6. How it maps to your project
- **PCL** = flexible insulating matrix/substrate.
- **PANI** = intrinsically conducting polymer (conjugation + acid doping). *(General.)*
- **Graphite** = conductive filler; conducts past the **percolation threshold**. *(General concept — cite your graphite-composite paper.)*
- **Yuk 2020** is your closest *published* precedent for printing a conductor (PEDOT:PSS). Read it with this primer in hand. Concrete benchmarks to expect from a printed conductor:
  - Conductivity **155 S/cm (dry), 28 S/cm (hydrogel)** — (Yuk 2020, p.4, Fig.3a).
  - **<5% conductivity drop over 10,000 bends** — (Yuk 2020, p.4, Fig.3c).
  - Printable ink window **5–7 wt%** nanofibrils — (Yuk 2020, p.2, Fig.1).
  - Conductivity arises after drying/annealing drives **percolation among the nanofibrils** — (Yuk 2020, p.2 & Methods p.6–7).

---

## Vocabulary to lock in *(all general terms)*
- **Conjugation** — alternating single/double bonds → delocalized pi electrons.
- **Delocalized π-electron cloud** — the conduction highway.
- **Doping** — add/remove electrons (PANI: protonate with acid) to create carriers.
- **Polaron / bipolaron** — the mobile carriers.
- **Emeraldine base vs salt** — PANI insulating vs conductive; acid converts base → salt.
- **Intrinsically conducting polymer (ICP)** — conducts on its own backbone (PANI, PEDOT) vs a filler composite (PCL + graphite).
- **Percolation threshold** — filler loading where a composite switches conductive *(cite composite paper)*.

## One-line summary
**Conjugation builds the electron highway; doping puts cars on it. PANI's highway switches on with acid. PCL bends but can't conduct — pair them (or load PCL with graphite) for flexible + conductive.**
