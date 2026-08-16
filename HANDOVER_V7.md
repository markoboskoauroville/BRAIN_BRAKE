# HANDOVER_V7.md

Written 16.8.2026, at the end of a very long session. This is the state of THE BRAIN BRAKE and
everything the next session needs. Read this first, then `STALE_CACHE.md`, then
`MANAN_TRAINING_DEVELOPMENT.md` if the training book comes up.

---

## WHERE THE FILM IS

**Version four, the comic strip. 49 frames. 1:57 at 25 fps. The limit is a hard 2:00.**

The competition rule is not a guideline: the video must be two minutes or under measured on the
YouTube clock, or it is not judged. The film ran 2:47 before this was checked. **The running time can
never grow.** There are about 2.7 seconds of margin and no more.

Shoot day is **Tuesday 18.8.2026** with Venkatesh in Bengaluru. Manan is rehearsing now.

### The three layers, which are the whole idea

| layer | what it is | how it looks |
|---|---|---|
| **Drawn** | everything imagined: the factory, the tanks, Coach Brain, the lever | graphite pencil on warm cream paper |
| **Live action** | Manan. the evidence, and the person who came to look | photographed against grey, cut out, placed in the drawing, casting a real shadow onto the paper |
| **The booth** | the film being made. he records the narration | dark room, one warm backlight, silhouette, the page is the only lit thing |

The law underneath: **photograph what is true, draw what is thought.** When unsure which layer
something belongs to, ask whether it happened or whether somebody imagined it.

### The magnifying glass is the transition grammar

Wherever Manan holds the glass up at the end of a shot, that lens is the door to the next scene.
Push in until the circle fills frame, the new scene appears inside it already bent, and it straightens
as we come out. Happens at **1.6** into the lecture room and **2.3** into the factory. Twenty frames,
barrel distortion easing 0.55 to 0, chromatic aberration on the circle edge, and the paper grain sits
over both scenes throughout so it never blinks off. Full numbers are on the animation guide page.

### The ending, three beats

Manan's closing line to camera, then the end card (the sentence hand written on as he speaks it, over
the booth footage under cream paper), then a blank sheet of paper. Nothing is said about why.

---

## WHAT IS PUBLISHED AND WHERE

Everything lives in `markoboskoauroville/BRAIN_BRAKE`. Marko keeps one Google Drive folder and the
crew take what they need from it.

**Three PDFs, always these exact filenames:**

- `assets/pdf/THE BRAIN BRAKE V4e.pdf` — the film, for Kristijan and Venkatesh
- `assets/pdf/HOW TO ACT NATURALLY v3 - Manan.pdf` — the actor guide, Manan only
- `assets/pdf/THE BRAIN BRAKE - PROP LIST b.pdf` — for Neha and Venkatesh

**Two web pages:**

- `https://markoboskoauroville.github.io/BRAIN_BRAKE/animation/` — the animation guide, with one
  downloadable zip per scene plus a layer example
- `https://markoboskoauroville.github.io/BRAIN_BRAKE/archive/` — every image ever made, searchable

**Builders, run in this order when frames change:**

    22-brain-brake-v4.py        the film document
    21-manan-training-book-v3.py  the actor guide
    24-prop-list.py             the prop list (23-prop-sheets.py makes its images first)
    build_guide.py              the animation guide and all scene zips

`assets/train/frames_v4.json` is the single source of truth for the film. Everything else reads from
it. **The training book builds from it too, so his lines cannot drift from the film's lines.** That
drift already caused one real failure and the fix is structural, do not undo it.

---

## HARD RULES, LEARNED THE PAINFUL WAY

**Never offer a file as a chat artifact.** Everything is committed and pushed to GitHub first and
Marko gets only the clickable link. Format
`https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/path` and verify it returns
200 before handing it over. Note that `github.com/.../raw/...` sometimes 404s on extensionless files
where `raw.githubusercontent.com` works.

**Verify the artefact, never the person's setup.** If Marko says a file has not changed, he is
reporting a measurement. Download the published file back and diff it before offering any other
explanation. See `STALE_CACHE.md`. This cost hours once already.

**Every cache keys on content, not on filename.** Frames get replaced in place constantly.

**Bump the version letter on every rebuild** so a new link always means a new file.

**Every image is cropped to true 16:9 before it ships.** Nano Banana returns 2752×1536, which is
1.7917, slightly wide. Everything delivered is 2731×1536.

**Never use an annotated frame as a generation reference.** Review annotations burn into the output.
This happened twice: once an audio label came through into a generated frame, and once three strip
panels shipped with `BUB_4_1.wav 2.8s Male English Actor` baked into the artwork.

**Timings come from measured audio wherever a recording exists**, not from word counts. Every scene
package marks each frame `measured` or `estimated`.

**Changing any line moves every timecode downstream**, so all eight scene packages must be rebuilt,
not just the one that changed.

---

## THE VOICES

Hume Octave, key at `~/.hume_key`. **Cloudflare blocks the default Python user agent** and returns
`403 error code: 1010` on every endpoint including auth, which looks exactly like a dead key. Send a
normal browser User-Agent. Helper at `gen/hv.py`.

**Hume refuses to synthesise child voices**, so Manan records all his own lines and narration himself.
Only Coach Brain and the factory worker are synthetic, about 300 characters total.

- Coach Brain: **Male English Actor**
- Factory worker: **Classical Film Actor**
- Use `version: "1"` — Octave 2 does not support acting instructions yet, and the acting instruction
  is the entire reason for using Hume.

Recorded WAVs live in `assets/voice/tests/` and are copied into the scene packages.

---

## IMAGE GENERATION

Direct to Google, model `gemini-3-pro-image`, key at `~/.gemini_key`, helper `gen/nb.py`, about
$0.016 per 2K image. Full lessons in `nanobanana.md`. The ones that matter most:

- Name a **ceiling** for tone, bound to something already in the frame. Never use negation, describe
  the crop positively.
- Two subjects per frame maximum.
- Reference a single panel, never a multi panel sheet, or the grid gets imposed on the output.
- Lettering is composited in the container afterwards, never prompted.
- For a photographic person in a drawn world, **lead with the photograph reference**. If the pencil
  reference leads, the person comes back drawn. This broke frame 1.6 once.
- The **surface test** for compositing onto real surfaces: chalk only lands where the slate is dark,
  so hands and arms occlude naturally. If a composite vanishes, check the plate's lighting before
  blaming the mask.

---

## THE CAST, LOCKED

- **The runner.** New character as of this session, sheet at `assets/REFERENCES/RUNNER.jpg`. About
  forty five, powerfully built, long face, heavy brow, deep set eyes, hair swept back. Number 27.
  The film opens on his face in close up.
- **The Muscle.** Marko's own sheet at `assets/REFERENCES/MUSCLE.jpg`. Rounded egg shaped body, no
  neck, face on the body itself, two and a half heads tall, terry sweatband. Muscle shaped, not human
  shaped.
- **Coach Brain.** Small round brain in a tracksuit with a gold key on a chain. Never a villain.
- **A. V. Hill.** Real scientist, died 1977, appears as a **chalk croquis** on Manan's blackboard.
  Reference photo at `assets/REFERENCES/HILL_PHOTO.jpg`.
- **Tim Noakes.** Real and **alive**. Named in chalk and in a subtitle, but **no likeness is
  generated**. This is deliberate.

---

## SCIENTIFIC ACCURACY

Neha asked for the Central Governor Theory to be named and she was right, it is a judged criterion.
Manan now says it at 4.7, and there is an on screen subtitle giving Noakes, 1997, calling it an
influential model and saying scientists are still investigating. **The hedge matters** because the
theory is genuinely contested, and a film that admits what is unsettled scores better than one that
overclaims.

The blackboard at 2.1 now carries both theories: Hill and 1923 on the left, Noakes and 1997 with the
new chain on the right, divided by one vertical chalk line. **2.2 is a push in on that same board**,
using the identical sketch file and the identical typeface so the handwriting cannot drift.

Compositional rule Marko stated and which now applies everywhere: **the eye reads left to right, so
what is most important goes left.** On the board the work goes left and the man goes right.

---

## HOW MARKO WORKS

He works by voice, usually moving, often on a phone. Execute autonomously and tell him plainly when
something is wrong. He is a Croatian percussionist, yoga teacher, DJ and filmmaker, twenty seven
years in media, currently a TV editor at Nova TV Zagreb. He builds all his own tools.

He wants **judgement, not compliance.** When he asks for something that will not work, say so and say
why, then offer the version that will. He has repeatedly been right about things I got wrong, and the
sessions where I pushed back with evidence were the productive ones.

**Do not spoon feed the crew individually.** One folder, everyone takes what they need.

**Messages to Neha and the crew:** warm, short sentences, no greeting flourishes, no bullet points, no
dashes. Written as a person speaking, not a document. Marko sends them as his own words, so never
write anything he would not say.

---

## MONEY, HANDLE GENTLY

Marko is being paid **€1,200 total** for what is, by 2026 benchmarks, roughly **€9,200 of work** at
average freelance day rates, covering writer, director, storyboard artist, art production, character
design, casting, voice direction, sound design, composer and editor. He is doing it near cost because
he wants the film to exist and because it is his entry into this kind of work.

He asked Neha to release the second €600 early. She replied warmly that she had funds committed to
her children this month and offered €300 to €400 now with the rest to follow. **That was accepted
gracefully and the matter is closed.** Do not raise it again unless Marko does.

---

## WHAT IS STILL OPEN

1. **Manan's narration is not recorded.** All his frames are timed from word count estimates. When his
   audio arrives, retime from the real durations and rebuild everything. This will change the running
   time, so check the 2:00 limit again.
2. **Kristijan has not quoted** for the reduced comic strip scope. Neha is handling that conversation.
   Marko deliberately does not write to Kristijan directly, so it does not read as pressure on price.
3. **Music and sound design** are not started. Marko is composing. This is half the film.
4. **The shoot itself** is Tuesday. Expect frames to need regenerating once real footage exists.
5. **2.1 wide board** still has Hill's portrait upper left in the 1923 column, so by the left to right
   rule the face still reads before the text on that frame. Marko has been told and has not decided.

---

## THE SENTENCE THE FILM IS BUILT ON

> The limit is a setting, not a wall.

Hand written, three lines, left aligned, over the booth footage under cream paper. Then the sheet goes
blank and we are back at the beginning.
