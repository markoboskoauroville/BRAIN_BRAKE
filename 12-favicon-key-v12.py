from PIL import Image, ImageDraw, ImageFilter
import math

# ---- shared geometry, 64 unit design space --------------------------------
# vertical key, bow at top, two teeth at lower right
SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f7d38a"/>
      <stop offset="0.45" stop-color="#e0a340"/>
      <stop offset="1" stop-color="#a86f1c"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="12" fill="#0b0e13"/>
  <g transform="rotate(-18 32 32)">
    <circle cx="32" cy="19" r="10.5" fill="none" stroke="url(#g)" stroke-width="5.5"/>
    <circle cx="32" cy="19" r="4.2" fill="#0b0e13"/>
    <rect x="29.4" y="27" width="5.2" height="26" rx="1.6" fill="url(#g)"/>
    <rect x="34.6" y="40" width="7.5" height="4.6" rx="1.4" fill="url(#g)"/>
    <rect x="34.6" y="48.4" width="5.6" height="4.6" rx="1.4" fill="url(#g)"/>
  </g>
</svg>'''
open('favicon.svg', 'w').write(SVG)

GOLD_HI = (247, 211, 138, 255)
GOLD    = (224, 163, 64, 255)
GOLD_LO = (168, 111, 28, 255)
BG      = (11, 14, 19, 255)


def grad_fill(mask_im, size):
    """Apply a diagonal gold gradient through the alpha mask."""
    g = Image.new('RGBA', (size, size))
    px = g.load()
    for y in range(size):
        for x in range(size):
            t = (x / size * 0.5) + (y / size * 0.5)
            if t < 0.45:
                f = t / 0.45
                c = tuple(int(GOLD_HI[i] + (GOLD[i] - GOLD_HI[i]) * f) for i in range(3))
            else:
                f = (t - 0.45) / 0.55
                c = tuple(int(GOLD[i] + (GOLD_LO[i] - GOLD[i]) * f) for i in range(3))
            px[x, y] = c + (255,)
    g.putalpha(mask_im)
    return g


def build(size):
    S = size * 8
    u = S / 64.0
    mask = Image.new('L', (S, S), 0)
    d = ImageDraw.Draw(mask)

    def R(x, y, w, h, r):
        d.rounded_rectangle([x * u, y * u, (x + w) * u, (y + h) * u], radius=r * u, fill=255)

    # bow ring
    d.ellipse([(32 - 10.5) * u, (19 - 10.5) * u, (32 + 10.5) * u, (19 + 10.5) * u],
              outline=255, width=int(5.5 * u))
    # shaft and teeth
    R(29.4, 27, 5.2, 26, 1.6)
    R(34.6, 40, 7.5, 4.6, 1.4)
    R(34.6, 48.4, 5.6, 4.6, 1.4)

    key = grad_fill(mask, S)

    # hole in the bow, punched after fill
    hole = Image.new('L', (S, S), 0)
    ImageDraw.Draw(hole).ellipse([(32 - 4.2) * u, (19 - 4.2) * u,
                                  (32 + 4.2) * u, (19 + 4.2) * u], fill=255)
    a = key.getchannel('A')
    a = Image.composite(Image.new('L', (S, S), 0), a, hole)
    key.putalpha(a)

    key = key.rotate(18, resample=Image.BICUBIC, center=(32 * u, 32 * u))

    # warm glow behind the key
    glow = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    glow.paste((232, 170, 70, 90), (0, 0), key.getchannel('A'))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=int(2.6 * u)))

    plate = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(12 * u), fill=BG)
    plate.alpha_composite(glow)
    plate.alpha_composite(key)
    return plate.resize((size, size), Image.LANCZOS)


build(32).save('favicon-32.png')
build(180).save('apple-touch-icon.png')
build(512).save('key-512.png')
print('favicon set written')
