# HANDOVER — THE BRAIN BRAKE
## Paste this whole document as the first message in the new chat.

You are continuing a live film production already in progress. Everything you need is below. Do not ask
Marko to re-explain any of it and do not ask permission for routine operations. He works by voice, often
while moving. Move fast, execute without check-ins, and write what you learn back into the repo.

**Last updated 10.8.2026. Scenes 1 and 2 complete, 3A and 3B approved, 3C recomposed from Marko's
sketch and back in the loop.**

---

## 0. FIRST TWO THINGS YOU DO, IN THIS ORDER

**One, clone the repo.** Marko will paste the token in chat.

```
cd /home/claude && TOKEN=[paste] && git clone -q "https://x-access-token:${TOKEN}@github.com/markoboskoauroville/BRAIN_BRAKE.git" && cd BRAIN_BRAKE && git config user.email "marko.bosko@auroville.community" && git config user.name "Marko Bosko" && ls
```

**Two, read these seven files before doing anything else.** They are the accumulated rules of this
production and they exist so that knowledge is not lost between chats.

| File | What it is |
|---|---|
| `storytelling.md` | Read first. Explains all the others. First law is empathy before curiosity. |
| `documents.md` | How to write anything. |
| `nanobanana.md` | How to control the image model. Long and load bearing. Read every line. |
| `codebox.md` | How to format code boxes and image deliveries in chat. |
| `elements.md` | The five elements as a wholeness check on the film. |
| `STATE.md` | The shared brain. Current state of everything. |
| `worlds.md` | The law of the two worlds and how they become one. Shadows, transparency, object sheets. |
| `correspondence.md` | Every message to and from the crew, plus the drafts that are still outstanding. |

Then read `scenes/S2.md` and `scenes/S3.md`, which are the finished scene documents.

To push after any change:

```
cd /home/claude/BRAIN_BRAKE && TOKEN=[paste] && git add -A && git commit -q -m "message" && git push -q "https://x-access-token:${TOKEN}@github.com/markoboskoauroville/BRAIN_BRAKE.git" main
```

---

## 1. THE PROJECT

A two minute science film called **THE BRAIN BRAKE**, entered into the **Breakthrough Junior Challenge
2026**. Subject is the Central Governor Theory: the limit an athlete hits is almost never the muscle
running out, it is a decision made upstream in the brain.

Competition deadline **15.9.** Internal delivery target **1.9.** Shoot date confirmed **18.8.**

The competition scores scientific accuracy and requires the entry to be the student's own work. Every
claim must trace to real research, and the one contested model is labelled as contested on screen.

The science, all real and published. Marcora showed athletes at genuine exhaustion could still produce
far more power immediately afterwards, so the muscle was not the limit and perception of effort was.
Stone et al had cyclists race a ghost of their own best ride secretly set two percent faster, and they
beat it. Mindfulness training increased time to exhaustion with no measurable physiological change.

---

## 2. THE PEOPLE

| Person | Role | Where |
|---|---|---|
| **Marko Boško** | Story mentor, director, editor, sound design, original score. Your user. | Zagreb / Rijeka |
| **Manan Periwal** | 14, writer and performer. Owns the concept and the science. | Bangalore |
| **Neha Sonthalia Periwal** | Manan's mother. Client, producer, sole approval point. | Bangalore |
| **Venkatesh Aurovenkatesh** | Cinematographer. +91 81488 97033 | Auroville |
| **Kristijan Kaurić** | Animation, runs Brojka in Zagreb, brojka.hr | Zagreb |

Manan has **ADHD**. The entire shooting method is built around it: one sentence per take, full reset
between lines, camera rolling through the resets, break every twenty minutes. Never rush him. This is
not a compromise, fragmented shooting produces a livelier cut.

---

## 3. MONEY

Marko's fee **1200 EUR**: 700 concept, direction and edit, 200 sound mix, 300 original score. Terms
50/50. **600 EUR advance received 3.8.** Balance on delivery.

Kristijan quoted **250 EUR per day, estimating 3 to 5 days**. Not yet approved by Neha. He invoices
Marko, who puts it in a shared folder for Neha. 50% before he starts animating.

Venkatesh quotes Neha directly and is paid locally in rupees, so only the European fees cross a border.

**Marko's bank:** Erste&Steiermärkische Bank d.d., Rijeka. IBAN HR4924020063206388466, SWIFT
ESBCHR22. OIB 76414630904. Kučićki put 1a, 51000 Rijeka. Production name **Mantra Productions**.

---

## 4. THE FILM AS IT NOW STANDS — VERSION FOUR, NINE SCENES

Any earlier description of the film, including the six scene version in older documents on the website,
is superseded. The arc is light to light.

```
S1  0:00-0:14   THE MAN WHO SHOULD HAVE STOPPED    complete
S2  0:14-0:26   THE REVERSAL                       complete
S3  0:26-0:33   THE ARRIVAL                        3A and 3B done, 3C outstanding
S4  0:33-0:49   INSIDE THE LEG, 1923
S5  0:49-0:58   THE CRACK
S6  0:58-1:09   UP THE BODY, INTO THE HEAD
S7  1:09-1:30   THE COACH
S8  1:30-1:51   THE RELEASE
S9  1:51-2:00   WHITE
```

**Three frames per scene, A introduction, B peak, C resolution.** The term hero image is retired,
because one frame cannot show an arc. Nine scenes at three frames is twenty seven frames, which is the
number on the runner's vest. That was not planned.

**What changed and why.** The old version put a factory and workers inside the leg, so the leg carried
both the science and the metaphor and did neither well. One space, one job. The leg is now a
laboratory and the head is the imagination, and the audience learns that below is real and above is
invented without being told.

**Retired:** the factory in the leg, the road workers in scene 1, the gutter key. The key moves to the
Coach's chain in S7 and appears nowhere else.

**Threads:** the number ladder 1, 3, 9, 27, with the 3 in 2A and the 9 in 2C. The needle climbs and
never enters red. Workers live only in the head. Light travels white, cream, graphite, gold, white.
Paper tone is decided, start cream and end white, and the shift happens **in the grade**, never in a
prompt, because tone comes from the reference and cannot be argued with.

**The glass thread needs a decision from Marko.** The old rule was a monotonic descent opposing the
rising key. The key has moved and the film now goes down into the leg and up into the head, so the
proposal on the table is that the glass falls to the leg, rises to the skull, and is put down in the
last scene.

**The five elements.** See `elements.md`. The honest diagnosis is that this film is strong in earth,
fire and wind, adequate in ether, and was almost empty of water, which is why Manan now arrives in
poured water in scene 2. Scene 5, THE CRACK, is flagged as the thinnest scene in the film by this
reading, pure wind with nothing under it. Unresolved, and worth solving before it is boarded.

---

## 5. FRAMES DONE, ALL IN `assets/V4/`

| Frame | What it is |
|---|---|
| `V4_1A` | The finished man, head back, hands open, empty paper. |
| `V4_1B` | Close on the face as the eyes fix. He reads ten years older here. Never use as an anchor. |
| `V4_1C` | The released sprint in profile. The frame that was right. Anchor to this one. |
| `V4_2A` | The run taken back, four figures ghost grey to firm dark along one path. |
| `V4_2B` | The jaw macro with a spray of drops returning into the skin. |
| `V4_2C` | Manan's face inside a teardrop of poured water, drawn faces in the drops around it. |
| `V4_3A` | The snap pull back. Built in the container from `V4_1C`, not generated. |
| `V4_3B` | Manan's full figure entrance, near to us at the right, runner small and facing him at the left. |

Rejected attempts are filed in `assets/V4/attempts/` with the reasons in `nanobanana.md`. Nothing paid
for is thrown away.

**Reference sheets in `assets/REFERENCES/`.** `MANAN.jpg` is the important one, photoreal, four views,
tan caped overcoat and deerstalker, brass magnifying glass, grey seamless. `RUNNER.jpg` is the runner
model sheet. `RUN_CYCLE.jpg` is four full size profile figures of the runner mid stride, saved from a
failed generation and genuinely useful as a run cycle sheet for Kristijan. Also `BRAIN.jpg`,
`BRAIN_ROOM.jpg`, `MUSCLE.jpg`, `TANKS.jpg`, `TANKS_MARKED.jpg` and `WORKERS.jpg` from the old version.

---

## 6. THE IMAGE MODEL — THE ONE RULE THAT COVERS EVERYTHING

Marko uses **ImgToImg.ai** running **Nano Banana Pro**, mode **Image To Image AI**, aspect **16:9**.
References go in as raw GitHub URLs. Full detail is in `nanobanana.md` and you must read it, but this
is the rule that explains every failure on this production.

> **The model varies objects. It cannot organise a field.**

Works: properties of one thing. Fade, line weight, pose, texture, material, what is behind what, how
many of a thing.

Fails: geometry of the whole frame. Refraction, radial streaks converging on a point, subject scale
against the sheet, anything bent or cropped by a surface, mirrors at another angle.

Consequences already paid for. **Refraction is impossible**, so where a lens is needed, put different
content inside the circle rather than a magnified version of what is behind it. **Subject scale is
inherited from the reference** and cannot be asked for, so a pull back is built in the container from an
approved frame instead of generated, which also makes continuity exact. **Manan renders as a genuine
photograph only when he is large, single and in the foreground**, and the reliable trick is to place him
nearer to us than the drawn figures, so depth gives him frame area without asking the model to scale
anybody. The **ruled finish line is dropped whenever a photoreal figure is present**, three times now,
and it is cheaper to draw it back in the container, masked by colour saturation so it passes behind him,
than to rerun.

Two runs then stop. A third failure means a missing reference or an overcrowded scene, not a wording
problem, unless the change is composition rather than wording, in which case it is a new frame.

---

## 7. HOW MARKO WANTS IMAGE DELIVERIES FORMATTED

Full rules in `codebox.md`. In short.

One line before the boxes stating the count and the settings, for example
`2 reference images, 1 prompt. Image To Image AI, 16:9.`

Then for each box, a bold caps title naming what is actually in the picture, one or two sentences of
summary, **two blank lines**, then the tag in square brackets on its own line, then the box. References
are `[R1]`, `[R2]`. Prompts are `[P1]`. Numbering restarts at every count line. The tag is the last line
before the box and nothing else shares that line.

**Beside the tag goes the file name and nothing else**, so `[R1] MANAN.jpg`, never the path or the URL.
Marko already holds a picture of each reference in his head and the file name is what retrieves it.

References always come first, each in its own box holding only its raw GitHub URL. The prompt comes
last. Never economise on references. If a returned frame breaks continuity, changes a character or
drifts in style, say so immediately.

---

## 8. HOW MARKO WANTS EVERYTHING ELSE FORMATTED

**Messages** to people go in a code block, message text only.

**Terminal commands** as a single chained one-liner joined with `&&`, no markdown symbols and no
backslash continuations, because he pastes into mobile Termux.

**Croatian dates as numbers only.** 1.9., 15.9., never month names.

**No dashes or em dashes** to organise text. Flowing prose with commas and conjunctions.

He works in Croatian and English. Messages to Kristijan are Croatian, to Neha and Venkatesh English.
Personal messages in lowercase Yshai style, business messages sentence case.

---

## 9. THE WEBSITE — CRITICAL WORKFLOW

Live at `https://markoboskoauroville.github.io/BRAIN_BRAKE/`, password `manan`, client side only and
known to be obscurity rather than security.

**Never hand-edit `index.html`.** It is generated. Regex patches on the HTML once left three orphaned
closing tags that silently broke every tab. The source of truth is `8-rebuild-site-v8.py`. Edit that,
run it, validate the HTML, test the tabs with Playwright, then push.

The sandbox proxy blocks `github.io`, so you cannot fetch the live page. Verify locally and trust the
push. **The site still describes the old version of the film and needs rebuilding for version four.**

---

## 10. THE BOOK

`How to Create a Winning Film` lives at `markoboskoauroville.github.io/WINNING_FILM/`, repo
`markoboskoauroville/WINNING_FILM`, currently **version nine**. It is a single generated `index.html`.
**Web only, never a PDF.** It is updated automatically as discoveries are made, without being asked.

Chapters added. Part twenty four, wide, medium, close, including the fourth framing and
why the impossible has to arrive in a small frame. Part twenty five, the last surge, on building a film
on what an audience already half knows. Part twenty six, the five elements as a diagnostic for
wholeness. Part twenty seven, **on model**, added 10.8.2026: the professional vocabulary of continuity,
model sheet and turnaround and off model and prop model sheet and hero prop and the bible, the part
almost nobody does which is treating objects as characters, and the new finding that with a generative
tool an object without a sheet does not drift between frames but disappears from them. The old checklist
chapter renumbered to part twenty eight.

When you add to it, take the craft frame and leave the dubious history behind. The five elements source
book carries a lot of claims that would damage a filmmaking book's credibility.

---

## 11. STILL OUTSTANDING

1. **The Croatian message to Kristijan.** Written and waiting in `correspondence.md` section 5.1, never sent.
2. **3C.** The prompt is in section 12 below, ready to run.
3. **Scene 4 onward**, three frames each.
4. **Scene 5 is thin.** Pure wind by the elements diagnosis. Fix before boarding it.
4. **The glass thread decision** from Marko.
5. **Rewrite the animation brief** from 25 pages to about 10, under `documents.md` rules.
6. **Rewrite both shot lists** for the nine scene structure.
7. **Rebuild the website** for version four.
8. **Camera work order PDF for Venkatesh.** Lighting, setups, eyelines, take protocol, wardrobe
   continuity, delivery spec.
9. **Animation brief for Kristijan in Croatian.** Note that `scenes/S2.md` already contains a long
   written shot description for him covering the reversal, because the still frames cannot carry it,
   and `scenes/S3.md` carries the four optical cues that make water read as a lens.

---

## 12. THE EXACT NEXT ACTION, READY TO PASTE

**`3C` is blocked and the block is the right one.** Four attempts. Three put the glass in the wrong place
because a hand was holding it, four dropped the glass out of the picture entirely because nothing was.
The missing thing in both is a **sheet**. Objects that carry meaning across scenes are characters and get
sheets, and without one the model has no identity to hold and treats the object as optional furniture.

**So the next action is `GLASS.jpg`, the magnifying glass object sheet, and then `3C` reruns with it
attached.** The reference to generate it from is `assets/REFERENCES/GLASS_SOURCE.jpg`, a crop of the
brass glass out of attempt three. Sheet is 3:2. Overwrite at that filename forever.

After the glass, the queue in `worlds.md` section 7: `DIAL.jpg`, `KEY.jpg`, `LAB.jpg`, `DOOR.jpg`.

**When `3C` reruns**, the composition is in `scenes/S3.md` and the three things that changed at attempt
four are: the leg is an anatomical study with no skin and no hair, with the intact calf over it as a
faint translucent contour, the cap is only the peak breaking the bottom border and not the whole crown,
and nothing is soft. Everything photographic is sharp and throws a directional shadow across the pencil
lines. `worlds.md` explains why that shadow is the most important detail in the film.

---

## 13. THINGS THAT WILL BITE YOU

- The sandbox proxy blocks `github.io`. Verify locally, never by fetching the live URL.
- `web_fetch` only works on URLs already in the conversation or returned by a search.
- The repo is large. Optimise before adding. Web copies at 1600px wide, JPEG quality 88, masters as PNG.
- Marko sometimes pushes files himself with different names than you expect. Always pull and list
  `assets/` before assuming.
- He sends images in chat rather than pushing them. Convert, name them correctly and push them yourself.
- When a frame is approved, store the **full resolution master** and not only the web copy. One frame
  was nearly lost to this.
- He gives feedback fast and bluntly and he is usually right about composition. When he says an image is
  bad, do not defend it, work out which rule it broke and write that rule down.
