# TAKEOVER

**This file is the front door. Read it first, every session, before anything else.**

It exists because a chat filled up, a new one started from a summary, and within the first
twenty minutes the new session found four things the summary had got wrong or left out: a helper
that was never committed, a document whose head contradicted its own tail, a folder of voice takes
where a superseded recording sat next to the real ones under a plausible name, and a set of
animator packages built by hand that had silently gone stale. Any one of them could have broken
the film. None of them announced themselves.

So the project now has a fixed structure. It has a name, THE TAKEOVER, and it has one rule:

> **Every session ends by updating this file and the files it points to.
> A change is not finished when it is pushed. It is finished when the takeover reflects it.**

---

## 1. READ IN THIS ORDER

Do not skip and do not reorder. Each one exists because something went wrong without it.

| # | File | What it is | Read it when |
|---|------|-----------|--------------|
| 1 | `TAKEOVER.md` | this file, the map | always |
| 2 | `HANDOVER_V7.md` | the state of the whole production | always |
| 3 | `STALE_CACHE.md` | a failure that cost hours and must never repeat | always |
| 4 | `nanobanana.md` | everything learned about image generation | before generating any image |
| 5 | `VOICES.md` | Hume, the cast, which takes are real | before recording or retiming |
| 6 | `ANIMATION.md` | the animator's site and layered packages | before touching animation |
| 7 | `MANAN_TRAINING_DEVELOPMENT.md` | how the acting guide was built | if the guide comes up |
| 8 | `storytelling.md`, `elements.md`, `worlds.md` | story and structure | if story or structure changes |
| 9 | `MESSAGES.md` | the voice for anything sent to the crew | before writing any message |

---

## 2. THE ONE SOURCE OF TRUTH

**`assets/train/frames_v4.json` is the film.** Fifty frames, in order, each with its id, scene,
layer, image, mode, speaker, line, duration in frames, in and out points, transition note, and
whether its timing is measured from real audio or estimated from a word count.

Every document, every package and every guide is derived from it. Nothing is typed by hand twice.
That is what stops Manan's lines drifting from the film's lines, which is exactly what happened
before the derivation existed.

If you change one frame, you have changed every timecode after it. **Rebuild everything.**

---

## 3. THE REBUILD CHAIN

Run in this order after any change to `frames_v4.json`. Every step is a committed script. If you
find yourself doing any of this by hand, stop, and write the script instead.

```
python3 25-lines-manan.py            # Manan's lines  -> assets/train/lines_manan.json
python3 22-brain-brake-v4.py         # the film        -> THE BRAIN BRAKE V4x.pdf
python3 21-manan-training-book-v4.py # acting guide    -> HOW TO ACT NATURALLY v4 - Manan.pdf
python3 26-camera-guide-venkatesh.py # camera guide    -> CAMERA GUIDE - Venkatesh.pdf
python3 27-scene-packages.py         # animator        -> 8 zips + animation/index.html cards
```

`index.html` at the repo root is **not** generated. It is the public making of page, written by
hand, and it must never carry a crew name beyond Manan and Neha, or any figure. See section 8.

Working layout the builders expect, because they use absolute paths:

```
/home/claude/BRAIN_BRAKE   -> symlink to the repo
/home/claude/train/frames.json -> symlink to assets/train/frames_v4.json
/home/claude/train/lines.json  -> symlink to assets/train/lines_manan.json
/home/claude/train/img/    <- assets/V7/*.jpg + assets/train/*.jpg + animation/img/endcard.jpg
/home/claude/tc.py         <- copy of tools/timecode.py
/home/claude/Caveat.ttf    <- the handwriting font
/home/claude/out/          <- where the PDFs land before being copied into assets/pdf/
```

Version letters go up every rebuild. The film is on `V4f`. Never overwrite a published letter.

---

## 4. THE RULES THAT COST US SOMETHING

- **Never hand over a chat artifact.** Commit, push, verify 200, then give the raw link.
- **Download the published file back and diff it** against the local build before handing it over.
  A file can be right on disk and stale everywhere the crew can reach it.
- **If Marko says a file has not changed, that is a measurement.** Pull the artefact and check it
  before offering any other explanation. Never blame his download, his browser or a CDN first.
- **Cache on content, never on filename.** Frames get replaced in place constantly.
- **Timings come from measured audio, never word counts.** Word counts were out by more than two
  seconds on a single line.
- **The running time can never grow past 2:00.** Not 2:00.1. The film is not judged if it runs over.
- **No API key, token or credential ever goes to GitHub.** The repo is public. Credentials live only
  in the sandbox and are re-uploaded each session.
- **Never use an annotated frame as a generation reference.** Review labels burn into the output.
  This has happened twice.
- **Key light is CAMERA RIGHT, always.** Corrected 17.8.2026. `nanobanana.md` said camera left and
  claimed it as the law from `worlds.md`. `worlds.md` names no side, only that the side never
  changes, and every existing frame is keyed camera right. Venkatesh found it from the reference
  frames the day before the shoot.
- **When a written rule and the artefact disagree, measure the artefact.** That is how all three of
  the above were found. A rule nobody checks against a picture will outlive the picture.
- **Every image ships cropped to 2731x1536.** Nano Banana returns 2752x1536, which is slightly wide.

---

## 5. WHERE EVERYTHING LIVES

```
assets/train/frames_v4.json     the film, the source of truth
assets/train/lines_manan.json   derived, Manan's lines only
assets/voice/final/             the six takes that are IN the film. Time against these only.
assets/voice/auditions/         eighteen candidates and superseded takes. Never time against these.
assets/V7/                      the frame images
assets/pdf/                     everything published to the crew
assets/props/                   the prop sheets
animation/                      the animator's site, see ANIMATION.md
tools/                          nanobanana_helper.py, hume_helper.py, timecode.py, mabanana, mavoice
NN-*.py                         the builders, numbered in the order they were written
```

---

## 6. STATE, AND WHAT IS STILL OPEN

Updated **18.8.2026**, film at **50 frames, 2945 frames, 1:57.80, margin 2.20 s**.
Shoot day is **18.8.2026** in Bengaluru.

**17.8. session.** Venkatesh found two written rules that disagreed with the artefacts and both were
corrected: the key light is CAMERA RIGHT, not left, and 1.5 enters from camera left. Worse, the
camera guide had invented its own four setup scheme while the film document already had A to H plus
the exterior, so six frames were listed as grey that are shot in his room. Both documents now read
one shared file, `assets/train/setups.json`. Published: camera guide v3, film V4g, acting guide v5
with the label above each line removed. A bike reference image is at `assets/reference/`. The
production site at the repo root had its passphrase gate removed and is now open.

**Kristijan is engaged at 1000 EUR** for animation, compositing and finishing only. Marko does all
preparation, including keying Manan off the grey and delivering him cut out with an alpha channel.
Kristijan never touches the grey footage and does not need a camera test. They will work in the same
room in Zagreb once the material is prepared.

Done in the session before: Neha's three restored lines are in the film. Manan asks whether the brain
is secretly pacing him at 4.4b. The ending is her original triplet at 8.6, 8.7 and 8.8. The Central
Governor Theory is defined out loud at 4.8. To pay for them, 7.6, 8.5 and 6.3 came out. Scene 7 is
now wordless and survives as three silent panels, so the film is still eight scenes and nothing was
renumbered except old 8.8 and 8.9 becoming 8.9 and 8.10.

Still open, in the order it will bite:

1. **Manan's narration is not recorded.** Forty-four of fifty frames are estimated. When his audio
   arrives, retime from the measured WAVs, set `measured: true`, run the whole rebuild chain, and
   check the total against 2:00 before anything is sent to anyone.
2. **4.4b and 4.8 have no plates.** They are live camera frames and only exist after the shoot.
   They are in the packages and the camera guide, marked as shot on the day.
3. **Manan's eyeline on some frames is unresolved.** 4.2 is marked `CAM`, meaning he speaks to
   camera, but its reference shows him in profile looking at Coach Brain. The mode field and the
   picture disagree and only Marko can say which is right. Check the rest of the `CAM` frames
   against their references before the shoot.
4. **Music and sound design have not started.** Marko is composing. This is half the film.
5. **Kristijan has not quoted** for the reduced comic strip scope. Neha is handling it and Marko
   deliberately stays out of that conversation so it does not read as pressure on price.
6. **The production site at the repo root is stale and now public.** It describes the old six scene,
   thirty five shot version with different lines, an old budget table and old delivery dates. The
   passphrase is gone, so anyone with the link sees that. Rebuild it from `frames_v4.json` or take
   it down.
7. **Sound design and music have their own software to build.** That is the next phase and it
   starts in a fresh session. Nothing exists for it yet.
8. **The prop sheets cannot be rebuilt.** `23-prop-sheets.py` reads plate images from a working
   directory that was never committed. The finished sheets in `assets/props/` are fine, but the
   generator cannot be re-run. Same class of problem as the ones this file exists to prevent.

---

## 6b. THE PUBLIC SITE

`https://markoboskoauroville.github.io/BRAIN_BRAKE/` is a single page called **How we made The
Brain Brake**. It replaced the old crew facing production site, which had a passphrase, ten tabs,
crew names and a money table, and which was accidentally left public for a few hours.

Rules for it, and they are not negotiable:

- **Only two people are named: Manan and Neha.** Everyone else is a role. The cinematographer, the
  animator, the director. No exceptions and no initials.
- **No figures.** No fees, no budgets, no day rates, no totals.
- It is one page on purpose. Marko reads it aloud with Speechify, so it must not be split across
  URLs and must not hide content behind tabs or JavaScript.
- The PDFs under `assets/pdf/` and the animator's site at `/animation/` still carry names in
  filenames and text. They were left alone because the crew are working from those links. Rename
  them once the shoot is delivered.

## 7. HOW TO CLOSE A SESSION

Do all four. This is the part that was missing before.

1. Run the rebuild chain. Do not skip a step because it "did not change" — the timecodes moved.
2. Commit, push, and **verify each raw link returns 200 and matches the local build byte for byte.**
3. Update section 6 above: the frame count, the running time, the margin, what was done, what is
   open.
4. Update the file that owns whatever you touched. Images changed, `nanobanana.md`. Voice changed,
   `VOICES.md`. Animation changed, `ANIMATION.md`. Film state changed, `HANDOVER_V7.md`.
