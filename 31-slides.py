#!/usr/bin/env python3
"""Rebuild every timeline slide from the film. Same filenames, always.

The slides in assets/slides are the picture track of BB_ANIMATICS_FINAL. They
carry the panel, its frame number and its line. Whenever the film changes, run
this. The filenames never change, so Claude Code pulls the repo and the slides
are replaced in place with nothing to rewire.

Prefers assets/train/frames_v5.json, falls back to v4.

    python3 31-slides.py
"""
from PIL import Image, ImageDraw, ImageFont
import json, os

REPO = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO, 'assets/train/frames_v5.json')
if not os.path.exists(SRC):
    SRC = os.path.join(REPO, 'assets/train/frames_v4.json')
OUT = os.path.join(REPO, 'assets/slides')
IMG = os.path.join(REPO, 'assets/V7')
os.makedirs(OUT, exist_ok=True)

DB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MB = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
F = lambda p, s: ImageFont.truetype(p, s)
W, H = 1920, 1080
PAPER = (242, 235, 218); INK = (34, 31, 25); BOX = (230, 220, 196)
RULE = (205, 191, 164); SOFT = (138, 129, 112); ACC = (138, 107, 46)


def wrap(d, t, f, mw):
    o, l = [], ""
    for w in t.split():
        tr = (l + " " + w).strip()
        if d.textlength(tr, font=f) <= mw:
            l = tr
        else:
            if l: o.append(l)
            l = w
    if l: o.append(l)
    return o


for f in os.listdir(OUT):
    if f.endswith('.jpg'):
        os.remove(os.path.join(OUT, f))

frames = json.load(open(SRC))
for fr in frames:
    # the panel fills the frame. the ONLY thing added is the frame number,
    # bottom centre, so the number is visible on the timeline as well as in
    # the filename. no dialogue, no speaker, nothing else.
    p = os.path.join(IMG, fr['img'])
    if os.path.exists(p):
        im = Image.open(p).convert('RGB').resize((W, H), Image.LANCZOS)
    else:
        im = Image.new('RGB', (W, H), BOX)
        d0 = ImageDraw.Draw(im)
        t = 'live footage'; ff = F(DB, 46)
        d0.text((W // 2 - d0.textlength(t, font=ff) // 2, H // 2 - 24), t, font=ff, fill=SOFT)

    d = ImageDraw.Draw(im, 'RGBA')
    tag = '[ %s ]' % fr['id']
    ft = F(MB, 34)
    tw_ = d.textlength(tag, font=ft)
    pad = 16
    bx0 = W / 2 - tw_ / 2 - pad; bx1 = W / 2 + tw_ / 2 + pad
    by1 = H - 26; by0 = by1 - 48
    d.rectangle([bx0, by0, bx1, by1], fill=(20, 18, 15, 190))
    d.text((W / 2 - tw_ / 2, by0 + 8), tag, font=ft, fill=(226, 196, 132, 255))

    im.save('%s/%s.jpg' % (OUT, fr['id'].replace('.', '_')), quality=92)

print('rebuilt %d slides from %s' % (len(frames), os.path.basename(SRC)))
