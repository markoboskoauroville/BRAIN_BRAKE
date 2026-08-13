# nanobanana.md

**How to control Nano Banana Pro and get the frame on the first or second run.**

Every rule here was paid for with credits. Read the whole thing before writing a prompt. If you
learn something new, add it at the bottom under NEW FINDINGS with the date, and move it up into the
rules once it has held twice.

---

## 1. THE TOOL

Marko uses **ImgToImg.ai**, engine **Nano Banana Pro**.

| Mode | When |
|---|---|
| **Image To Image AI** | The main one. Upload a reference plus prompt. Anything with a recurring character or location. |
| **AI Image Generator** | Only when nothing recurring is in the frame and no reference exists. |
| **AI Image Editor** | Local fixes to a frame that is otherwise right. |
| AI Video Generator | Not used for the film. |

Per generation the site exposes: Model, Image Upload or Image URL, Prompt, Aspect Ratio, Outputs,
Watermark. Recent tasks are re-editable and regenerable — **always re-edit an existing task rather
than starting a fresh one**, because the reference stays attached and one variable changes.

**Film frames are always 16:9.** Character sheets are 3:2.

Always state in the instruction to Marko: **which mode**, **which reference to upload**, **aspect
ratio**. A prompt without those three is an incomplete instruction and costs a wasted run.

---

## 2. THE FOUR RULES, EACH LEARNED FROM A FAILURE

**1. Scene first, style second.**
A long style preamble pushes the content out and the model builds the wrong picture entirely. Open
with the room, the person, the action. Put the medium sentence after the scene is fully described.

**2. Never name text you do not want.**
Writing "no captions, no panel numbers, no watermark" put those exact things into the picture. The
model has no reliable negation. Either say nothing about text, or give a tight **whitelist** of the
only words permitted, e.g. *"the only lettering anywhere is the number 27 stencilled on the crates"*.

**3. Describe, never instruct.**
Write what the image *contains*, not what the generator should *do*. Instructions get drawn as text
in the frame. Never write "make sure", "focus on", "the goal is", "render", "use". Write nouns and
verbs of the world.

**4. The mixed media rule.**
Manan is a photograph, everything else is a pencil drawing. This exact wording works and weaker
phrasing fails every time:

> *"a real fourteen year old Indian boy, and he alone is a genuine photograph composited into this
> pencil drawing. Warm brown skin with visible texture, short black hair, natural light on his face,
> real woven wool in his clothes."*

"Warm colour with soft realistic shading" produced a cartoon boy on every attempt. The words that do
the work are **genuine photograph**, **visible texture**, **real woven wool**.

---

## 3. REFERENCE SHEET DISCIPLINE

**The sheet decides the style, more strongly than the prompt does.** This was the single biggest
discovery of the project. Manan kept rendering as a cartoon until the reference sheet itself was
regenerated photorealistic. After that he came out photoreal *even in prompts that never said so*.

Consequences:

- **Fix the sheet, not the frame.** If a character is wrong in three frames, the sheet is wrong.
  Regenerating one sheet is one credit; regenerating three frames is three and they will drift again.
- **Never upload a drawn sheet alongside Manan.** Its style bleeds onto him and he goes cartoon.
  If a frame needs both him and a drawn character, upload only his sheet and describe the other in
  words.
- **Overwrite sheets at the same filename and URL.** Every prompt already written stays valid. Never
  version a sheet into a new name.
- **When a face drifts, generate one view per run.** Four views in one run makes the model invent the
  unseen sides. Slower, but the face holds. Same crop uploaded each time, one view asked for.
- The Manan sheet doubles as **Venkatesh's lighting and wardrobe reference** — grey seamless backdrop,
  the exact light he must match. That is deliberate, do not restyle it.

Current sheets live in `assets/REFERENCES/`: `MANAN.jpg` (the important one, photoreal),
`BRAIN.jpg`, `BRAIN_ROOM.jpg`, `RUNNER.jpg`, `MUSCLE.jpg`, `WORKERS.jpg`, `TANKS.jpg`.

---

## 4. FAILURE MODES SEEN, AND THE FIX

Read this table before blaming the prompt.

| What came back | Why | Fix |
|---|---|---|
| Boy rendered as a cartoon | Style bled from a drawn reference, or the photoreal block came too late | Photoreal block **first**, upload only his sheet |
| **Boy missing from the frame entirely** | Scene too dense. Machinery, workers, crates and a stamp all competed and the single small photographic figure was dropped | Give him the foreground and real estate. Describe him **before** the machinery. Or generate the plate empty and composite him in post |
| Unwanted captions, numbers, panel labels | They were named in a negative | Say nothing, or whitelist |
| A symbol floating with nothing holding it (the gold key hanging in mid air on a wall) | A symbol was named without being physically placed | Always give a symbol a **support**: on a chain round his neck, lying in the gutter, hanging from a nail |
| Characters at the wrong scale, two heads tall | The model sheet was cartoon-proportioned | Redraw the sheet from the hero frame that is right, not the reverse |
| Location drifts between shots of the same room | No empty location sheet exists, only heroes with characters in them | Make an **empty location sheet** before breaking a scene into shots |
| An object different in every frame | It has no sheet. The dial appeared in eight shots with a different face each time | One sheet per recurring object, with its states drawn on it |
| Text on a board unreadable or invented | Long chalked sentences | Keep board text to **four short words maximum**, in a whitelist |
| An instrument aimed at nothing, raised for the camera | A hand was holding it. Arm pose is a property of the figure, aim is a relationship between two objects, and the property wins | **Remove the hand.** Let the instrument lie on the thing it is examining and let a fragment of the character enter at the frame edge |
| A lens, glass or window comes back empty | Its contents were named after the object instead of as the subject | Give the interior as many words as the surface around it |
| The exact thing you forbade appears in the picture | You named it. The model renders nouns and ignores the word in front of them | **Never write a negation.** Describe the crop positively until there is no room for the unwanted thing |
| One of four described elements silently missing, a different one each run | The frame is over its budget of about two subjects | Build the frame in passes, drawn world first, photographic objects second, image to image |
| Generation failed, credits returned, nothing comes back | A refusal or a service error, not a craft problem | Bisect. Strip to the safest version, then add one suspect group per run. See section 4d |

---

## 5. THE PROMPT SKELETON

Write in this order, always. Plain sentences, no bullet points, no headings inside the prompt.

```
[1] THE PHOTOREAL SUBJECT, if any. Who he is, that he alone is a genuine
    photograph, skin texture, hair, light on his face, real fabric.
    What he is doing and where he stands in the frame.

[2] THE ROOM. What it is, what is in it, what the light is doing.

[3] THE OTHER FIGURES. Who, how many, what they are doing, their scale.

[4] THE OBJECTS THAT CARRY MEANING. Each one physically placed on
    something.

[5] THE FEELING. One sentence. "This is a discovery, not a warning."

[6] THE MEDIUM. Graphite pencil on warm cream paper, loose hand drawn
    lines, soft shading, sixteen by nine, thin dark border.

[7] THE FRAMING. Wide shot, low camera, the boy small in the lower third.

[8] THE WHITELIST, only if lettering is wanted. "The only lettering
    anywhere is the number 27 on the crates."
```

Block [1] goes first even though it feels backwards. It is the thing most likely to be lost.

---

## 6. THE CREDIT-SAVING PROTOCOL

The order of work matters more than the wording.

1. **Sheets before frames.** Every recurring character, location and object gets a sheet first. A
   sheet is one credit and saves five.
2. **One variable per run.** Change the light *or* the pose *or* the lens, never two. When two change
   and it gets worse you have learned nothing.
3. **Re-edit the task, do not start a new one.** The reference stays attached and the result stays
   in the same family.
4. **Two runs then stop.** If a frame is wrong twice, the prompt is not the problem — a sheet is
   missing or the scene is too dense. Diagnose, do not re-roll. Re-rolling the same prompt hoping for
   luck is how credits die.
5. **Accept the near miss and fix it in the editor.** A frame that is right except for one object is
   an AI Image Editor job, not a regeneration.
6. **Generate the hardest frame of a scene first.** If the establishing shot works, the rest of the
   scene inherits it as a reference.

---

## 7. THE STYLE LAW OF THIS FILM

Non-negotiable, and every prompt must satisfy it:

- Graphite pencil on warm cream paper, loose hand drawn lines, soft shading.
- 16:9, thin dark border.
- Humans are **realistic**, drawn as adults with adult proportions.
- Cartoon is permitted **only** for Coach Brain and the Muscle.
- **Manan is always photographic**, never drawn.
- Palette: graphite, cream, gold, red. Nothing else.
- **Red appears only on the needle**, and the needle never enters the red.

---

## 8. WHAT TO SEND BACK, SO THE NEXT PROMPT IS BETTER

When a generation is wrong, send the image **and** one line saying what is wrong with it. Not "bad",
but "he is a cartoon" or "the key is floating" or "the boy is missing". The failure mode names in
section 4 are the vocabulary. With the image plus one line the fix is usually a single sentence
moved, not a rewrite.

Also say **which mode and which reference** was used. Half the failures are the wrong sheet uploaded,
and that is invisible from the picture alone.

---

## 9. NEW FINDINGS

Append here. Date, what happened, what it means.

**9.8.2026 — the dense frame drops the photograph.** `HERO_V3_2` came back beautiful and complete —
gears, conveyor, crates stencilled 27, two workers, the cracked stamp — and with **no Manan in it at
all**, although the prompt placed him walking through with the glass. Reading it back, he was
described after the machinery and given no space in the composition. Lesson: the photoreal figure is
the first thing the model discards when the scene is crowded. Put him in block [1], give him the
foreground, and keep the drawn population under four figures.

**9.8.2026 — a named symbol without a support floats.** In the same frame the gold key is hanging in
mid air against a wall, attached to nothing. It was named in the prompt as a thread but never
physically placed. Lesson: a symbol always needs a noun to sit on.

**9.8.2026 — a busy style anchor does NOT bleed its content.** Frame 1A was generated with the
runner model sheet plus `HERO_V3_1` as a style anchor, and that anchor is full of things not wanted
in the new frame: a crowd, crash barriers, a kerb, a road, Manan and the gold key. **None of it
appeared.** The paper came back completely empty. This answers a question we had never tested and it
changes the economics: a finished frame can be used as a style reference without dragging its scene
along, so from now on always anchor to the best-drawn existing frame rather than fearing the bleed.
What transferred was exactly what was wanted, the line weight, the paper, the border and the hand.

**9.8.2026 — the style anchor beats the prompt on paper tone.** The prompt asked three times for
paper "close to pure white, with only the faintest warmth left in it". It came back at the standard
warm cream of the anchor. Lesson: tone, palette and line weight are decided by the reference, and
writing against the reference does not win. If a frame needs a different paper tone, either use an
anchor that already has that tone, or accept the anchor's tone and do the shift in the grade.

**9.8.2026 — camera angle instructions are weak.** The prompt said "seen from very low down, looking
up at him so he towers and fills the frame from below", stated twice. The result is close to eye
level with the figure occupying the middle third. Composition and camera height are the least
reliable things to ask for in words. If a specific angle matters, it has to come from a reference
that already has it, or be accepted as whatever the model gives and chosen from several outputs.

**9.8.2026 — a repeated figure reads as one man through line weight, not through overlap.** `V4_2A`
asked for four versions of the runner overlapping along one path. They came back cleanly separated
with almost no overlap, and it works anyway: the model carried the reading entirely in **progressive
line weight**, ghost grey at the left to firm dark graphite at the right. Lesson: when a figure has to
repeat across one frame, ask for the fade and let the spacing go. Overlap is a composition request and
composition is the weakest thing to ask for; density of line is a content request and lands every time.

**9.8.2026 — the labelled model sheet did not bleed its labels.** `RUNNER.jpg` carries hand lettered
view captions and a title, and was uploaded alongside two finished frames for `V4_2A`. None of that
lettering appeared. Together with the busy style anchor finding, this closes the question: references
transfer the **hand**, not the furniture. Stop hesitating over what else is in a reference.

**9.8.2026 — four figures of the same man held one face.** No ageing drift across four repetitions in
a single frame, with `V4_1C` as the anchor. Confirms the rule that the anchor should be the last frame
that was RIGHT rather than the most recent, and that it holds even when the model must draw the face
four times in one run.

**9.8.2026 — a hanging drop and a climbing drop are drawn the same way unless the skin tells you.**
`2B` attempt two came back beautiful and physically ambiguous: one large drop on the jaw with a wet
trail above it. Nothing in the picture says which way it is travelling, so the eye defaults to falling,
because that is what water does. Lesson: direction of motion cannot live in the shape of the moving
object. It has to live in **what the object has done to the surface behind it**. Dry skin on one side,
wet on the other, or a thread of water still connecting it to where it came from.

**9.8.2026 — the photoreal figure fails on SIZE and COUNT, not only on co-references.** `2C` attempt
one was run with `MANAN.jpg` as the only reference, exactly as the sheet discipline demands, and he
still came back as a soft grey render rather than a photograph, nine times over. So the rule needs
widening. A drawn co-reference is one way to lose him. The other two are asking for him **small** and
asking for him **many times**, because each repetition is another chance for the model to fall back on
drawing. Fix: at most three legible copies, each large in the frame, and let any further multiplication
be suggested by shapes too small to read.

**9.8.2026 — a repeated object at one scale becomes wallpaper.** Nine drops of nearly equal size laid
across the frame read as a decorative pattern rather than as a surface with things on it, and the
graphite ground stopped reading as skin entirely. Lesson: when something repeats, it must repeat at
**different distances**, with a few near and large and the rest receding, or the frame flattens into
ornament. Keep one piece of anatomy in shot, a jaw edge or a stubble line, so the eye knows what the
things are sitting on.

**9.8.2026 — the photoreal boy cannot live INSIDE a drawn object, and trying makes the whole frame a
photograph.** `2C` attempt two asked for Manan photoreal inside droplets sitting on drawn skin. The
model resolved the contradiction the only way it could: it photographed everything. Full colour skin,
brown flesh tones, glossy three dimensional spheres, the style law gone. This is the exact inverse of
the earlier failure where he was dropped from a crowded frame, and together they define the boundary.

**The rule, now settled.** Manan renders photographic when he is **a separate body standing in the
drawn world**, at a size where he reads as a person. He cannot be embedded inside a drawn object, and
he cannot be small, and he cannot be repeated. Two runs confirmed it from opposite directions. Stop
attempting it.

**9.8.2026 — the model cannot vary a small repeated element.** The hundred receding droplets came back
as one identical stamp tiled across the paper, same size, same content, same spacing. A field of many
small things has to be described as a field with its own texture, not as many copies of one described
thing.

**9.8.2026 — where a frame is impossible, draw the hint and write the shot.** The finished shot is an
animation, and the still only has to point at it. Reflections and shadows can be silhouettes, which
graphite does beautifully and which the model produces without argument.

**9.8.2026 — a lens does not read as a lens without something to compare it against.** `2C` attempt
four put a perfect photoreal Manan inside a clean drop and it read as a boy in a glass ball, not as a
boy seen through water, because nothing in the frame was magnified. Magnification is a **relationship**,
not a texture. The eye needs the same thing visible at two sizes: something crossing behind the drop
that is thin outside it and thick and bent inside it. In this film that something already exists and is
free, the ruled finish line.

**The four things that actually make water read as a lens.** One, the image inside **overflows the rim**,
so a face is cropped by the edge rather than sitting inside with headroom. Two, something continuous
crosses behind and is **displaced and thickened** where it passes through. Three, the centre is clear
and the image **squeezes and bends toward the rim**. Four, a bright ring just inside the edge and a
darker band outside it. Ask for the four as content. Never ask for magnification as a word.

**9.8.2026 — a complete portrait inside a small shape reads as a sticker, a fragment reads as a
reflection.** The secondary drops each came back holding a whole tidy face, which flattened them into
pasted images. In water you would see part of an eye, a piece of mouth, an edge of a cap. Fragments in
the small drops, one legible face in the large one.

**9.8.2026 — Manan renders photographic reliably now.** Two consecutive frames have produced a genuine
photograph of the boy with `MANAN.jpg` alone plus one drawn frame alongside it. The condition is size,
not isolation. Large, single, foreground.

**9.8.2026 — Nano Banana cannot do refraction. Stop asking. This is a capability limit, not a wording
problem.** Two runs, the second written with four separate optical cues described as content, and it
produced none of them. The ruled line crossed behind the drop and came out **thin, straight and
unbroken**. The face sat centred with clean headroom instead of overflowing the rim. There was no edge
compression and no bright ring.

**The reason, and it generalises.** The model composites, it does not transform. It can put a thing
behind, inside or in front of another thing, because that is arrangement. It cannot take content and
**bend, displace or crop it according to a surface**, because that is a transformation of something it
has already decided to draw. So refraction, reflections that distort, mirrors that show a different
angle, anything seen through moving water or curved glass, all of it is outside the tool. Ask for the
arrangement, get the distortion in post or in the animation.

**9.8.2026 — a perfect circle over a whole human face reads as a helmet.** Attempt five came back
funny rather than powerful and the shape is why. A circular transparent sphere containing a centred
complete face is one of the strongest visual priors there is: fishbowl, spacesuit, bubble. The earlier
teardrop shape escaped it purely by not being a circle. If a face has to sit inside water, keep the
water a **teardrop or an irregular blob**, never a perfect round.

**The rule this settles.** Where a frame needs an optical effect the model cannot produce, do not spend
a third run. Approve the strongest composition available, then write the missing physics into the scene
document for the animator. The still is a hint. The shot is the thing.

**9.8.2026 — SCALE IS INHERITED FROM THE REFERENCE AND CANNOT BE ASKED FOR.** `3A` asked for the
runner small in the middle of a large sheet with wide empty margins, anchored to `V4_1C` and `V4_2A`.
It came back as four runners at full frame height, which is `V4_2A` again. Every reference we own shows
a figure filling most of the frame, so that is the only size the model knows. There is no wording that
beats it. If a frame needs a different subject-to-paper ratio than any existing reference, the model
will not give it.

**And the radiating streaks did not appear either, which explains itself the same way.**

**THE UNIFYING RULE, AND IT COVERS EVERY FAILURE ON THIS PRODUCTION.** The model **varies objects but
cannot organise a field.**

    WORKS      properties of one thing            fade, line weight, pose, texture, material,
                                                  what is behind what, how many of a thing
    FAILS      geometry of the whole frame        refraction, radial streaks converging on a point,
                                                  subject scale against the sheet, anything bent or
                                                  cropped by a surface, mirrors at another angle

The fade across four figures in `2A` worked because fade is a property each figure carries. Streaks
radiating from a point fail because that is one geometry imposed on the entire sheet. Refraction fails
for the same reason. Read a new prompt against this table before spending a credit.

**What to do instead.** A pull back is a scale change of a drawing that already exists, so build it in
the container from the approved frame, which also makes continuity free because the figure is pixel
identical. `V4_3A` was made this way from `V4_1C`.

**9.8.2026 — Manan is solved, and the solution is depth.** `3B` produced the strongest photoreal boy of
the whole production: reads fourteen, real wool, real brass, real skin against pure graphite. The
conditions were large, single, foreground and **nearer to us than the drawn figure**. Putting him in
the near ground rather than beside the drawn character is what finally did it, because it gives him
frame area without asking the model to scale anybody.

**But he arrives holding the frame's one broken rule.** The glass came up on its own and it is aimed at
open paper. A named symbol without a physical support floats, and this is that failure in its purest
form: the most meaningful object in the film pointing at nothing. Where an object is an instrument, say
what it is trained on in the same sentence, or it will be raised for the camera rather than used.

**9.8.2026 — the ruled line is dropped whenever a photoreal figure is in the frame.** Three frames now.
It is not worth a rerun. It is two pixels of graphite and it can be drawn back in the container in a
minute, masked by colour saturation so it passes behind the boy and never across him. `V4_3B` was
finished this way.

**10.8.2026 — A HAND HOLDING AN INSTRUMENT DEFEATS EVERY WORD ABOUT WHERE THE INSTRUMENT IS POINTING.
Take the hand out.** `3C` attempt three is filed at `assets/V4/attempts/3C_a3_glass_off_the_muscle.png`.
The prompt placed the glass against the middle of the muscle with graphite surrounding the circle on
every side, and named the laboratory inside it. What came back is a beautiful giant calf, a correct back
of the head, real tweed, real wool, and the glass **small, empty and held out over bare paper in the top
right corner**, with nothing inside it at all.

**Why, and it is the unifying rule again.** The arm is a property of the figure and the model draws arms
the way arms are drawn, raised and out to the side. Where the glass is pointing is a **relationship
between two objects**, which is the thing the model cannot do. So the arm wins every time, and it takes
the glass out of the frame with it. This is the same failure as the floating gold key, but worse,
because a hand is a support, so the object is not floating and the earlier rule does not catch it. A
symbol needs a support. **An instrument needs a target, and a hand is not a target.**

**The fix, and it is Marko's sketch.** No arm, no hand, no figure. The glass **lies on the muscle** as an
object resting on a surface, which is arrangement and lands every time, and the only human thing in the
picture is a **piece** of the cap cut off by the bottom border, with the handle running down behind it.
The boy is therefore present, holding it, and never drawn. A fragment of a character at the frame edge
is safer than a whole one, because a whole one arrives with limbs that have to be posed.

**And an empty circle stays empty unless what is inside it is described as the subject.** The laboratory
was named after the glass and came back as clean glass. Content inside a circle only survives if the
circle is large, if the sentence says outright that there is no skin and no muscle in there, and if the
room gets as many words as the leg does.

**One more, and it follows.** Scale of an object against the frame is inherited like subject scale is:
the glass came back at the size a held magnifying glass is normally drawn. Asking for it large only
works when it is lying on something whose size the frame already establishes.

**10.8.2026 — TAKING THE HAND OUT FIXED THE AIM AND COST THE OBJECT. THE GLASS VANISHED COMPLETELY.**
`3C` attempt four is filed at `assets/V4/attempts/3C_a4_no_glass_hairy_leg.png`. The anatomy came back
superb and the tweed came back real, and **there is no magnifying glass anywhere in the picture**, in a
prompt that gave it its own sentence, its size, its rim, its handle and its contents.

**Why, and it completes the pair.** Attempt three had a hand, so the glass survived and went to the wrong
place. Attempt four had no hand, so the glass had nothing holding it in the frame and was simply dropped.
An object with no support is either misplaced or deleted, and wording cannot decide which. **The thing
that was actually missing in both is a sheet.** Every character in this film that renders reliably has
one. The glass has never had one, so the model has no identity to hold on to and treats it as optional
furniture. This is the failure table row about objects drifting between frames, seen at its extreme: an
object with no sheet does not merely drift, it disappears.

**The rule. An object that carries meaning across scenes is a character and gets a sheet, multiple
angles, 3:2, before it is asked for in a frame.** Sheets before frames was already the protocol and it
was applied to people only. See `worlds.md` section 7 for the queue.

**10.8.2026 — body hair on an anatomical drawing destroys the register.** "Fine hairs on the skin" was
in the prompt and the model drew them faithfully across a flayed muscle study, which is a contradiction
the eye catches immediately without being able to name it. If a drawing is anatomical, it has no skin and
no hair. Ask for muscle, tendon and fascia and nothing that belongs to a living surface.

**10.8.2026 — softness was asked for and delivered, and it was the wrong idea, not a wrong render.** The
cap came back correctly soft. Depth of field is not what marries a photograph to a drawing. **A cast
shadow is.** From now on every photographic element on the paper is sharp and throws a directional shadow
across the pencil lines. Written up as a law in `worlds.md`.

**10.8.2026 — TWO THINGS LANDED FIRST TIME AND BOTH ARE NOW PROVEN.** `3C` attempt five, filed at
`assets/V4/attempts/3C_a5_front_view_leg_small_no_cap.png`. **The cast shadow works**, the real brass and
wood throw a soft directional shadow onto the paper and the pencil stays readable under it, exactly as
`worlds.md` requires. **The translucent skin over the anatomy works too**, a faint continuous contour of
the intact leg laid over the muscle study, the x-ray reading, first attempt, no argument. Neither of
these needs to be fought for again. Transparency and shadow are both properties of one thing, which is
the half of the tool that works.

**10.8.2026 — NEVER DESCRIBE THE PAPER AS AN OBJECT IN SPACE. THE PAPER IS THE FRAME, NOT A THING IN
THE FRAME.** The same prompt opened with "seen from directly above, looking straight down onto a large
sheet of warm cream paper lying flat", and the model did precisely that: it **photographed a sheet of
paper on a table**, with the physical edge of the sheet visible down the left side, a grey surface
beyond it, and the drawing sitting small in the middle with wide margins all round. A still life of a
drawing instead of a drawing.

**And that one phrase also destroyed the subject scale**, which had been the only reason for uploading an
anchor with a big diagonal leg. Given a sheet of paper as an object, the model gives the sheet its
margins, because that is what paper has. The leg came back a third of the width and centred, with the
drawing politely inset. So the earlier rule that scale is inherited from the reference has a companion:
**scale can also be destroyed by a spatial description that gives the paper edges.** Say nothing about
the paper except in the medium sentence at the end, where "graphite pencil on warm cream paper" has been
safe in every approved frame.

**10.8.2026 — the photoreal fragment was dropped again, and this time it was my own fault, not the
model's.** The cap was written in the middle of the prompt, after the leg and the glass. The skeleton in
section 5 says the photoreal subject goes in block [1] because it is the thing most likely to be lost,
and the one time that rule was broken on this production the photograph vanished. Open with the
photograph. Every time. No exceptions for framing, camera position or anything else.

**10.8.2026 — anatomical view has to be named as a view.** "An anatomical study of the calf" produced a
symmetrical posterior view, both heads of the gastrocnemius, straight on, which is what an anatomy plate
looks like by default. If a limb is meant to be seen in profile, say profile, say which edge is the calf
and which is the shin, and say it is not symmetrical.

---

## 4b. THE TWO FINDINGS THAT MATTER MOST, FROM ATTEMPT SIX

`assets/V4/attempts/3C_a6_arm_appeared_glass_gone.png`. Read this section before writing any prompt.

### NEGATION ADDS THE THING. IT NEVER REMOVES IT.

The prompt said **no arm** anywhere in the picture. The model drew a complete anatomical study of an arm,
bent at the elbow, occupying the top left half of the frame. The prompt said **no knee and no ankle**.
The model drew a knee. Every single noun that appeared inside a negation in that prompt appeared in the
picture.

**The model renders nouns. It does not process the word in front of them.** Naming a thing in order to
forbid it is the most reliable way to summon it. This was already the rule for lettering in section 2 and
it is now proved for anatomy, and there is no reason to think it is different for anything else. The
earlier frames where "no knee, no ankle, no foot" appeared to work were not the negation working, they
were the closeness of the crop leaving no room for a knee.

**What to do instead. Describe the crop, positively.** Not "no knee and no ankle", but *the muscle runs
off the top border and off the bottom border*. Not "no arm anywhere", but *the picture is filled from
edge to edge by one calf*. A frame with no space in it cannot contain an arm, and nothing has to be
forbidden. **Delete every negation from every prompt from now on.**

### THE FRAME HAS A BUDGET OF ABOUT TWO SUBJECTS, AND OVER THAT IT DROPS ONE AT RANDOM

Six attempts at one frame, and the prompt grew from about a hundred and eighty words to about three
hundred and eighty, because each attempt added a clause to repair the last failure. The failures got
worse, not better, and here is the proof that it is not a wording problem:

    attempt five   kept the glass, kept the ghost skin, DROPPED THE CAP
    attempt six    kept the cap, DROPPED THE GLASS, dropped the ghost skin

**It is not the same element that fails.** The same four subjects were described with the same care both
times and the model discarded different ones. That is a capacity limit, not a phrasing error, and no
amount of rewriting will fix it. Above roughly two subjects the model spends its attention on whichever
two it happens to start with and quietly abandons the rest.

**And a model sheet does not save an object from this.** `GLASS.jpg` was attached to attempt six and the
glass still vanished. A sheet fixes an object's **identity**, so that it is the same object every time it
appears. It does not buy the object a **place in the queue**. The two problems are separate and both have
to be solved.

### THEREFORE, BUILD A FRAME IN PASSES

This is the composition version of sheets before frames, and it should have been obvious earlier.

    pass one    the drawn world alone. The leg, the room, the background.
                Nothing photographic, no objects. One subject, all the
                attention on anatomy, view and scale.

    pass two    image to image on the approved result of pass one, adding
                only the photographic objects. Two subjects at most.

Each pass stays inside the budget, and each pass is cheap to rerun because a failure only costs the pass
rather than the whole frame. It also means the anatomy, once right, is **locked**, and cannot be lost
again in a later run, which is what happened to the ghost skin between five and six.

**The cast shadow is the one thing that has now worked twice out of two**, in five and again in six, and
it is beautiful in six. It does not need protecting. Everything else does.

### AND THE TECHNIQUE THAT FOLLOWS FROM ALL OF IT: SHOW THE COMPOSITION, DO NOT DESCRIBE IT

Composition is a relationship between things, which is the half of the tool that does not work, and six
attempts were spent proving it again. **So stop writing it and build it.**

Pass one gave a correct profile calf that was too small, upright and sharing the paper with an arm. That
result was then **rotated eighteen degrees clockwise, zoomed to about four times, recentred on the calf
belly and cropped to sixteen by nine in the container**, until it matched Marko's sketch. The output is
soft, because it is an upscale, and softness does not matter at all: it is going back in as the anchor,
and the anchor is where the model reads framing, scale and angle. It reads those from a picture
perfectly and from a sentence hardly at all.

    assets/V4/attempts/3C_composition_guide_rotated_zoomed.png

**This is now the standard move whenever a frame is right in content and wrong in framing.** Do not
rewrite the prompt. Take the render, crop and rotate it by hand into the composition you want, feed it
back, and ask only for quality. It costs no credits, it takes two minutes, and it converts an
unanswerable request into the one the model is good at, which is redrawing something it can already see.

**It worked.** Pass one version two held the framing, the angle and the lean, and came back crisp. Filed
as `3C_p1_a2_framing_held_leg_drifted_right.png`, trimmed and locked as `3C_p1_PLATE_leg_locked.png`.

### AND ONE LIMIT THAT IS NOT THE MODEL'S FAULT, IT IS THE DRAWING'S

Trying to push the plate all the way to the zoom in Marko's sketch, where the leg crosses about seventy
percent of the frame width, was attempted four times in the container and abandoned. **Past a certain
magnification an anatomical study stops reading as a leg and becomes vertical striation.** Muscle fibre
is directional texture, and texture without a silhouette around it is wallpaper. The calf is legible only
while enough of its taper is in frame for the eye to close the shape.

So the plate sits slightly wider than the sketch, with both edges of the ghost skin contour visible and
the calf narrowing at the bottom. **The glass is what will make the extreme closeness work**, because
once a circle lies on that texture the frame stops being an abstract drawing and becomes a man being
examined. The instrument tells the eye where to look, and the abstraction turns from a problem into the
point. Do not solve legibility by pulling back further once the glass is on.

---

## 4c. A FRAGMENT OF A CHARACTER MUST BE CUT BY THE FRAME EDGE, OR IT READS AS ABANDONMENT

`assets/V4/attempts/3C_p3_a1_cap_reads_as_abandoned.png`. The prompt asked for the peak of the cap
breaking in over the bottom right corner. What came back is **a whole cap lying complete inside the
frame**, entire, resting on the paper next to the glass, with its own shadow. It is beautifully made
and it is the exact opposite of what it was for. A hat lying by itself says the person has gone.

**The rule, and it refines the presence law in `worlds.md` 6b.** A fragment only reads as presence if
**the frame cuts it**. Anything complete inside the borders is an object, and an object belonging to a
person who is not there is a stronger statement of absence than empty paper. So the words that matter
are not "a piece of the cap" but **"cut by the bottom border", "continuing out of the picture",
"only part of it is in the picture"**. The model will otherwise centre and complete anything it is
given, because completing objects is what it does.

Two runs were spent on this and `3C` was locked without the cap instead. The presence of Manan in this
frame is carried by the handle of his glass running out of the lower right corner, which is a cut
fragment of his property and does the job at no cost.

---

## 4d. A HARD FAILURE IS NOT A BAD IMAGE, AND IT IS DIAGNOSED DIFFERENTLY

10.8.2026. `4A` returned **Generation failed, credits returned**, twice in three minutes. Nothing came
back at all. That is a refusal or a service error, not a composition problem, and rewriting for craft is
wasted effort until it is cleared.

**WRONG. THIS WHOLE PARAGRAPH IS WRONG AND IS KEPT ONLY AS A WARNING. THE CAUSE WAS A FULL IMAGE LIBRARY
ON THE PLATFORM ACCOUNT, NOTHING ELSE. SEE SECTION 4f. What follows was a confident theory built on a
real correlation and it was still false.**

**11.8.2026 UPDATE, AND IT WAS NOT THE WORDS AT ALL. IT IS THE WEIGHT OF THE REFERENCE FILES.** The
same hard failure then happened on the **AI Image Editor**, a completely different model on the same
platform, and a tool that had run successfully on 4.8. Two different engines failing within half an hour
is not a content filter, it is the input.

Every reference file ever used successfully on this production is **under about half a megabyte**. The
two `4A` runs are the first that ever pointed at `LAB.jpg`, which is **1.21 MB**, and the editor run
pointed at a **5.9 MB PNG** collage. All four failed. Nothing else has ever been that heavy.

    worked, every time     0.11 to 0.47 MB
    failed, every time     1.21 MB, and 5.90 MB

**THE RULE. NEVER POINT EITHER TOOL AT A MASTER FILE. ALWAYS SERVE A `_web` COPY, LONGEST EDGE 1600,
JPEG QUALITY 85, UNDER 400 KB.** Masters stay in the repo for the edit and the grade. The tools get the
light copy. `LAB_web.jpg`, `SCIENTIST_web.jpg`, `GLASS_web.jpg` and `MANAN_web.jpg` were made on
11.8.2026 for exactly this reason, and a `_web` copy is made of every reference from now on at the moment
the master is saved.

This also explains why the earlier sheets all worked. They were saved as attempt crops and web jpgs,
which are small by accident. The moment the pipeline started serving full sheets, it stopped.

**The old suspect list, kept because it may still be a second cause.** In this prompt the anatomical plates on the wall are named as **a
skeleton, a ribcage, a femur and a full figure**. A full anatomical figure is an unclothed body, and
skeleton and ribcage sit near medical and gore filters. The same words passed once, in the `LAB.jpg`
sheet prompt, when the room was **empty**. Adding a person into a room described that way is the one
thing that changed, and a filter that is looking at the combination rather than the words would fire
exactly there.

**But do not be certain.** A hard failure twice in a row can also be the service. The two causes are
told apart by the same method either way.

**The bisect protocol, use it for any hard failure.**

    1. Strip the prompt to its safest possible version, plain nouns only,
       and run it. If that also fails, the problem is the service and not
       the words, so wait and rerun rather than rewrite.
    2. If the safe version renders, add back one suspect group per run.
    3. The group that kills it is the trigger. Write it here.

**And when a word is the trigger, replace the register rather than the noun.** Charts, diagrams,
figures, printed sheets and studies all describe the same wall without naming a body or a bone. The
picture is identical and the words are not, which is the whole trick.

---

## 4e. 11.8.2026, AND THE WEIGHT THEORY IS ONLY HALF RIGHT

The room prompt failed on `LAB_web.jpg`, which is **0.26 MB**, well inside the limit that had just been
established. So weight explained the **editor** failure and does not explain Nano Banana's.

**The pattern as it now stands.** Nano Banana has failed three times today, on three different prompts,
with references from 0.26 MB to 1.21 MB. The editor has succeeded three times in the same window on the
same platform with the same kind of files. **One model is working and the other is not**, which points
at the model or the quota behind it rather than at anything we are writing.

**The test that settles it, and it costs one credit.** Run the smallest possible Nano Banana job, a
proven small reference and a prompt of a few words. If that fails, the model is unavailable and the
correct response is to stop rewriting and work in the editor until it returns. If it succeeds, then
something in the long prompts is the trigger and the bisect protocol in 4d applies.

**And the standing lesson underneath both of these.** When two tools share a platform, a failure in one
and success in the other is evidence about the tool, not about the prompt. Check what else is working
before rewriting anything.

**The fallback that needs no generator at all.** A coherent single room already exists inside
`LAB.jpg` view one, drawn in one go. Cropping it to sixteen by nine in the container gives correct
geometry from a single source, no stitching, no seam, at the cost of a tighter frame and the corner
falling outside the picture. Filed as `assets/V4/attempts/4_ROOM_single_source_web.jpg`. Architecture
does not always have to be generated. It has to be **single source**, which is the real rule.

---

## 4f. THE ACTUAL CAUSE, AND THE LESSON IS ABOUT ME AND NOT ABOUT THE TOOL

11.8.2026. Marko **deleted the stored images from his account on the platform** and everything worked
immediately, on the first try, with the same prompt and the same reference that had just failed. The
storage was full. That was the entire cause of every hard failure today.

**So both diagnoses in 4d and 4e were wrong, and they were wrong in an instructive way.**

    4d said     the anatomy words are triggering a content filter
    4e said     the reference files are too heavy
    truth       the account's image library was full

Every piece of evidence used was real. The anatomy words genuinely did appear in the failing prompts.
Every file that had ever worked genuinely was under half a megabyte, and the failing ones genuinely were
heavier. Both correlations were perfect and both were **accidental**, because the true cause was
accumulating in the background the whole time and made everything later fail regardless of its content.

**The rules that are now cancelled.** There is no file weight limit. There is no anatomy trigger. Full
resolution masters can be served as references. Nothing has to be shrunk. `_web` copies are still worth
making for phones and for speed, but they are not a safety measure and never were.

### THE RULE THAT REPLACES THEM

**When failures start suddenly and affect everything, look for something that accumulates.** Storage,
quota, credits, sessions, a cache. A cause that builds up over time produces a perfect correlation with
whatever you happened to change most recently, which is why the evidence looked so convincing twice in a
row. Content and size and wording are all things we vary deliberately, so they are the first suspects
and they are exactly the ones a background cause will frame.

**And check the boring thing first.** Storage full, credits out, logged out, disk full. It costs nothing
to look and it would have saved four credits and about an hour today.

**11.8.2026, LATER. IT CAME BACK, AND THAT CONFIRMS IT RATHER THAN CONTRADICTING IT.** Fourteen minutes
and **four successful jobs** after the library was cleared, the failures started again. So the storage
does not just have to be emptied once, it **fills up as you work**, and roughly four or five generations
is enough to do it.

**So this is maintenance, not a bug to diagnose.** Clear the stored images on the platform every few
jobs, the way you would empty a bin. Download anything worth keeping first, since everything that matters
is in this repo anyway.

**And it is a good example of why the earlier theories were so convincing.** Between two clearings there
is a window where everything works, then a window where nothing does, and whatever you happened to change
at the boundary looks like the cause. It was the anatomy words the first time and the file size the
second. It was the bin both times.

**11.8.2026 — a whitelist does not guarantee lettering, it only bounds it.** The scene 5 storyboard named
eight exact short phrases as the only words allowed on the sheet and the model drew **none of them**.

**CORRECTED THE SAME DAY, AND THIS IS THE USEFUL VERSION.** The six script zero boards came back with
lettering that is clean, correctly spelled and well placed, including full sentence captions under every
panel. So the tool **can** letter, and letters well. What decides it is the job:

    short label in a fixed place        reliable. FRONT VIEW, ABSORBED, EPIPHANY,
                                        SCENE 4 OF 9, a caption under a panel.

    long annotations scattered over
    small objects in a drawing          invented gibberish. The anatomy plate labels.

    a list of exact phrases with no
    place named for each of them        dropped entirely. The scene 5 board.

**So lettering is a layout problem, not a spelling problem.** Give each piece of text a **position** and
keep it short, and it lands. Ask for words without saying where they go, and they vanish. Ask for many
small words over a busy surface, and they are invented.

Anything that must be exactly right in a final frame still goes on in the container, where it costs
nothing. Boards and sheets can carry their own titles.

**And the storyboard sheet itself is a method worth keeping.** Six rough thumbnails, no reference images,
one prompt, one credit, and Marko chose a scene direction off it in a few seconds that had taken several
paragraphs of prose to describe badly. **When a decision is about story rather than craft, board it
instead of writing it.** Rough is the point: a thumbnail that looks finished invites notes on the drawing
rather than a decision about the film.

**11.8.2026 — CLEANING A REFERENCE DOES NOT IMMUNISE THE NEXT GENERATION.** `ROOM.jpg` was cleaned of a
recognisable public figure and of every invented word, and the very next sheet generated **from that
cleaned reference** put the same poster back on the wall, with the same garbled name across it.

**Because the fault was never in the reference. It is in the model's own idea of what a boy's room in
India contains.** A reference biases; it does not forbid. Anything the model reaches for by default will
keep coming back for as long as the prompt leaves a gap where it fits.

**So there are two ways to keep a fault out and both are needed.** Specify the thing **positively** in
every prompt that could summon it, a flat silhouette poster rather than silence about posters. And run a
clean up pass on every output regardless, because the prompt will not catch everything.

**This is the same shape as the negation finding in section 4b.** Leaving something unsaid is not the
same as excluding it. The model fills gaps, and it fills them with the most common thing.

**11.8.2026 — A MULTI PANEL REFERENCE IMPOSES ITS LAYOUT ON THE OUTPUT. SHEETS BEGET SHEETS.** The first
final frame was asked for as a single film frame and came back as **another six panel character sheet**,
because both references handed to it were six panel sheets. The prompt said film frame, said single, and
described one continuous scene. The layout of the reference beat every word of it.

**This is the same law as everywhere else on this tool: the reference decides form, the prompt decides
content.** It was already known that an anchor dictates line weight, paper and hand. Panel structure is
part of that same inheritance and it is the strongest part.

**So sheets are for making sheets, and single frames need single frame references.** Crop one panel out
of the sheet and feed that instead. It costs nothing, it takes a minute in the container, and it is now
the standing practice. `MANAN_AT_DESK.jpg` and `ROOM_WIDE.jpg` were cut out of `MANAN.jpg` and
`ROOM.jpg` for exactly this.

**The general form of the rule, worth holding on to.** Whatever is structural in a reference will
transfer whether it was asked for or not. Aspect, panel grid, borders, labels, the number of subjects.
If the output should not have it, the reference must not have it either.

**11.8.2026, SECOND ATTEMPT, AND THE SINGLE PANEL CROPS DID NOT FIX IT.** Fed two single images, asked
for one continuous photograph, and it returned **a seven panel grid in portrait**, having also ignored
the requested sixteen by nine. So the cause is not the panel structure of the reference. Something else
is holding it in sheet mode.

**The remaining suspects, and there are only three.**

    the references     any reference of this boy in this room may now read as
                       documentation to the model, whatever its crop
    the tool state     an aspect or mode control left set from the last job,
                       which would also explain the portrait output
    the prompt         a word in it reading as a layout instruction

**The test that separates them costs one credit: run the prompt with no reference images at all.** If a
single frame comes back, the references are the cause and final frames get made from text plus the
editor. If a grid comes back again, it is the tool and not us, and no rewriting will help.

**This is the bisect protocol from section 4d and it applies to any stubborn failure.** Strip to the
simplest possible version first, then add one thing back at a time. Two credits have now gone on
guessing instead of testing, which is the mistake that section exists to prevent.

**11.8.2026 — FOUND IT, AND IT WAS NEVER THE PROMPT OR THE REFERENCES. THE TOOL CARRIES STATE BETWEEN
JOBS.** A screenshot of the form settled three runs of guessing in one look.

    the prompt box     still held the tail of the PREVIOUS prompt, appended after
                       the new one. The visible text ended "sixteen by nine., its
                       screen turned away from us. A steel water bottle..." which is
                       the end of one prompt followed by the middle of another.
                       Pasting APPENDS. It does not replace.
    the image list     both reference images were still attached on a run that was
                       meant to have none
    aspect ratio       set to AUTO, which is why sixteen by nine kept coming back
                       as portrait. On auto the model picks, and given sheet like
                       content it picks tall.

**So the grids were almost certainly the model faithfully obeying the leftover fragment of the character
sheet prompt**, which asked for six photographs arranged in two rows of three. It was never disobeying.
It was answering a question we could not see.

### THE PRE FLIGHT, RUN IT BEFORE EVERY SINGLE JOB

    1. clear the stored images on the account
    2. remove every attached reference with the X, one by one
    3. select all in the prompt box and delete, then check it is empty
    4. set the aspect ratio explicitly, never leave it on auto
    5. paste the new references, paste the new prompt, run

**And the general lesson, which is now three for three on this production.** Every unexplained failure so
far has been **stale state** and none of them has been the wording. The full image library, the leftover
prompt, the carried over attachments, the auto aspect. Before rewriting anything, look at what the tool
is still holding from last time.

## TONE NEEDS A CEILING TOO, 13.8.2026

Frame 2.6, the over the shoulder on the stamp. The prompt said the boy's head and shoulder should be
"dark and solid against the paper". No bound, so it went to maximum: 19% of pixels below luminance 80,
against 6.5% on the panel it replaced and 10.9% on the darkest existing Manan panel. He came back as a
black silhouette instead of pencil.

**This is the same law as intensity everywhere else. Name the ceiling, not the direction.** Tone is an
intensity instruction and needs a bound compared to something already in the frame.

Write: *no darker than the wooden stamp handle already in this frame.* Not: dark and solid.

**And it was repairable in the container for free.** A lift of `L + (160-L)*0.34` where `L<160`, applied
as a scale on all three channels so the cream stays cream, brought it to 7.6% and it reads as pencil
again. Tone is a container job. Do not spend a credit regenerating for tone.

**The tool overruled the prompt on light direction and it was right.** The prompt asked for a key from
upper right. The tool put it camera left, which is the film's own law from `worlds.md`. Every Manan
frame is keyed from camera left at forty five degrees. Do not write anything else.
