#!/usr/bin/env python3
"""The studio recording pack. Printed, taken into the booth, read from.

    python3 tools/recording_batch1.py

This is the ONLY thing Neha and the studio need. Two sections, nothing else from
the film. Every spoken line carries the board beside it exactly as it stands at
that moment, so whoever records can see what the drawing is doing while they
speak.

Board states come from the animator repo. Downscaled before embedding: a
read-through once reached 137 MB and GitHub refused the push.
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
OUT = '/home/claude/out/BRAIN_BRAKE_RECORDING_BATCH_1_v2.pdf'
W, H = A4
M = 44

PAPER = (0.976, 0.945, 0.878)
CARD  = (0.957, 0.918, 0.847)
INK   = (0.11, 0.10, 0.09)
DIM   = (0.45, 0.42, 0.38)
BRASS = (0.58, 0.40, 0.13)

for n, p in [('B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
             ('R', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
             ('M', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')]:
    if os.path.exists(p):
        pdfmetrics.registerFont(TTFont(n, p))

_S = os.path.join(tempfile.gettempdir(), 'rec2'); os.makedirs(_S, exist_ok=True)

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

def foot(label=''):
    PG[0] += 1
    c.setFont('M', 6.8); c.setFillColorRGB(*DIM)
    c.drawString(M, 22, label); c.drawRightString(W - M, 22, '%d' % PG[0])

def newpage(label=''):
    foot(label); c.showPage(); bg()

def wrap(t, f, s, w):
    out = []
    for pr in str(t).split('\n'):
        line = ''
        for word in pr.split():
            trial = (line + ' ' + word).strip()
            if pdfmetrics.stringWidth(trial, f, s) <= w:
                line = trial
            else:
                out.append(line); line = word
        out.append(line)
    return out

def para(x, y, t, w, size=9.2, lead=12.6, font='R', col=INK):
    c.setFont(font, size); c.setFillColorRGB(*col)
    for ln in wrap(t, font, size, w):
        c.drawString(x, y, ln); y -= lead
    return y

def img(path, x, y, bw, bh):
    if not os.path.exists(path): return 0, 0
    iw, ih = Image.open(path).size
    s = min(bw/iw, bh/ih); w, h = iw*s, ih*s
    c.drawImage(ImageReader(small(path)), x, y-h, width=w, height=h, mask='auto')
    c.setStrokeColorRGB(0.72, 0.68, 0.60); c.setLineWidth(0.5)
    c.rect(x, y-h, w, h, fill=0, stroke=1)
    return w, h

def rule(y):
    c.setStrokeColorRGB(*BRASS); c.setLineWidth(1); c.line(M, y, W-M, y)

B10 = os.path.join(ANIM, 'BB_C_10/build')
B11 = os.path.join(ANIM, 'BB_C_11/build')

# ---------------------------------------------------------------- cover
bg()
c.setFillColorRGB(*CARD); c.rect(0, H-236, W, 236, fill=1, stroke=0)
c.setFont('B', 26); c.setFillColorRGB(*INK); c.drawString(M, H-104, 'THE BRAIN BRAKE')
c.setFont('R', 13.5); c.setFillColorRGB(*DIM); c.drawString(M, H-128, 'Recording script for the studio')
c.setFont('M', 8.4); c.setFillColorRGB(*BRASS)
c.drawString(M, H-164, 'BATCH ONE   \xb7   TWO SECTIONS ONLY   \xb7   MANAN AND COACH BRAIN')
c.setFont('M', 7.2); c.setFillColorRGB(*DIM)
c.drawString(M, H-181, 'Mantra Productions   \xb7   Breakthrough Junior Challenge 2026')

y = H-286
y = para(M, y, 'This is a short session. Two sections, nothing else from the film. Everything else has '
         'already been recorded and is not touched here.', W-2*M, size=10.4, lead=14)
y -= 12
y = para(M, y, 'These lines are new. In both sections the words appear on a board as they are spoken, '
         'drawn by hand in real time. The voice carries the whole idea and the board catches only the '
         'phrases, the way somebody takes notes in a lecture.', W-2*M, size=10.4, lead=14)
y -= 12
y = para(M, y, 'On the pages that follow, each line is printed with the board beside it exactly as it '
         'stands at that moment. The bold lines are the ones the chalk or the marker writes. Land on '
         'them: a small beat before, then say them cleanly and a little slower. Everything between them '
         'is ordinary speech and should sound like thinking out loud, not reciting.',
         W-2*M, size=10.4, lead=14)
y -= 24
rule(y); y -= 20
c.setFont('B', 11); c.setFillColorRGB(*INK); c.drawString(M, y, 'Two takes of each, please.')
y -= 16
y = para(M, y, 'One at the pace marked, one a little slower. We would rather choose in the edit than ask '
         'for the room again.', W-2*M, size=10, lead=13.4)
y -= 18
c.setFont('B', 11); c.setFillColorRGB(*INK); c.drawString(M, y, 'Timing.')
y -= 16
para(M, y, 'Manan runs about eighteen seconds, Coach Brain about twenty two. Much shorter means it is '
     'being rushed and the drawing cannot keep up.', W-2*M, size=10, lead=13.4)
newpage('the brain brake, recording script, batch one')

def section(title, sub, who, lines, tail):
    global c
    y = H - M - 4
    c.setFont('B', 17); c.setFillColorRGB(*INK); c.drawString(M, y, title)
    c.setFont('M', 8); c.setFillColorRGB(*BRASS)
    c.drawString(M + pdfmetrics.stringWidth(title, 'B', 17) + 12, y+2, sub)
    y -= 10; rule(y); y -= 18
    y = para(M, y, who, W-2*M, size=9.4, lead=12.6, col=DIM)
    y -= 18
    IMW = 172; TXW = W - 2*M - IMW - 20
    for text, cue, state in lines:
        bold = cue is not None
        fs = 11.6 if bold else 10.6
        rows = wrap(text, 'B' if bold else 'R', fs, TXW)
        imh = (IMW*9/16) if state else 0
        blockh = max(len(rows)*15.4 + (12 if cue else 4), imh + 14)
        if y - blockh < 74:
            newpage(title.lower()); y = H - M - 10
        if state:
            img(os.path.join(state[0], state[1]), W-M-IMW, y+6, IMW, imh)
            c.setFont('M', 6.3); c.setFillColorRGB(*DIM)
            c.drawRightString(W-M, y+6-imh-9, state[2].upper())
        c.setFont('B' if bold else 'R', fs); c.setFillColorRGB(*INK)
        yy = y
        for ln in rows:
            c.drawString(M + (10 if bold else 0), yy, ln); yy -= 15.4
        if cue:
            c.setFont('M', 6.5); c.setFillColorRGB(*BRASS)
            c.drawString(M + 10, yy + 3, cue.upper())
        y -= blockh + 6
    y -= 4; rule(y); y -= 16
    para(M, y, tail, W-2*M, size=9, lead=12, col=DIM)
    newpage(title.lower())

section('One.  Manan', 'the old theory, 1923',
  'He has read this in a book and he believes it. He is not being sceptical yet. He is laying out the '
  'answer everybody accepted, and he finds it satisfying, which is what makes it land when it turns '
  'out to be wrong.',
  [('Nineteen twenty three. A. V. Hill puts runners on a treadmill and measures everything they do. '
    'His answer is simple.', None, (B10, '10-0-BUILD-1.png', 'the arm is already drawn')),
   ('FATIGUE IS IN THE MUSCLE.', 'chalk writes it', (B10, '10-0-BUILD-2.png', 'first line appears')),
   ('You run, the muscle burns through its oxygen,', None, None),
   ('THE FUEL RUNS OUT,', 'chalk writes it', (B10, '10-0-BUILD-3.png', 'second line appears')),
   ('and when the tank reads empty,', None, (B10, '10-0-BUILD-4.png', 'the gauge appears at empty')),
   ('THE BODY STOPS.', 'chalk writes it', (B10, '10-0-BUILD-5.png', 'the board is complete')),
   ("That's it. We're done. And for seventy four years, nobody reopened it.", None, None)],
  'About eighteen seconds at an unhurried pace. Do not rush the three bold lines; the drawing has to '
  'keep up with them.')

section('Two.  Coach Brain', 'the new theory',
  'He is not a villain and not a machine. He has been doing this job quietly the whole time and is '
  'slightly amused to be found out. Warm, dry, unhurried. He is explaining something obvious to '
  'somebody who has finally asked.',
  [('Heart rate. Breath. Temperature. Water. Distance. I read all of it, all the time, and I ask one '
    'question. Can we keep going safely?', None, (B11, '11-0-BUILD-1.png', 'the brain is already drawn')),
   ('When the answer starts to look like no, I slow you down. So no.', None, None),
   ('FATIGUE IS IN THE BRAIN.', 'marker writes it', (B11, '11-0-BUILD-2.png', 'first line appears')),
   ('Not in your legs. Up here. And I decide long before anything is actually wrong.', None, None),
   ('IT DECIDES WHEN TO STOP.', 'marker writes it', (B11, '11-0-BUILD-3.png', 'second line appears')),
   ('And here is the part nobody tells you. When I stop you,', None,
    (B11, '11-0-BUILD-4.png', 'the gauge appears at full')),
   ('THE FUEL IS STILL THERE.', 'marker writes it', (B11, '11-0-BUILD-5.png', 'the board is complete')),
   ('There is always something left. I am just not letting you spend it.', None, None)],
  'About twenty two seconds. The three bold lines are the argument; everything else is him being '
  'reasonable.')

y = H - M - 4
c.setFont('B', 17); c.setFillColorRGB(*INK)
c.drawString(M, y, 'Why the two boards are opposites')
y -= 10; rule(y); y -= 18
bw = (W - 2*M - 16)/2
_, hh = img(os.path.join(B10, '10-0-BUILD-5.png'), M, y, bw, 150)
img(os.path.join(B11, '11-0-BUILD-5.png'), M+bw+16, y, bw, 150)
y -= max(hh, 120) + 20
y = para(M, y, 'Blackboard and white chalk for the old theory. Whiteboard and black marker for the new '
         'one. Same layout, same three lines, same fuel gauge, every value reversed. The audience feels '
         'the reversal before they follow the argument.', W-2*M, size=10, lead=13.4)
y -= 10
y = para(M, y, 'The gauge does the real work. It is the same instrument in both, with the needle moved '
         'from empty to full. That says the fuel was always there without a word being spoken.',
         W-2*M, size=10, lead=13.4)
y -= 22
c.setFont('B', 11); c.setFillColorRGB(*INK); c.drawString(M, y, 'What we need back')
y -= 16
para(M, y, 'Two takes of each section, as recorded, with no processing and no noise reduction. WAV if '
     'the studio can, otherwise the highest quality the room offers. Send them as they are and we will '
     'do the rest.', W-2*M, size=10, lead=13.4)
foot('why the two boards are opposites')
c.save()
print('written %s, %d pages, %d KB' % (OUT, PG[0], os.path.getsize(OUT)//1024))
