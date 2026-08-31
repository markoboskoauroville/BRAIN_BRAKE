#!/usr/bin/env python3
"""Manan's lines to record. Portrait, one column, two panels a page.

    python3 tools/recording_batch1.py

Baba, 30.8.2026: portrait, easy to read, easy to turn. Picture, then who speaks,
then the line. Manan only.
"""
import os, hashlib, tempfile
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANIM = os.path.join(os.path.dirname(ROOT), 'ANIMATOR_COLLABORATION')
OUT = '/home/claude/out/6-BRAIN_BRAKE_MANAN_LINES_v6.pdf'
W, H = A4
M = 46

PAPER = (0.945, 0.933, 0.898)
BOX   = (0.898, 0.878, 0.827)
INK   = (0.11, 0.10, 0.09)
DIM   = (0.48, 0.45, 0.40)
BRASS = (0.58, 0.40, 0.13)

for n, p in [('B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
             ('R', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
             ('M', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')]:
    if os.path.exists(p):
        pdfmetrics.registerFont(TTFont(n, p))

_S = os.path.join(tempfile.gettempdir(), 'rec5'); os.makedirs(_S, exist_ok=True)

def small(path, maxdim=1100, q=84):
    st = os.stat(path)
    k = hashlib.md5(('%s|%d|%d' % (path, st.st_size, int(st.st_mtime))).encode()).hexdigest()[:14]
    o = os.path.join(_S, k + '.jpg')
    if not os.path.exists(o):
        im = Image.open(path).convert('RGB')
        if max(im.size) > maxdim:
            im.thumbnail((maxdim, maxdim), Image.LANCZOS)
        im.save(o, quality=q, optimize=True)
    return o

c = rl.Canvas(OUT, pagesize=A4)
PG = [0]

def bg():
    c.setFillColorRGB(*PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)

def foot():
    PG[0] += 1
    c.setFont('M', 7); c.setFillColorRGB(*DIM)
    c.drawRightString(W - M, 26, '%d' % PG[0])

def newpage():
    foot(); c.showPage(); bg()

def wrap(t, f, s, w):
    out, line = [], ''
    for word in str(t).split():
        trial = (line + ' ' + word).strip()
        if pdfmetrics.stringWidth(trial, f, s) <= w:
            line = trial
        else:
            out.append(line); line = word
    out.append(line)
    return out

B10 = os.path.join(ANIM, 'BB_C_10/build')

PANELS = [
 ('10-0-BUILD-1.png', '1', 'storytelling',
  'Nineteen twenty three. A. V. Hill puts runners on a treadmill and measures everything they do. '
  'His answer is simple.', False),
 ('10-0-BUILD-2.png', '2', 'firm', 'Fatigue is in the muscle.', True),
 ('10-0-BUILD-2.png', '3', 'neutral', 'You run, the muscle burns through its oxygen,', False),
 ('10-0-BUILD-3.png', '4', 'firm', 'The fuel runs out,', True),
 ('10-0-BUILD-4.png', '5', 'neutral', 'and when the tank reads empty,', False),
 ('10-0-BUILD-5.png', '6', 'firm', 'The body stops.', True),
 ('10-0-BUILD-5.png', '7', 'calm',
  "That's it. We're done. And for seventy four years, nobody reopened it.", False),
]

CW = W - 2*M
IMW = CW * 0.68                  # measured: 2.26 panels a page, so two fit with headroom
IMH = IMW * 9 / 16

bg()
c.setFont('B', 18); c.setFillColorRGB(*INK)
c.drawString(M, H - M - 2, 'THE BRAIN BRAKE')
c.setFont('R', 11); c.setFillColorRGB(*DIM)
c.drawString(M, H - M - 22, 'Manan, lines to record')
c.setFont('M', 7.2); c.setFillColorRGB(*BRASS)
c.drawString(M, H - M - 42, 'READ THE LINE UNDER EACH PICTURE')
c.drawString(M, H - M - 54, 'THE WORD IN BRACKETS IS HOW TO SAY IT')
c.drawString(M, H - M - 66, 'THE LINES IN BOLD A LITTLE SLOWER, SMALL PAUSE BEFORE EACH')
c.drawString(M, H - M - 78, 'TWO TAKES OF EVERYTHING')
y = H - M - 108
TOP = H - M - 6

for fn, pid, emo, line, bold in PANELS:
    fs = 14 if bold else 12
    rows = wrap('\u201c' + line + '\u201d', 'B' if bold else 'R', fs, CW - 30)
    boxh = len(rows) * (fs + 7) + 34
    blockh = 16 + IMH + 10 + boxh + 30
    if y - blockh < 46:
        newpage(); y = TOP
    c.setFont('M', 8); c.setFillColorRGB(*DIM)
    c.drawString(M, y, '[ %s ]' % pid)
    y -= 16
    p = os.path.join(B10, fn)
    if os.path.exists(p):
        iw, ih = Image.open(p).size
        s = min(IMW/iw, IMH/ih); w, h = iw*s, ih*s
        c.drawImage(ImageReader(small(p)), M, y - h, width=w, height=h, mask='auto')
        y -= h + 10
    c.setFillColorRGB(*BOX); c.rect(M, y - boxh, CW, boxh, fill=1, stroke=0)
    c.setFont('M', 7); c.setFillColorRGB(*BRASS)
    c.drawString(M + 15, y - 18, 'MANAN')
    c.setFont('R', 9.5); c.setFillColorRGB(*DIM)
    c.drawString(M + 15 + 52, y - 18, '( %s )' % emo)
    yy = y - 36
    c.setFont('B' if bold else 'R', fs); c.setFillColorRGB(*INK)
    for ln in rows:
        c.drawString(M + 15, yy, ln); yy -= fs + 7
    y -= boxh + 30

foot()
c.save()
print('written %s, %d pages, %d KB' % (OUT, PG[0], os.path.getsize(OUT)//1024))
