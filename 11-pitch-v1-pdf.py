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

OUT = "assets/pdf/4-THE-BRAIN-BRAKE-outline-VERSION-ONE-original.pdf"
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
    c.drawString(ML, 30, "THE BRAIN BRAKE   ·   outline, version one   ·   written by Manan Periwal")
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
    dict(n=1, t="THE MYSTERY", tc="0:00 – 0:20", img="assets/SC1_3.png", key="s1",
         line="A man with nothing left does something impossible.",
         body="A marathon broadcast. An athlete is barely running and the commentator writes him off. Then, just "
              "before the finish line, he launches into a remarkable sprint.\n\n"
              "Everything freezes. Only Manan moves. He steps into the frozen race with a detective's magnifying "
              "glass, examines the runner, and turns to the camera. Question marks explode across the screen and a "
              "detective board appears.",
         quote="Hold on. If he's completely exhausted, where did THAT come from?"),
    dict(n=2, t="THE OLD THEORY", tc="0:20 – 0:40", img="assets/HERO_V1_2.png", key="s2",
         line="Present the answer scientists believed for decades. Then show the crack in it.",
         body="The detective board opens Case File One: Muscles. A dusty classroom, a chalkboard, and A.V. Hill, "
              "the Nobel Prize winner who proposed in 1923 that fatigue begins in the muscles.\n\n"
              "A flowchart builds itself, and the runner becomes a cartoon factory. Oxygen delivery trucks arrive, "
              "then stop arriving. An alarm rings. Tiny workers panic and haul a lever marked backup power. Smoke "
              "fills the factory and production slows.\n\n"
              "A giant stamp comes down. Case closed. Then the sprint replays, and the stamp cracks.",
         quote="Except… it doesn't explain this."),
    dict(n=3, t="THE NEW SUSPECT", tc="0:40 – 1:15", img="assets/HERO_V1_3.png", key="s3",
         line="The emotional centre of the film. Meet Super Coach Brain.",
         body="The chalkboard shatters and behind it is a mission control room. Screens everywhere showing heart "
              "rate, temperature, water, oxygen and blood pressure. A large chair turns.\n\n"
              "Super Coach Brain, a cheerful cartoon brain in a tracksuit with a whistle, a headset and running "
              "shoes, calmly sipping coffee. He has been watching the whole race, every second.\n\n"
              "Glowing lines connect every system in the body back to him. He moves one small lever, from one "
              "hundred percent down to eighty two, and the runner settles into a pace he can hold.",
         quote="I'm not trying to stop you. I'm trying to get you to the finish line."),
    dict(n=4, t="YOUR PHONE ALREADY KNOWS THIS", tc="1:15 – 1:40", img="assets/HERO_V1_4.png", key="s4",
         line="An ordinary analogy everybody understands instantly.",
         body="A monitor fills the screen and becomes a phone. The battery drops, and a notification appears: low "
              "power mode. The screen dims, background apps quietly close themselves.\n\n"
              "Manan asks whether it is broken. It is not. It is protecting itself, so that it lasts when it is "
              "really needed. A shield forms around the battery.\n\n"
              "The phone morphs back into Coach Brain, the battery becomes the runner and the shield becomes a "
              "finish line. He never touches the stop button. He simply eases the lever down a little.",
         quote="Fatigue may work a little like low power mode."),
    dict(n=5, t="BACK TO THE MARATHON", tc="1:40 – 1:55", img="assets/HERO_V1_5.png", key="s5",
         line="Return to the opening mystery and answer it.",
         body="Split screen. On one side the exhausted runner, metres from the line. On the other, mission control, "
              "every monitor updating in real time.\n\n"
              "Coach Brain runs a final safety scan. Every screen flashes green. He eases the lever from eighty two "
              "to ninety five, and never to one hundred.\n\n"
              "The runner's stride opens and the crowd erupts. Inside his legs, more muscle fibres light up. The "
              "detective board returns and flips over to reveal the answer written on the back.",
         quote="The brain didn't suddenly create extra energy. It decided it was finally safe to use a little more."),
    dict(n=6, t="THE SCIENTIFIC TWIST", tc="1:55 – 2:00", img="assets/HERO_V1_6.png", key="s6",
         line="End on scientific honesty rather than a neat answer.",
         body="Everything turns white. Only Manan, the Muscle and Coach Brain remain, with a giant brake marked "
              "fatigue between them. Instead of arguing, they shake hands.\n\n"
              "Manan asks who was right. Both point up at an enormous question mark. Hill in 1923, Noakes from 1997, "
              "and today's understanding that both contribute, with scientists still investigating exactly how.\n\n"
              "The film closes on what science actually is. Not certainty, but the willingness to keep testing.",
         quote="Great ideas aren't accepted because they sound convincing. They're accepted because scientists keep testing them."),
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
c.drawString(ML, y, "Version one, the original script.")
y -= 34
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 26
y = text("A two minute film for the Breakthrough Junior Challenge. This is the outline of the original script, one "
         "picture and a few lines per scene. It takes about three minutes to read.", y, 'D', 11.5, 17)
y -= 8
y = text("This is Manan's own screenplay, laid out so it can be read alongside the second version and compared "
         "fairly. Every scene, every character and every idea in it is his.", y, 'D', 11.5, 17)
y -= 8
y = text("The film explains the Central Governor Theory. The brain applies a protective brake, fatigue is a "
         "warning rather than a failure, and the sprint at the end of a marathon is the brake easing off. It closes "
         "on the honest admission that scientists are still arguing about it.", y, 'DB', 11.5, 17)

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
c.drawString(ML + 118, y, "written entirely by him")

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
c.drawString(ML, H - 84, "Two versions, side by side")
c.setStrokeColor(INK)
c.setLineWidth(1.2)
c.line(ML, H - 96, W - MR, H - 96)

y = H - 132
y = text("There are two outlines. This one, and a second version. They share the same subject, the same theory, the "
         "same detective and the same characters. What differs is where the story goes.",
         y, 'DO', 12, 18, SOFT)
y -= 16

for h, b in [
    ("Version one, this document",
     "The brain applies a brake to protect the body. Fatigue is a warning, not a failure. The film explains the "
     "mechanism clearly and ends on the honest admission that scientists are still debating it. Written entirely "
     "by Manan."),
    ("Version two",
     "The same science, asking the next question. If the brake is real, where is the limit actually, and can it "
     "move? Research says it can, so the film builds from curiosity to astonishment to release, and ends with a boy "
     "breathing calmly, understanding that what stopped him was a decision. Manan's concept, developed with Marko."),
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
c.drawString(ML, y, "Choosing between them")
y -= 20
y = text("Read both and pick whichever film Manan wants to make. Neither choice is wrong and neither is more work "
         "than the other. Version one is complete and shootable exactly as written here.",
         y, 'D', 11.5, 17)
y -= 10
y = text("Whichever is chosen, the same production follows: the shot breakdown, the camera plan for Venkatesh in "
         "Pondicherry, the animation brief for Kristijan in Zagreb, and an original score written to picture.",
         y, 'D', 11.5, 17)
y -= 10
y = text("Everything lives on a private page online, including both scripts, the character designs and every "
         "version of the film as it is cut.", y, 'D', 11.5, 17)

y -= 30
c.setFont('DO', 12.5)
c.setFillColor(ACC)
c.drawString(ML, y, "It is Manan's film either way.")
y -= 19
c.drawString(ML, y, "We only need to know which one he wants to make.")

foot()
c.save()
print("written", OUT, round(os.path.getsize(OUT) / 1024), "KB")
