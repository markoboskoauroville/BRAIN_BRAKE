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

**Finding one, 11.8.2026, and it is about the platform rather than the model. Reference files must be
light.** The first editor run returned **Generation failed, credits returned**, on a 5.9 MB PNG input.
Nano Banana had failed the same way twice in the half hour before, on a 1.21 MB reference. A previous
E-Pro job on 4.8. had succeeded. Two different engines, same failure, same window: the input, not the
words and not the model.

Every reference that has ever worked here is under about half a megabyte. **Serve a `_web` copy of
everything, longest edge 1600, JPEG quality 85, under 400 KB.** PNG is the worst offender because a
pencil drawing full of grain does not compress, and a 16 by 9 PNG at 2752 wide runs to six megabytes.
The collage was rebuilt as `4A_editor_input_collage_web.jpg` at 0.34 MB.

**Finding two, 11.8.2026. The editor passed four of five and failed the one that matters, and that
failure defines exactly what it is for.**

    A  MERGE      PASS, and better than expected. Two views of one room became one continuous
                  space with a real corner, the ceiling line and floorboards running through,
                  no seam anywhere.
    B  POSE       PASS. A standing figure was seated on a chair, turned to the desk, head down,
                  pen in hand, legs behind the desk. A full pose change, done cleanly.
    D  STYLE      PASS. The pasted figure is now made of the same pencil as the room. No seam
                  of hand, no difference in line weight.
    C  LIGHT      PARTIAL. Soft shading appeared under the desk, but no clear directional cast
                  shadow of the man. Ask for shadows more specifically, or add them here.
    G  FIDELITY   FAIL. It redrew the entire picture. The oil lamp vanished. The cup vanished.
                  The desk became a different desk, the papers rearranged, the wall plates moved
                  and multiplied, the chairs changed.

**So it is not an editor. It is a re-compositor.** It takes an arrangement and rebuilds it as one
coherent drawing, which is exactly the job Nano Banana cannot do, and it does it beautifully. What it
will not do is leave a thing alone. "Leave everything else exactly as it is" was in the prompt and was
ignored completely.

### THE OPERATIONAL RULE THAT FOLLOWS, AND IT IS ABSOLUTE

**Never point the editor at an approved frame.** Anything already locked, anything already in
`assets/V4/`, anything that took six runs to get right, is not to be sent to this tool for a small fix,
because there are no small fixes. It rebuilds. Small objects are the first casualties, and a lamp is a
light source and a continuity item, not decoration.

**And once a frame is locked, it becomes the reference for the rest of its scene.** `4B` and `4C` are
built from the approved `4A`, not from `LAB.jpg`, because the room in the approved frame is now the room.

---

## 5. THE TOOLBOX, DECIDED

    NANO BANANA     Makes what does not exist yet. Model sheets, characters, rooms,
                    objects, anatomy, texture, the first version of any world.
                    Slow, expensive, the master draughtsman. Cannot arrange.

    THE EDITOR      Merges, poses, stages and unifies. Turns a rough hand built
                    collage into one drawing. Cheap, fast, obedient about change
                    and careless about everything it was not asked about.
                    Use it to build. Never to touch.

    THE CONTAINER   Decides. Position, scale, rotation, crop, which part of which
                    sheet goes where. Costs nothing, is exact, and is the only one
                    of the three that does what it is told.

**The working order for a frame from now on.** Sheets from Nano Banana, arrangement in the container,
unification in the editor, lock. That is three cheap steps instead of six expensive guesses, and it is
how `4A` was made after `3C` took eleven. First run is `4A`, testing A, B, C, D and G at once, on the collage at
`assets/V4/attempts/4A_editor_input_collage.png`, built from `LAB.jpg` view one and view three with the
figure from `SCIENTIST.jpg` pasted in at rough scale.

Testing five at once is deliberate and is not the bisect protocol. This first run is asking whether the
tool is worth anything at all. Once it is, the tests go one at a time.

E-Pro at 1.5 credits rather than E-Turbo at 1, because the first reading of a tool should be of its best
version. If E-Pro cannot do a thing, E-Turbo will not.

---

## 6. FINDING THREE, AND IT CORRECTS FINDING TWO. FIDELITY DEPENDS ON THE INPUT, NOT THE TOOL

11.8.2026. The second editor run on `4A` added a lit oil lamp, a cup and saucer, the warm light around
the flame and a soft vignette into the corners, and **changed nothing else**. The wall plates are in the
same places, the bookshelf, the door, the window, the chairs, the papers on the floor, all identical.
That is a surgical edit, and it is the opposite of what the first run did.

**The difference is not the prompt. It is what the tool was given.**

    incoherent input     a collage with a seam and a pasted figure
                         it rebuilds the whole picture from scratch

    coherent input       a finished single drawing
                         it changes what it was asked to change and leaves the rest

Which makes sense. Given something that does not hold together, the only way to make it hold together is
to redraw it. Given something that already does, there is nothing to reconcile.

**So the rule from section 4 is narrowed, not withdrawn.** The danger was never the tool, it was sending
it a mess and expecting precision. In practice:

    first pass on a collage      expect a full rebuild. Do not include anything
                                 precious that is not also in a reference.
    later passes on the result   safe, surgical, cheap. Use freely.

**And there is a distinction that matters more than it sounds.** Do not send an approved frame to be
**fixed in place**, because the approved file must never change. Do send an approved frame to have a
**new frame derived from it**, saved under a new name. That is how `4B` and `4C` are made: the room is
already right, the man is already right, and only his pose and the light change. It is also how the
whole film gets its continuity, because every frame in a scene is then literally the same drawing.

