#!/usr/bin/env python3
"""Is the top of the head cut off?

    python3 tools/check_headroom.py <image> [<image> ...]

Measures the ink in the picture and reports how much clear paper sits above it.
The rule this enforces is in nanobanana.md: the whole head, including the top of
the hair, is always inside the picture. A head that runs off the top edge is a
reject, and the fix is to zoom out until the hair has paper above it.

Why a script. "Does it look cut off" is a squint. Ink touching row zero is a
measurement, and it takes a second.

Exit code 1 if any image fails, so it can sit in a check sweep.
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

# a head that ends this close to the top edge is either cut or about to be
MIN_TOP_CLEARANCE = 0.015          # 1.5% of the height, about 23px on a 1536 frame


def find_border(fig):
    """Older artwork carries a hand drawn panel border. The border is ink, so a
    naive measurement reports every bordered frame as clipped. Find the rectangle
    and measure inside it instead.

    This was written after the first version of this script reported 54 of the 63
    V7 frames as cut at the top, which was the border every time and not one head.
    """
    h, w = fig.shape
    rows = fig.mean(axis=1)
    cols = fig.mean(axis=0)
    top = max([i for i in range(int(h * .14)) if rows[i] > .55] or [-1])
    bot = min([i for i in range(int(h * .86), h) if rows[i] > .55] or [h])
    lef = max([i for i in range(int(w * .14)) if cols[i] > .55] or [-1])
    rig = min([i for i in range(int(w * .86), w) if cols[i] > .55] or [w])
    if top < 0 and bot >= h and lef < 0 and rig >= w:
        return None
    pad = 3
    return (max(top + pad, 0), min(bot - pad, h), max(lef + pad, 0), min(rig - pad, w))


def ink_box(path):
    """Where the drawing actually is. Local contrast, not absolute darkness:
    a dark frame makes everything dark, and the figure is what is dark
    AGAINST its surroundings. See nanobanana.md, MEASURE DO NOT SQUINT."""
    im = Image.open(path).convert('L')
    L = np.asarray(im).astype(float)
    # Real graphite, by absolute darkness. The local-contrast method used for
    # locating a figure is wrong here: it reads the paper vignette at the frame
    # edge as ink and reports every frame, including blank paper, as clipped.
    # A head is drawn in graphite. Paper, however warm, is not.
    fig = L < 165
    bord = find_border(fig)
    if bord:
        t, b, l, r = bord
        fig = fig[t:b, l:r]
        L = L[t:b, l:r]
    if not fig.any():
        return None
    ys, xs = np.nonzero(fig)
    h, w = L.shape
    return dict(h=h, w=w,
                top=ys.min() / h, bottom=1 - ys.max() / h,
                left=xs.min() / w, right=1 - xs.max() / w,
                top_px=int(ys.min()),
                touching_top=bool(fig[0, :].any()),
                bordered=bord is not None,
                top_run=float(fig[0, :].mean()))


def check(path):
    b = ink_box(path)
    name = path.split('/')[-1]
    if b is None:
        print('  %-34s EMPTY, no ink found' % name)
        return False
    # a stray speck of ink at the edge is a paper mark. A head is wide.
    ok = (b['top_run'] < 0.02) and b['top'] >= MIN_TOP_CLEARANCE
    print('  %-34s top clearance %5.2f%% (%4dpx)  bottom %5.2f%%  %-24s %s'
          % (name, b['top'] * 100, b['top_px'], b['bottom'] * 100,
             'OK' if ok else 'CUT AT THE TOP -> zoom out',
             '(measured inside the panel border)' if b['bordered'] else ''))
    if b['touching_top']:
        print('  %-34s   ink reaches row 0 across %.1f%% of the width'
              % ('', b['top_run'] * 100))
    return ok


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    results = [check(p) for p in sys.argv[1:]]
    sys.exit(0 if all(results) else 1)
