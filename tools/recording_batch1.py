#!/usr/bin/env python3
"""Build the batch 1 recording script as a PDF.

    python3 tools/recording_batch1.py

Two voices, the two theory sections, with the board sync written next to every
line so the person recording can hear where the chalk lands.

Images come from the animator repo. Downscaled before embedding, because a
read-through reached 137 MB doing otherwise and GitHub rejected the push.
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
OUT = '/home/claude/out/BRAIN_BRAKE_RECORDING_BATCH_1_v1.pdf'
W, H = A4
M = 46

PAPER = (0.976, 0.945, 0.878)
INK = (0.10, 0.09, 0.08)
DIM = (0.42, 0.40, 0.36)
BRASS = (0.58, 0.40, 0.13)
RED = (0.55, 0.18, 0.12)

for n, p in [('B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'),
             ('R', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
             ('M', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'),
             ('MB', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf')]:
    if os.path.exists(p):
        pdfmetrics.registerFont(TTFont(n, p))

_S = os.path.join(tempfile.gettempdir(), 'rec_small')
os.makedirs(_S, exist_ok=True)


def small(path, maxdim=1400, q=82):
    st = os.stat(path)
    k = hashlib.md5(('%s|%d|%d' % (path, st.st_size, int(st.st_mtime))).encode()).hexdigest()[:16]
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
    c.setFillColorRGB(*PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def newpage(label=''):
    PG[0] += 1
    c.setFont('M', 7)
    c.setFillColorRGB(*DIM)
    c.drawString(M, 24, label)
    c.drawRightString(W - M, 24, str(PG[0]))
    c.showPage()
    bg()


def wrap(t, f, s, w):
    out = []
    for para in str(t).split('\n'):
        line = ''
        for word in para.split():
            trial = (line + ' ' + word).strip()
            if pdfmetrics.stringWidth(trial, f, s) <= w:
                line = trial
            else:
                out.append(line)
                line = word
        out.append(line)
    return out


def para(x, y, t, w, size=9.4, lead=13, font='R', col=INK):
    c.setFont(font, size)
    c.setFillColorRGB(*col)
    for ln in wrap(t, font, size, w):
        c.drawString(x, y, ln)
        y -= lead
    return y


def head(y, t, sub=''):
    c.setFont('B', 15)
    c.setFillColorRGB(*INK)
    c.drawString(M, y, t)
    if sub:
        c.setFont('M', 7.5)
        c.setFillColorRGB(*DIM)
        c.drawString(M + pdfmetrics.stringWidth(t, 'B', 15) + 10, y + 1, sub)
    c.setStrokeColorRGB(*BRASS)
    c.setLineWidth(1)
    c.line(M, y - 7, W - M, y - 7)
    return y - 24


def img(path, x, y, bw, bh):
    if not os.path.exists(path):
        return 0
    iw, ih = Image.open(path).size
    s = min(bw / iw, bh / ih)
    w, h = iw * s, ih * s
    c.drawImage(ImageReader(small(path)), x, y - h, width=w, height=h, mask='auto')
    c.setStrokeColorRGB(0.74, 0.70, 0.62)
    c.setLineWidth(0.5)
    c.rect(x, y - h, w, h, fill=0, stroke=1)
    return h


# ------------------------------------------------------------------ cover
bg()
c.setFont('B', 26)
c.setFillColorRGB(*INK)
c.drawString(M, H - 120, 'THE BRAIN BRAKE')
c.setFont('B', 15)
c.drawString(M, H - 146, 'Recording script, batch one')
c.setFont('M', 9)
c.setFillColorRGB(*BRASS)
c.drawString(M, H - 172, 'THE TWO THEORY SECTIONS   ·   MANAN AND COACH BRAIN')

y = H - 220
y = para(M, y, 'This is the first batch. Two sections only, the old theory and the new one. '
         'Everything else in the film is already recorded and is not touched here.', W - 2 * M)
y -= 8
y = para(M, y, 'These lines are new. They exist because the boards say things the recorded voice never '
         'says, and in these two sections the writing on the board appears as it is spoken. So the '
         'voice has to carry the whole theory and the board catches only the phrases, the way somebody '
         'takes notes in a lecture.', W - 2 * M)
y -= 8
y = para(M, y, 'The bold phrases in the script are the moments the chalk or the marker writes. Land on '
         'them. Everything around them is ordinary speech and should sound like thinking out loud, not '
         'like reciting.', W - 2 * M)
y -= 16
c.setFillColorRGB(*RED)
c.setFont('B', 10)
c.drawString(M, y, 'Send this batch back before recording anything else.')
y -= 14
para(M, y, 'If the timing or the wording is wrong we would rather find out on two sections than on all '
     'of them.', W - 2 * M, col=DIM)

c.setFont('M', 7.5)
c.setFillColorRGB(*DIM)
c.drawCentredString(W / 2, 60, 'markoboskoauroville.github.io/ANIMATOR_COLLABORATION')
newpage('recording script, batch one')

# ------------------------------------------------------------------ Manan
y = head(H - M - 6, 'One.  Manan', 'the old theory, 1923')
h = img(os.path.join(ANIM, 'BB_C_10/10-0-A-v2.png'), M, y, W - 2 * M, 190)
y -= h + 14
y = para(M, y, 'He has read this in a book and he believes it. He is not performing scepticism yet. He is '
         'laying out the answer everybody accepted, and he finds it satisfying, which is what makes it '
         'land when it turns out to be wrong.', W - 2 * M, col=DIM)
y -= 10

c.setFont('M', 8)
c.setFillColorRGB(*BRASS)
c.drawString(M, y, 'SCRIPT')
y -= 16

SCRIPT_MANAN = [
    ('Nineteen twenty three. A. V. Hill puts runners on a treadmill and measures everything '
     'they do.', None),
    ('His answer is simple.', None),
    ('FATIGUE IS IN THE MUSCLE.', 'chalk writes it'),
    ('You run, the muscle burns through its oxygen,', None),
    ('THE FUEL RUNS OUT,', 'chalk writes it'),
    ('and when the tank reads empty,', 'gauge appears at EMPTY'),
    ('THE BODY STOPS.', 'chalk writes it'),
    ("That's it. We're done. And for seventy four years, nobody reopened it.", None),
]
for line, cue in SCRIPT_MANAN:
    bold = cue is not None and 'writes' in cue
    f = 'B' if bold else 'R'
    yy = para(M + 10, y, line, W - 2 * M - 150, size=11 if bold else 10.4, lead=14.5, font=f)
    if cue:
        c.setFont('M', 7)
        c.setFillColorRGB(*BRASS)
        c.drawRightString(W - M, y, cue.upper())
    y = yy - 7

y -= 8
y = para(M, y, 'Timing: about eighteen seconds at an unhurried pace. Do not rush the three bold lines, '
         'the drawing has to keep up with them.', W - 2 * M, col=DIM, size=8.6)
newpage('one, Manan, the old theory')

# ------------------------------------------------------------------ Coach Brain
y = head(H - M - 6, 'Two.  Coach Brain', 'the new theory')
h = img(os.path.join(ANIM, 'BB_C_11/11-0-A-v1.png'), M, y, W - 2 * M, 190)
y -= h + 14
y = para(M, y, 'He is not a villain and not a machine. He is the one who has been doing this job quietly '
         'the whole time and is slightly amused to be found out. Warm, dry, unhurried. He is explaining '
         'something obvious to somebody who has finally asked.', W - 2 * M, col=DIM)
y -= 10

c.setFont('M', 8)
c.setFillColorRGB(*BRASS)
c.drawString(M, y, 'SCRIPT')
y -= 16

SCRIPT_BRAIN = [
    ('Heart rate. Breath. Temperature. Water. Distance.', None),
    ('I read all of it, all the time, and I ask one question. Can we keep going safely?', None),
    ('When the answer starts to look like no, I slow you down. So no.', None),
    ('FATIGUE IS IN THE BRAIN.', 'marker writes it'),
    ('Not in your legs. Up here. And I decide long before anything is actually wrong.', None),
    ('IT DECIDES WHEN TO STOP.', 'marker writes it'),
    ('And here is the part nobody tells you. When I stop you,', None),
    ('THE FUEL IS STILL THERE.', 'marker writes it'),
    ('There is always something left. I am just not letting you spend it.', None),
]
for line, cue in SCRIPT_BRAIN:
    bold = cue is not None and 'writes' in cue
    f = 'B' if bold else 'R'
    yy = para(M + 10, y, line, W - 2 * M - 150, size=11 if bold else 10.4, lead=14.5, font=f)
    if cue:
        c.setFont('M', 7)
        c.setFillColorRGB(*BRASS)
        c.drawRightString(W - M, y, cue.upper())
    y = yy - 7

y -= 8
para(M, y, 'Timing: about twenty two seconds. The three bold lines are the argument; everything else is '
     'him being reasonable.', W - 2 * M, col=DIM, size=8.6)
newpage('two, Coach Brain, the new theory')

# ------------------------------------------------------------------ the inversion
y = head(H - M - 6, 'Why the two boards are opposites')
bw = (W - 2 * M - 14) / 2
h1 = img(os.path.join(ANIM, 'BB_C_10/10-0-A-v2.png'), M, y, bw, 150)
img(os.path.join(ANIM, 'BB_C_11/11-0-A-v1.png'), M + bw + 14, y, bw, 150)
y -= max(h1, 150) + 16
y = para(M, y, 'Blackboard and white chalk for the old theory. Whiteboard and black marker for the new '
         'one. Same layout, same three lines, same fuel gauge, every value reversed. The audience feels '
         'the reversal before they follow the argument, which is the same trick the frame rate plays '
         'elsewhere in the film: the form carries the meaning and nobody has to be told.', W - 2 * M)
y -= 8
y = para(M, y, 'The gauge does the real work. It is the same instrument in both frames with the needle '
         'moved from EMPTY to FULL. That says the fuel was always there without a word being spoken.',
         W - 2 * M)
y -= 14
y = para(M, y, 'The drawing style for both sections is RSA Animate, the series drawn by Andrew Park at '
         'Cognitive Media. A hand draws the argument while the voice explains it, in real time, and the '
         'board is never revealed finished. Four of them are linked on the film site under phases ten '
         'and eleven.', W - 2 * M)
newpage('the inversion')

c.save()
print('written %s, %d pages, %d KB' % (OUT, PG[0], os.path.getsize(OUT) // 1024))
