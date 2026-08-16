#!/usr/bin/env python3
"""THE BRAIN BRAKE - CAMERA GUIDE - Venkatesh.

Builds from assets/train/frames_v4.json, the single source of truth, so the
shot list can never drift from the film. Everything that is drawn, animated,
composited or spoken by Coach Brain is filtered out. What is left is only the
work that has to happen in front of a camera on the day.

Run 25-lines-manan.py first if frames_v4.json has changed.
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import json, os, sys

sys.path.insert(0, '/home/claude')
from tc import tc, FPS

for n, f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DO','DejaVuSans-Oblique.ttf'),
             ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))
pdfmetrics.registerFont(TTFont('H', '/home/claude/Caveat.ttf'))

W, H = A4
ML, MR = 46, 46
CW = W - ML - MR
PAPER = HexColor("#f2ebda"); INK = HexColor("#2b2822"); SOFT = HexColor("#6f6757")
ACC   = HexColor("#8a6b2e"); RULE = HexColor("#c9bfa4"); LIVE = HexColor("#8a3b2e")
BOX   = HexColor("#e6dcc4"); GO = HexColor("#3d6b4a")

IMG = "/home/claude/train/img"
REPO = os.path.dirname(os.path.abspath(__file__))
OUT = "/home/claude/out/THE BRAIN BRAKE - CAMERA GUIDE - Venkatesh.pdf"
os.makedirs("/home/claude/out", exist_ok=True)

VERSION = "version one"

c = canvas.Canvas(OUT, pagesize=A4)
pg = [0]

def bg():
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)

def foot():
    pg[0] += 1
    c.setFont('M', 7); c.setFillColor(SOFT)
    c.drawString(ML, 28, "THE BRAIN BRAKE  \u00b7  camera guide  \u00b7  %s  \u00b7  Venkatesh" % VERSION)
    c.drawRightString(W - MR, 28, str(pg[0]))

def newpage():
    foot(); c.showPage(); bg()

def wrap(t, f, s, mw):
    out, line = [], ""
    for w in t.split():
        trial = (line + " " + w).strip()
        if pdfmetrics.stringWidth(trial, f, s) <= mw:
            line = trial
        else:
            if line: out.append(line)
            line = w
    if line: out.append(line)
    return out

def para(x, y, t, f, s, lead, mw):
    c.setFont(f, s); c.setFillColor(INK)
    for ln in wrap(t, f, s, mw):
        c.drawString(x, y, ln); y -= lead
    return y

def img(fn, y, maxh, w=None):
    p = os.path.join(IMG, fn)
    if not os.path.exists(p):
        c.setFillColor(BOX); c.rect(ML, y - maxh, CW, maxh, fill=1, stroke=0)
        c.setStrokeColor(RULE); c.setDash(3, 3); c.rect(ML, y - maxh, CW, maxh, fill=0, stroke=1)
        c.setDash()
        c.setFont('MB', 8); c.setFillColor(LIVE)
        c.drawCentredString(W / 2, y - maxh / 2 - 3, "NO PLATE YET  \u00b7  THIS FRAME IS SHOT ON THE DAY")
        return y - maxh - 10
    im = Image.open(p); iw, ih = im.size
    ww = w or CW
    hh = ww * ih / iw
    if hh > maxh:
        hh = maxh; ww = hh * iw / ih
    x = ML + (CW - ww) / 2
    c.drawImage(ImageReader(p), x, y - hh, ww, hh, mask='auto')
    c.setStrokeColor(RULE); c.setLineWidth(0.7); c.rect(x, y - hh, ww, hh, fill=0, stroke=1)
    return y - hh - 10

# ---------------------------------------------------------------- the setups
SETUPS = {
 "A": ("TO CAMERA",
       "Manan against plain mid grey, medium, lens at his eye height, key from camera left. "
       "This is the setup the film lives in. He speaks straight down the lens. Nothing else is "
       "in shot and nothing moves behind him.",
       ["Mid grey seamless, lit evenly, no gradient and no hot spot.",
        "Key camera left, soft, slightly above eye line. Never relight between frames in this setup.",
        "Frame him with clear space above the hair. He gets cut out and placed inside drawings, "
        "so anything touching the edge cannot be used.",
        "One sentence per take. Reset fully between lines.",
        "Keep rolling through the resets. The unguarded moment between takes is often the one we cut."]),
 "B": ("THE BLACKBOARD",
       "A real blackboard, real chalk, and Manan actually writing. Everything that appears written "
       "is added later in Zagreb, but his hand and arm must genuinely move, so the chalk sound and "
       "the arm passing in front of the writing are real.",
       ["THE BOARD IS SHOT COMPLETELY EMPTY except for one vertical chalk line down the middle.",
        "He writes with real chalk on the empty board. It does not matter what he writes.",
        "Give us a clean pass of the empty board first, locked off, no Manan, five seconds.",
        "Same lighting as setup A if the room allows it."]),
 "C": ("SILENT PLATES",
       "No lines. These are the pictures between the words, and the film breathes on them. Each one "
       "is on screen for well under half a second, so what matters is that they are clean and still, "
       "not that they are performed.",
       ["Shoot each one much longer than we need. We take the stillest part.",
        "No performance at all. He is not acting in these, he is simply there.",
        "Same grey, same key, same distance unless the note says otherwise."]),
 "D": ("THE MAGNIFYING GLASS",
       "The brass glass is the film's transition. Twice the picture goes through it into the next "
       "scene, so the glass has to be real, in his hand, and in focus.",
       ["Insert of the glass held up, the circle of the lens filling as much of frame as it can.",
        "Hold it steady for a slow count of five. We push in on it later.",
        "One pass with his eye visible through the glass, one pass with the lens empty."]),
}

# frame id -> (setup, what the camera does)
CAM = {
 "1.5": ("A", "He walks into frame from camera right, stops, and looks off. Half a second on screen. "
              "Shoot the walk in six or seven times and let him arrive differently each time."),
 "1.6": ("A", "The first time he speaks to us. Straight to lens, glass at chest height. He has just "
              "seen something impossible and he is asking us about it, not telling us. Shoot past the "
              "point where it feels finished. Take six is usually the one."),
 "2.1": ("B", "He writes on the empty board and says the name and the year over it. His arm must pass "
              "in front of where the writing will be. Do not worry about what he writes."),
 "2.3": ("D", "Insert. The glass raised, lens filling frame. We travel through it into the next scene, "
              "so hold it long and hold it steady."),
 "2.6": ("A", "Over his shoulder, looking back at the board. Voice only, he is not to camera here, so "
              "his face can be three quarters. Shoot it also as a clean profile."),
 "3.2": ("C", "He looks at something low and to camera left that is not there. Give him a mark. "
              "Curious, not worried."),
 "3.3": ("C", "His hand reaching forward, palm open, at chest height. The door is drawn in later. "
              "Shoot the hand alone as an insert too."),
 "3.4": ("C", "Wide, him small in frame, looking up and around at nothing. He is standing in an "
              "enormous room that does not exist yet. Give him time to actually look."),
 "3.6": ("A", "To camera. This is the end of the mystery and the start of the argument. Certain, "
              "quiet, no push."),
 "4.2": ("A", "To camera, level, an accusation that is not angry. He has just worked out who is "
              "responsible and he is almost pleased about it."),
 "4.4b": ("A", "NEW. Same setup and same eye line as 4.2, one step closer. He is not accusing any "
               "more, he is working it out, and he is impressed without wanting to show it. "
               "A small pause before the word secretly."),
 "4.5": ("C", "Voice only over a picture of him. Him looking down at his own hand as though holding "
              "a phone, but with nothing in it. Shoot the empty hand clean."),
 "4.7": ("A", "To camera. He names the theory. A subtitle goes under this later, so leave the lower "
              "quarter of frame uncluttered."),
 "4.8": ("A", "NEW, AND IMPORTANT. Shoot this as one continuous take with 4.7, on the same breath. "
              "We cut it into two panels afterwards. This is the only sentence in the film that "
              "states the science plainly, so it is slow, still, and straight down the lens. "
              "A clear beat before and keeps something in reserve."),
 "5.4": ("C", "Close, his face as an idea lands. No line. Shoot a long unbroken take of him simply "
              "thinking and we will find the moment."),
 "5.5": ("C", "Voice only. Him from behind or three quarters, about to start something."),
 "5.6": ("C", "Movement. Him running on the spot or leaning into a stride against the grey. "
              "Shoot high frame rate if the camera allows it."),
 "5.7": ("C", "The hardest moment. Effort, not pain. He is working, not suffering."),
 "5.8": ("C", "Eyes closed, completely still, breathing. Shoot a full unbroken minute and we will "
              "use the stillest twenty frames. No performance at all."),
 "5.9": ("A", "Eyes open, to camera. The quietest line in the film and the one the whole experiment "
              "is for. Do not let him push it."),
 "7.3": ("C", "Him against white, small, still. A breath between two scenes."),
 "8.1": ("C", "Breathing, eyes closed, calm. Same as 5.8 but at the end of the film rather than the "
              "middle. Shoot it separately so the two do not match too exactly."),
 "8.3": ("C", "His hand, raised, closing around something that is not there. The lever is drawn in "
              "later. Insert, and shoot it twice at two heights."),
 "8.6": ("A", "The first line of the ending. He is already looking at us before he speaks. He is "
              "setting something up and he knows it, so the line does not finish. Leave it open."),
 "8.7": ("A", "The turn. Gentle, not a telling off. Everyone gets this wrong including him at the "
              "start of the film."),
 "8.8": ("A", "The last thing he says on camera in the whole film. Completely still, dead to lens, "
              "no movement at all. Let the last take be the tired one. It will be the best."),
}

BOOTH_NOTE = ("8.9 is the end card. It is voice only, recorded separately in a quiet room, and needs "
              "nothing from the camera. If there is a quiet corner on the day we will take it there, "
              "otherwise it happens later.")

# ---------------------------------------------------------------- build
frames = json.load(open(os.path.join(REPO, 'assets/train/frames_v4.json')))
live = [f for f in frames if f['layer'] == 'LIVE']
total = sum(f['fr'] for f in frames)

bg()

# ---- cover
c.setFillColor(HexColor("#171512")); c.rect(0, H - 250, W, 250, fill=1, stroke=0)
c.setFont('DB', 27); c.setFillColor(PAPER)
c.drawString(ML, H - 96, "THE BRAIN BRAKE")
c.setFont('D', 13); c.setFillColor(HexColor("#9b9080"))
c.drawString(ML, H - 120, "camera guide  \u00b7  everything that happens in front of a lens")
c.setFont('MB', 9); c.setFillColor(HexColor("#c9bfa4"))
c.drawString(ML, H - 168, "FOR VENKATESH")
c.drawString(ML, H - 182, "SHOOTING DAY  \u00b7  TUESDAY 18 AUGUST 2026  \u00b7  BENGALURU")
c.drawString(ML, H - 196, "%s  \u00b7  built from the film, not typed by hand" % VERSION)

y = H - 300
c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "THE ONE THING TO UNDERSTAND"); y -= 16
y = para(ML, y,
    "You are not filming a film. You are filming a boy in an empty grey room, talking to a lens, "
    "reacting to things that do not exist yet. The runner, the factory, the mission control room, "
    "Coach Brain and every drawn world in this story are made in Zagreb afterwards and built around "
    "him.", 'D', 10.6, 14.6, CW)
y -= 8
y = para(ML, y,
    "So the job is to hand over a clean, consistent, evenly lit boy who can be cut out and placed "
    "anywhere. Consistency beats beauty on this one. A gorgeous take we cannot cut out is worth "
    "nothing, and a plain take we can is worth everything.", 'D', 10.6, 14.6, CW)
y -= 20

c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "THE DAY, IN NUMBERS"); y -= 14
stats = [("Frames in the finished film", str(len(frames))),
         ("Frames that need you", str(len(live))),
         ("Frames with a line to camera", str(len([f for f in live if f['mode'] == 'CAM']))),
         ("Camera setups", "4"),
         ("Cast", "Manan only"),
         ("Finished running time", "1:57"),
         ]
for k, v in stats:
    c.setFont('D', 10); c.setFillColor(SOFT); c.drawString(ML, y, k)
    c.setFont('DB', 10); c.setFillColor(INK); c.drawRightString(ML + 300, y, v)
    y -= 15
y -= 10

c.setFillColor(BOX); c.rect(ML, y - 74, CW, 74, fill=1, stroke=0)
c.setStrokeColor(ACC); c.setLineWidth(2.4); c.line(ML, y - 74, ML, y)
c.setFont('MB', 7); c.setFillColor(ACC); c.drawString(ML + 16, y - 17, "TECHNICAL")
c.setFont('M', 8.6); c.setFillColor(INK)
for i, ln in enumerate(["4K, 25 fps, 16:9, no in camera sharpening",
                        "Original camera files, untouched. No transcode, no grade.",
                        "Separate audio with the slate intact. His voice is the film.",
                        "Photograph the wardrobe and each lighting setup before you strike them."]):
    c.drawString(ML + 16, y - 31 - i * 11, "\u00b7  " + ln)
y -= 92

newpage()

# ---- working with Manan
y = H - 70
c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "WORKING WITH MANAN"); y -= 8
c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML, y, W - MR, y); y -= 24
y = para(ML, y,
    "Manan is fourteen and he has ADHD. The whole shooting method is built around that, and it "
    "happens to produce a better film anyway.", 'D', 10.6, 14.6, CW)
y -= 14
for t in ["One sentence per take. Never ask him to run a paragraph.",
          "Let the camera roll through the resets. The moment between takes is often the take.",
          "No counting down and no pressure language. Roll, and let him go when he is ready.",
          "Break every twenty minutes. A tired take is a wasted card.",
          "Shoot past the point where it feels finished. Take six is usually the one.",
          "He has rehearsed from a book that gives him one line per page. If you ask for a line by "
          "its number, he will know exactly which one you mean."]:
    c.setFont('DB', 10); c.setFillColor(ACC); c.drawString(ML, y, "\u00b7")
    y = para(ML + 14, y, t, 'D', 10.4, 14, CW - 14) - 6
y -= 12

c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "THE FOUR SETUPS"); y -= 8
c.setStrokeColor(RULE); c.line(ML, y, W - MR, y); y -= 22
for k in "ABCD":
    name, blurb, notes = SETUPS[k]
    ids = [f['id'] for f in live if CAM.get(f['id'], ("", ""))[0] == k]
    c.setFont('DB', 13); c.setFillColor(LIVE); c.drawString(ML, y, "SETUP %s   %s" % (k, name)); y -= 15
    c.setFont('M', 7.6); c.setFillColor(SOFT)
    c.drawString(ML, y, "%d frames   \u00b7   %s" % (len(ids), "  ".join(ids))); y -= 14
    y = para(ML, y, blurb, 'D', 10, 13.4, CW) - 6
    for n in notes:
        c.setFont('DB', 9); c.setFillColor(ACC); c.drawString(ML + 6, y, "\u00b7")
        y = para(ML + 18, y, n, 'D', 9.4, 12.6, CW - 18) - 3
    y -= 16
    if y < 130:
        newpage(); y = H - 70

newpage()

# ---- the shot list, one page per frame
y = H - 70
c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "THE SHOTS, IN ORDER"); y -= 8
c.setStrokeColor(RULE); c.line(ML, y, W - MR, y); y -= 22
y = para(ML, y,
    "In film order, which is not shooting order. Group them by setup on the day and shoot whatever "
    "is lit. Each page carries the timecode it lands on in the finished film, how long it is on "
    "screen, the words he says over it if any, and what the camera has to do. The picture is a "
    "reference for framing and mood. It is not a photograph of anything real, it was drawn to show "
    "you the intention.", 'D', 10, 13.4, CW)
newpage()

for i, f in enumerate(live):
    setup, note = CAM.get(f['id'], ("C", "Plate. Clean and still."))
    y = H - 66
    c.setFont('MB', 8); c.setFillColor(ACC)
    c.drawString(ML, y, "SHOT %d OF %d   \u00b7   FRAME %s   \u00b7   SETUP %s   \u00b7   %s"
                 % (i + 1, len(live), f['id'], setup, SETUPS[setup][0]))
    c.setFont('M', 7.6); c.setFillColor(SOFT)
    c.drawRightString(W - MR, y, "SCENE %d" % f['scene'])
    y -= 8
    c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML, y, W - MR, y); y -= 18

    secs = f['fr'] / float(FPS)
    c.setFont('M', 8.4); c.setFillColor(INK)
    c.drawString(ML, y, "%s  \u2192  %s" % (tc(f['in'] / float(FPS)), tc(f['out'] / float(FPS))))
    c.drawRightString(W - MR, y, "%d frames   \u00b7   %.1f seconds on screen" % (f['fr'], secs))
    y -= 20

    if f['text'].strip():
        body = wrap("\u201c" + f['text'] + "\u201d", 'DB', 15, CW - 36)
        bh = 26 + len(body) * 20 + 14
        c.setFillColor(BOX); c.rect(ML, y - bh, CW, bh, fill=1, stroke=0)
        c.setStrokeColor(ACC); c.setLineWidth(2.4); c.line(ML, y - bh, ML, y)
        c.setFont('MB', 6.8); c.setFillColor(ACC)
        c.drawString(ML + 18, y - 17,
                     "HE SAYS THIS" + ("   \u00b7   TO CAMERA" if f['mode'] == 'CAM'
                                       else "   \u00b7   VOICE OVER, HIS FACE NEED NOT BE TO LENS"))
        c.setFont('DB', 15); c.setFillColor(INK)
        yy = y - 30 - 13
        for ln in body:
            c.drawString(ML + 18, yy, ln); yy -= 20
        y = y - bh - 16
    else:
        c.setFillColor(BOX); c.rect(ML, y - 30, CW, 30, fill=1, stroke=0)
        c.setStrokeColor(RULE); c.setLineWidth(0.8); c.rect(ML, y - 30, CW, 30, fill=0, stroke=1)
        c.setFont('MB', 8); c.setFillColor(SOFT)
        c.drawString(ML + 18, y - 19, "NO LINE.  PICTURE ONLY.")
        y -= 46

    y = img(f['img'], y, 230)
    y -= 8

    c.setFont('MB', 7); c.setFillColor(ACC); c.drawString(ML, y, "CAMERA"); y -= 12
    y = para(ML, y, note, 'D', 10.4, 14, CW)
    y -= 10

    if f['trans'].strip():
        c.setFont('MB', 7); c.setFillColor(SOFT); c.drawString(ML, y, "WHAT HAPPENS TO THIS FRAME AFTERWARDS"); y -= 11
        c.setFont('DO', 9.2); c.setFillColor(SOFT)
        for ln in wrap(f['trans'], 'DO', 9.2, CW):
            c.drawString(ML, y, ln); y -= 12
    newpage()

# ---- closing page
y = H - 70
c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "THE VOICE, AND WHAT WE NEED BACK"); y -= 8
c.setStrokeColor(RULE); c.line(ML, y, W - MR, y); y -= 24
y = para(ML, y, BOOTH_NOTE, 'D', 10.6, 14.6, CW); y -= 16
y = para(ML, y,
    "Every word Manan speaks in this film is his own voice. Nothing he says is replaced later, so "
    "the sound you record is the sound in the finished film. If a take sounds right and looks wrong, "
    "keep it anyway and tell us.", 'D', 10.6, 14.6, CW)
y -= 24

c.setFont('MB', 8); c.setFillColor(ACC); c.drawString(ML, y, "DELIVERY"); y -= 14
for t in ["Original camera files, untouched.",
          "Separate audio files, slate intact.",
          "A photograph of the wardrobe and of each lighting setup.",
          "Upload within 48 hours. The whole Zagreb schedule starts the moment they land."]:
    c.setFont('DB', 10); c.setFillColor(ACC); c.drawString(ML, y, "\u00b7")
    y = para(ML + 14, y, t, 'D', 10.4, 14, CW - 14) - 5
y -= 20

c.setFillColor(BOX); c.rect(ML, y - 60, CW, 60, fill=1, stroke=0)
c.setStrokeColor(GO); c.setLineWidth(2.4); c.line(ML, y - 60, ML, y)
c.setFont('MB', 7); c.setFillColor(GO); c.drawString(ML + 16, y - 17, "IF IN DOUBT")
para(ML + 16, y - 32, "Shoot it wider and shoot it longer. We can crop and we can trim. We cannot "
                      "invent what is outside the frame.", 'DB', 10, 13, CW - 32)

foot(); c.showPage(); c.save()
print("written %s  pages %d  live frames %d  runtime %s" % (OUT, pg[0], len(live), tc(total / float(FPS))))
