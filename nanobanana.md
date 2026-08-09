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
