from PIL import Image, ImageDraw, ImageFont
import os, textwrap

OUT = 'assets/shots'
os.makedirs(OUT, exist_ok=True)

W = 1400
FRAME_H = int(W * 9 / 16)
PAPER = (240, 232, 213)
PAPER_D = (228, 218, 194)
INK = (44, 41, 36)
INK_S = (96, 89, 76)
RULE = (176, 166, 145)
ACC = (150, 112, 48)

FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FM = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
FMB = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'

def f(path, size):
    return ImageFont.truetype(path, size)

SHOTS = {
 '1_1': dict(
   code='1.1', scene='SCENE 1 — THE MYSTERY', tc='0:00 – 0:05', dur='5 sec',
   slug='EXT. MARATHON COURSE — DAY',
   kind='ANIMATION ONLY',
   desc='The runner is failing. Low wide angle near road level. Head rolled back, arms hanging useless, stride collapsed into a shuffle. Barriers line both sides, the crowd behind them deliberately unfocused so the eye stays on his body. This man is beaten and everyone watching knows it.',
   words=[('COMMENTATOR (V.O.)', "He's got nothing left.")],
   notes=[('CAM','Nothing required. Manan does not appear.'),
          ('ANIM','Full frame animation. Bib 27 legible. Crowd loose and simplified.'),
          ('SND','Broadcast crowd wash, compressed. Ragged breath close and dry on top. Footfall dragging on tarmac.'),
          ('MUS','No score. Only the race.')]),
 '1_2': dict(
   code='1.2', scene='SCENE 1 — THE MYSTERY', tc='0:05 – 0:08', dur='3 sec',
   slug='EXT. MARATHON COURSE — CONTINUOUS',
   kind='ANIMATION ONLY',
   desc='The impossible sprint. Same man, transformed. Knees driving, arms pumping, jaw set. Camera tracks alongside at chest height. Dense speed lines streak the frame, dust kicks from the trailing foot, background reduced to horizontal smears. It should feel like it should not be possible.',
   words=[],
   notes=[('CAM','Nothing required.'),
          ('ANIM','The turn of the whole film. Hold on it just long enough for the audience to register the contradiction.'),
          ('SND','Crowd surges. Footfall sharpens from drag to strike. Breath drives.'),
          ('MUS','Nothing yet. Let the sound carry it.')]),
 '1_3': dict(
   code='1.3', scene='SCENE 1 — THE MYSTERY', tc='0:08 – 0:13', dur='5 sec',
   slug='EXT. FROZEN WORLD — CONTINUOUS',
   kind='LIVE ACTION IN ANIMATION',
   desc='Everything stops. Speed lines, dust and crowd hang suspended mid air. Manan walks into the frozen tableau from frame right, coat swinging, magnifying glass raised toward the runner. He is the only living thing in the picture.',
   words=[],
   notes=[('CAM','SETUP A. Manan enters frame right, four steps, stops in profile, raises the glass toward an eyeline mark at camera left. Nothing is really there. Give him the mark.'),
          ('ANIM','The freeze is the effect. Absolutely nothing else moves, including dust and speed lines.'),
          ('SND','World drops to a single low tone. Only his footsteps and coat remain. Best sound moment in the film.'),
          ('MUS','Three note motif enters alone, unaccompanied.')]),
 '1_4': dict(
   code='1.4', scene='SCENE 1 — THE MYSTERY', tc='0:13 – 0:15', dur='2 sec',
   slug='INSERT — THE EVIDENCE',
   kind='LIVE ACTION IN ANIMATION',
   desc='Close on the brass magnifying glass held steady in his hand. Inside the lens, magnified and sharpened, a single running shoe print pressed into the tarmac and a stopwatch lying beside it. His face soft and out of focus at the edge of frame, tilted down, concentrating.',
   words=[],
   notes=[('CAM','SETUP A. Tight insert of his hand gripping the glass. Shoot it locked off, let his hand tremble slightly, do not stabilise it.'),
          ('ANIM','The magnified contents of the lens are drawn. Everything outside the glass stays soft.'),
          ('SND','Near silence. A faint watch tick inside the lens, if anything at all.'),
          ('MUS','Motif holds, suspended.')]),
 '1_5': dict(
   code='1.5', scene='SCENE 1 — THE MYSTERY', tc='0:15 – 0:18', dur='3 sec',
   slug='EXT. FROZEN WORLD — CONTINUOUS',
   kind='LIVE ACTION IN ANIMATION',
   desc='He lowers the glass and turns to the lens. One eyebrow raised, the expression of somebody who has just realised the story they were told does not hold together. Question marks bloom in the air around him. The title lands.',
   words=[('MANAN', 'Hold on.'),
          ('MANAN', 'He had nothing left.'),
          ('MANAN', 'So where did THAT come from?'),
          ('TITLE', 'THE BRAIN BRAKE')],
   notes=[('CAM','SETUP A. Medium, direct to lens. ONE SENTENCE PER TAKE, full reset between each. Minimum three clean takes of every line.'),
          ('ANIM','Question marks and title card drawn over the live plate. They arrive on the last word, not before.'),
          ('SND','Absolute quiet under the lines. A single soft impact on the title.'),
          ('MUS','Motif left unresolved. Do not answer it here. It resolves at 1:48.')]),
}

def wrap(draw, text, font, maxw):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def build(key, d):
    src = Image.open(f'assets/SC{key}.png').convert('RGB')
    src = src.resize((W, int(W * src.size[1] / src.size[0])), Image.LANCZOS)
    fh = src.size[1]

    # measure text block height first
    tmp = Image.new('RGB', (10, 10)); td = ImageDraw.Draw(tmp)
    f_desc = f(FR, 25)
    f_nm = f(FMB, 19)
    f_ln = f(FM, 24)
    f_note = f(FR, 22)
    f_tag = f(FMB, 16)

    pad = 54
    colw = W - pad * 2
    y = 0
    y += 92                       # header band
    y += 30
    desc_lines = wrap(td, d['desc'], f_desc, colw)
    y += len(desc_lines) * 36 + 26
    if d['words']:
        y += 34
        for nm, ln in d['words']:
            y += 28
            for _ in wrap(td, ln, f_ln, colw - 40): y += 34
            y += 12
        y += 14
    y += 34
    for tag, txt in d['notes']:
        ls = wrap(td, txt, f_note, colw - 96)
        y += max(len(ls) * 31, 34) + 16
    y += 40
    text_h = y

    H = fh + text_h
    im = Image.new('RGB', (W, H), PAPER)
    dr = ImageDraw.Draw(im)
    im.paste(src, (0, 0))
    dr.rectangle([0, 0, W - 1, fh], outline=INK, width=3)

    yy = fh
    # header band
    dr.rectangle([0, yy, W, yy + 92], fill=PAPER_D)
    dr.line([0, yy, W, yy], fill=INK, width=3)
    dr.line([0, yy + 92, W, yy + 92], fill=RULE, width=2)
    dr.text((pad, yy + 20), d['code'], font=f(FB, 44), fill=INK)
    dr.text((pad + 130, yy + 22), d['slug'], font=f(FB, 26), fill=INK)
    dr.text((pad + 130, yy + 56), d['kind'], font=f(FM, 19), fill=INK_S)
    tcw = dr.textlength(d['tc'], font=f(FMB, 28))
    dr.text((W - pad - tcw, yy + 22), d['tc'], font=f(FMB, 28), fill=ACC)
    dw = dr.textlength(d['dur'], font=f(FM, 19))
    dr.text((W - pad - dw, yy + 58), d['dur'], font=f(FM, 19), fill=INK_S)

    yy += 92 + 30
    for ln in desc_lines:
        dr.text((pad, yy), ln, font=f_desc, fill=INK); yy += 36
    yy += 26

    if d['words']:
        dr.line([pad, yy, W - pad, yy], fill=RULE, width=2); yy += 34
        for nm, ln in d['words']:
            dr.text((pad, yy), nm, font=f_nm, fill=ACC); yy += 28
            for l in wrap(dr, ln, f_ln, colw - 40):
                dr.text((pad + 34, yy), l, font=f_ln, fill=INK); yy += 34
            yy += 12
        yy += 14

    dr.line([pad, yy, W - pad, yy], fill=RULE, width=2); yy += 34
    for tag, txt in d['notes']:
        dr.rectangle([pad, yy - 2, pad + 74, yy + 26], outline=INK_S, width=2)
        tw = dr.textlength(tag, font=f_tag)
        dr.text((pad + 37 - tw / 2, yy + 4), tag, font=f_tag, fill=INK_S)
        ls = wrap(dr, txt, f_note, colw - 96)
        ty = yy
        for l in ls:
            dr.text((pad + 96, ty), l, font=f_note, fill=INK); ty += 31
        yy += max(len(ls) * 31, 34) + 16

    im.save(f'{OUT}/SH{key}.jpg', 'JPEG', quality=88, optimize=True, progressive=True)
    # web copy
    web = im.copy(); web.thumbnail((900, 4000), Image.LANCZOS)
    web.save(f'{OUT}/SH{key}_w.jpg', 'JPEG', quality=84, optimize=True, progressive=True)
    print(f'SH{key}.jpg', im.size, round(os.path.getsize(f"{OUT}/SH{key}.jpg")/1024), 'KB')

for k, v in SHOTS.items():
    build(k, v)
print('done')
