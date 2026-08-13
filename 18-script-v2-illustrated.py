from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import sys, os
sys.path.insert(0, '/home/claude')
from shrink import small

for n, f in [('D', 'DejaVuSans.ttf'), ('DB', 'DejaVuSans-Bold.ttf'), ('DO', 'DejaVuSans-Oblique.ttf'),
             ('M', 'DejaVuSansMono.ttf'), ('MB', 'DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))

W, H = A4
ML, MR = 56, 56
CW = W - ML - MR
PAPER = HexColor("#f2ebda")
INK = HexColor("#2b2822")
SOFT = HexColor("#6f6757")
ACC = HexColor("#8a6b2e")
RULE = HexColor("#c9bfa4")
A = "/home/claude/BRAIN_BRAKE/assets"

c = canvas.Canvas("/home/claude/out/13 - script v2 illustrated.pdf", pagesize=A4)
page = [0]


def bg():
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def foot():
    page[0] += 1
    c.setFont('M', 7)
    c.setFillColor(SOFT)
    c.drawString(ML, 30, "THE BRAIN BRAKE  ·  script v2  ·  Manan Periwal & Marko Boško")
    c.drawRightString(W - MR, 30, str(page[0]))


def newpage():
    foot()
    c.showPage()
    bg()


def wrap(t, f, s, mw):
    o = []
    for p in t.split("\n"):
        words = p.split()
        if not words:
            o.append("")
            continue
        l = words[0]
        for x in words[1:]:
            if pdfmetrics.stringWidth(l + " " + x, f, s) <= mw:
                l += " " + x
            else:
                o.append(l)
                l = x
        o.append(l)
    return o


def para(x, y, t, f='D', s=9.6, lead=13.4, mw=CW, col=INK):
    c.setFont(f, s)
    c.setFillColor(col)
    for ln in wrap(t, f, s, mw):
        c.drawString(x, y, ln)
        y -= lead
    return y


def image(path, y, maxh=340):
    p = small(os.path.join(A, path), 1500)
    im = Image.open(p)
    ar = im.size[0] / im.size[1]
    iw = CW
    ih = iw / ar
    if ih > maxh:
        ih = maxh
        iw = ih * ar
    c.drawImage(ImageReader(p), ML + (CW - iw) / 2, y - ih, iw, ih, mask=None)
    return y - ih - 16


def speech(x, y, who, line):
    c.setFont('MB', 8)
    c.setFillColor(ACC)
    c.drawString(x + 40, y, who)
    y -= 12
    y = para(x + 40, y, line, 'D', 9.6, 13.4, CW - 80)
    return y - 6


bg()

# ---------------------------------------------------------------- title
y = H - 120
c.setFont('DB', 32)
c.setFillColor(INK)
c.drawString(ML, y, "THE BRAIN BRAKE")
y -= 26
c.setFont('DO', 13)
c.setFillColor(ACC)
c.drawString(ML, y, "The limit is a setting, not a wall.")
y -= 40
c.setStrokeColor(RULE)
c.setLineWidth(0.8)
c.line(ML, y, W - MR, y)
y -= 24
for k, v in [("Running time", "2:00"),
             ("Format", "16:9, live action composited into hand drawn animation"),
             ("Entry", "Breakthrough Junior Challenge 2026"),
             ("Draft", "Version 2, illustrated")]:
    c.setFont('MB', 7.6)
    c.setFillColor(SOFT)
    c.drawString(ML, y, k.upper())
    c.setFont('D', 9.6)
    c.setFillColor(INK)
    c.drawString(ML + 92, y, v)
    y -= 16
y -= 20
c.setFont('MB', 8)
c.setFillColor(ACC)
c.drawString(ML, y, "WRITTEN BY")
y -= 18
c.setFont('DB', 11)
c.setFillColor(INK)
c.drawString(ML, y, "Manan Periwal")
c.setFont('D', 9.4)
c.setFillColor(SOFT)
c.drawString(ML + 130, y, "Concept, science and story")
y -= 18
c.setFont('DB', 11)
c.setFillColor(INK)
c.drawString(ML, y, "Marko Boško")
c.setFont('D', 9.4)
c.setFillColor(SOFT)
c.drawString(ML + 130, y, "Story mentor and direction")
y -= 34
y = para(ML, y,
         "This draft is a collaboration. The concept, the science and the choice of subject are Manan's, "
         "taken from his first draft. The change in this version is the shape of the story rather than "
         "its substance.")
y -= 10
y = para(ML, y,
         "Draft one explained a mechanism: the brain applies a brake to protect the body. Accurate, and "
         "it ended in a closed case. This draft asks a different question. If the brake exists, where is "
         "the limit really, and can it move? The research says it can, and that turns an explanation into "
         "a discovery.")
y -= 10
y = para(ML, y,
         "The film now rises rather than settles. Curiosity, then astonishment, then release. It ends "
         "with a boy breathing calmly, understanding that what stopped him was a decision, and that "
         "decisions can be trained.")
newpage()

# ---------------------------------------------------------------- spine
y = H - 84
c.setFont('DB', 20)
c.setFillColor(INK)
c.drawString(ML, y, "The spine")
y -= 12
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 26
y = para(ML, y,
         "A runner with nothing left produces an impossible sprint. A boy goes looking for where it came "
         "from. He expects to find an empty tank. He finds a full one, and a door that somebody closed on "
         "purpose.", 'DO', 11, 15)
y -= 22
y = para(ML, y, "The three findings the film is built on. Each one is real, published, and stranger "
                "than the explanation it replaces.", 'DB', 9.6)
y -= 14
for n, t in [("One", "Athletes taken to genuine exhaustion were tested immediately afterwards and could "
                     "still produce far more power than they had just produced. The muscle was not the "
                     "thing that stopped them."),
             ("Two", "Cyclists raced a ghost of their own best ride. The ghost was secretly set two "
                     "percent faster. They beat it. A reserve is held back, and it is released by the "
                     "belief that the effort is sustainable."),
             ("Three", "Mindfulness training increased how long athletes could keep going, with no "
                       "measurable change in the body. What changed was how hard it felt.")]:
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML, y, n.upper())
    y = para(ML + 52, y, t, 'D', 9.6, 13.4, CW - 52)
    y -= 12
y -= 8
y = para(ML, y, "So the sentence at the centre of the film is this. The wall is real. But somebody set "
                "it, and settings can move.", 'DB', 10.5, 14.6)
y -= 16
y = para(ML, y,
         "Underneath, unnamed and never argued, sits an older idea: that attention and breath are the "
         "instruments by which a person meets their own limits. The film does not say this. It shows a "
         "boy going still, and then flying. The audience can take from that whatever they already carry.",
         'D', 9.6, 13.4, CW, SOFT)
newpage()

# ---------------------------------------------------------------- cast
y = H - 84
c.setFont('DB', 20)
c.setFillColor(INK)
c.drawString(ML, y, "The cast")
y -= 12
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 24
cast = [("sb/char-manan.jpg", "MANAN, boy detective. Deerstalker cap, caped coat, brass magnifying glass."),
        ("sb/char-coach-brain.jpg", "COACH BRAIN. Tracksuit, whistle, coffee, and a small key on a chain."),
        ("sb/char-runner.jpg", "THE MARATHON RUNNER. Number 27."),
        ("sb/char-muscle.jpg", "THE MUSCLE. Proud, stubborn, two and a half heads."),
        ("sb/char-workers.jpg", "THE FACTORY WORKERS. Overalls, hard hats, crates.")]
for i, (img, cap) in enumerate(cast):
    if y < 210:
        newpage()
        y = H - 84
    y = image(img, y, 200)
    y = para(ML, y, cap, 'D', 8.8, 12, CW, SOFT)
    y -= 18
newpage()

# ---------------------------------------------------------------- the film
y = H - 84
c.setFont('DB', 22)
c.setFillColor(INK)
c.drawString(ML, y, "The film")
y -= 12
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
newpage()

SCENES = [
 ("SCENE 1", "THE MYSTERY", "0:00 – 0:18", "EXT. MARATHON COURSE, DAY. ANIMATION.",
  ["HERO_V3/HERO_V3_1_web.jpg"],
  [("A lean runner is failing on an open road. Head rolling, arms hanging, stride collapsed to a shuffle. "
    "He is beaten and everyone watching knows it.", None, None),
   (None, "COMMENTATOR (V.O.)", "He's got nothing left."),
   ("He explodes into a sprint. The world freezes around him, speed lines suspended in the air. MANAN "
    "walks into the frozen frame, magnifying glass raised. Through the lens: a footprint, a stopwatch. "
    "He lowers the glass and turns to camera.", None, None),
   (None, "MANAN", "Hold on. He had nothing left. So where did THAT come from?"),
   ("Question marks bloom around him. TITLE: THE BRAIN BRAKE.", None, None)]),

 ("SCENE 2", "THE FULL TANK", "0:18 – 0:40", "INT. THE MUSCLE FACTORY. ANIMATION WITH MANAN COMPOSITED.",
  ["HERO_V3/HERO_V3_2_web.jpg", "HERO_V3/HERO_V3_3_web.jpg"],
  [("Inside the leg, a working factory. Gears turning where the calf would be, conveyors, tiny workers "
    "hauling crates. Manan walks through it, unhurried, the only calm figure in the room.", None, None),
   (None, "MANAN (V.O.)", "For a hundred years we blamed the muscles. Ran out of fuel. Ran out of air. "
                          "Simple."),
   ("The machines slow. A worker wipes his brow and shrugs: that's it, we're done. But Manan has stopped. "
    "At the back of the factory there is a door, and it is shut.", None, None),
   (None, "MANAN (V.O.)", "Except when scientists tested runners the moment they gave up, the muscles "
                          "could still do far more."),
   ("He pushes the door. It opens onto an enormous hall of storage tanks, and every one of them is full. "
    "Light floods his face.", None, None),
   (None, "MANAN", "It was never empty.")]),

 ("SCENE 3", "THE GATEKEEPER", "0:40 – 1:05", "INT. MISSION CONTROL. ANIMATION WITH MANAN COMPOSITED.",
  ["HERO_V3/HERO_V3_4_web.jpg"],
  [("A warm, glowing room of monitors. A chair turns. COACH BRAIN, tracksuit, whistle, coffee, and a "
    "small brass key on a chain around his neck. He is delighted to be found.", None, None),
   (None, "MANAN", "You closed that door."),
   (None, "COACH BRAIN", "I keep the key."),
   ("He gestures and the room lights up. Glowing lines run out to a heart, lungs, a thermometer, a water "
    "drop, a distance counter, all feeding back to a single dial marked from EASY to DANGER.", None, None),
   (None, "COACH BRAIN", "Every heartbeat. Every breath. Every drop of sweat. I'm asking one question. "
                         "Can we keep going safely?"),
   (None, "MANAN", "So the limit isn't my body. It's your guess."),
   ("Coach Brain grins, entirely unembarrassed.", None, None),
   (None, "COACH BRAIN", "It's my best guess. And I'd rather you finish than break."),
   ("SUBTITLE, two seconds: One influential model, the Central Governor Theory, proposed by Prof. Tim "
    "Noakes, 1997. Scientists still debate exactly how brain and muscle share the work.", None, None)]),

 ("SCENE 4", "THE TRICK", "1:05 – 1:25", "INT. SPORTS LABORATORY. ANIMATION.",
  ["HERO_V3/HERO_V3_5_web.jpg"],
  [("A cyclist on a stationary bike, screen in front of him showing a translucent ghost rider. He has "
    "been told the ghost is a recording of his own best ever ride.", None, None),
   (None, "MANAN (V.O.)", "So scientists tried something cheeky. They let a cyclist race himself."),
   ("Behind glass, a researcher quietly turns a small dial. On her screen: +2%.", None, None),
   (None, "MANAN (V.O.)", "Except they made the ghost slightly faster. And they didn't tell him."),
   ("The cyclist chases. Strains. Draws level. Passes. The ghost falls behind.", None, None),
   (None, "MANAN (V.O.)", "He beat his own maximum. Which means it was never his maximum."),
   ("Manan turns to camera, delighted.", None, None),
   (None, "MANAN", "Change what the brain believes, and the door opens.")]),

 ("SCENE 5", "THE RELEASE", "1:25 – 1:50", "EXT. EVERYWHERE. ANIMATION. THE PEAK OF THE FILM.",
  ["HERO_V3/HERO_V3_6_web.jpg", "HERO_V3/HERO_V3_7_web.jpg"],
  [("Coach Brain looks at his dial, then at Manan. He smiles, and eases it open.", None, None),
   ("Inside the runner's legs, muscle fibres light one after another, more and more of them. His stride "
    "opens. He flies. Speed lines. The crowd erupts.", None, None),
   ("And the film breaks loose. A traceur launching rooftop to rooftop. A dancer turning in the air. A "
    "swimmer leaving the wall. Bodies doing what they could always do, permitted at last. All of it "
    "rising.", None, None),
   (None, "MANAN (V.O.)", "The brain didn't make new energy. It gave permission."),
   ("Manan himself, mid air, coat flying, laughing.", None, None),
   ("CAPTION: More muscle fibres recruited. Notice: still not maximum.", None, None)]),

 ("SCENE 6", "THE INVITATION", "1:50 – 2:00", "EVERYTHING SETTLES TO WHITE. MANAN ALONE. LIVE ACTION.",
  ["HERO_V3/HERO_V3_8_web.jpg"],
  [("The motion drains away. Manan stands still, eyes closed, breathing. Calm. The dial hangs in the air "
    "beside him, and this time his own hand is on it.", None, None),
   (None, "MANAN", "The wall is real. But somebody set it."),
   (None, "MANAN", "And what your brain believes is safe can be trained."),
   ("Coach Brain steps up, takes the key from around his neck, and hands it over. A small, warm moment. "
    "Manan opens his eyes.", None, None),
   ("Cut to black.", None, None)]),
]

for num, title, timing, slug, imgs, beats in SCENES:
    y = H - 80
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML, y + 20, "%s   ·   %s" % (num, timing))
    c.setFont('DB', 21)
    c.setFillColor(INK)
    c.drawString(ML, y, title)
    y -= 14
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(ML, y, W - MR, y)
    y -= 16
    c.setFont('M', 7.6)
    c.setFillColor(SOFT)
    c.drawString(ML, y, slug)
    y -= 20

    y = image(imgs[0], y, 300)
    y -= 6

    for txt, who, line in beats:
        need = 60
        if y < need:
            newpage()
            y = H - 80
        if who:
            y = speech(ML, y, who, line)
        else:
            y = para(ML, y, txt)
            y -= 8

    for extra in imgs[1:]:
        if y < 240:
            newpage()
            y = H - 80
        y = image(extra, y, 300)
        y -= 6
    newpage()

# ---------------------------------------------------------------- shot breakdown scene 1
y = H - 84
c.setFont('DB', 20)
c.setFillColor(INK)
c.drawString(ML, y, "Scene 1, shot breakdown")
y -= 12
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 24
for i in range(1, 6):
    if y < 250:
        newpage()
        y = H - 84
    y = image("shots/SH1_%d.jpg" % i, y, 300)
    y -= 10
newpage()

# ---------------------------------------------------------------- end card
y = H / 2 + 40
c.setFont('MB', 8)
c.setFillColor(ACC)
c.drawCentredString(W / 2, y + 30, "END CARD")
c.setFont('DB', 18)
c.setFillColor(INK)
c.drawCentredString(W / 2, y, "THE LIMIT IS A SETTING, NOT A WALL.")
foot()
c.showPage()
c.save()
print("done", os.path.getsize("/home/claude/out/13 - script v2 illustrated.pdf"))
