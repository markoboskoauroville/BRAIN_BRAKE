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

**It happens twice, and only twice.**

    1   the runner, when he sees the finish line and sprints
    2   Manan, when he tries the bicycle

Two is the number. If it happens a third time it stops meaning anything. Anywhere else in the film,
however good the moment, the animation stays strobed.

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
carries no detail. **That is why the face has drifted through every version of frame 1.1.** v3 fixed
the eyes, v4 restored the lean, v5 held, and v6 came back as a visibly different man with a longer
face and a startled stare. Nothing anywhere holds his identity at portrait scale, so each run invents
it again.

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

**V7 is not deleted and not edited.** It stays as it is, because a published letter is never
overwritten, and frames V8 has not reached yet are still V7 frames and still ship. The animator site
carries **V8 DRAFT** in the bar on every page and a line at the top of the landing page saying so, so
Kristijan is never looking at a page without knowing what generation it belongs to.

**Two tracks, and they must not be merged.** V8 is artwork. The film document is on its own letter,
`V4f`, which goes up on every rebuild of the PDF and has nothing to do with the artwork number. A
conversation that says only "v8" is talking about the pictures.

**Still to do:** `HANDOVER_V7.md` becomes `HANDOVER_V8.md` when the state of the production is next
written up, and `TAKEOVER.md` points at it. Not done yet, and it should not be done until scene 1 has
actual V8 frames in it, or the handover will describe a generation that is empty.

---

## 6. OPEN QUESTIONS

Written down rather than guessed at.

- **Is 1.2b a drawing or a photograph?** The finish line between the trees is something he *sees*, in
  the world, which by the film's law makes it a photograph. But scene 1 is entirely drawn up to this
  point and Manan does not arrive until 1.4. Needs a decision before the frame is prompted.
- **Does the strobe drop at 1.2a, at 1.2b, or at 1.3?** The release is at the sprint, but the moment
  he *sees* may want to be the hinge. This is an animation decision for Kristijan and Baba together.
- **Which existing scenes are being cut or combined**, to pay for the richer scene 1 and to get back
  under two minutes.
