from PIL import Image, ImageDraw, ImageFont
import numpy as np, math

FONT = '/home/claude/Caveat.ttf'
INK  = (48,44,38)

def _wrap(d, text, font, maxw):
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: line = t
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    return lines

def speech(img, text, cx, cy, tail_to, maxw=760, size=64, pad=42):
    """Hand drawn speech bubble centred on cx,cy with a tail pointing at tail_to."""
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, size)
    lines = _wrap(d, text, font, maxw)
    lh = int(size*1.12)
    tw = max(d.textlength(l, font=font) for l in lines)
    th = lh*len(lines)
    w, h = tw+pad*2, th+pad*2
    x0, y0 = cx-w/2, cy-h/2

    # wobbly hand drawn ellipse
    pts=[]
    rng = np.random.RandomState(int(abs(cx)+abs(cy)))
    for i in range(120):
        a = 2*math.pi*i/120
        jitter = 1.0 + 0.012*math.sin(a*7+1.3) + 0.010*math.sin(a*3+0.4)
        pts.append((cx + (w/2)*jitter*math.cos(a), cy + (h/2)*jitter*math.sin(a)))
    d.polygon(pts, fill=(252,249,240))
    d.line(pts+[pts[0]], fill=INK, width=5, joint="curve")

    # tail
    ang = math.atan2(tail_to[1]-cy, tail_to[0]-cx)
    b1 = (cx + (w/2)*0.55*math.cos(ang-0.30), cy + (h/2)*0.90*math.sin(ang-0.30))
    b2 = (cx + (w/2)*0.55*math.cos(ang+0.30), cy + (h/2)*0.90*math.sin(ang+0.30))
    d.polygon([b1, b2, tail_to], fill=(252,249,240))
    d.line([b1, tail_to], fill=INK, width=5)
    d.line([b2, tail_to], fill=INK, width=5)

    ty = cy - th/2
    for l in lines:
        d.text((cx - d.textlength(l,font=font)/2, ty), l, font=font, fill=INK)
        ty += lh
    return img

def caption(img, text, size=46):
    """Narrator strip along the bottom, the storybook voice."""
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, size)
    W,H = img.size
    lines = _wrap(d, text, font, W-160)
    lh = int(size*1.15); box_h = lh*len(lines)+46
    d.rectangle([40, H-box_h-34, W-40, H-34], fill=(250,246,235), outline=INK, width=4)
    y = H-box_h-34+22
    for l in lines:
        d.text((70, y), l, font=font, fill=INK); y += lh
    return img
