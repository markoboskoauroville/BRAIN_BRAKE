from PIL import Image, ImageDraw
import os

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#0b0e13"/>
  <rect x="26" y="10" width="12" height="44" rx="3" fill="#12171f" stroke="#2b3542" stroke-width="2"/>
  <rect x="29" y="34" width="6" height="18" rx="2" fill="#e8a33d"/>
  <line x1="18" y1="16" x2="23" y2="16" stroke="#4dd6e8" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="18" y1="24" x2="23" y2="24" stroke="#2b3542" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="18" y1="32" x2="23" y2="32" stroke="#2b3542" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="18" y1="40" x2="23" y2="40" stroke="#2b3542" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="18" y1="48" x2="23" y2="48" stroke="#2b3542" stroke-width="2.5" stroke-linecap="round"/>
  <rect x="20" y="26" width="24" height="9" rx="4.5" fill="#efe4cd" stroke="#0b0e13" stroke-width="2"/>
  <circle cx="44" cy="30.5" r="5.5" fill="#e8a33d" stroke="#0b0e13" stroke-width="2"/>
</svg>'''
open('favicon.svg', 'w').write(SVG)

def raster(size):
    S = size * 8
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    u = S / 64.0
    def R(x, y, w, hh, r, fill, out=None, wd=0):
        d.rounded_rectangle([x*u, y*u, (x+w)*u, (y+hh)*u], radius=r*u, fill=fill, outline=out, width=int(wd*u) or 1)
    R(0, 0, 64, 64, 12, (11, 14, 19, 255))
    R(26, 10, 12, 44, 3, (18, 23, 31, 255), (43, 53, 66, 255), 2)
    R(29, 34, 6, 18, 2, (232, 163, 61, 255))
    for i, yy in enumerate([16, 24, 32, 40, 48]):
        c = (77, 214, 232, 255) if i == 0 else (43, 53, 66, 255)
        d.line([18*u, yy*u, 23*u, yy*u], fill=c, width=int(2.6*u))
    R(20, 26, 24, 9, 4.5, (239, 228, 205, 255), (11, 14, 19, 255), 2)
    d.ellipse([(44-5.5)*u, (30.5-5.5)*u, (44+5.5)*u, (30.5+5.5)*u],
              fill=(232, 163, 61, 255), outline=(11, 14, 19, 255), width=int(2*u))
    return im.resize((size, size), Image.LANCZOS)

raster(32).save('favicon-32.png')
raster(180).save('apple-touch-icon.png')
raster(512).save('/home/claude/look/fav512.png')
print('favicon.svg, favicon-32.png, apple-touch-icon.png written')
