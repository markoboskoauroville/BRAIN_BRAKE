#!/usr/bin/env python3
"""The read-from-it script. Picture, who speaks, the line. Nothing else.

    python3 tools/recording_batch1.py

Baba, 30.8.2026: simplify. No background story, no explanation of the boards,
no craft notes. Manan opens it in the booth and reads. One beat per block, the
picture above it so he can see where he is.
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
OUT = '/home/claude/out/BRAIN_BRAKE_RECORDING_BATCH_1_v3.pdf'
W, H = A4
M = 52

PAPER = (0.976, 0.945, 0.878)
INK   = (0.11, 0.10, 0.09)
DIM   = (0.48, 0.45, 0.40)
BRASS = (0.58, 0.40, 0.13)

for n, p in [('B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
             ('R', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
             ('M', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')]:
    if os.path.exists(p):
        pdfmetrics.registerFont(TTFont(n, p))

_S = os.path.join(tempfile.gettempdir(), 'rec3'); os.makedirs(_S, exist_ok=True)

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

def newpage():
    PG[0] += 1
    c.setFont('M', 7); c.setFillColorRGB(*DIM)
    c.drawRightString(W - M, 26, '%d' % PG[0])
    c.showPage(); bg()

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

def img(path, x, y, bw, bh):
    if not os.path.exists(path): return 0
    iw, ih = Image.open(path).size
    s = min(bw/iw, bh/ih); w, h = iw*s, ih*s
    c.drawImage(ImageReader(small(path)), x + (bw-w)/2, y-h, width=w, height=h, mask='auto')
    c.setStrokeColorRGB(0.74, 0.70, 0.62); c.setLineWidth(0.5)
    c.rect(x + (bw-w)/2, y-h, w, h, fill=0, stroke=1)
    return h

B10 = os.path.join(ANIM, 'BB_C_10/build')
B11 = os.path.join(ANIM, 'BB_C_11/build')

# ------------------------------------------------------------------ cover
bg()
c.setFont('B', 24); c.setFillColorRGB(*INK)
c.drawString(M, H - 130, 'THE BRAIN BRAKE')
c.setFont('R', 13); c.setFillColorRGB(*DIM)
c.drawString(M, H - 155, 'Lines to record')
y = H - 220
for ln in wrap('Read the lines under each picture. The picture is what will be on screen while you '
               'say them.', 'R', 12.5, W - 2*M):
    c.setFont('R', 12.5); c.setFillColorRGB(*INK); c.drawString(M, y, ln); y -= 18
y -= 18
for ln in wrap('The lines in bold are the important ones. Small pause before each, then say it a '
               'little slower.', 'R', 12.5, W - 2*M):
    c.setFont('R', 12.5); c.setFillColorRGB(*INK); c.drawString(M, y, ln); y -= 18
y -= 18
for ln in wrap('Two takes of everything, please.', 'R', 12.5, W - 2*M):
    c.setFont('R', 12.5); c.setFillColorRGB(*INK); c.drawString(M, y, ln); y -= 18
newpage()

def block(state, who, line, bold):
    """One picture, who says it, the line. That is the whole document."""
    global c
    IMW = (W - 2*M) * 0.52          # small enough that three blocks fit a page
    imh = IMW * 9 / 16
    fs = 15 if bold else 13
    rows = wrap(line, 'B' if bold else 'R', fs, IMW)
    need = imh + 22 + len(rows) * (fs + 7) + 34
    if block.y - need < 60:
        newpage(); block.y = H - M - 6
    y = block.y
    if state:
        img(os.path.join(state[0], state[1]), M, y, IMW, imh)
        y -= imh + 20
    c.setFont('M', 8); c.setFillColorRGB(*BRASS)
    c.drawString(M, y, who.upper())
    y -= 20
    c.setFont('B' if bold else 'R', fs); c.setFillColorRGB(*INK)
    for ln in rows:
        c.drawString(M, y, ln); y -= fs + 7
    block.y = y - 26
block.y = H - M - 6

BLOCKS = [
 ((B10,'10-0-BUILD-1.png'), 'MANAN',
  'Nineteen twenty three. A. V. Hill puts runners on a treadmill and measures everything they do. '
  'His answer is simple.', False),
 ((B10,'10-0-BUILD-2.png'), 'MANAN', 'Fatigue is in the muscle.', True),
 (None, 'MANAN', 'You run, the muscle burns through its oxygen,', False),
 ((B10,'10-0-BUILD-3.png'), 'MANAN', 'The fuel runs out,', True),
 ((B10,'10-0-BUILD-4.png'), 'MANAN', 'and when the tank reads empty,', False),
 ((B10,'10-0-BUILD-5.png'), 'MANAN', 'The body stops.', True),
 (None, 'MANAN', "That's it. We're done. And for seventy four years, nobody reopened it.", False),
 ((B11,'11-0-BUILD-1.png'), 'COACH BRAIN',
  'Heart rate. Breath. Temperature. Water. Distance. I read all of it, all the time, and I ask one '
  'question. Can we keep going safely?', False),
 (None, 'COACH BRAIN', 'When the answer starts to look like no, I slow you down. So no.', False),
 ((B11,'11-0-BUILD-2.png'), 'COACH BRAIN', 'Fatigue is in the brain.', True),
 (None, 'COACH BRAIN', 'Not in your legs. Up here. And I decide long before anything is actually wrong.', False),
 ((B11,'11-0-BUILD-3.png'), 'COACH BRAIN', 'It decides when to stop.', True),
 ((B11,'11-0-BUILD-4.png'), 'COACH BRAIN', 'And here is the part nobody tells you. When I stop you,', False),
 ((B11,'11-0-BUILD-5.png'), 'COACH BRAIN', 'The fuel is still there.', True),
 (None, 'COACH BRAIN', 'There is always something left. I am just not letting you spend it.', False),
]
for st, who, line, bold in BLOCKS:
    block(st, who, line, bold)

PG[0] += 1
c.setFont('M', 7); c.setFillColorRGB(*DIM); c.drawRightString(W - M, 26, '%d' % PG[0])
c.save()
print('written %s, %d pages, %d KB' % (OUT, PG[0], os.path.getsize(OUT)//1024))
