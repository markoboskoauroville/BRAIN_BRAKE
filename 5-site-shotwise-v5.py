import re

p = 'index.html'
h = open(p, encoding='utf-8').read()

h = h.replace('<div class="ver">3 (a)</div>', '<div class="ver">4 (a)</div>')

# remove every old board image + caption (boards were deleted from the repo)
h = re.sub(r'<img class="board" src="assets/sb/SC\d\.jpg"[^>]*>\s*<div class="board-cap">[^<]*</div>', '', h)

# extra css for the shot sheets
css = """
.sheets{display:grid;gap:20px;margin:20px 0 4px}
.shot{background:var(--panel);border:1px solid var(--rule);padding:12px}
.shot img{width:100%;height:auto;display:block;cursor:zoom-in}
.shot .sc-t{
  font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--dim);margin-top:9px;
  display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;
}
.shot .sc-t b{color:var(--signal);font-weight:500}
.pend{
  border:1px dashed var(--rule);padding:20px;margin:18px 0 4px;
  font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--dim);
  letter-spacing:.08em;line-height:1.8;
}
"""
h = h.replace('/* lightbox */', css + '/* lightbox */')

SHEETS = [
 ('1_1','1.1','0:00 – 0:05','Animation only'),
 ('1_2','1.2','0:05 – 0:08','Animation only'),
 ('1_3','1.3','0:08 – 0:13','Setup A · live action'),
 ('1_4','1.4','0:13 – 0:15','Setup A · insert'),
 ('1_5','1.5','0:15 – 0:18','Setup A · to camera'),
]

gallery = '<div class="sheets">'
for key, code, tc, kind in SHEETS:
    gallery += (f'<div class="shot"><img class="board" src="assets/shots/SH{key}_w.jpg" '
                f'data-full="assets/shots/SH{key}.jpg" alt="Shot {code}" loading="lazy">'
                f'<div class="sc-t"><b>Shot {code}</b><span>{tc} · {kind}</span></div></div>')
gallery += '</div>'

PEND = ('<div class="pend">Boards for this scene are being redrawn shot by shot, the same way as Scene 1.<br>'
        'The frame notes below are final and can be worked from now.</div>')

# split into scene blocks and rewrite
parts = h.split('<div class="sc">')
out = [parts[0]]
for seg in parts[1:]:
    if '<h2>Scene 1 — The Mystery</h2>' in seg:
        # replace the .frames block with the shot sheet gallery
        seg = re.sub(r'<div class="frames">.*?</div></div></div></div>', gallery, seg, flags=re.S)
    else:
        seg = seg.replace('<div class="frames">', PEND + '<div class="frames">', 1)
    out.append(seg)
h = '<div class="sc">'.join(out)

# lightbox should open the full-resolution sheet when one exists
h = h.replace("if(t && t.classList && t.classList.contains('board')){ lbi.src=t.src; lb.classList.add('on'); }",
              "if(t && t.classList && t.classList.contains('board')){ lbi.src=t.dataset.full||t.src; lb.classList.add('on'); }")

# stats on the storyboard pane
h = h.replace('<div class="stat"><div class="k">Boards</div><div class="v">6</div><div class="n">One per scene, three frames each</div></div>',
              '<div class="stat"><div class="k">Shots</div><div class="v">35</div><div class="n">Scene 1 boarded, 30 to draw</div></div>')
h = h.replace('<div class="stat"><div class="k">Live action frames</div><div class="v">10</div><div class="n">Three camera setups, one day</div></div>',
              '<div class="stat"><div class="k">Live action shots</div><div class="v">12</div><div class="n">Three camera setups, one day</div></div>')
h = h.replace('<div class="stat"><div class="k">Pure animation</div><div class="v">8</div><div class="n">No camera required</div></div>',
              '<div class="stat"><div class="k">Pure animation</div><div class="v">23</div><div class="n">No camera required</div></div>')
h = h.replace('<button class="tab" data-p="board"><span class="led go"></span>Storyboard<span class="who">18 frames</span></button>',
              '<button class="tab" data-p="board"><span class="led hold"></span>Storyboard<span class="who">35 shots</span></button>')
h = h.replace('<p class="standfirst">Six boards, eighteen frames, two minutes exactly. Every frame carries its own words and its own instruction for each department, so nobody has to guess what happens either side of their own work.</p>',
              '<p class="standfirst">Thirty five shots, two minutes exactly. Each shot is a sheet in its own right, carrying the frame, the words spoken over it, and a separate instruction for every department. Scene 1 is drawn. The rest follow the same pattern.</p>')
h = h.replace('<div class="foot">Storyboard · 18 frames · locked to 2:00</div>',
              '<div class="foot">Storyboard · 35 shots · Scene 1 drawn · locked to 2:00</div>')

open(p, 'w', encoding='utf-8').write(h)
print('ok, size', len(h))
print('sheets embedded:', h.count('assets/shots/SH'))
