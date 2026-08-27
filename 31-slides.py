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
    im = Image.new('RGB', (W, H), PAPER); d = ImageDraw.Draw(im)
    text = (fr.get('text') or '').strip(); who = (fr.get('who') or '').strip()
    M = 52; CWD = W - 2 * M
    size = 44 if len(text) < 70 else (36 if len(text) < 120 else 30)
    ft = F(DB, size)
    body = wrap(d, '\u201c' + text + '\u201d', ft, CWD - 44) if text else []
    block = (64 + len(body) * int(size * 1.34) + 30) if text else 0
    top = 76; avail = H - top - 44 - (block + 26 if text else 0)
    d.text((M, 28), '[ %s ]' % fr['id'], font=F(MB, 26), fill=ACC)
    p = os.path.join(IMG, fr['img'])
    if os.path.exists(p):
        src = Image.open(p).convert('RGB'); iw, ih = src.size
        w = CWD; h = int(w * ih / iw)
        if h > avail:
            h = avail; w = int(h * iw / ih)
        src = src.resize((w, h), Image.LANCZOS)
        x = M + (CWD - w) // 2
        im.paste(src, (x, top))
        d.rectangle([x, top, x + w - 1, top + h - 1], outline=RULE, width=1)
        y = top + h + 26
    else:
        h = min(avail, int(CWD * 9 / 16))
        d.rectangle([M, top, M + CWD, top + h], fill=BOX, outline=RULE)
        t = 'live footage'; ff = F(DB, 26)
        d.text((W // 2 - d.textlength(t, font=ff) // 2, top + h // 2 - 14), t, font=ff, fill=SOFT)
        y = top + h + 26
    if text:
        d.rectangle([M, y, M + CWD, y + block], fill=BOX)
        d.rectangle([M, y, M + 5, y + block], fill=ACC)
        d.text((M + 26, y + 18), who.upper(), font=F(MB, 17), fill=ACC)
        yy = y + 62
        for ln in body:
            d.text((M + 26, yy), ln, font=ft, fill=INK); yy += int(size * 1.34)
    im.save('%s/%s.jpg' % (OUT, fr['id'].replace('.', '_')), quality=92)

print('rebuilt %d slides from %s' % (len(frames), os.path.basename(SRC)))
