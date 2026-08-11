# codebox.md

**Every code box gets a title and a summary above it. No exceptions.**

Sits beside `nanobanana.md` and `documents.md`. This one is about the chat itself rather than the
film, and it exists because Marko scrolls back through very long sessions on a phone and must be
able to identify any box at a glance without opening it.

---

## 1. THE RULE

Immediately **before** every code box:

1. A **bold title line in capitals**, naming exactly what the box is.
2. **One or two plain sentences** summarising what is inside it.

Both go **outside** the box. Never inside. The box holds only the thing to be copied, nothing else.

Number them when several appear together in one response.

---

## 2. THE TITLE

The title says **what this specific thing is**, not what category it belongs to.

Weak titles, all useless when scrolling:

- REFERENCE IMAGE
- PROMPT
- CODE
- IMAGE 1

Strong titles, each identifiable at a glance:

- **REFERENCE 1, MANAN, THE DETECTIVE COAT AND DEERSTALKER CAP**
- **REFERENCE 2, THE MARATHON RUNNER MODEL SHEET, FOUR VIEWS**
- **REFERENCE 3, THE STYLE ANCHOR, LIGHT PENCIL ON PALE PAPER**
- **PROMPT, 1B, PEAK, THE MOMENT HE SEES THE FINISH LINE**
- **MESSAGE TO NEHA, ASKING FOR A FEW MORE DAYS**

For a reference image, **name what is actually in the picture**. Who the character is, what he is
wearing, what the sheet shows. "Manan reference" is not enough. "Manan, photoreal, four views, tan
caped overcoat and deerstalker cap, brass magnifying glass" is a title that can be recognised without
clicking anything.

---

## 3. THE SUMMARY

One or two sentences. It answers two questions:

- **What is in it.** For an image, describe the frame. For a prompt, describe the shot.
- **Why it is here.** What this box is for, or what it holds together.

Example:

> **REFERENCE 2, THE MARATHON RUNNER MODEL SHEET, FOUR VIEWS**
> Four views of the runner in graphite on cream: doubled over with hands on knees, three quarter
> running, profile mid stride, and rear with 27 on the vest. Lean, gaunt, adult proportions.
> Uploaded to hold his build and face across every frame he appears in.

The summary is not a label repeated. If the summary only restates the title, it is doing nothing.

---

## 4. ORDER, FOR IMAGE WORK

Reference images always come **before** the prompt. See `nanobanana.md` section on delivery format.

1. Each reference image in its own box, with its own title and summary.
2. The prompt last, in one box, with its own title and summary.

---

## 4b. THE COUNT, BEFORE EVERY SET OF IMAGE BOXES

One line before the first box, stating how many reference images are coming and the three settings a
prompt is incomplete without. No table. The count is read once and held in the head, and the boxes are
then copied top to bottom without scrolling back.

    2 reference images, 1 prompt. Image To Image AI, 16:9.

**Why the count and not a description.** A reference silently skipped is the most expensive mistake on
this production, because the frame comes back plausible and wrong and the wrongness gets blamed on the
prompt. The number is the only thing needed to catch that, and it costs one line. Each box already
carries its own title saying what it is.

**One count per delivery.** Two frames in one message is two counts, each immediately above its own
set of boxes.

**Every box carries a short tag on its own line, directly above it, inside square brackets.**

**References carry their position and the total, `[R1/3]`, `[R2/3]`, `[R3/3]`.** Changed 10.8.2026 at
Marko's request and it is not cosmetic. He pastes these one at a time on a phone while moving, and the
count in the tag is what tells him he has not dropped one. A tag that says `[R2/3]` is a checksum. A tag
that says `[R2]` is a name.

**THE COUNT LINE IS A TABLE.** Set 11.8.2026. The line that used to read `2 reference images, 1 prompt.
Image To Image AI, 16:9.` is now a two column table, because Marko scans it on a phone before he starts
setting the form and a table is read at a glance where a sentence has to be parsed.

| | |
|---|---|
| **Tool** | Image To Image AI |
| **Model** | Nano Banana Pro |
| **Aspect** | 16:9 |
| **References** | 1 |
| **Prompts** | 1 |

Fill only the rows that apply. For an editor job the tool row reads AI Image Editor and the model row
reads E-Pro. **Pre flight** goes in the table too when it needs saying, which is every time.

**The prompt tag carries the aspect ratio.** Set 11.8.2026. `[prompt 16:9]`, `[prompt 3:2]`. The tool has
an aspect control that is easy to leave on **auto** from the last job, and on auto the model picks for
itself, which has already cost a full resolution frame that had to be cropped down to 1600 by 900. The
aspect belongs on the line Marko is looking at when he sets the form, not buried in a sentence above it.

    [prompt 16:9]      every film frame
    [prompt 3:2]       every model sheet and every storyboard

**The prompt tag is `[prompt]`, in lower case, inside the brackets.** Not `[P1]`. There is one prompt
per delivery and it does not need a number, and the lower case word is instantly distinguishable from
the reference tags above it at a glance, which is the whole point of a tag.

The brackets are not decoration, they are what makes it a tag rather than a word. The tag is the **last
line before the box** and nothing else shares that line. It does not go in the title and it does not go
above the summary.

**Scene deliveries are named `SCENE n/total [VERSION]`.** Set 11.8.2026. `SCENE 5/9 [V4]`, not
`V4 SCENE 5`. The count comes before the version for the same reason the reference tags carry a
denominator: Marko is reading these on a phone while moving, and the first thing he needs to know is
where he is in the film, not which draft it belongs to. Script zero boards are `SCENE 5/6 [S0]`.

**Beside the tag, the file name and nothing else.** A reference tag reads `[R1/3] MANAN.jpg`, not the
path and not the URL. A prompt tag reads `[prompt] 3C` or just `[prompt]`. The file name is what Marko
already holds a picture of in his head, so one word tells him which reference this is without reading
the title or opening the link.

    THE FULL SPRINT, V4_1C, THE WHOLE FIGURE IN PROFILE
    The runner alone on open paper, side on, the finish line crossing behind him.
    <blank line>
    <blank line>
    [R1/1] V4_1C_web.jpg
    [box]

Two blank lines above the tag, one below it. The double gap is what lifts the tag off the summary and
parks it on the box.

**Why the last line and not the title.** A title sits above a paragraph of summary, so by the time the
eye reaches the box the tag has scrolled out of view. Sitting immediately above the box, the tag and
the thing it names are one object. Glance at the box, glance up one line, done, without reading a word
of the description.

**Numbering restarts at every count.** Two deliveries in one message is `[R1/2]`, `[R2/2]`, `[prompt]`
and then `[R1/2]`, `[R2/2]`, `[prompt]` again. The count line resets the sequence, and the denominator
is the total for **that delivery**, never for the message.

---

## 5. WHAT GOES INSIDE A BOX

Only the thing to be pasted. A raw URL, a prompt, a message, a command. No labels, no headings, no
commentary, no explanation, nothing that would have to be deleted after pasting.

---

## 6. WHY

Marko works by voice on a phone, across sessions that run for hours and cover several projects at
once. A response is scrolled past twenty times before it is used. The title is how a box is found
again, and the summary is how it is trusted without being opened.

A box without a title is a box that has to be read to be identified, and by then the scrolling has
already cost more than writing the title would have.
