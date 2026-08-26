#!/usr/bin/env python3
"""THE BRAIN BRAKE, read through.

The film as printed pages. Nothing else. No camera notes, no animation notes, no
transition notes, no setups, no timecodes in the body. One panel per page, the
picture large, and underneath it the line as it is spoken, marked with who says
it. A silent panel is a picture and a blank space, which is what it is in the
film.

Prefers assets/train/frames_v5.json if it exists, since that is the film retimed
to the real performances, and falls back to v4.

    python3 29-readthrough.py
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
OUT = "/home/claude/out/THE BRAIN BRAKE - READ THROUGH.pdf"
os.makedirs("/home/claude/out", exist_ok=True)

W, H = landscape(A4)
ML = 40
CW = W - ML * 2
PAPER = HexColor("#f2ebda"); INK = HexColor("#221f19")
SOFT = HexColor("#8a8170"); RULE = HexColor("#cdbfa4")
BOX = HexColor("#e6dcc4"); ACC = HexColor("#8a6b2e")

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


frames = json.load(open(SRC))

# ---- title page
bg()
c.setFont('DB', 46); c.setFillColor(INK)
c.drawCentredString(W / 2, H / 2 + 40, "THE BRAIN BRAKE")
c.setFont('D', 15); c.setFillColor(SOFT)
c.drawCentredString(W / 2, H / 2 + 6, "the film, read through")
c.setStrokeColor(RULE); c.setLineWidth(0.8)
c.line(W / 2 - 90, H / 2 - 16, W / 2 + 90, H / 2 - 16)
c.setFont('M', 9); c.setFillColor(SOFT)
c.drawCentredString(W / 2, H / 2 - 40, "%d panels" % len(frames))
c.showPage()

for f in frames:
    bg()
    pg[0] += 1

    text = (f.get('text') or "").strip()
    who = (f.get('who') or "").strip()

    # the line first, so the picture can size itself to what is left
    size = 22 if len(text) < 70 else (18 if len(text) < 120 else 15)
    body = wrap("\u201c" + text + "\u201d", 'DB', size, CW - 40) if text else []
    block = (28 + len(body) * size * 1.34 + 20) if text else 0

    top = H - 34
    avail = top - 40 - (block + 22 if text else 0)

    p = os.path.join(IMG, f['img'])
    if os.path.exists(p):
        im = Image.open(p); iw, ih = im.size
        w = CW; h = w * ih / iw
        if h > avail:
            h = avail; w = h * iw / ih
        x = ML + (CW - w) / 2
        c.drawImage(ImageReader(p), x, top - h, w, h, mask='auto')
        c.setStrokeColor(RULE); c.setLineWidth(0.7)
        c.rect(x, top - h, w, h, fill=0, stroke=1)
        y = top - h - 22
    else:
        h = min(avail, CW * 9 / 16)
        c.setFillColor(BOX); c.rect(ML, top - h, CW, h, fill=1, stroke=0)
        c.setStrokeColor(RULE); c.setDash(3, 3)
        c.rect(ML, top - h, CW, h, fill=0, stroke=1); c.setDash()
        c.setFont('D', 12); c.setFillColor(SOFT)
        c.drawCentredString(W / 2, top - h / 2 - 4, "this panel is the live footage")
        y = top - h - 22

    if text:
        c.setFillColor(BOX); c.rect(ML, y - block, CW, block, fill=1, stroke=0)
        c.setStrokeColor(ACC); c.setLineWidth(2.4)
        c.line(ML, y - block, ML, y)
        c.setFont('MB', 7.5); c.setFillColor(ACC)
        c.drawString(ML + 20, y - 18, who.upper())
        c.setFont('DB', size); c.setFillColor(INK)
        yy = y - 28 - size * 0.92
        for ln in body:
            c.drawString(ML + 20, yy, ln); yy -= size * 1.34

    c.setFont('M', 7); c.setFillColor(SOFT)
    c.drawRightString(W - ML, 22, str(pg[0]))
    c.showPage()

# ---- last page
bg()
c.setFont('H', 30); c.setFillColor(INK)
c.drawCentredString(W / 2, H / 2, "The limit is a setting, not a wall.")
c.showPage()

c.save()
total = sum(f['fr'] for f in frames)
print("written %s  pages %d  panels %d  %d frames" % (OUT, pg[0] + 2, len(frames), total))
