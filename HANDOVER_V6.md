# HANDOVER, 11.8.2026, END OF THE V6 BOARDING SESSION

Read `HANDOVER.md` first, then this. This file covers what changed today.

## WHERE THE FILM IS
Version six is boarded in full. Eight scenes, forty eight panels, `assets/V6/boards/V6_S1` to `V6_S8`.
Boards go to Neha by midday tomorrow on WhatsApp. Before they go, work the defect register.

## THE ONLY OPEN JOB
`assets/V6/DEFECTS.md`. Seven defects, three of them priority one. Fix one panel at a time in the
editor.

**Corrected 12.8.2026.** This file previously said the S8 lever prompt was issued and not yet run. It
was run. Marko produced the repaired sheet and the repo was simply a build behind it. The new
`V6_S8.jpg` is committed. Two of the three S8 p3 faults are gone, the lever is upright with its scale
and the ball reads 95 with the gap open above it. One fault remains, the hand is still an adult's and
must be the boy's.

## THE FILM
V3 script, eight scenes, plus four things from Manan's V1: the muscle factory, the phone in low power
mode, the seven step flowchart with real terms, and the closing line about better questions. Every
request Neha made came from V1, so the honest description is Manan's original told with V3's discipline
and Marko's visuals.

## THE METHOD THAT WORKED
One sheet per scene, Nano Banana Pro, 3:2, two references: a cast strip built in the container plus the
previous approved sheet. Then single panel repair in the editor for any beat that missed. Four of eight
needed one.


## READ STALE_CACHE.md BEFORE BUILDING ANY DOCUMENT

`STALE_CACHE.md` in the repo root. A path keyed image cache served old pictures into every rebuilt PDF
for hours on 13.8.2026 while Marko was repeatedly told to refresh his download. He was right, the tool
was wrong.

Two rules from it, and they are not optional:

1. **Every cache keys on content, size and mtime, never on a filename.** Frames are replaced in place on
   this film, so a name keyed cache will lie.
2. **When somebody says the output did not change, verify the artefact, not their setup.** Download the
   published file back and diff a page against the local build before offering any other explanation.
