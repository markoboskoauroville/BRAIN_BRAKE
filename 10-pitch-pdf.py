from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import os

for n, f in [('D', 'DejaVuSans.ttf'), ('DB', 'DejaVuSans-Bold.ttf'),
             ('DO', 'DejaVuSans-Oblique.ttf'), ('M', 'DejaVuSansMono.ttf'),
             ('MB', 'DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))

W, H = A4
ML, MR = 52, 52
PAPER = HexColor("#f2ebda")
INK = HexColor("#2b2822")
SOFT = HexColor("#6f6757")
ACC = HexColor("#8a6b2e")
RULE = HexColor("#c9bfa4")

OUT = "assets/pdf/2-THE-BRAIN-BRAKE-v2-FIRST-JOINT-DRAFT.pdf"
os.makedirs("build", exist_ok=True)
c = canvas.Canvas(OUT, pagesize=A4)
page = [0]


def prep(src, key, maxw=2000):
    """downscale for a light pdf"""
    p = f"build/{key}.jpg"
    im = Image.open(src).convert("RGB")
    if im.size[0] > maxw:
        im = im.resize((maxw, int(maxw * im.size[1] / im.size[0])), Image.LANCZOS)
    im.save(p, "JPEG", quality=86, optimize=True)
    return p


def bg():
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def foot(txt=""):
    c.setFont('M', 7.5)
    c.setFillColor(SOFT)
    c.drawString(ML, 30, "THE BRAIN BRAKE   ·   version two   ·   Manan Periwal & Marko Boško")
    if txt:
        c.drawCentredString(W / 2, 30, txt)
    c.drawRightString(W - MR, 30, str(page[0]))


def newpage():
    if page[0]:
        foot()
        c.showPage()
    page[0] += 1
    bg()


def wrap(t, font, size, width):
    words, lines, cur = t.split(), [], ''
    for w in words:
        s = (cur + ' ' + w).strip()
        if pdfmetrics.stringWidth(s, font, size) <= width:
            cur = s
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(t, y, font='D', size=11, lead=16.5, color=INK, x=ML, width=None):
    width = width or (W - ML - MR)
    for ln in wrap(t, font, size, width):
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawString(x, y, ln)
        y -= lead
    return y


# ---------------- SCENES ----------------
SCENES = [
    dict(n=1, t="THE MYSTERY", tc="0:00 – 0:18", img="assets/SC1_3.png", key="s1",
         line="A man with nothing left does something impossible.",
         body="A marathon runner is finished. Head rolling, legs gone. The commentator writes him off. "
              "Then, metres from the line, he explodes into a sprint.\n\n"
              "Everything freezes. Manan walks into the stopped world with a magnifying glass, examines the runner, "
              "and turns to us with the question the whole film will answer.",
         quote="Hold on. He had nothing left. So where did THAT come from?"),
    dict(n=2, t="THE FULL TANK", tc="0:18 – 0:40", img="assets/HERO_2.png", key="s2",
         line="He expects to find an empty tank. He finds a full one.",
         body="Inside the leg, a factory. Gears turning where the muscle would be, workers hauling crates. Then the "
              "machines slow and a worker shrugs. That is it. We are done.\n\n"
              "But at the back there is a door nobody opened. Manan pushes it, and behind it stand row upon row of "
              "storage tanks, every gauge reading full.\n\n"
              "This is real. When scientists tested athletes at the exact moment they gave up, the muscles could "
              "still produce far more power. The tank was never empty.",
         quote="It was never empty."),
    dict(n=3, t="THE GATEKEEPER", tc="0:40 – 1:05", img="assets/HERO_3.png", key="s3",
         line="Somebody closed that door. He is not a villain, and he has the key.",
         body="Coach Brain, tracksuit, whistle, coffee, and a small brass key on a chain. He is not caught out. "
              "He is delighted to be found.\n\n"
              "He shows Manan the network. Heart, breath, temperature, water, distance, everything feeding back to a "
              "single dial. He is asking one question, constantly, and setting the limit by the answer.\n\n"
              "So the limit was never the body. It was a judgement.",
         quote="It's my best guess. And I'd rather you finish than break."),
    dict(n=4, t="THE TRICK", tc="1:05 – 1:25", img="assets/HERO_4.png", key="s4",
         line="Scientists lied to a cyclist about his own best time. He beat it.",
         body="A cyclist races a ghost on a screen. He is told the ghost is a recording of his own fastest ever ride.\n\n"
              "Behind the glass, a researcher quietly turns it up by two percent, and says nothing.\n\n"
              "He chases. He passes. He beats a time he already believed was everything he had, which means it was "
              "never everything he had. Change what the brain believes, and the door opens.",
         quote="He beat his own maximum. Which means it was never his maximum."),
    dict(n=5, t="THE RELEASE", tc="1:25 – 1:50", img="assets/HERO_5.png", key="s5",
         line="What it looks like when the limit moves.",
         body="Coach Brain looks at his dial, and eases it open.\n\n"
              "Muscle fibres light one after another. The runner flies. And the film breaks loose, a traceur rooftop "
              "to rooftop, a dancer turning in the air, a swimmer leaving the wall. Bodies doing what they could "
              "always do, finally permitted.\n\n"
              "Nothing new was created. Something already there was released.",
         quote="The brain didn't make new energy. It gave permission."),
    dict(n=6, t="THE INVITATION", tc="1:50 – 2:00", img="assets/HERO_6.png", key="s6",
         line="Still, bright, and quietly handed over.",
         body="Everything settles to white. Manan stands alone, eyes closed, breathing. Completely calm.\n\n"
              "The dial hangs beside him, and this time his own hand is on it. Coach Brain lifts the key from his "
              "neck and hands it across. No fanfare. Manan opens his eyes.\n\n"
              "The film ends on one idea, and the audience carries it out of the room.",
         quote="The wall is real. But somebody set it."),
]

# ---------------- COVER ----------------
newpage()
img = prep("assets/SC1_3.png", "cover", 2200)
iw = W - ML - MR
ih = iw * 9 / 16
c.drawImage(ImageReader(img), ML, H - 132 - ih, iw, ih, mask='auto')
c.setStrokeColor(INK)
c.setLineWidth(1)
c.rect(ML, H - 132 - ih, iw, ih, fill=0, stroke=1)

y = H - 132 - ih - 46
c.setFont('DB', 32)
c.setFillColor(INK)
c.drawString(ML, y, "THE BRAIN BRAKE")
y -= 24
c.setFont('DO', 12.5)
c.setFillColor(SOFT)
c.drawString(ML, y, "The limit is a setting, not a wall.")
y -= 34
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 26
y = text("A two minute film for the Breakthrough Junior Challenge. This is the outline, one picture and a few lines "
         "per scene. It takes about three minutes to read.", y, 'D', 11.5, 17)
y -= 8
y = text("The subject, the science and the detective are Manan's, from his first draft. What has changed is the "
         "shape of the story. Draft one explained that the brain applies a brake to protect you. This version asks "
         "the next question. If the brake is real, where is the limit actually, and can it move?", y, 'D', 11.5, 17)
y -= 8
y = text("The research says it can. That turns an explanation into a discovery, and the film rises instead of "
         "settling.", y, 'DB', 11.5, 17)

y -= 22
c.setFont('MB', 8.5)
c.setFillColor(ACC)
c.drawString(ML, y, "WRITTEN BY")
y -= 16
c.setFont('DB', 12)
c.setFillColor(INK)
c.drawString(ML, y, "Manan Periwal")
c.setFont('D', 10)
c.setFillColor(SOFT)
c.drawString(ML + 118, y, "concept, science and story")
y -= 18
c.setFont('DB', 12)
c.setFillColor(INK)
c.drawString(ML, y, "Marko Boško")
c.setFont('D', 10)
c.setFillColor(SOFT)
c.drawString(ML + 118, y, "story mentor and direction")

# ---------------- SCENE PAGES ----------------
for s in SCENES:
    newpage()
    # header strip
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML, H - 56, f"SCENE {s['n']}")
    c.drawRightString(W - MR, H - 56, s['tc'])
    c.setFont('DB', 25)
    c.setFillColor(INK)
    c.drawString(ML, H - 84, s['t'])
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.line(ML, H - 96, W - MR, H - 96)

    img = prep(s['img'], s['key'], 2200)
    iw = W - ML - MR
    ih = iw * 9 / 16
    top = H - 118
    c.drawImage(ImageReader(img), ML, top - ih, iw, ih, mask='auto')
    c.setStrokeColor(RULE)
    c.setLineWidth(0.9)
    c.rect(ML, top - ih, iw, ih, fill=0, stroke=1)

    y = top - ih - 34
    c.setFont('DO', 13)
    c.setFillColor(ACC)
    for ln in wrap(s['line'], 'DO', 13, W - ML - MR):
        c.drawString(ML, y, ln)
        y -= 19
    y -= 12

    for para in s['body'].split("\n\n"):
        y = text(para, y, 'D', 11.5, 17.5)
        y -= 9

    # quote block
    y -= 6
    qlines = wrap(s['quote'], 'M', 11, W - ML - MR - 34)
    boxh = len(qlines) * 17 + 24
    c.setFillColor(HexColor("#e5dcc4"))
    c.rect(ML, y - boxh + 12, W - ML - MR, boxh, fill=1, stroke=0)
    c.setStrokeColor(ACC)
    c.setLineWidth(2)
    c.line(ML, y - boxh + 12, ML, y + 12)
    yy = y - 4
    for ln in qlines:
        c.setFont('M', 11)
        c.setFillColor(INK)
        c.drawString(ML + 18, yy, ln)
        yy -= 17

# ---------------- CLOSING ----------------
newpage()
c.setFont('DB', 25)
c.setFillColor(INK)
c.drawString(ML, H - 84, "What happens next")
c.setStrokeColor(INK)
c.setLineWidth(1.2)
c.line(ML, H - 96, W - MR, H - 96)

y = H - 132
y = text("This is the outline, not the finished plan. Everything below follows once you are happy with the direction.",
         y, 'DO', 12, 18, SOFT)
y -= 14

for h, b in [
    ("The shot breakdown",
     "Every scene split into individual shots, each one drawn, timed to the second, with the exact words spoken "
     "over it. Thirty three shots in total. Scene one is already drawn."),
    ("The camera plan, for Venkatesh in Pondicherry",
     "One shooting day. Manan is filmed against a plain grey background and placed into the drawn world afterwards, "
     "so the shoot itself is simple. Lighting, framing and eyelines all specified in advance, and the lines are shot "
     "one sentence at a time so nothing is ever rushed."),
    ("The animation brief, for Kristijan in Zagreb",
     "Character models, per shot instructions, and which shots are drawn from scratch against which are drawn over "
     "the filmed material. His quote follows from this document."),
    ("Sound and original music",
     "An original score written to the finished picture. Two voices, percussion for the body and a sustained tone "
     "for the mind, and the film holds its resolution back until the release."),
]:
    c.setFont('DB', 13)
    c.setFillColor(INK)
    c.drawString(ML, y, h)
    y -= 19
    y = text(b, y, 'D', 11, 16.5)
    y -= 16

y -= 10
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 26
c.setFont('DB', 13)
c.setFillColor(INK)
c.drawString(ML, y, "What we need from you")
y -= 20
y = text("Only a yes or a no on the direction, and anything Manan wants changed. It is his subject and his "
         "understanding driving the film. If a line does not sound like him, we change it. If he wants his original "
         "ending back, we do that, without argument.", y, 'D', 11.5, 17)
y -= 10
y = text("Everything for this production lives on a private page online, including both drafts of the script, the "
         "character designs, the storyboard as it grows, and every version of the film as it is cut. You will always "
         "be able to see exactly where it stands.", y, 'D', 11.5, 17)

y -= 30
c.setFont('DO', 12.5)
c.setFillColor(ACC)
c.drawString(ML, y, "A film that does not just explain something.")
y -= 19
c.drawString(ML, y, "One that leaves a person lighter than when they sat down.")

foot()
c.save()
print("written", OUT, round(os.path.getsize(OUT) / 1024), "KB")
