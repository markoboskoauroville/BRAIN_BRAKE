#!/usr/bin/env python3
"""THE BRAIN BRAKE, read through. Built from the slides themselves.

Four panels to a landscape page. Each panel IS the timeline slide, so the page
and the film show the identical frame: the picture, the frame number in the
corner and the line as a subtitle across the bottom.

The magnifying glass between the last panel of a scene and the first of the
next carries the next scene inside its lens.

    python3 32-readthrough.py
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import json, os

for n, f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),
             ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))
pdfmetrics.registerFont(TTFont('H', '/home/claude/Caveat.ttf'))

REPO = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO, 'assets/train/frames_v5.json')
if not os.path.exists(SRC):
    SRC = os.path.join(REPO, 'assets/train/frames_v4.json')
SLIDES = os.path.join(REPO, 'assets/slides')
IMG = os.path.join(REPO, 'assets/V7')
OUT = "/home/claude/out/THE BRAIN BRAKE - READ THROUGH.pdf"
os.makedirs("/home/claude/out", exist_ok=True)

W, H = landscape(A4)
M = 26; GX, GY = 20, 18
PAPER = HexColor("#f2ebda"); SOFT = HexColor("#8a8170"); RULE = HexColor("#cdbfa4")
CW = (W - M * 2 - GX) / 2
CH = (H - M * 2 - GY) / 2

c = canvas.Canvas(OUT, pagesize=landscape(A4))
pg = [0]


def bg():
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)


def glass(cx, cy, r, nxt):
    """The film's transition. The next scene seen inside the lens."""
    p = os.path.join(SLIDES, nxt['id'].replace('.', '_') + '.jpg')
    c.saveState()
    c.setFillColor(PAPER); c.circle(cx, cy, r + 8, fill=1, stroke=0)
    if os.path.exists(p):
        path = c.beginPath(); path.circle(cx, cy, r); c.clipPath(path, stroke=0)
        im = Image.open(p); iw, ih = im.size
        h = r * 2.3; w = h * iw / ih
        c.drawImage(ImageReader(p), cx - w / 2, cy - h / 2, w, h, mask='auto')
    c.restoreState()
    c.setStrokeColor(HexColor("#9C7A31")); c.setLineWidth(3.2)
    c.circle(cx, cy, r, fill=0, stroke=1)
    c.setStrokeColor(HexColor("#c9a35a")); c.setLineWidth(1.0)
    c.circle(cx, cy, r - 2.4, fill=0, stroke=1)
    c.saveState(); c.translate(cx, cy); c.rotate(-135)
    c.setStrokeColor(HexColor("#9C7A31")); c.setLineWidth(6); c.setLineCap(1)
    c.line(0, r + 1, 0, r + 20)
    c.restoreState()


def cell(f, col, row):
    x = M + col * (CW + GX)
    top = H - M - row * (CH + GY)
    p = os.path.join(SLIDES, f['id'].replace('.', '_') + '.jpg')
    if not os.path.exists(p):
        p = os.path.join(IMG, f['img'])
    if os.path.exists(p):
        im = Image.open(p); iw, ih = im.size
        w = CW; h = w * ih / iw
        if h > CH:
            h = CH; w = h * iw / ih
        ix = x + (CW - w) / 2; iy = top - h - (CH - h) / 2
        c.drawImage(ImageReader(p), ix, iy, w, h, mask='auto')
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.rect(ix, iy, w, h, fill=0, stroke=1)


frames = json.load(open(SRC))

bg()
c.setFont('DB', 40); c.setFillColor(HexColor("#221f19"))
c.drawCentredString(W / 2, H / 2 + 34, "THE BRAIN BRAKE")
c.setFont('D', 13); c.setFillColor(SOFT)
c.drawCentredString(W / 2, H / 2 + 6, "the film, read through")
c.setStrokeColor(RULE); c.setLineWidth(0.8)
c.line(W / 2 - 80, H / 2 - 12, W / 2 + 80, H / 2 - 12)
c.setFont('M', 9)
c.drawCentredString(W / 2, H / 2 - 34, "%d panels" % len(frames))
c.showPage(); bg()

for i, f in enumerate(frames):
    slot = i % 4
    col, row = slot % 2, slot // 2
    cell(f, col, row)
    nxt = frames[i + 1] if i + 1 < len(frames) else None
    if nxt and nxt['scene'] != f['scene'] and col == 0:
        glass(M + CW + GX / 2, H - M - row * (CH + GY) - CH * 0.5, 30, nxt)
    if slot == 3 or i == len(frames) - 1:
        pg[0] += 1
        c.setFont('M', 7); c.setFillColor(SOFT)
        c.drawRightString(W - M, 14, str(pg[0]))
        c.showPage(); bg()

c.setFont('H', 26); c.setFillColor(HexColor("#221f19"))
c.drawCentredString(W / 2, H / 2, "The limit is a setting, not a wall.")
c.showPage(); c.save()
print("written %s  pages %d  panels %d" % (OUT, pg[0] + 2, len(frames)))
