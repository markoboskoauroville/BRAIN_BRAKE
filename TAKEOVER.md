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
| 3b | `MEMORY.md` | the film's own memory: the strobe law, why scene 1 is being rebuilt | always |
| 3c | `ARTWORK_INDEX.md` | every generation of artwork, what is in the cut, what is spare | before generating any image |
| 4 | `nanobanana.md` | everything learned about image generation | before generating any image |
| 4b | `MANTRA_MANIFEST/modules/imgtoimg.md` | the platform Baba actually uses, and the coin ledger | before writing any prompt for imgtoimg.ai |
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
python3 30-readthrough-4up.py        # read through    -> 8-BRAIN_BRAKE_READ_THROUGH_v8.pdf
                                     #   filed ONLY into ANIMATOR_COLLABORATION/DOCS/
python3 tools/artwork_index.py       # the library     -> ARTWORK_INDEX.md
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

Version letters go up every rebuild. The film document is on `V4i` on disk, although this line said `V4f` until 28.8.2026 and the artefact was three letters ahead of the doctrine. Never overwrite a published letter.

**The read through is synced to the artwork.** On 28.8.2026 it jumped from `v4` straight to `v8`, skipping 5, 6 and 7, so that the read through and the artwork generation carry the same number. `8-BRAIN_BRAKE_READ_THROUGH_v8.pdf`. From here they move together. The film document letters are still their own track.

**Artwork is a separate track and it is on `V8` from 28.8.2026**, opened by the scene 1 rebuild. New frames land in `assets/V8/`. `assets/V7/` stays exactly as it is and its frames still ship wherever V8 has not reached. Do not merge the two numbers: `V4f` is the document, `V8` is the pictures. See `MEMORY.md` section 5.

---

## 3b. RULES ADDED 27 AND 28 AUGUST

- **Artwork is edge to edge. No panel border.** Kristijan adds the frame himself as its own layer.
  Anything the old border was clipping gets restored.
- **Never crop an overlay.** A picture placed over another is scaled and moved, never cut. Only the
  frame crops. `nanobanana.md` item 9.
- **Every change is a new version number, however small**, and **never overwrite a file that has left
  the machine**. `1-1-v3.png` is v3 for ever. Whole numbers.
- **No exports.** Timelines only, unless Baba asks in that message.
- **One audio track.** Nobody speaks over anybody.
- **Three second minimum shot length.** No shot shorter, whatever it holds.
- **Colour management goes on the timelines, not the project**, all selected at once. V-Log is never
  auto detected. `modules/resolve-color.md`.
- **Never replace a span of a file by index.** Match the exact text and assert it was found. This
  silently deleted a function and three constants on 28.8 and shipped broken.

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

| repo | what it is | public? |
|---|---|---|
| `BRAIN_BRAKE` | **this one.** the film. script, artwork, footage stills, documents, builders | public |
| `MANTRA_MANIFEST` | the studio. how things are done, and `EXCHANGE.md`, the handover to Claude Code | private |
| `ANIMATOR_COLLABORATION` | Kristijan's site and his material, `BB_C_1` to `BB_C_8` | public, passphrase `kristijan` |
| `WATCH_FOLDER_DAEMON` | the folder that pushes what Baba drops in it, and the `watch` menu | private |

**On the Mac**

```
~/Developer/brain_break/            the working folder
  Brain Break - Aurovenkatesh Footages/   77 GB, read only, never edited
  _WATCH_FOLDER/                    drop a file here and it goes to the animator repo
  MANAN_CLONED_VOICE/               the cleaned recording for cloning
  animator_repo/                    a clone of ANIMATOR_COLLABORATION
~/.watchfolder/                     the daemon: config, log, worker, and its own source clone
```

**DaVinci Resolve.** `1-brainbreak_v1` holds everything built up to 27.8. `2-brainbreak_v2` is the
current one, 25 fps 4K, colour managed, with `ANIMATIC` and the eight `S1_TAKES` to `S8_TAKES` reels.
**Nothing outside the `ANIMATICS` bin and those reels is ever touched.**

## 5b. THE ANIMATOR MATERIAL HAS MOVED OUT OF THIS REPOSITORY

*28.8.2026.*

**`animator/` is gone from `BRAIN_BRAKE`. It now lives in its own private repository,
`markoboskoauroville/ANIMATOR_COLLABORATION`.** Everything that was in it moved across unchanged:
the images, `README.md` and `CHANGES.md`, and the `inbox/`.

**Why.** This repository had reached about 1.4 GB and pushes were failing on size. The animation
material is what grows fastest from here, so it was the right thing to take out.

**The scene folders are named differently there**, `BB_C_1` to `BB_C_8` rather than `scene_01` to
`scene_08`, so a folder name can never be read as a frame id.

**Removing the folder did not make this repository smaller** and it was never going to. The objects
are still in the history. History was deliberately **not** rewritten: no force push, no `filter-repo`,
no BFG. The point was to stop the growth, not to reclaim what is already spent.

`tools/watch.py` and the watch folder now push to the new repository. `CHANGES.md` continues there
without a break.

---

## 6. STATE, AND WHAT IS STILL OPEN

*28.8.2026.*

**The film.** Fifty frames, eight scenes, gap free numbering. `ANIMATIC` in `2-brainbreak_v2` runs
**4354 frames, 00:02:54:04**, three second floor on every shot, one audio track. The two minute limit
still governs the finished entry but does **not** govern this edit: Baba shortens it later with the
whole film in front of him.

**Sound.** Manan's session recording is cleaned and cut, `MANAN VOICE SAMPLE FOR CLONING.wav` and
`MANAN VOICE SAMPLE EDITED.wav`, by cutting only, no gain and no filters. The six Coach Brain and
worker takes in `assets/voice/final/` are already in the film.

**Pictures.** All twenty seven live stills are re-pulled through Resolve and are Rec.709, not log.
`assets/live/SOURCES.csv` holds the clip and in-clip timecode for every one.

**The read through** is `8-BRAIN_BRAKE_READ_THROUGH_v8.pdf`, and **it lives in `ANIMATOR_COLLABORATION/DOCS/`,
not in this repository**, from 28.8.2026. Four panels a page, drawn beside footage
where both exist with the clip and timecode stamped, and an appendix of one clean frame per shot.

### Open

- **Manan's delivery.** He speaks inward, nasally, aimed at nobody. Plan is in
  `MANAN_RECORDING_GUIDE.md`: generate his lines with Hume, let him copy the placement, take the
  reference away before the take. Recording around the 5th or 6th of next month, after picture lock.
  **Neha has been told and is waiting.** The reference recordings were promised to arrive *with* the
  lines, so they must exist by then.
- **Frame 1.1 is being reworked with Kristijan.** v2 removed the border, v3 fixed the eyes, v4 is
  wanted with the forward lean restored. Nothing else has started.
- **Scene 1 layers** exist for 1.1 to 1.5. No other scene has layers, and **breakdowns are now made
  on request only**, through the tick boxes on the site.
- **The ten 2400x1792 frames** are still 4:3 and were left alone deliberately, since they are
  placeholders that real footage replaces.
- **`CHOSEN.csv` and `MATCHES.csv`** were built before the renumbering. Every frame carries `old_id`
  so they translate rather than being redone.

## 6c. WHERE FRAME 1.1 IS, AS OF 28.8.2026

The first frame is being reworked with Kristijan, one version at a time, and this is the pattern for
every frame that follows.

| version | what it did | status |
|---|---|---|
| v2 | border removed, artwork to all four edges, head no longer clipped | superseded |
| v3 | eyes fixed, level into the distance | superseded, went fully upright |
| v4 | the forward lean restored | superseded, empty paper behind him |
| v5 | the road added, converging to a flat horizon | **the panel border came back** |
| v6 | v5 with no border | **asked for, not yet made** |

**The filename convention, so Baba never has to think.** Chat Claude gives the name every time, twice:
above the prompt as `Save as: 1-1-v6.png`, and as the first line **inside** the prompt block, `FILE:
1-1-v6.png`, so it travels with the paste into the image editor. The editor ignores that line.

Frame number with hyphens, then the next whole version, **always the next one, even for a tiny
change**. A shot that does not exist in the film yet gets a letter on the frame number, so something
between 1.3 and 1.4 is `1-3a-v1`. Versions never restart.

**The loop.** Chat Claude writes a prompt and gives it a filename. Baba runs it in an image to image
editor and drops the result in `_WATCH_FOLDER`. The daemon pushes it to `ANIMATOR_COLLABORATION`,
files it by its leading number, and rebuilds the site. Chat Claude looks at it, writes its note into
`catalog.json`, marks the previous one superseded, rebuilds and pushes. Baba never has to think about
a filename or a version.

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

## 6d. THE THREE THINGS THAT RUN ON THE MAC

| what | how | notes |
|---|---|---|
| **watch folder daemon** | `watch` for the menu, `watch-update` to update | its own repo, `WATCH_FOLDER_DAEMON`. **Claude Code does not touch it**, see EXCHANGE step 61 |
| **accessibility finger** | `1` sends the message in Claude, in Chrome | still Claude Code's, `com.mantra.brainbreak.finger` |
| **Claude Code** | in `~/Developer/brain_break` | talks to chat Claude through `EXCHANGE.md` in the manifest |

**The exchange protocol.** Chat Claude appends a numbered STEP to `MANTRA_MANIFEST/EXCHANGE.md` and
pushes. Baba pastes *pull the manifest and do step N*. Claude Code does it, appends its `### REPORT`
and pushes. Nothing is deleted from that file, so the whole history of instructions survives. The
standing rules live at the **top** of it and override every step below.

**Claude Code has been slow and dropping connections.** When it stalls, chat Claude does the work
directly and pushes, which is faster. Claude Code is for the things chat Claude cannot reach: the
77 GB of footage, DaVinci Resolve, and anything on the Mac.

---

## 7. HOW TO CLOSE A SESSION

Do all four. This is the part that was missing before.

1. Run the rebuild chain. Do not skip a step because it "did not change" — the timecodes moved.
2. Commit, push, and **verify each raw link returns 200 and matches the local build byte for byte.**
3. Update section 6 above: the frame count, the running time, the margin, what was done, what is
   open.
4. Update the file that owns whatever you touched. Images changed, `nanobanana.md`. Voice changed,
   `VOICES.md`. Animation changed, `ANIMATION.md`. Film state changed, `HANDOVER_V7.md`.
