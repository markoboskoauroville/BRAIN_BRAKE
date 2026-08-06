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

OUT = "assets/pdf/3-THE-BRAIN-BRAKE-v3-RECOMMENDED.pdf"
os.makedirs("build", exist_ok=True)
os.makedirs("assets/pdf", exist_ok=True)
c = canvas.Canvas(OUT, pagesize=A4)
page = [0]


def prep(src, key, maxw=2000):
    p = f"build/{key}.jpg"
    im = Image.open(src).convert("RGB")
    if im.size[0] > maxw:
        im = im.resize((maxw, int(maxw * im.size[1] / im.size[0])), Image.LANCZOS)
    im.save(p, "JPEG", quality=86, optimize=True)
    return p


def bg():
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def foot():
    c.setFont('M', 7.5)
    c.setFillColor(SOFT)
    c.drawString(ML, 30, "THE BRAIN BRAKE   ·   version three   ·   Manan Periwal & Marko Bo\u0161ko")
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


SCENES = [
    dict(n=1, t="THE MYSTERY", tc="0:00 – 0:14", img="assets/SC1_3.png", key="s1",
         line="A man with nothing left does something impossible.",
         body="A marathon runner is finished. Head rolling, legs gone. The commentator writes him off. "
              "Then, metres from the line, he explodes into a sprint.\n\n"
              "Everything freezes. Manan walks into the stopped world with a magnifying glass, examines the "
              "runner, and turns to us with the question the whole film will answer.",
         quote="Hold on. He had nothing left. So where did THAT come from?"),

    dict(n=2, t="THE OLD THEORY", tc="0:14 – 0:30", img="assets/HERO_V1_2.png", key="s2",
         line="The answer science believed for a century. Then the crack in it.",
         body="Case file one, the muscle. A. V. Hill, Nobel laureate, proposed in 1923 that fatigue begins in "
              "the muscle itself. Run faster, run out of oxygen, fatigue, stop.\n\n"
              "The runner becomes a factory. Oxygen crates stop arriving, the machines slow, a worker wipes his "
              "brow and shrugs. That is it, we are done. A stamp comes down. Case closed.\n\n"
              "Then the sprint replays, and the stamp cracks.",
         quote="Except\u2026 it doesn't explain this."),

    dict(n=3, t="THE FULL TANK", tc="0:30 – 0:48", img="assets/HERO_2.png", key="s3",
         line="He expects to find an empty tank. He finds a full one.",
         body="At the back of the factory there is a door nobody opened. Manan pushes it, and behind it stand "
              "row upon row of storage tanks, every gauge reading full.\n\n"
              "This is real, and it is the finding the whole film turns on. When scientists tested athletes at "
              "the exact moment they gave up, the muscles could still produce far more power than the athlete "
              "had just produced.\n\n"
              "So the muscle was not the thing that stopped him. Something else closed that door.",
         quote="It was never empty."),

    dict(n=4, t="THE GATEKEEPER", tc="0:48 – 1:14", img="assets/HERO_3.png", key="s4",
         line="Meet the Central Governor. He is not a villain, and he has the key.",
         body="Coach Brain, tracksuit, coffee, and a small gold key on a chain. He is not caught out. He is "
              "delighted to be found.\n\n"
              "He shows Manan the network. Heart rate, breath, temperature, water, distance, everything feeding "
              "back to a single dial. He is asking one question, constantly, and setting the pace by the answer. "
              "Can we keep going safely? This is the Central Governor Theory, proposed by Professor Tim Noakes "
              "in 1997.\n\n"
              "Two seconds on a phone. The battery drops, the screen dims, background apps close. The phone is "
              "not broken. It is protecting itself so it lasts. Fatigue may work a little like low power mode.\n\n"
              "So the limit was never the body. It was a judgement, and a judgement can be wrong.",
         quote="I'm not trying to stop you. I'm trying to get you to the finish line."),

    dict(n=5, t="THE TRICK", tc="1:14 – 1:30", img="assets/HERO_4.png", key="s5",
         line="Scientists lied to a cyclist about his own best time. He beat it.",
         body="A cyclist races a ghost on a screen, told it is a recording of his own fastest ever ride.\n\n"
              "Behind the glass, a researcher quietly turns it up by two percent and says nothing.\n\n"
              "He chases. He passes. He beats a time he already believed was everything he had, which means it "
              "was never everything he had. Change what the brain believes, and the door opens.",
         quote="He beat his own maximum. Which means it was never his maximum."),

    dict(n=6, t="THE RELEASE", tc="1:30 – 1:46", img="assets/HERO_5.png", key="s6",
         line="What it looks like when the limit moves.",
         body="Coach Brain runs his safety check. Every reading comes back green. He looks at the dial, and "
              "eases it open. Never to one hundred.\n\n"
              "Muscle fibres light one after another. The runner flies. And the film breaks loose, a traceur "
              "rooftop to rooftop, a dancer turning in the air, a swimmer leaving the wall. Bodies doing what "
              "they could always do, finally permitted.",
         quote="The brain didn't make new energy. It gave permission."),

    dict(n=7, t="THE VERDICT", tc="1:46 – 1:54", img="assets/HERO_V1_6.png", key="s7",
         line="Who was right. The film answers the question it opened.",
         body="Everything turns white. The Muscle and Coach Brain face each other with the brake between them, "
              "and instead of arguing, they shake hands.\n\n"
              "Hill in 1923, the muscle. Noakes in 1997, the brain. Today, the evidence says both contribute, "
              "and researchers are still working out exactly how the two share the work.\n\n"
              "The film says this plainly rather than hiding it, because that willingness to keep testing is "
              "what science actually is.",
         quote="Great ideas aren't accepted because they sound convincing. They're\naccepted because scientists keep testing them."),

    dict(n=8, t="THE INVITATION", tc="1:54 – 2:00", img="assets/HERO_6.png", key="s8",
         line="Still, bright, and quietly handed over.",
         body="Manan stands alone in the white, eyes closed, breathing. Completely calm.\n\n"
              "The dial hangs beside him and this time his own hand is on it. Coach Brain lifts the key from his "
              "neck and hands it across. No fanfare. Manan opens his eyes.\n\n"
              "The film ends on one idea, and the audience carries it out of the room.",
         quote="The wall is real. But somebody set it. And what your brain\nbelieves is safe can be trained."),
]

# ---------------- COVER ----------------
newpage()
img = prep("assets/SC1_3.png", "cover", 2200)
iw = W - ML - MR
ih = iw * 9 / 16
c.drawImage(ImageReader(img), ML, H - 132 - ih, iw, ih, mask='auto')
c.setStrokeColor(RULE)
c.setLineWidth(0.9)
c.rect(ML, H - 132 - ih, iw, ih, fill=0, stroke=1)

y = H - 132 - ih - 46
c.setFont('DB', 34)
c.setFillColor(INK)
c.drawString(ML, y, "THE BRAIN BRAKE")
y -= 24
c.setFont('DO', 12.5)
c.setFillColor(SOFT)
c.drawString(ML, y, "Version three. The version we recommend shooting.")
y -= 30
c.setStrokeColor(RULE)
c.setLineWidth(1)
c.line(ML, y, W - MR, y)
y -= 28

y = text("A two minute film for the Breakthrough Junior Challenge. This is the outline, one picture and a few "
         "lines per scene. It takes about four minutes to read.", y, 'D', 11.5, 17.5)
y -= 8
y = text("Version one is Manan's original screenplay. Version two was our first draft together, which changed "
         "the shape of the story. This version answers Neha's note on that draft, and it is the two of them "
         "put together properly.", y, 'D', 11.5, 17.5)
y -= 8
c.setFont('DB', 11.5)
c.setFillColor(INK)
for ln in wrap("Manan's theory, explained as he wrote it. Our story shape, which rises instead of settling. "
               "And his conclusion, which answers the question the film opens with.", 'DB', 11.5, W - ML - MR):
    c.drawString(ML, y, ln)
    y -= 17.5

y -= 26
c.setFont('MB', 9)
c.setFillColor(ACC)
c.drawString(ML, y, "WRITTEN BY")
y -= 20
c.setFont('DB', 13)
c.setFillColor(INK)
c.drawString(ML, y, "Manan Periwal")
c.setFont('D', 10)
c.setFillColor(SOFT)
c.drawString(ML + 118, y, "concept, science and story")
y -= 19
c.setFont('DB', 13)
c.setFillColor(INK)
c.drawString(ML, y, "Marko Bo\u0161ko")
c.setFont('D', 10)
c.setFillColor(SOFT)
c.drawString(ML + 118, y, "story mentor and direction")

# ---------------- WHAT CHANGED ----------------
newpage()
c.setFont('DB', 25)
c.setFillColor(INK)
c.drawString(ML, H - 84, "What changed, and why")
c.setStrokeColor(INK)
c.setLineWidth(1.2)
c.line(ML, H - 96, W - MR, H - 96)

y = H - 132
y = text("Neha's note asked for two things. Both are in this version, and nothing was lost to make room for them.",
         y, 'DO', 12, 18, SOFT)
y -= 16

for h, b in [
    ("One. The theory is explained as Manan wrote it",
     "Scene two is his old theory scene, restored. A. V. Hill, 1923, the muscle, the flowchart, the factory "
     "running out of oxygen, the stamp coming down and then cracking. In scene four the Central Governor "
     "Theory is named on screen, with Professor Tim Noakes and 1997, and Coach Brain explains the mechanism "
     "in his own words. His low power mode analogy is kept, compressed to two seconds, because it is the "
     "clearest everyday explanation in either draft."),
    ("Two. The film now reaches a definitive conclusion",
     "Scene seven is his ending. The Muscle and Coach Brain shake hands, the film states who was right, Hill "
     "for the muscle and Noakes for the brain, and that today the evidence says both contribute while "
     "researchers work out how. The question the film opens with is answered out loud, and the honesty about "
     "what is still debated stays, because judges read for exactly that."),
    ("What we kept from version two",
     "The shape. The film moves from curiosity to astonishment to release rather than explaining and then "
     "stopping. The full tank discovery, which is the finding that makes the science surprising rather than "
     "merely correct. The key as a single physical object that travels through the film and changes hands at "
     "the end. And no villain anywhere, because the moment an audience has somebody to blame they stop "
     "thinking."),
    ("The ending now does both jobs",
     "Version two ended on feeling and left the science open. Version one ended on the science and left the "
     "feeling flat. Here the verdict comes first, eight seconds of clear answer, and then six seconds of "
     "handover in silence. The audience leaves knowing what the research says and carrying the idea out with "
     "them."),
]:
    c.setFont('DB', 13)
    c.setFillColor(INK)
    c.drawString(ML, y, h)
    y -= 19
    y = text(b, y, 'D', 11, 16.5)
    y -= 16

y -= 4
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 24
c.setFont('DO', 12)
c.setFillColor(ACC)
c.drawString(ML, y, "Eight scenes now instead of six. Same two minutes, tighter cutting.")

# ---------------- SCENE PAGES ----------------
for s in SCENES:
    newpage()
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

    y -= 6
    qlines = []
    for seg in s['quote'].split("\n"):
        qlines += wrap(seg, 'M', 11, W - ML - MR - 34)
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
y = text("Nothing below starts until Manan and Neha say yes to this direction. Once that yes arrives, the rest "
         "is already planned.", y, 'DO', 12, 18, SOFT)
y -= 14

for h, b in [
    ("The shot breakdown",
     "Every scene split into individual shots, each one drawn, timed to the second, with the exact words spoken "
     "over it. Character and location reference sheets are already finished, so every frame is drawn against "
     "the same designs and the film reads as one hand rather than a set of separate pictures."),
    ("The camera plan, for Venkatesh in Pondicherry",
     "One shooting day. Manan is filmed against a plain grey background and placed into the drawn world "
     "afterwards, so the shoot itself is simple. Four setups, lighting, framing and eyelines specified in "
     "advance, and the lines shot one sentence at a time so nothing is ever rushed. Ready two to three days "
     "after the script is approved."),
    ("The animation brief, for Kristijan in Zagreb",
     "Character models, per shot instructions, and which shots are drawn from scratch against which are drawn "
     "over the filmed material."),
    ("Sound and original music",
     "An original score written to the finished picture. Two voices, percussion for the body and a sustained "
     "tone for the mind, and the film holds its resolution back until the release."),
]:
    c.setFont('DB', 13)
    c.setFillColor(INK)
    c.drawString(ML, y, h)
    y -= 19
    y = text(b, y, 'D', 11, 16.5)
    y -= 16

y -= 6
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 26
c.setFont('DB', 13)
c.setFillColor(INK)
c.drawString(ML, y, "What we need from you")
y -= 20
y = text("A yes or a no on this version, and anything Manan wants changed in the wording. It is his subject and "
         "his understanding driving the film, and every line of science in it is his. If a sentence does not "
         "sound like him, we change it.", y, 'D', 11.5, 17)
y -= 10
y = text("Everything for this production lives on one private page online, all three versions of the script, the "
         "character designs, the storyboard as it grows, and every cut of the film. You will always be able to "
         "see exactly where it stands.", y, 'D', 11.5, 17)

y -= 30
c.setFont('DO', 12.5)
c.setFillColor(ACC)
c.drawString(ML, y, "A film that explains something properly.")
y -= 19
c.drawString(ML, y, "And leaves a person lighter than when they sat down.")

foot()
c.save()
print("written", OUT, round(os.path.getsize(OUT) / 1024), "KB")
