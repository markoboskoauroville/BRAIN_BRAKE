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
OUT = '/home/claude/out/7-BRAIN_BRAKE_COACH_BRAIN_LINES_v7.pdf'
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

B10 = os.path.join(ANIM, 'BB_C_11/build')

PANELS = [
 ('11-0-BUILD-1.png', '1', 'announcer',
  'Heart rate. Breath. Temperature. Water. Distance. I read all of it, all the time, and I ask one '
  'question. Can we keep going safely?', False),
 ('11-0-BUILD-1.png', '2', 'calm',
  'When the answer starts to look like no, I slow you down. So no.', False),
 ('11-0-BUILD-2.png', '3', 'firm', 'Fatigue is in the brain.', True),
 ('11-0-BUILD-2.png', '4', 'kind',
  'Not in your legs. Up here. And I decide long before anything is actually wrong.', False),
 ('11-0-BUILD-3.png', '5', 'firm', 'It decides when to stop.', True),
 ('11-0-BUILD-4.png', '6', 'storytelling',
  'And here is the part nobody tells you. When I stop you,', False),
 ('11-0-BUILD-5.png', '7', 'firm', 'The fuel is still there.', True),
 ('11-0-BUILD-5.png', '8', 'kind',
  'There is always something left. I am just not letting you spend it.', False),
]

CW = W - 2*M
IMW = CW * 0.68                  # measured: 2.26 panels a page, so two fit with headroom
IMH = IMW * 9 / 16

bg()
c.setFont('B', 18); c.setFillColorRGB(*INK)
c.drawString(M, H - M - 2, 'THE BRAIN BRAKE')
c.setFont('R', 11); c.setFillColorRGB(*DIM)
c.drawString(M, H - M - 22, 'Coach Brain, lines to record')
c.setFont('M', 7.2); c.setFillColorRGB(*BRASS)
c.drawString(M, H - M - 42, 'READ THE LINE UNDER EACH PICTURE')
c.drawString(M, H - M - 54, 'THE WORD IN BRACKETS IS HOW TO SAY IT')
c.drawString(M, H - M - 66, 'THE LINES IN BOLD A LITTLE SLOWER, SMALL PAUSE BEFORE EACH')
c.drawString(M, H - M - 78, 'TWO TAKES OF EVERYTHING')
y = H - M - 108

# ------------------------------------------------- the acting page comes first
def actingpage():
    global y
    def P(t, size=11, lead=15.5, font='R', col=INK, gap=10):
        global y
        c.setFont(font, size); c.setFillColorRGB(*col)
        for ln in wrap(t, font, size, W - 2*M):
            c.drawString(M, y, ln); y -= lead
        y -= gap
    c.setFont('B', 16); c.setFillColorRGB(*INK)
    c.drawString(M, y, 'You are playing somebody else now')
    y -= 12
    c.setStrokeColorRGB(*BRASS); c.setLineWidth(1); c.line(M, y, W - M, y)
    y -= 22
    P('In the first batch you were yourself. A boy who read something in a book and is telling us '
      'about it. That is easy because it is true.')
    P('These lines are different. This is Coach Brain, and he is not you. He lives in your head, he '
      'has been quietly deciding when you stop for your whole life, and he is only talking now '
      'because you finally found him.')
    c.setFont('B', 12); c.setFillColorRGB(*INK)
    c.drawString(M, y, 'The difference, in one thing')
    y -= 20
    P('When you are yourself, you are working something out while you speak. There is effort in it. '
      'You are a little excited, because you have just understood something.')
    P('Coach Brain is not working anything out. He has known all of it for years. He is explaining '
      'something obvious to somebody who has finally asked the right question. So there is no effort '
      'and no excitement. He is unhurried, and a bit amused to have been caught.')
    c.setFont('B', 12); c.setFillColorRGB(*INK)
    c.drawString(M, y, 'How to make it sound like a different person')
    y -= 20
    P('Do not do a voice. No accent, no growl, no robot. If you try to sound like a character it will '
      'sound like a boy doing an impression, and the audience will stop listening to the words.')
    P('Change these three things instead, and let the voice stay your own.')
    P('SLOWER. He is never in a hurry. He has all the time there is.', font='B', size=11, gap=6)
    P('LOWER AND FLATTER. Take the lift out of the end of your sentences. You go up at the end when '
      'you are excited. He does not.', font='B', size=11, gap=6)
    P('WARMER, NOT COLDER. He is not a villain and not a machine. He likes you. He has been looking '
      'after you the whole time and you never noticed.', font='B', size=11, gap=10)
    c.setFont('B', 12); c.setFillColorRGB(*INK)
    c.drawString(M, y, 'One image that helps')
    y -= 20
    P('He is not a scientist and not a computer. He is more like a doctor who has known you since you '
      'were small, sitting back in his chair, telling you something he assumed you already knew.')
    P('If you find yourself pushing, stop and start again slower. Almost every mistake in this section '
      'is going too fast.')
    newpage()
    y = H - M - 6          # the panel loop starts from the top of the fresh page,
                           # otherwise its own page check fires and leaves a blank one
actingpage()
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
    c.drawString(M + 15, y - 18, 'COACH BRAIN')
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
