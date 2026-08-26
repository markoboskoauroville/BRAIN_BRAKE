#!/usr/bin/env python3
"""THE BRAIN BRAKE, read through, four panels to a page.

Landscape A4, four frames per page in a two by two grid, each with its frame
number and its line. Nothing else. No camera notes, no animation notes, no
timecodes. A silent panel is a picture and a blank space.

Prefers assets/train/frames_v5.json if it exists, falls back to v4.

    python3 30-readthrough-4up.py
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
IMG = os.path.join(REPO, 'assets/V7')
OUT = "/home/claude/out/THE BRAIN BRAKE - READ THROUGH 4UP.pdf"
os.makedirs("/home/claude/out", exist_ok=True)

W, H = landscape(A4)
M = 26                      # page margin
GX, GY = 18, 14             # gap between cells
PAPER = HexColor("#f2ebda"); INK = HexColor("#221f19")
SOFT = HexColor("#8a8170"); RULE = HexColor("#cdbfa4")
BOX = HexColor("#e6dcc4"); ACC = HexColor("#8a6b2e")

CW = (W - M * 2 - GX) / 2
CH = (H - M * 2 - GY) / 2

c = canvas.Canvas(OUT, pagesize=landscape(A4))
pg = [0]


def bg():
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)


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


def cell(f, col, row):
    x = M + col * (CW + GX)
    top = H - M - row * (CH + GY)

    # frame number, top left of the cell
    c.setFont('MB', 10); c.setFillColor(ACC)
    c.drawString(x, top - 11, f['id'])
    if f.get('who'):
        c.setFont('MB', 7.5); c.setFillColor(SOFT)
        c.drawRightString(x + CW, top - 11, f['who'].upper())
    y = top - 20

    text = (f.get('text') or "").strip()
    size = 11.5 if len(text) < 60 else (10 if len(text) < 110 else 8.8)
    body = wrap("\u201c" + text + "\u201d", 'DB', size, CW - 22) if text else []
    block = (12 + len(body) * size * 1.3 + 10) if text else 0
    avail = CH - 20 - (block + 10 if text else 0)

    p = os.path.join(IMG, f['img'])
    if os.path.exists(p):
        im = Image.open(p); iw, ih = im.size
        w = CW; h = w * ih / iw
        if h > avail:
            h = avail; w = h * iw / ih
        ix = x + (CW - w) / 2
        c.drawImage(ImageReader(p), ix, y - h, w, h, mask='auto')
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.rect(ix, y - h, w, h, fill=0, stroke=1)
        y -= h + 10
    else:
        h = min(avail, CW * 9 / 16)
        c.setFillColor(BOX); c.rect(x, y - h, CW, h, fill=1, stroke=0)
        c.setStrokeColor(RULE); c.setDash(2.5, 2.5)
        c.rect(x, y - h, CW, h, fill=0, stroke=1); c.setDash()
        c.setFont('D', 8.5); c.setFillColor(SOFT)
        c.drawCentredString(x + CW / 2, y - h / 2 - 3, "live footage")
        y -= h + 10

    if text:
        c.setFillColor(BOX); c.rect(x, y - block, CW, block, fill=1, stroke=0)
        c.setStrokeColor(ACC); c.setLineWidth(1.8)
        c.line(x, y - block, x, y)
        c.setFont('DB', size); c.setFillColor(INK)
        yy = y - 12 - size * 0.85
        for ln in body:
            c.drawString(x + 12, yy, ln); yy -= size * 1.3


frames = json.load(open(SRC))

bg()
c.setFont('DB', 40); c.setFillColor(INK)
c.drawCentredString(W / 2, H / 2 + 34, "THE BRAIN BRAKE")
c.setFont('D', 13); c.setFillColor(SOFT)
c.drawCentredString(W / 2, H / 2 + 6, "the film, read through")
c.setStrokeColor(RULE); c.setLineWidth(0.8)
c.line(W / 2 - 80, H / 2 - 12, W / 2 + 80, H / 2 - 12)
c.setFont('M', 9); c.setFillColor(SOFT)
c.drawCentredString(W / 2, H / 2 - 34, "%d panels" % len(frames))
c.showPage()

bg()
for i, f in enumerate(frames):
    slot = i % 4
    cell(f, slot % 2, slot // 2)
    if slot == 3 or i == len(frames) - 1:
        pg[0] += 1
        c.setFont('M', 7); c.setFillColor(SOFT)
        c.drawRightString(W - M, 14, str(pg[0]))
        c.showPage(); bg()

c.setFont('H', 26); c.setFillColor(INK)
c.drawCentredString(W / 2, H / 2, "The limit is a setting, not a wall.")
c.showPage()
c.save()
print("written %s  pages %d  panels %d" % (OUT, pg[0] + 2, len(frames)))
