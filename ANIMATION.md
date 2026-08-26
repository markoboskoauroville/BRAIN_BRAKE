# ANIMATION

Everything about the animator's site and the layered scene packages. Read `TAKEOVER.md` first.

The animator is **Kristijan Kaurić**, in Zagreb. He works in Croatian. He comes onto a finished cut
and receives instructions frame by frame. What goes into animation and why is Marko's decision.
How it looks is Kristijan's.

---

## THE SITE

Live at **https://markoboskoauroville.github.io/BRAIN_BRAKE/animation/**

Source is `animation/index.html`. A single self-contained page, no build step, no framework, near
black header on the project's cream and gold palette. It carries the look of the film, the layer
philosophy, the working rules, and one download card per scene.

**The page itself holds no timecodes and no dialogue.** That is deliberate. Everything that can go
stale lives in the packages, so the page cannot quietly contradict the film. The only two numbers
on it are the running time and the margin, and `27-scene-packages.py` rewrites both on every build.

`animation/img/` holds the page's own illustrations. `animation/downloads/` holds the zips.

---

## THE PACKAGES

One zip per scene, eight scenes, plus a layer example that is not a scene.

```
SCENE_04_THE_GATEKEEPER.zip
└── SCENE_04_THE_GATEKEEPER/
    ├── FRAMES/    every frame of the scene at full size, named SCENE_04_THE_GATEKEEPER_4_4b.jpg
    ├── AUDIO/     the recorded takes that belong to this scene, at 48 kHz mono
    ├── SCENE_04_THE_GATEKEEPER_TIMECODE.csv
    └── SCENE_04_THE_GATEKEEPER_INFO.txt
```

**TIMECODE.csv** has one row per frame: `frame, layer, in, out, frames, timing, mode, who, line,
note`. The `timing` column is the important one. `measured` means the frame is cut to a real
recording and will not move. `estimated` means it is timed from a word count and **will** move once
Manan is recorded.

**INFO.txt** is the same thing for a human: the scene's in and out, then each frame with its
duration, its line, and any transition note.

Frame ids use a dot in the film and an underscore in filenames. `4.4b` becomes `4_4b`.

---

## REBUILDING

```
python3 27-scene-packages.py
```

That is the whole job. It reads `assets/train/frames_v4.json`, writes all eight zips, pulls the
matching audio out of `assets/voice/final/`, and rewrites the download cards on the site so the
frame counts, durations and file sizes always match the files behind them.

**Never build a package by hand.** They were built by hand once, in a chat working directory, and
when the film changed they went stale without a word. Scene 8 was still shipping a frame called
8.5 with a line that had been cut, at a timecode that no longer existed. If Kristijan had started
from that, he would have animated to the wrong clock.

Three things the script knows that you would otherwise have to rediscover:

- **The `AUD` map is the authority** on which recording belongs to which frame. If it and
  `assets/voice/final/` ever disagree, the map is right and something has been moved.
- **Missing plates are not an error.** A frame with no image is one that gets shot on the day. It
  still appears in the CSV and INFO so the timing is complete, and the script prints which ones.
  Right now that is `4.4b` and `4.8`.
- **Scene folder names are linked from the site.** Do not rename one without rewriting
  `index.html` in the same commit.

---

## WHAT MOVES WHEN THE FILM MOVES

A single added frame shifts every timecode after it. When Neha's three lines went in at 4.4b, 4.8
and the 8.6 to 8.8 triplet, scenes 5, 6, 7 and 8 all moved even though nothing in them changed.
So the packages are rebuilt as a set, always, never one scene at a time.

The big one is still ahead. **Forty-four of fifty frames are estimated.** When Manan's narration is
recorded, most of the film retimes at once and every package changes. Kristijan should be told
plainly that current timings are provisional, which is why the `estimated` flag is in the CSV
rather than buried in a note.

---

## SCENE 7 IS NOW WORDLESS

Worth knowing before it looks like a bug. Scene 7's only spoken frame, 7.6, was cut to make room
for Neha's lines. Its three silent panels stayed, so scene 7 is a 1.2 second wordless breath
between the release and the invitation. The folder is still called `THE_VERDICT`, which no longer
describes it, but renaming would break the site links for a scene that may yet change again. Rename
it when the film is locked, not before.
