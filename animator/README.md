# ANIMATOR

**The working folder between Marko and Kristijan. Final phase of production.**

Opened 19.8.2026 after their meeting. Everything made from here on for the animation goes in this
folder and nowhere else, so there is one place to look and one history to read.

---

## WHAT THIS IS FOR

Scene by scene, the two of them decide what the animation needs. Some frames get **variations**, a
different pose or a different framing of the same moment. Some scenes need **extra frames** that are
not in the film yet, because a cut that reads on paper needs a step in between once it moves.

This folder holds all of it, and `CHANGES.md` records every decision so neither of them has to
remember.

---

## THE SHAPE

```
animator/
  README.md          this file
  CHANGES.md         the log. every image, why it exists, what it replaces
  scene_01/
  scene_02/          made as each scene is worked on
  ...
```

Inside a scene folder, one file per image:

```
1-3_v2_wider.jpg           a variation of an existing frame
1-3a_new_glance.jpg        an extra frame that is not in the film yet
1-3_v2_wider_BG.jpg        its background plate, where one exists
1-3_v2_wider_FG.png        its foreground, transparent, solid body
```

**Naming.** Frame number with a hyphen, as in the layer packages. `_v2` and up for a variation of an
existing frame. A **letter** for a new frame between two existing ones, `1-3a` sits between 1.3 and
1.4, so nothing has to be renumbered and `frames_v4.json` stays the source of truth until a change is
accepted into the film.

---

## THE RULES THAT ALREADY EXIST AND STILL APPLY

- **2731 x 1536**, true 16:9. Nano Banana returns 2752 wide and it gets cropped.
- **Never crop an overlay.** A picture over another picture is scaled and moved, never cut.
  `nanobanana.md` item 9.
- **Characters come from `CHARACTERS.md`**, from their locked single figure reference, with the
  costume line pasted in. Never from the frame they appear in, never from a four view sheet.
- **Key light is camera RIGHT.**
- **Describe what remains, never what should be gone.** Naming a thing summons it.
- **Look at every image before it ships.** The tool returning OK means the API answered, nothing
  more.

---

## HOW A CHANGE BECOMES PART OF THE FILM

Nothing in this folder is in the film. It is a proposal until Marko says otherwise.

When a variation or a new frame is accepted, it goes into `assets/V7/`, `frames_v4.json` is updated,
and the slides, the read through and the scene packages are rebuilt from it. **Only then** does it
exist as far as the rest of the production is concerned.

`CHANGES.md` records that moment too, so the log says not only what was made but what was taken.
