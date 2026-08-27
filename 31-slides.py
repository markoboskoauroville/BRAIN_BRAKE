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
    text = (fr.get('text') or '').strip()
    who = (fr.get('who') or '').strip()

    # the panel fills the frame, and the line is a subtitle over the bottom of it
    p = os.path.join(IMG, fr['img'])
    if os.path.exists(p):
        src = Image.open(p).convert('RGB')
        im = src.resize((W, H), Image.LANCZOS)
    else:
        im = Image.new('RGB', (W, H), BOX)
        d0 = ImageDraw.Draw(im)
        t = 'live footage'; ff = F(DB, 46)
        d0.text((W // 2 - d0.textlength(t, font=ff) // 2, H // 2 - 24), t, font=ff, fill=SOFT)

    d = ImageDraw.Draw(im, 'RGBA')
    d.text((44, 34), '[ %s ]' % fr['id'], font=F(MB, 26), fill=(138, 107, 46, 220))

    if text:
        size = 46 if len(text) < 70 else (38 if len(text) < 120 else 32)
        ft = F(DB, size)
        body = wrap(d, '\u201c' + text + '\u201d', ft, int(W * 0.84))
        lh = int(size * 1.34)
        block = len(body) * lh + 46
        d.rectangle([0, H - block, W, H], fill=(20, 18, 15, 205))
        d.text((W // 2 - d.textlength(who.upper(), font=F(MB, 17)) // 2, H - block + 14),
               who.upper(), font=F(MB, 17), fill=(198, 162, 92, 255))
        yy = H - block + 44
        for ln in body:
            d.text((W // 2 - d.textlength(ln, font=ft) // 2, yy), ln, font=ft,
                   fill=(246, 242, 232, 255))
            yy += lh

    im.save('%s/%s.jpg' % (OUT, fr['id'].replace('.', '_')), quality=92)

print('rebuilt %d slides from %s' % (len(frames), os.path.basename(SRC)))
