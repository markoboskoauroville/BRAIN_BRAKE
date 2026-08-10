# editor.md

**The second tool. AI Image Editor on ImgToImg, models E-Turbo and E-Pro.**

Opened 10.8.2026. `nanobanana.md` covers the generator. This file covers the editor, and the two are
different machines that want different language. Everything learned about the editor goes here, whether
it worked or not, because a negative result costs a credit and is worth keeping.

---

## 1. WHAT IT IS AND WHY IT MATTERS

Nano Banana composes badly. That is the finding this whole production has paid for: it varies objects
brilliantly and cannot organise a field. Every framing win on scene 3 came from **building the
arrangement by hand and feeding it back**, which worked every time it was tried.

The editor is that same move with a machine doing the blending instead of a paste. If it can take a
rough hand built collage and make it one coherent drawing, then the division of labour for the rest of
the film is settled:

    Nano Banana      makes things.     Model sheets, characters, rooms, objects, textures.
    The editor       arranges things.  Position, scale, pose, merging, shadow, cleanup.
    The container    decides things.   Where everything actually goes, at no credit cost.

**One reference image only.** So every input is a single canvas built here first, a collage, a split
screen, or a rough composite with the pieces already roughly in place.

---

## 2. CREATION LANGUAGE VERSUS EDITING LANGUAGE

Nano Banana is told **what exists**. The editor is told **what to change**. Writing generator prose at
an editor wastes the thing that makes it useful, which is that it can already see the answer and only
has to move it.

    generator     A small untidy study of nineteen twenty three, a man at a desk...
    editor        Seat this man on the chair. Remove the seam on the right.

Editing verbs to reach for: move, seat, turn, rotate, scale, remove, erase, extend, merge, blend,
straighten, lighten, darken, add a shadow, match the style, join the two halves.

---

## 3. THE TEST PLAN

Each run tests one capability and the answer gets written under section 4 whether it passes or fails.

    A   MERGE        can it join two views of one room into one continuous space
    B   POSE         can it seat a standing figure, or turn a head
    C   LIGHT        can it add a correct cast shadow that was not in the input
    D   STYLE        can it unify a pasted element into the surrounding hand
    E   GEOMETRY     can it rotate or re-angle an object in three dimensions
    F   REMOVAL      can it delete an element and repair what was behind it
    G   FIDELITY     does it preserve the parts it was not asked to touch

**G is the one that decides everything.** An editor that quietly redraws the whole picture is a
generator with extra steps and is no use for continuity. If G fails, the tool is only good for throwaway
guides. If G passes, it becomes the main tool for the rest of the film.

---

## 4. WHAT WE KNOW

Nothing yet. First run is `4A`, testing A, B, C, D and G at once, on the collage at
`assets/V4/attempts/4A_editor_input_collage.png`, built from `LAB.jpg` view one and view three with the
figure from `SCIENTIST.jpg` pasted in at rough scale.

Testing five at once is deliberate and is not the bisect protocol. This first run is asking whether the
tool is worth anything at all. Once it is, the tests go one at a time.

E-Pro at 1.5 credits rather than E-Turbo at 1, because the first reading of a tool should be of its best
version. If E-Pro cannot do a thing, E-Turbo will not.
