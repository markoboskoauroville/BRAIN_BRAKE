ONE REAL STILL PER LIVE FRAME. STEP 33, redone by setup in STEP 36.

Pulled by Claude Code from the shoot footage on Baba's Mac, 2731x1536, the same
size as every other picture in the film. Named by frame id with dots as
underscores.

ALL TWENTY SEVEN LIVE FRAMES NOW SHOW MANAN. There are no desks left in here.

WHAT WENT WRONG THE FIRST TIME, AND WHY IT IS WORTH KNOWING.

STEP 33 pulled the still from the take that STEP 14 had chosen. Those takes were
chosen on WORDS. For ten frames the winning take came out of PANA6346 or
PANA6347, which are the read through, where the camera is on a desk and a book
and Manan is not in the picture at all. Nine more frames never had a take chosen
because they carry no line, so they had nothing to pull from.

None of that was missing footage. Every one of those frames was shot. It was
never selected, because selection ran on dialogue and these frames have none.

So STEP 36 selected on the SETUP instead. setups.json says which of the nine
camera setups each live frame belongs to, and a still from every one of the 163
clips on disk was looked at to see what each clip is actually pointing at. Not
the 62 that had matching dialogue: the frames with no line are exactly the part
MATCHES.csv cannot see.

WHERE EACH STILL COMES FROM

  A   grey backdrop, walking and reacting
      1.4 PANA6251   2.5 PANA6258   3.2 PANA6305   3.3 PANA6296   3.4 PANA6307
      1.5 and 3.5 kept their STEP 33 stills, which were already right
  B   standing eyeline, reacting to Coach Brain
      4.2, 4.5, 4.8, 4.9 kept their STEP 33 stills
  C   white void, still, to lens
      7.2 PANA6288   8.1 PANA6280   8.2 PANA6281   8.3 PANA6282
      8.4 and 8.5 kept their STEP 33 stills
  E   his room, at his desk
      2.3 PANA6197   4.6 PANA6210   5.3 PANA6204
  F   his room, at the blackboard
      2.1 PANA6218
  G   his room, on the stationary bike
      5.5 PANA6229   5.6 PANA6234   5.7 PANA6236   5.8 PANA6240
  H   the booth
      8.6 PANA6340
  EXT one quiet road, early morning
      5.4 PANA6180

TWO CLIPS WERE WRONGLY THROWN OUT IN STEP 33 and are back. The bike clips were
called "a different person"; they are Manan in a green shirt and they are setup
G. The booth clips were excluded as never usable; they are setup H, and the booth
is the only place 8.6 was ever shot. A clip is not wrong footage, it is footage
of a different setup.

TWO WERE REJECTED OFF THE FIRST CONTACT SHEET AND RE-PULLED from elsewhere in the
same clip: 2.5, where he was mid blink at the 40 percent mark, and 4.6, where his
head was turned away from the camera.

ONE TO LOOK AT. Frame 1.4 is marked LIVE in frames_v4.json but its artwork is
V7_1_3_sprint.jpg, the same drawing that DRAWN frame 1.3 carries. It may have no
live element at all. A setup A still is here so there is something, but check it
before it goes in a document.

What each of the 163 clips is pointing at is in tools/live_by_setup.py in the
working folder, with the contact sheets tools/clip_sheet.py builds.
