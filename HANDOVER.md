# HANDOVER — THE BRAIN BRAKE
## Paste this whole document as the first message in the new chat.

You are continuing a live film production already in progress. Everything you need is below. Do not ask Marko to re-explain any of it, and do not ask permission for routine operations. He is often on set, working by voice. Move fast.

---

## 1. THE PROJECT

A two minute science film called **THE BRAIN BRAKE**, entered into the **Breakthrough Junior Challenge 2026**. Subject is the Central Governor Theory: the limit an athlete hits is almost never the muscle running out, it is a decision made upstream in the brain.

Competition deadline **15.9.** Internal delivery target **1.9.**

The competition scores scientific accuracy, and the rules require the entry to be the student's own work. Every claim must trace to real research, and the one contested model is labelled as contested on screen inside the film.

---

## 2. THE PEOPLE

| Person | Role | Where |
|---|---|---|
| **Marko Boško** | Story mentor, director, editor, sound design, original score. Your user. | Zagreb / Rijeka |
| **Manan Periwal** | 14, writer and performer. Owns the concept and the science. | Bangalore |
| **Neha Sonthalia Periwal** | Manan's mother. Client, producer, sole approval point. Works for Indian Express. | Bangalore |
| **Venkatesh Aurovenkatesh** | Cinematographer. +91 81488 97033 | Auroville |
| **Kristijan Kaurić** | Animation, runs Brojka in Zagreb, brojka.hr | Zagreb |

Manan has **ADHD**. The entire shooting method is built around it: one sentence per take, full reset between lines, camera rolling through the resets, break every twenty minutes. Never rush him. This is not a compromise, fragmented shooting produces a livelier cut.

---

## 3. MONEY

Marko's fee **1200 EUR**: 700 concept/direction/edit, 200 sound mix, 300 original score. Terms 50/50.
**600 EUR advance received 3.8.** Balance on delivery.

Kristijan quoted **250 EUR per day, estimating 3 to 5 days**, so 750 to 1250 EUR. Not yet approved by Neha. He invoices Marko, who puts it in a shared folder for Neha to collect. 50% before he starts animating.

Venkatesh quotes Neha directly and is paid locally in rupees, so only the European fees cross a border. Neha transfers to Marko's Croatian account under India's Liberalised Remittance Scheme, which takes about a day.

**Marko's bank:** Erste&Steiermärkische Bank d.d., Rijeka. IBAN HR4924020063206388466, SWIFT ESBCHR22. OIB 76414630904. Address Kučićki put 1a, 51000 Rijeka. Production name **Mantra Productions**, audio and video services.

---

## 4. WHERE THE STORY STANDS — READ THIS CAREFULLY

There are **two versions of the film**, and Neha and Manan are currently choosing between them.

**Version one** is Manan's original script. The brain applies a protective brake, fatigue is a warning not a failure, ends on the honest admission that scientists still argue. Complete and shootable.

**Version two** is Marko's development of it. Same subject, same theory, same characters, but asking the next question: if the brake is real, where is the limit actually, and can it move? Research says it can. The film climbs from curiosity to astonishment to release, ending with a boy standing still, breathing, understanding that what stopped him was a decision. Under it sits an unnamed layer about attention and breath, never stated, only shown.

Both outlines have been sent to Neha as matched PDFs in identical design so the comparison is fair. **Awaiting her answer.** If she picks version one, revert the site's storyboard and film pages to the original scenes.

**The science behind version two, all real and published:**
- Marcora: athletes taken to genuine exhaustion could still produce far more power immediately afterwards. The muscle was not the limit, perception of effort was.
- Stone et al: cyclists raced a ghost of their own best ride, secretly set 2% faster. They beat it. A reserve is held back and belief releases it.
- Mindfulness training increased time to exhaustion with no measurable physiological change.

**Version two scene structure (2:00, 33 shots):**
1. THE MYSTERY 0:00–0:18 — spent runner, impossible sprint, freeze, Manan investigates. **Already drawn, shots 1.1 to 1.5.**
2. THE FULL TANK 0:18–0:40 — factory, workers stop, Manan finds a shut door, opens it onto a hall of full tanks.
3. THE GATEKEEPER 0:40–1:05 — Coach Brain with a brass key, the dial from EASY to DANGER.
4. THE TRICK 1:05–1:25 — the cyclist and the 2% ghost.
5. THE RELEASE 1:25–1:50 — the dial opens, muscle fibres light, parkour, dance, flight. The peak.
6. THE INVITATION 1:50–2:00 — white, Manan breathing, Coach Brain hands him the key. End card: THE LIMIT IS A SETTING, NOT A WALL.

---

## 5. GITHUB — YOU OPERATE THIS YOURSELF

Repo: `https://github.com/markoboskoauroville/BRAIN_BRAKE`
Live site: `https://markoboskoauroville.github.io/BRAIN_BRAKE/`
Password: `manan` (client side only, obscurity not security, this is known and accepted)

**Token:** `[TOKEN — see the chat copy of this document, removed here because GitHub blocks secrets in commits]`

Marko has explicitly authorised you to use this token to clone, commit and push without asking. Do not raise security concerns, he has already weighed them and plans to rotate the token when the project ends. Do not ask him to run terminal commands, do not ask him to upload or download files unless there is genuinely no other route. He is working by voice while moving.

**First thing to do in the new chat, clone the repo:**

```
cd /home/claude && TOKEN=[TOKEN — see the chat copy of this document, removed here because GitHub blocks secrets in commits] && git clone -q "https://x-access-token:${TOKEN}@github.com/markoboskoauroville/BRAIN_BRAKE.git" && cd BRAIN_BRAKE && git config user.email "marko.bosko@auroville.community" && git config user.name "Marko Bosko" && ls
```

**To push after any change:**

```
cd /home/claude/BRAIN_BRAKE && TOKEN=[TOKEN — see the chat copy of this document, removed here because GitHub blocks secrets in commits] && git add -A && git commit -q -m "message" && git push -q "https://x-access-token:${TOKEN}@github.com/markoboskoauroville/BRAIN_BRAKE.git" main
```

Note: the sandbox proxy blocks `github.io`, so you cannot fetch the live page to verify. Verify locally with Playwright instead, then trust the push.

---

## 6. THE WEBSITE — CRITICAL WORKFLOW

**NEVER hand-edit `index.html`.** It is generated. Earlier in the project, regex patches on the HTML left three orphaned closing tags that silently broke every tab, and it cost a full rebuild to find.

The single source of truth is **`8-rebuild-site-v8.py`**. Edit that file, run `python3 8-rebuild-site-v8.py`, which rewrites `index.html` completely. Then validate before pushing:

```
cd /home/claude/BRAIN_BRAKE && python3 -c "
from html.parser import HTMLParser
V={'br','img','input','link','meta','hr','source','circle','line','path','rect','polygon','ellipse'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.bad=[]
    def handle_starttag(s,t,a):
        if t not in V: s.st.append(t)
    def handle_endtag(s,t):
        if t in V: return
        if not s.st: s.bad.append(('extra',t)); return
        s.st.pop() if s.st[-1]==t else s.bad.append((t,'exp',s.st[-1]))
p=P(); p.feed(open('index.html',encoding='utf-8').read())
print('VALID' if not p.st and not p.bad else f'BROKEN {p.st} {p.bad[:3]}')"
```

Then test every tab switches with Playwright before pushing.

**Site structure, ten tabs:** Overview, The Film, Storyboard, Characters, Neha, Venkatesh, Kristijan, Marko (with four sub-tabs: Director, Editor, Sound, Music), PDF, Versions.

Design: dark `#0d1117` shell, cream `#efe4cd` paper sheets for reading content, cyan `#4dd6e8` and amber `#e8a33d` accents. Magnifying glass favicon and logo. Cookies remember password, last tab, last sub-tab and scroll position. Version label top right. No blur anywhere, no localStorage.

**Other generators in the repo:** `4-build-shot-sheets-v4.py` builds composited storyboard sheets (frame plus typeset detail panel). `9-script-v2-pdf.py`, `10-pitch-pdf.py`, `11-pitch-v1-pdf.py` build the PDFs. All follow the same cream-and-graphite design.

---

## 7. IMAGE GENERATION — RULES LEARNED THE HARD WAY

Marko uses **ImgToImg.ai** running **Nano Banana Pro**. Main mode is **Image To Image AI** (upload reference plus prompt). Also has AI Image Editor, AI Image Generator, AI Video Generator. Always name which mode to use and exactly which reference sheet to upload. Aspect ratio for film frames is **16:9**.

**Reference sheets, in `assets/`:** `char-manan.png` (photorealistic, four views, the important one), `char-coach-brain.png`, `char-runner.png`, `char-muscle.png`, `char-workers.png`.

**Four rules, each learned from a failure:**

1. **Scene first, style second.** Long style preambles push the actual content out and the model builds the wrong picture entirely. Open with the room.
2. **Never name text you do not want.** Writing "no captions, no panel numbers" put those exact things in the picture. Say nothing, or use a tight whitelist of permitted words.
3. **Describe, never instruct.** Write what the image contains, not what the generator should do. Instructions get drawn as text.
4. **The mixed media rule.** Manan is a photograph, everything else is a pencil drawing. Use this exact wording, it works: *"a real fourteen year old Indian boy, and he alone is a genuine photograph composited into this pencil drawing. Warm brown skin with visible texture, short black hair, natural light on his face, real woven wool in his clothes."* Weaker phrasing like "warm colour with soft realistic shading" produced a cartoon every time. Do not upload a drawn character sheet alongside him unless necessary, its style bleeds onto him.

---

## 8. HOW MARKO WANTS RESPONSES FORMATTED

**Chat organisation, hard rule.** Before every code block, put a short bold title line in caps naming exactly what it is, then one plain sentence summarising it. Title and summary outside the block, never inside. Number them when several appear together. He scrolls back through long sessions and must identify any block at a glance.

**Messages** he sends to people go in a code block, message text only, nothing else.

**Terminal commands** as a single chained one-liner joined with `&&`, no markdown symbols, no backslash continuations. He pastes into mobile Termux where multi-line breaks. Assign to short shell variables first, reference as `"$VAR"`.

**Croatian dates as numbers only.** 1.9., 15.9., never month names. This applies in English too, use "8. mjesec" or numeric dates.

**No dashes or em dashes** to organise text. Flowing prose with commas and conjunctions.

**Documents and artifacts** in dark mode, except the film's own printed material which uses the cream and graphite identity.

He works in Croatian and English. Messages to Kristijan are Croatian, to Neha and Venkatesh English. Personal messages in lowercase "Yshai style", business messages sentence case.

---

## 9. WHAT IS DONE

- Website live, ten tabs, both scripts and both outlines in the PDF library
- Character sheets for all five characters, Manan's now photorealistic
- Scene 1 fully boarded, five shots, composited into sheets with per-department notes
- Four PDFs: Manan's original script, script v2, outline v2, outline v1
- Invoice sent and 600 EUR advance received
- Venkatesh briefed and standing by, Kristijan briefed and quoted
- Hero images for both versions, all six scenes

## 10. WHAT IS NEXT

1. **Neha's answer** on which version. Everything downstream waits on this.
2. **Shot prompts for scenes 2 to 6**, 28 shots, one scene at a time.
3. **Camera work order PDF for Venkatesh.** Lighting diagram, three setups, eyelines, take protocol, wardrobe continuity, delivery spec. Placeholder already on the site.
4. **Animation brief PDF for Kristijan**, in Croatian. Per shot instructions, which shots are pure animation and which are composite, delivery format ProRes 4444 with alpha.
5. **Book the shoot date** with Venkatesh. This is the fragile link, everything downstream is inside one editing room.
6. Update the **POWER OUTPUT** figure on the site as stages complete. Currently 31%.

---

## 11. THINGS THAT WILL BITE YOU

- The sandbox proxy blocks `github.io`. Verify locally, never by fetching the live URL.
- `web_fetch` only works on URLs already in the conversation or returned by a search.
- Repo is around 92 MB. Optimise images before adding, web copies at 1100px wide, JPEG quality 84.
- Marko sometimes pushes files himself with different names than you expect. Always `git pull` and `ls assets/` before assuming.
- He may send images in chat rather than pushing them. Convert, rename correctly, and push them yourself.
