# HANDOVER_V9.md

> **READ `TAKEOVER.md` FIRST.** It is the front door: reading order, the one source of truth, the
> rebuild chain and the rules that cost us something. This file is step 2. If anything here disagrees
> with the takeover, the takeover is newer and wins.

Written 28.8.2026. This replaces `HANDOVER_V7.md`, which was written on 16.8.2026 and had gone twelve
days stale while sitting second in the reading order. It described a 49 frame film with a factory in
it, a shoot that had not happened yet, and eight scenes. All three were wrong.

---

## WHERE THE FILM IS, 28.8.2026

**V9. Twelve phases. 60 panels in `frames_v4.json`, up from 50.** The two minute limit is unchanged
and is a hard rule: over two minutes on the YouTube clock and it is not judged.

**The shoot happened**, 18.8.2026 in Bengaluru with Venkatesh. Manan re-records around the 5th or 6th
of September, after picture lock. Baba wants the cut around the 10th, and **those two dates still
contradict each other.** Nobody has resolved it. Neha is waiting on the earlier one and the Hume
reference recordings were promised to arrive with his lines.

### The twelve phases

    1   THE RUNNER            LOCKED. Built, on the site, 17 key frames across 7 shots.
    2   HE TRIES IT HIMSELF   Manan on a real bicycle on a real road.
    3   RACING HIMSELF        On the trainer at home, racing a recording of himself.
    4   HE IS DONE            Nothing left.
    5   HE CLOSES HIS EYES    Stops, breathes. The way in.
    6   A DOOR OF LIGHT       Inside his head. The house of the body.
    7   HE WALKS INTO IT      White. He is inside the light.
    8   GANESHA               Rises out of the white, grows, is gone.
    9   COACH BRAIN           "What happened?"  "I pulled the brakes on you."
    10  THE OLD THEORY        Blackboard, white chalk, drawing itself as he speaks.
    11  THE NEW THEORY        Whiteboard, black marker. The inversion. Then the key.
    12  IT IS A SETTING       Fresh again, then the fourth wall.

**Only phase 1 is built.** Everything else is a placeholder on the site pulled from the old library.

### What was deleted

**The factory is gone.** Its door survives as the door of light. `V7_3_1_factory_empty` and the rest
of old scene 3 are out of the film. The tanks stay, as one room in the house of the body and as a
symbol in the glossary.

---

## THE LAWS, AND THERE ARE FIVE THAT DECIDE EVERYTHING

**1. Photograph what is true, draw what is thought.** Manan is a photograph. Everything imagined is
graphite on warm cream paper. Unchanged since V4 and still the foundation.

**2. The frame rate is the second language.** Nothing is smooth except one thing. 2 to 3 fps where he
is dying, 5 to 7 as the default, 8 to 10 once he runs, 25 for the muscle activation and nothing else.
The rate rises as the brake comes off and the audience feels it without being told. Never smooth
between tiers inside a shot.

**3. The muscle activation is a motif, not an effect.** The same four frames, copy pasted, three
times: the runner seeing the finish line, Manan on the bicycle, Coach Brain naming the limit. Built
once, used three times. Remake it for any of the three and the recognition dies.

**4. The audience asks why, then we answer.** Effect first, cause second, every cut. It is why the
face changes before we see the finish line, and why the rooms of the body come before Coach Brain
says the sensor list they are made of.

**5. Anything that moves on its own is a layer.** The panel border, the sweat, anything that drips or
travels. It ships as three files: plate, layer, composite. The artwork itself runs edge to edge and
the frame is a separate transparent matte.

---

## WHAT EXISTS NOW THAT DID NOT ON 16.8.2026

**The animator site is live and is the delivery surface.** `markoboskoauroville.github.io/ANIMATOR_COLLABORATION`.
The homepage is a brainstorming board: twelve phases, every picture we own under each. The breakdown
page holds the sheets, the frame, the rate scale, the glossary and the change log. Scene pages open
with the storyboard and then the shots. **The passphrase gate is currently OFF** at Baba's request and
goes back on with `GATED = True` in the builder.

**The runner has a face.** Until 28.8 the only description of him anywhere was nine generic words, so
every frame invented him again and he kept landing on a well known actor. `CHARACTER_SHEET_RUNNER_FACE-v2`
is the lock, and `CHARACTERS.md` carries the written spec. The three features that must never be
dropped from a prompt: the flattened bridge of the nose, the wide set deep eyes under a straight brow,
the narrow jaw under wide cheekbones.

**The house of the body**, `MEMORY.md` section 14. The rooms are Coach Brain's own sensor line and
each room's walls are built of the organ itself.

**Ganesha**, the homage to India, both as a murti on the console and as the appearance in the light.

**Working tools:** `tools/check_headroom.py`, `tools/artwork_index.py`, `tools/alpha_probe.py` in the
manifest, and in the animator repo `tools/build_site.py`, `print_pack.py`, `archive_scan.py`.

---

## HOW IMAGES ARE MADE NOW

`MANTRA_MANIFEST/modules/imgtoimg.md` is the governing document and it supersedes what
`nanobanana.md` says about tooling.

**The AI Image Editor is retired.** It re-drew the face however short the prompt was. Everything now
goes through **Image to Image AI with Nano Banana Pro**, two coins, with the character sheet attached
as a reference. Identity comes from a reference, never from wording.

**Scale and camera angle are inherited from the reference and cannot be asked for in words.** If a
frame needs a different framing, build the reference that carries it.

**Nano Banana letters well.** Dictate every word and where it goes. Gibberish only appears where text
was left unspecified.

**Baba's coin balance was 463.5 at the end of 28.8.2026.** Ledger in `MANTRA_MANIFEST/IMGTOIMG_LEDGER.md`.

---

## WHAT IS OPEN

- **The recording date against picture lock.** The only item with a third party and a deadline.
- **Phases 2 to 12 are not drawn.** Phases 6, 7, 8 and 11 have nothing close in the library.
- **Shot 1.3 has no airborne mid-stride.** Four attempts all came back with three legs; abandoned, and
  Kristijan can interpolate from the two good ends.
- **Manan's composite for shots 1.5 and 1.6.** The generated version still sits better in the paper
  than the real keyed footage. The gap is the cast shadow and the light direction, not the key.
- **`assets/pdf/` is 646 MB and `BRAIN_BRAKE/.git` is over 1.7 GB.** Removing files does not shrink
  it; only a history rewrite would, and that was deliberately not done.
- **EXCHANGE steps 62, 64 and 65** are written and waiting for Claude Code.
