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
# version at both ends, underscores, no spaces. see modules/design-language.md
VERSION = 2
OUT = "/home/claude/out/%d-BRAIN_BRAKE_READ_THROUGH_v%d.pdf" % (VERSION, VERSION)
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


def glass(cx, cy, r, nxt):
    """The film's own transition. A brass magnifying glass sitting in the gutter,
    with the first frame of the next scene inside the lens."""
    p = os.path.join(IMG, nxt['img'])
    c.saveState()
    c.setFillColor(PAPER)
    c.circle(cx, cy, r + 7, fill=1, stroke=0)          # clear the panels behind it
    if os.path.exists(p):
        path = c.beginPath(); path.circle(cx, cy, r)
        c.clipPath(path, stroke=0)
        im = Image.open(p); iw, ih = im.size
        h = r * 2.3; w = h * iw / ih
        c.drawImage(ImageReader(p), cx - w / 2, cy - h / 2, w, h, mask='auto')
    c.restoreState()
    c.setStrokeColor(HexColor("#9C7A31")); c.setLineWidth(3.2)
    c.circle(cx, cy, r, fill=0, stroke=1)
    c.setStrokeColor(HexColor("#c9a35a")); c.setLineWidth(1.0)
    c.circle(cx, cy, r - 2.4, fill=0, stroke=1)
    c.saveState()                                       # the handle, down and right
    c.translate(cx, cy); c.rotate(-135)
    c.setStrokeColor(HexColor("#9C7A31")); c.setLineWidth(6)
    c.setLineCap(1)
    c.line(0, r + 1, 0, r + 20)
    c.restoreState()


def cell(f, col, row):
    x = M + col * (CW + GX)
    top = H - M - row * (CH + GY)

    # frame number, top left of the cell
    c.setFont('MB', 10); c.setFillColor(ACC)
    c.drawString(x, top - 11, "[ %s ]" % f['id'])
    y = top - 20

    text = (f.get('text') or "").strip()
    size = 11.5 if len(text) < 60 else (10 if len(text) < 110 else 8.8)
    body = wrap("\u201c" + text + "\u201d", 'DB', size, CW - 22) if text else []
    block = (24 + len(body) * size * 1.3 + 10) if text else 0
    avail = CH - 20 - (block + 10 if text else 0)

    # a live frame gets the real footage. where a drawn picture exists too, both.
    live = os.path.join(REPO, 'assets/live', f['id'].replace('.', '_') + '_LIVE.jpg')
    drawn = os.path.join(IMG, f['img'])
    pair = os.path.exists(live) and os.path.exists(drawn) and f['layer'] in ('LIVE', 'BOOTH')
    if pair:
        a = Image.open(drawn).convert('RGB'); b = Image.open(live).convert('RGB')
        h0 = 900
        a = a.resize((int(h0 * a.width / a.height), h0), Image.LANCZOS)
        b = b.resize((int(h0 * b.width / b.height), h0), Image.LANCZOS)
        gap = 16
        sheet = Image.new('RGB', (a.width + gap + b.width, h0), (242, 235, 218))
        sheet.paste(a, (0, 0)); sheet.paste(b, (a.width + gap, 0))
        tmp = '/tmp/pair_%s.jpg' % f['id'].replace('.', '_')
        sheet.save(tmp, quality=92)
        p = tmp
    elif os.path.exists(live) and f['layer'] in ('LIVE', 'BOOTH'):
        p = live
    else:
        p = drawn
    if os.path.exists(p):
        im = Image.open(p); iw, ih = im.size
        w = CW; h = w * ih / iw
        if h > avail:
            h = avail; w = h * iw / ih
        ix = x + (CW - w) / 2
        c.drawImage(ImageReader(p), ix, y - h, w, h, mask='auto')
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.rect(ix, y - h, w, h, fill=0, stroke=1)
        if pair:
            c.setFont('MB', 6.5); c.setFillColor(SOFT)
            c.drawString(ix + 4, y - h + 4, "DRAWN")
            c.drawRightString(ix + w - 4, y - h + 4, "FOOTAGE")
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
        c.setFont('MB', 7); c.setFillColor(ACC)
        c.drawString(x + 12, y - 12, (f.get('who') or '').upper())
        c.setFont('DB', size); c.setFillColor(INK)
        yy = y - 24 - size * 0.85
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
c.drawCentredString(W / 2, H / 2 - 34, "%d panels   \u00b7   version %d" % (len(frames), VERSION))
c.showPage()

bg()
for i, f in enumerate(frames):
    slot = i % 4
    col, row = slot % 2, slot // 2
    cell(f, col, row)
    nxt = frames[i + 1] if i + 1 < len(frames) else None
    if nxt and nxt['scene'] != f['scene']:
        r = 34
        if col == 0:                       # side by side, glass sits in the gutter
            gx = M + CW + GX / 2
            gy = H - M - row * (CH + GY) - CH * 0.42
        else:                              # row or page break, glass hangs off the corner
            gx = M + CW + GX + CW
            gy = H - M - row * (CH + GY) - CH * 0.42
        glass(gx, gy, r, nxt)
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
