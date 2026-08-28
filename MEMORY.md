# MEMORY

**The film's own memory. What was decided, why, and what it means for the pictures.**

`TAKEOVER.md` is the map and says what to read. `HANDOVER_V7.md` is the state of the production.
**This file is the reasoning.** The decisions that are not obvious from looking at a frame, in Baba's
words, so that nobody has to rediscover them and nobody argues with them from a stale document.

Not to be confused with `MANTRA_MANIFEST/MEMORY.md`, which is Baba's memory across every project.
That one holds people, places and one-off facts. **This one holds only THE BRAIN BRAKE.**

Newest decisions go at the bottom of their section. Nothing is deleted. When something turns out to
be wrong it is corrected in place with a note saying what changed, because a memory that is quietly
wrong is worse than no memory.

---

## 1. THE LANGUAGE OF THE FILM

### 1a. THE STROBE LAW

*Decided 28.8.2026. This is the central visual idea of the film and everything else serves it.*

**The whole film is strobed.** Posterized time, stepped, not on ones. The animation deliberately does
not run at full frame rate. Baba calls it strobe because that is how he thinks about it; an animator
will call it posterizing or stepping, and it is the same thing.

**Why: it says something is breaking. Something is stuck.** The audience never has to be told this.
Reduced frame rate reads in the body as a machine that is not turning over cleanly, and that is the
subject of the film. The strobe is the brain brake, made visible, before a single word explains it.

**And then it breaks the rule on purpose. Every time a muscle is truly activated, the animation goes
to full frame rate. No strobe. Smooth.**

That is the payoff, and it only works because everything around it is stepped. The eye does not need
to understand it to feel it: the film loosens exactly when the body is released.

**CORRECTED 28.8.2026. It happens three times, and it is the same sequence every time.**

    1   the runner, the moment he sees the finish line, before he sprints
    2   Manan, when he tries the bicycle
    3   Coach Brain, at the line about the limit being a setting

**This section first said twice, and that a third time would kill it. Baba's call is three, and it is
a stronger idea than the one it replaces**, because the three are not three similar moments. They are
**the same sequence, copy pasted**. Identical frames, identical timing, three times. That is what
turns it from an effect into a motif: the audience learns it on the runner, recognises it on the
bicycle, and understands it when Coach Brain names it.

**So it is built once and used three times.** One set of key frames, one folder, referenced from all
three insert points. Never three versions of the same thing, or they drift and the recognition dies.

**Rates.** Everything in the film is stepped at roughly **five to seven frames a second**. The muscle
activation runs at **twenty five**. Anywhere else, however good the moment, the animation stays
stepped.

**The parkour material is absorbed into this sequence** and is no longer its own scene. The existing
scene 6 artwork is the sequence in draft: `V7_6_4_one_fibre`, `V7_6_5_cluster`, `V7_6_6_leg_alight`,
`V7_6_6_whole_leg`, `V7_6_7_whole_body`, `V7_6_8_pushing_off`, `V7_6_8_traceur`, `V7_6_9_the_leap`.
Two of those, `traceur` and `the_leap`, are among the sixteen V7 frames made and never used. See
`ARTWORK_INDEX.md`.

**Kristijan has to be told this before he animates anything**, because it is not a note about one
shot, it is the frame rate policy of the entire film and it changes how every scene is built. It is
also the cheapest idea in the film: stepping costs less work than full animation, so the film is
mostly cheap and spends everything it has on two moments.

### 1b. THE PARKOUR SEQUENCE IS REPURPOSED

*Decided 28.8.2026.*

The parkour material is no longer its own idea. **It is now the film's signal for muscle activation**
and it is used wherever muscles come alive. Same principle as the strobe: one visual language, used
consistently, so the audience learns it once and then reads it everywhere without being taught again.

### 1c. THE OLDER LAW THIS SITS ON TOP OF

Anything **real** is a photograph. Anything **thought** is a pencil drawing on cream paper. That has
not changed and the strobe law does not touch it. See `worlds.md`.

---

## 2. THE HOLE IN SCENE 1, AND THE FIX

*Found by Baba, 28.8.2026.*

### What is wrong

Scene 1 as built runs:

    1.1   V7_1_1_face.jpg         the spent face, gasping, close
    1.2   V7_1_2_going_down.jpg   buckling, head thrown back, going down
    1.3   V7_1_3_sprint.jpg       upright, driving, sprinting

**He collapses and then he sprints, and nothing in between tells us why.** The sprint has no
motivation. It is the single biggest structural fault in the opening.

**And there is a second thing, found while looking at the three frames together: nobody in scene 1
looks at anything.** In 1.1 the eyes go to camera or into nothing. In 1.2 the head is thrown back at
the sky. In 1.3 he faces front and runs. There is not one eyeline in the whole scene, so there is
nothing in the world for him to want. The missing motivation is not only a missing shot, it is a
missing *direction of attention*, and that is why the cut feels arbitrary rather than fast.

### The fix

**He sees the finish line between the trees.** That is the motivation. He sees it, he gets it back,
the brake comes off, and he runs like a fresh man.

**Between the seeing and the running, the muscle activation goes in.** Scene 1 runs: down and dying,
he lifts, he sees, **cut to what he sees**, **cut to the muscle activation at full frame rate**, cut
to him running fresh. The motif is the bridge from the internal state to the external one: the
muscles come alive inside him, and only then does the outside of him change.

Two new frames, between 1.2 and 1.3:

    1.2a   he sees it. Down, spent, and his eyes find something off in the distance.
           The eyeline is the whole shot.
    1.2b   the cut. What he sees. The finish line, glimpsed between the trees.

**And 1.3, the sprint, is where the strobe drops away and the animation goes to full frame rate.**
That is the first of the film's two releases and it is what the new frames are paying for. The
sequence now reads: spent, going down, he sees, that is what he sees, and the film itself changes
gear.

**Numbering.** A shot that does not exist in the film yet gets a letter on the frame number, so these
are `1.2a` and `1.2b`, files `1-2a-v1.png` and `1-2b-v1.png`. Versions never restart. See
`MANTRA_MANIFEST/modules/versioning.md`.

**Not yet done, and it must be done when they are wired in:** adding two frames changes every timecode
after them. `assets/train/frames_v4.json` is the film and the whole rebuild chain runs after any
change to it. See `TAKEOVER.md` section 3.

---

## 3. SCENE 1 IS BEING REBUILT FROM SCRATCH

*Decided 28.8.2026.*

**Scene 1 is the most important scene in the film**, because it is not only the opening, it is where
the audience is taught the entire language: photograph versus drawing, the strobe, and the release.
If it does not land, nothing after it can.

So it gets completely new frames rather than repairs. Everything currently in `assets/V7/V7_1_*` is
treated as a draft.

Two things carry over into every new scene 1 frame:

- **No panel border.** All three existing V7 scene 1 frames have the hand drawn rectangle around
  them. The rule since 27.8 is that artwork runs edge to edge and Kristijan adds the frame himself as
  its own layer.
- **2731 x 1536**, always, cropped from the 2752 the tool returns.

### The economy behind this, and it applies to the whole film

**Make the important scenes rich. Reduce the ones that are not.** Scenes will be taken out and
scenes will be combined. The film is currently 2:54 against a 2:00 ceiling, so this is not only a
craft decision, it is where the two minutes are going to come from. Spend the frames, the animation
and the credits where the film is actually won, and let the rest be economical.

---

## 4. THE RUNNER, AND WHAT HIS SHEET DOES NOT HAVE

*28.8.2026.*

**The sheet exists.** `assets/REFERENCES/RUNNER.jpg`, 2752 x 1536, titled THE MARATHON RUNNER. Four
views: front, three quarter, profile, rear. Lean man of about forty five, singlet and shorts, bib
**27**, worn racing shoes, hair swept back. There is also `RUN_CYCLE.jpg`, four positions of the same
man running, and `RUNNER_END_REF.jpg`.

**What it does not have is a face.** Every view on the sheet is full body, so the head is small and
carries no detail. Nothing anywhere holds his identity at portrait scale, so every run has to invent
the head again.

**CORRECTED 28.8.2026, and the correction is mine.** This section first said v6 came back as a
visibly different man with a startled stare, and that the spent heavy lidded performance won in v3
and v4 had been thrown away. That was overstated. Put the original `V7_1_1_face.jpg` beside v5 and
v6 at head size and **the original is already wide eyed and staring**, with the same round eye and
the same white showing that I criticised in v6. v6 did not invent a new man. It drifted back toward
the original one. v5 is the outlier of the three, not v6.

**What is still true about v6** is the part that has nothing to do with the face: the head turned,
the framing pushed in and the road was rebuilt to a single vanishing point, none of which was asked
for. The lesson about edit prompts stands. The verdict on the man was wrong.

**And which eye the film wants is Baba's call, not mine.** The spent look and the staring look are
both defensible and they are different films. It should be decided once, on the face sheet, and then
every frame inherits it.

**So before scene 1 is rebuilt, the runner needs a face sheet.** One head, several angles, at a size
where the features are actually drawn. Generated once from the strongest existing face and then never
regenerated, exactly as `nanobanana.md` section 3 requires: fix the sheet, not the frame. This is one
run and it saves five.

**The strongest existing face to build it from is `V7_1_1_face.jpg`**, which is the original 1.1 and
is a better and more specific face than anything the reworking has produced since.

The sheet is annotated with view captions and a title, and that is safe. It was tested on 9.8.2026
and none of the lettering bled into the output. But it is a **multi panel sheet**, so it must never be
handed to a single frame job directly — sheets beget sheets. Crop the one view that is needed and feed
that.

---

## 5. THE FILM IS ON V8 FROM 28.8.2026

*Confirmed by Baba, 28.8.2026.*

**V8 is the eighth generation of artwork.** The generations on disk run `V3A, V4, V5, V6, V7`, and
V7 was current until today. The scene 1 rebuild is what opens V8, so everything made from here lands
in `assets/V8/`.

**V7 is stored, not superseded.** All fifty frames of the cut still point at V7 images, so V7 is not
the previous artwork, it *is* the film as it currently stands. It stays exactly as it is and every
frame of it can be referenced and reused. The animator site carries **V8 DRAFT** in the bar on every
page and a line at the top of the landing page, so Kristijan always knows which generation he is
looking at. That line used to say V7 was superseded. It was wrong and it has been corrected.

**Two tracks, and they must not be merged.** V8 is artwork. The film document is on its own letter,
`V4f`, which goes up on every rebuild of the PDF and has nothing to do with the artwork number. A
conversation that says only "v8" is talking about the pictures.

**The read through is now synced to it.** On 28.8.2026 the read through jumped from `v4` straight
to `v8`, skipping three numbers, so the document and the artwork carry the same number and nobody
has to translate between them. `VERSION` in `30-readthrough-4up.py` is the single place it is set.
`4-BRAIN_BRAKE_READ_THROUGH_v4.pdf` is not deleted, it stays in `assets/pdf/` and on the animator
site marked superseded, and its link still works.

**And a doctrine fault found while doing it.** `TAKEOVER.md` said the film document was on `V4f`.
The disk has `V4g`, `V4h` and `V4i`. The written rule was three letters behind the artefact, which
is the same failure as the border line and the camera-left line before it. Corrected.

**V8 lives in the animator repository, not here.** From 28.8.2026 the read through has one home,
`ANIMATOR_COLLABORATION/DOCS/`, and is no longer copied into `BRAIN_BRAKE` as well. New V8 artwork
already lands in the animator repo, because the watch folder pushes there. So `assets/V8/` in this
repository stays as a marker and the pictures live where the animator can reach them.

**And the honest part, which matters more than the move.** Deleting the file from this repository
does **not** make it smaller and never will. The 75 MB blob is already in the history and it stays
there for ever. This is exactly what `TAKEOVER.md` section 5b already recorded when `animator/` was
taken out and the repository did not shrink. What the move actually buys is that **v9, v10 and every
one after cost 75 MB once instead of 150 MB twice.** It stops the bleeding, it does not heal it.
`assets/pdf/` still holds read throughs v1 to v4 and the whole `THE BRAIN BRAKE V*.pdf` series, and
the pack is 1.73 GB.

**The only thing that would actually reclaim it is rewriting history**, with `filter-repo` or BFG and
a force push. That was deliberately not done on 28.8.2026 when the animator folder moved out, and the
reasoning then was to stop the growth rather than reclaim what is already spent. Nothing has changed
that reasoning. It should not be done casually, and never without Baba saying so, because it rewrites
every commit id and breaks every existing clone and every link that points at a commit.

**Still to do:** `HANDOVER_V7.md` becomes `HANDOVER_V8.md` when the state of the production is next
written up, and `TAKEOVER.md` points at it. Not done yet, and it should not be done until scene 1 has
actual V8 frames in it, or the handover will describe a generation that is empty.

---

## 6. THE LAW OF THE LIBRARY

*Baba, 28.8.2026.*

**Nothing is deleted. It is stored, in its own folder, and it can be referenced.** A new generation
never kills the one before it.

**If an old image is better than a new one, modify the old one and use it.** A rework is not obliged
to win. When a v6 comes back worse than the v5 it replaced, going back to v5 and changing the one
thing that was wrong is not a failure, it is the cheapest move available: the old file already has
the right hand, the right paper and the right performance, and it costs nothing.

**So being aware of the old artwork is part of the job**, not an afterthought. `ARTWORK_INDEX.md` at
the root of this repo lists every generation, every V7 frame, which frames of the cut use it, and
which were made and never used. It is generated by `tools/artwork_index.py` from what is actually on
disk, so it cannot drift. **Read it before generating anything new.**

**Two things that index turned up on the day it was written.**

*Sixteen V7 frames were made and are not in the cut*, and two of them are exactly the material the
strobe law needs: `V7_6_8_traceur.jpg`, the parkour rooftop leap, and `V7_5_1_bike.jpg`, the bicycle.
Both of the film's two full frame rate moments already have artwork sitting unused in the library.

*Two frames of the cut point at images that do not exist anywhere in the repository.* Frame 4.5 wants
`V7_4_4b_pacing.jpg` and frame 4.9 wants `V7_4_8_definition.jpg`. Both are LIVE frames, so real
footage covers them in the edit and nothing is broken on screen, but the source of truth is pointing
at nothing and any builder that places a picture for those frames has nothing to place.

**And modifying an old image still produces a new number.** Reaching back to `V7_1_1_runner.jpg` and
changing it does not overwrite it. It becomes the next version under the new frame's name. A
published file is never edited in place.

---

## 7. THE THREE LEVELS: SCENE, SHOT, KEY FRAME

*Baba, 28.8.2026. This changes the working vocabulary of the whole production, so it goes near the
top of anyone's reading.*

    SCENE       the largest division. Eight of them. "Scene 1, The Mystery."
    SHOT        smaller. A shot lives inside a scene. 1.1 is a shot.
    KEY FRAME   smaller again. A key frame lives inside a shot.

**And the workflow changes with it. We now generate per shot, not per scene, and what we generate
are key frames.** A shot is not one picture any more. It is a set of key frames, and the animation
happens between them.

**Why this follows from the strobe law.** The film is stepped, and stepping is drawn between poses.
A shot that is one picture has nothing to step between. Naming the key frame as its own level is
what makes the animation plannable at all, and it is what Kristijan actually needs handed to him:
not "here is shot 1.1" but "here is where 1.1 starts and here is where it ends."

**What Baba sent on 28.8.2026** was the panel marked `[ 1.1 ]` out of the read through: the spent
runner, framed. He called it **the main key frame reference** for that shot. So a shot has one main
key frame that establishes it, and others that come off it.

### Naming, PROPOSED, NOT YET AGREED

Written down so it is decided once rather than drifted into. **Nothing is generated under this until
Baba confirms it.**

    1-1-v7.png        the MAIN key frame of shot 1.1. The existing chain continues
                      unbroken, versions never restart
    1-1-K2-v1.png     a second key frame in shot 1.1
    1-1-K3-v1.png     a third
    1-2a-v1.png       a NEW SHOT between 1.2 and 1.3. Lowercase letter on the shot
                      number, which is the existing rule and does not change

The point of the capital K is that the existing lowercase-letter rule already means *a new shot*, so
key frames need a mark that cannot be confused with it. `1-3a` is a shot. `1-1-K2` is a key frame
inside a shot.

### What this changes that has not been done yet

- **The animator site says "Frames".** Under this vocabulary a scene page holds shots, and a shot
  holds key frames. The page should say so. Not changed yet, because changing it before the naming
  is agreed would mean changing it twice.
- **`frames_v4.json` calls everything a frame** and its ids are shot ids. The word is now wrong even
  though the data is right. Renaming the field would break every builder, so this is a documentation
  fix and not a data one, unless Baba wants otherwise.

---

## 8. ANYTHING THAT MOVES ON ITS OWN IS A LAYER, NOT PART OF THE DRAWING

*Baba, 28.8.2026. Starts with the sweat on shot 1.1 and applies to everything after it.*

**The sweat droplets are going to be animated, so they cannot be drawn into the frame.** Every key
frame ships with **dry skin**, and the droplets arrive as their own transparent layer that Kristijan
can isolate, move and time.

**This is the same law as the panel border and it generalises.** The border came out of the artwork
and became `FRAME_BORDER-v2.png` because it has to be able to move. Sweat has to be able to run. Any
element that animates independently of the drawing underneath it is a layer:

    the panel border      done, FRAME_BORDER-v2.png
    sweat droplets        starting now, shot 1.1
    anything that drips, blinks, flickers, breathes or travels

**So the question to ask of every new frame is: what in this picture moves on its own?** Whatever
the answer is comes out before the frame is delivered, not after.

### How to get a layer out, cheapest first

1. **Cut it, free.** Works when the thing is separable by position or tone, as the border was: it sat
   on a known rectangle and nothing else was there. **It does not work for sweat.** Droplets are the
   same graphite as the skin they sit on, in the same tonal range, scattered over the exact surface
   they must be separated from. There is no threshold that finds them.
2. **Generate the plate without it, then difference, free.** Get the dry version, register it against
   the wet one, and what changed is the layer. Costs one run instead of two and the registration is
   perfect by construction. Only works if the two pictures are otherwise near identical, which is
   exactly what a short edit prompt is for and exactly what a long one destroys.
3. **Generate the layer on its own, one credit.** The fallback when 2 comes back too noisy: ask for
   the droplets alone on empty cream paper. Cream, not black, because every reference the model has
   of this film is graphite on cream and asking for black changes the medium as well as the content.

**Try 2 before spending on 3.** It costs nothing to look.

---

## 9. THE WHY LAW, AND HOW SCENE 1 IS CUT

*Baba, 28.8.2026. This is the editing law of the whole film, not a note about one scene.*

**The audience asks why, and then we answer.** Every cut in the film works this way. Show the effect
first and let them want the cause. Never explain before they have asked. That is what moves the film
forward and it is what decides shot order everywhere.

### The hole this fixes

He is finished, and then he runs. Nothing tells us why. The sprint has no motivation and the cut
reads as arbitrary.

### Why he is so tired, which was never stated anywhere

**He does not know he is near the end.** He believes he still has ten kilometres to run. That belief
is the reason the exhaustion is total: he is not spent at the finish, he is spent in the middle of
what he thinks is still to come. The finish line is hidden behind trees, so he cannot see it.

### The three shots, in order

**One. The close up, and the emotion changes inside the shot.**
He is almost dying. Head down, eyes on the ground. Then he slowly rises. He glimpses something behind
the trees. His face changes. **All of this happens in one shot without a cut**, which is the whole
point: the audience sees a man change and has no idea why.

Because the change happens inside the shot, **this shot needs several key frames**, not one. At
minimum: down and dying, rising, and the face after it changes. That is the first real use of the
scene / shot / key frame structure in section 7.

**Two. What he sees. His subjective view.**
The finish banner, caught between the trees, the word FINISH on it. This is a point of view shot and
it is the answer to the question the previous shot planted. It also explains the trees: he could not
have seen it before, so his exhaustion was honest and not stupidity.

**Three. He runs like a fresh man.**
Not a tired man finding something left. A man who has just started the race. This is where the strobe
drops and the animation goes to full frame rate, section 1a.

### What this changes

- Scene 1 has more shots than the five in `frames_v4.json`, and more will appear as the scene is
  built. Numbering is decided when the shots are, not before.
- The subjective shot is the film's first point of view frame. Whether it is drawn or photographed is
  still open, section 10, and it matters more now: it is the only thing the audience is given as an
  answer, so it has to read instantly.

---

## 10. THESE FRAMES ARE THE FINISHED ARTWORK, NOT REFERENCE

*Baba, 28.8.2026.*

**Kristijan animates the delivered file itself.** He is not redrawing from it. So a key frame is not a
guide that is close enough, it is the picture that ends up on screen, and it gets polished until it
is right before it is handed over.

**What that changes in practice.** Anything that would have been "fine as a guide" is now a reject:
framing that drifts between key frames of the same shot, an element present in one key frame and
absent in the next, artwork touching an edge it should not, a face that has moved. Across a shot
where the emotion changes without a cut, **the framing must not move at all**, or the audience reads
it as a camera move instead of the man rising.

**And the cheapest way to hold framing is to feed the approved key frame back in as the reference for
the next one in the same shot.** Not the character sheet. The sheet holds who he is; the previous key
frame holds where the camera is.

---

## 11. OPEN QUESTIONS

Written down rather than guessed at.

- **Is 1.2b a drawing or a photograph?** The finish line between the trees is something he *sees*, in
  the world, which by the film's law makes it a photograph. But scene 1 is entirely drawn up to this
  point and Manan does not arrive until 1.4. Needs a decision before the frame is prompted.
- **Does the strobe drop at 1.2a, at 1.2b, or at 1.3?** The release is at the sprint, but the moment
  he *sees* may want to be the hinge. This is an animation decision for Kristijan and Baba together.
- **Which existing scenes are being cut or combined**, to pay for the richer scene 1 and to get back
  under two minutes.
