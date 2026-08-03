import re, io, os

p = 'index.html'
h = open(p, encoding='utf-8').read()

# ---------- 1. version ----------
h = h.replace('<div class="ver">2 (a)</div>', '<div class="ver">3 (a)</div>')

# ---------- 2. extra CSS ----------
css_add = """
/* storyboard */
.sc{margin-top:38px;padding-top:30px;border-top:1px solid var(--rule)}
.sc:first-of-type{border-top:0;padding-top:0;margin-top:26px}
.sc-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:6px}
.sc-head h2{
  font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:30px;
  text-transform:uppercase;letter-spacing:.03em;color:#eef3f8;line-height:1;
}
.sc-head .tc{
  font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.16em;
  color:var(--lever);margin-left:auto;
}
.sc-log{color:#93a3b6;font-style:italic;max-width:64ch;margin-bottom:18px}
.board{
  width:100%;max-width:560px;height:auto;display:block;
  border:1px solid var(--rule);cursor:zoom-in;
}
.board-cap{
  font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--dim);margin-top:8px;
}
.frames{margin-top:22px;display:grid;gap:14px}
.fr{background:var(--panel);border:1px solid var(--rule);padding:16px 18px;display:flex;gap:16px}
.fr-id{
  font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:26px;
  color:var(--signal);line-height:1;flex:0 0 44px;letter-spacing:.02em;
}
.fr-b{flex:1;min-width:0}
.fr-t{
  font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--dim);margin-bottom:7px;
}
.fr-a{color:#c8d3e0;font-size:15px;margin-bottom:11px;max-width:66ch}
.said{
  background:var(--paper);color:var(--graphite);padding:11px 14px;margin:0 0 12px;
  font-family:'IBM Plex Mono',monospace;font-size:12.5px;line-height:1.75;white-space:pre-wrap;
}
.said .nm{font-weight:600;letter-spacing:.1em}
.silent{
  font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--dim);
  letter-spacing:.1em;text-transform:uppercase;margin-bottom:12px;
}
.notes{display:grid;gap:7px}
.nt{display:flex;gap:11px;align-items:flex-start;font-size:14px;color:#9fb0c4;line-height:1.55}
.tag{
  font-family:'IBM Plex Mono',monospace;font-size:8.5px;letter-spacing:.14em;
  padding:3px 7px;border:1px solid var(--rule);color:var(--dim);
  flex:0 0 auto;margin-top:2px;text-transform:uppercase;
}
.tag.cam{color:var(--signal);border-color:rgba(77,214,232,.4)}
.tag.anim{color:var(--lever);border-color:rgba(232,163,61,.4)}
.tag.snd{color:#a99bd6;border-color:rgba(169,155,214,.4)}
.tag.mus{color:#7ed957;border-color:rgba(126,217,87,.35)}
/* lightbox */
#lb{position:fixed;inset:0;background:rgba(4,6,9,.96);z-index:200;display:none;
    align-items:center;justify-content:center;padding:18px;cursor:zoom-out;overflow:auto}
#lb img{max-width:100%;max-height:96vh;height:auto;display:block}
#lb.on{display:flex}
@media(max-width:880px){
  .fr{flex-direction:column;gap:8px}
  .fr-id{flex:none}
  .board{max-width:100%}
}
"""
h = h.replace('@media(max-width:880px){\n  .wrap{display:block}', css_add + '\n@media(max-width:880px){\n  .wrap{display:block}')

# ---------- 3. nav tab ----------
h = h.replace(
 '<button class="tab" data-p="chars"><span class="led go"></span>Characters<span class="who">Design</span></button>',
 '<button class="tab" data-p="board"><span class="led go"></span>Storyboard<span class="who">18 frames</span></button>\n      <button class="tab" data-p="chars"><span class="led go"></span>Characters<span class="who">Design</span></button>')

# ---------- 4. character sheets -> optimised ----------
for n in ['char-manan','char-coach-brain','char-runner','char-muscle','char-workers']:
    h = h.replace(f'src="assets/{n}.png"', f'src="assets/sb/{n}.jpg"')

# ================= FRAME DATA =================
def fr(fid, t, action, said, notes):
    s = f'<div class="fr"><div class="fr-id">{fid}</div><div class="fr-b">'
    s += f'<div class="fr-t">{t}</div>'
    s += f'<div class="fr-a">{action}</div>'
    if said:
        s += f'<div class="said">{said}</div>'
    else:
        s += '<div class="silent">No words. Picture and sound only.</div>'
    s += '<div class="notes">'
    for tag, cls, txt in notes:
        s += f'<div class="nt"><span class="tag {cls}">{tag}</span><span>{txt}</span></div>'
    s += '</div></div></div>'
    return s

SCENES = []

# ---- SCENE 1 ----
SCENES.append(dict(
 n=1, title='The Mystery', tc='0:00 – 0:18', img='SC1',
 log='A man who has nothing left does something impossible. A boy in a coat decides to find out why.',
 frames=[
  fr('1A','0:00 – 0:05 · wide · animation only',
     'The runner is failing on an open road. Head rolling, arms hanging, barriers and a loose crowd sketched behind him. He is beaten and everyone watching knows it.',
     '<span class="nm">COMMENTATOR (V.O.)</span>\nHe\'s got nothing left.',
     [('anim','anim','Full frame animation. Bib 27. Keep the crowd loose and unfocused so the eye stays on the body.'),
      ('cam','cam','Nothing required. Manan does not appear.'),
      ('snd','snd','Broadcast crowd wash, compressed. Ragged breath close and dry on top. Footfall dragging on tarmac.'),
      ('mus','mus','No score. Only the race.')]),
  fr('1B','0:05 – 0:12 · wide · live action inside animation',
     'The runner explodes into a sprint and the world stops dead around him. Speed lines hang frozen in the air. Manan walks into the frozen frame from the right, coat swinging, magnifying glass raised, and studies him.',
     None,
     [('cam','cam','SETUP A. Manan enters frame right, walks four steps, stops in profile, raises the glass toward an eyeline mark placed at camera left. Nothing is really there. Give him the mark.'),
      ('anim','anim','The freeze is the effect. Everything except Manan holds absolutely still, including dust and speed lines.'),
      ('snd','snd','The world drops to a single low tone. Only Manan\'s footsteps and coat movement remain. This silence is the best sound moment in the film.'),
      ('mus','mus','Three note motif enters alone, unaccompanied.')]),
  fr('1C','0:12 – 0:18 · insert then close · live action',
     'Through the magnifying glass, the evidence. A footprint and a stopwatch enlarged in the lens, Manan\'s face soft behind it. He lowers the glass and turns to camera. Question marks bloom around him and the title lands.',
     '<span class="nm">MANAN</span>\nHold on.\nHe had nothing left.\nSo where did THAT come from?\n\n<span class="nm">TITLE</span>\nTHE BRAIN BRAKE',
     [('cam','cam','SETUP A. Two pieces. First an insert of his hand holding the glass steady, shot tight. Then a medium of him turning to lens for the three lines, one sentence per take.'),
      ('anim','anim','The magnified contents of the lens are drawn. Question marks and title card are drawn over the live plate.'),
      ('snd','snd','Absolute quiet under the lines. A single soft impact on the title.'),
      ('mus','mus','Motif holds unresolved. Do not answer it here.')]),
 ]))

# ---- SCENE 2 ----
SCENES.append(dict(
 n=2, title='The Old Answer', tc='0:18 – 0:42', img='SC2',
 log='For a century the muscles took the blame. The case looked closed.',
 frames=[
  fr('2A','0:18 – 0:24 · static · animation only',
     'A dusty classroom. Light falls across an old chalkboard carrying a portrait of a moustached scientist and a chalked chain of reasoning. The room feels abandoned, which is the point.',
     '<span class="nm">MANAN (V.O.)</span>\nFor a hundred years, we blamed the muscles.',
     [('anim','anim','Chalkboard text must read RUN FASTER, then OXYGEN, then FATIGUE, then STOP. Portrait is labelled A.V. HILL, 1923. Drawn, never photographic.'),
      ('cam','cam','Nothing required.'),
      ('snd','snd','Dry dead room. Chalk on slate. A clock somewhere.'),
      ('mus','mus','Score drops out entirely. Let the room be silent.')]),
  fr('2B','0:24 – 0:36 · wide · live action inside animation',
     'Inside the leg, a factory. Gears turn in the shape of a calf muscle, conveyor belts run, a BACKUP POWER lever waits at the far wall. Three workers labour, panic and haul. Manan walks through it all with his glass, unbothered, the only calm thing in the room.',
     '<span class="nm">MANAN (V.O.)</span>\nOxygen comes in. Fuel burns. Everything runs.\nUntil it doesn\'t.',
     [('cam','cam','SETUP A. Manan stands still, holding the glass at chest height, looking slowly left to right at nothing. Shoot thirty seconds of him simply observing. No lines to camera here.'),
      ('anim','anim','The heaviest frame in the film. Machinery, three workers, smoke, conveyor, BACKUP POWER sign. Workers stay small so Manan reads as the subject.'),
      ('snd','snd','Industrial. Hydraulics, trucks arriving, then not arriving. An alarm klaxon. Machines slowing to a grind.'),
      ('mus','mus','Percussion leads. Mechanical, on the beat, almost a work song.')]),
  fr('2C','0:36 – 0:42 · macro · animation only',
     'Close on a gear grinding to a halt as smoke pours across it, and a pressure gauge with the needle buried in the red. The old theory reaching its limit.',
     '<span class="nm">MANAN (V.O.)</span>\nExcept it doesn\'t explain this.',
     [('anim','anim','The red needle is the only colour permitted in the whole film besides skin tones. Use it once, here.'),
      ('cam','cam','Nothing required.'),
      ('snd','snd','Metal stress, a deep groan, then the CASE CLOSED stamp landing hard.'),
      ('mus','mus','Percussion stops mid bar. Do not resolve it.')]),
 ]))

# ---- SCENE 3 ----
SCENES.append(dict(
 n=3, title='The Suspect', tc='0:42 – 1:12', img='SC3',
 log='Behind the broken chalkboard, somebody has been watching the whole race.',
 frames=[
  fr('3A','0:42 – 0:52 · wide · animation only',
     'A curved wall of monitors reading HEART RATE, TEMPERATURE, HYDRATION. In the middle of it all, a cartoon brain in a tracksuit sits in a large chair with a coffee mug, entirely unhurried.',
     None,
     [('anim','anim','The reveal. Push in slowly. Every monitor is live and moving. Coach Brain does not react to the camera arriving.'),
      ('cam','cam','Nothing required.'),
      ('snd','snd','Soft electronic beeps, a low room hum. Clinical and calm. The opposite of the factory.'),
      ('mus','mus','Sustained pad enters for the first time. This is the brain\'s voice in the score.')]),
  fr('3B','0:52 – 1:02 · two shot · live action inside animation',
     'Manan and Coach Brain face each other. Manan is genuinely startled. Coach Brain is delighted and completely relaxed, mug in hand.',
     '<span class="nm">MANAN</span>\nYou\'ve been watching the whole race?\n\n<span class="nm">COACH BRAIN</span>\nEvery second.\nEvery heartbeat. Every breath. Every drop of sweat.',
     [('cam','cam','SETUP B. Tennis ball on a stand at seated height, camera left, for his eyeline. Shoot the line, then ten seconds of silent reaction: surprise, listening, half smile.'),
      ('anim','anim','Glowing lines radiate from Coach Brain out to a drawn heart, lungs, thermometer and water droplet as he speaks.'),
      ('snd','snd','A soft click on each item as the network connects. Four clicks, evenly spaced.'),
      ('mus','mus','Pad holds. Percussion pulls right back. The film gets quieter as it gets more interesting.')]),
  fr('3C','1:02 – 1:12 · two shot with screen · live action inside animation',
     'A monitor between them shows the runner. Coach Brain eases the POWER OUTPUT lever from 100 down to 82 without putting down his coffee. On screen the runner does not collapse. He settles into a pace he can hold.',
     '<span class="nm">MANAN</span>\nSo you\'re controlling my muscles.\n\n<span class="nm">COACH BRAIN</span>\nI\'m not stopping you.\nI\'m getting you to the finish line.\n\n<span class="nm">SUBTITLE, 2 SEC</span>\nCentral Governor Theory, proposed by Prof. Tim Noakes, 1997. Still debated by scientists.',
     [('cam','cam','SETUP B continued. Same eyeline. He listens, then answers. Keep him small in frame so the screen has room.'),
      ('anim','anim','The lever is the single most important object in the film and is currently missing from this frame. Numerals 100% and 82% must be legible as it moves.'),
      ('snd','snd','A mechanical clunk as the lever seats. The runner\'s breathing eases audibly under it.'),
      ('mus','mus','One note steps down as the lever moves. The score does what the picture does.')]),
 ]))

# ---- SCENE 4 ----
SCENES.append(dict(
 n=4, title='Low Power Mode', tc='1:12 – 1:32', img='SC4',
 log='The idea everybody already understands, sitting in their pocket the whole time.',
 frames=[
  fr('4A','1:12 – 1:18 · macro · animation only',
     'A phone fills the frame. The battery reads twenty percent, a LOW POWER MODE banner slides across, and the background apps quietly close themselves and drift away.',
     '<span class="nm">MANAN (O.S.)</span>\nWait. Is it broken?',
     [('anim','anim','Phone must be fully generic. No notch, no recognisable silhouette, no brand. Redraw the handset shape before this goes near a final render.'),
      ('cam','cam','Nothing required.'),
      ('snd','snd','One clean notification chime, then the world audibly dims as each app closes.'),
      ('mus','mus','Almost nothing. One held note. The quietest point in the film.')]),
  fr('4B','1:18 – 1:26 · wide · live action inside animation',
     'Manan stands small at the foot of the screen, dwarfed by it, looking up as a shield forms around the battery and the words PROTECTING BATTERY appear.',
     '<span class="nm">MANAN</span>\nIt\'s saving something for later.',
     [('cam','cam','SETUP B. Manan looking up and slightly off camera. This is the emotional centre of the whole film. Shoot it eight to ten times. Take six is usually the one.'),
      ('anim','anim','The shield draws itself as he says the line, not before. Let the picture arrive on the word.'),
      ('snd','snd','Nothing underneath the line. Let it sit completely bare.'),
      ('mus','mus','Held note only. Do not add anything here, however tempting.')]),
  fr('4C','1:26 – 1:32 · close up · live action inside animation',
     'Tight on Manan looking up, the shielded battery glowing beside his face. Then the phone morphs back into Coach Brain, the battery becomes the runner, the shield becomes a finish line.',
     '<span class="nm">COACH BRAIN</span>\nTired might not mean empty.\nIt might mean, ease off, we\'re not home yet.',
     [('cam','cam','SETUP B. Low angle close up, chin slightly raised, eyes up. No dialogue on his face here, just listening.'),
      ('anim','anim','The morph is one continuous move. Phone to brain, battery to runner, shield to finish line, all in the same breath.'),
      ('snd','snd','A soft rising tone across the transformation. No hard cut.'),
      ('mus','mus','Pad swells gently, then holds. Still no resolution.')]),
 ]))

# ---- SCENE 5 ----
SCENES.append(dict(
 n=5, title='The Finish', tc='1:32 – 1:52', img='SC5',
 log='The question from the first eighteen seconds, finally answered.',
 frames=[
  fr('5A','1:32 – 1:38 · split screen · animation only',
     'Left, the runner twenty metres out, sweat pouring, the tape just ahead. Right, Coach Brain at his desk reading every screen, calm, mug still in hand. Both happening at the same instant.',
     None,
     [('anim','anim','The hairline split is drawn, not a hard digital edge. Distance counter ticking 20, 19, 18 somewhere on his console.'),
      ('cam','cam','Nothing required. Manan does not appear in this scene at all.'),
      ('snd','snd','Left side loud, breath and crowd. Right side almost silent. The contrast is the whole idea.'),
      ('mus','mus','Pulse returns underneath, quiet at first.')]),
  fr('5B','1:38 – 1:48 · wide · animation only',
     'The sprint. Speed lines streaming, the legs drawn semi transparent, muscle fibres lighting up one after another as more are recruited. The lever has gone from 82 to 95 and never to 100.',
     '<span class="nm">MANAN (V.O.)</span>\nThe brain didn\'t make new energy.\nIt just decided it was finally safe to spend it.\n\n<span class="nm">CAPTION</span>\nMore muscle fibres recruited.\nNotice: not maximum.',
     [('anim','anim','The glowing fibres are the money shot of the animation. Light them in sequence, not all at once, so recruitment reads as a process.'),
      ('cam','cam','Nothing required.'),
      ('snd','snd','Everything opens up. Crowd erupts, footfall sharpens, breath drives. Loudest point of the film.'),
      ('mus','mus','Pulse builds hard but never fully resolves. The brain never goes to 100 percent, so neither does the music.')]),
  fr('5C','1:48 – 1:52 · static · animation only',
     'The detective board swings over on its easel to reveal what was written on the back all along, while behind it the runner crosses the line and freezes.',
     '<span class="nm">ON THE BOARD</span>\nYOUR BRAIN WAS SAVING SOME ALL ALONG.',
     [('anim','anim','The handwriting on the reverse must be clean and legible. Current board carries placeholder scribble and needs a final pass with the real sentence.'),
      ('cam','cam','Nothing required.'),
      ('snd','snd','The board swinging on its hinge, then everything cuts to nothing on the freeze.'),
      ('mus','mus','The three note motif from 0:12 returns complete. This is the release the film has withheld for ninety seconds.')]),
 ]))

# ---- SCENE 6 ----
SCENES.append(dict(
 n=6, title='The Twist', tc='1:52 – 2:00', img='SC6',
 log='Nobody wins the argument, and that is the honest ending.',
 frames=[
  fr('6A','1:52 – 1:55 · wide · live action inside animation',
     'White void. Manan stands between the Muscle and Coach Brain. Between them, an emergency brake marked FATIGUE. Instead of arguing, the two of them reach across and shake hands.',
     '<span class="nm">MANAN</span>\nSo who was right?',
     [('cam','cam','SETUP C. Manan against grey, arms at his sides, one line to lens. Also shoot him looking left and looking right so the two characters can be placed beside him.'),
      ('anim','anim','Pure white. No floor detail, no horizon. The handshake happens over the brake, not beside it.'),
      ('snd','snd','Near silence. A faint high tone. Everything else gone.'),
      ('mus','mus','Motif thins out to a single sustained note.')]),
  fr('6B','1:55 – 1:58 · wide · live action inside animation',
     'Pull back. All three are tiny against an enormous FATIGUE lever that dwarfs them completely. Nobody is in charge of it.',
     '<span class="nm">MANAN</span>\nScientists are still arguing.\nThat\'s the best part.',
     [('cam','cam','SETUP C continued. Same position, two short lines. He should sound pleased, not resigned.'),
      ('anim','anim','Scale is the joke. The lever should feel absurdly, comically larger than all three of them.'),
      ('snd','snd','Room tone only.'),
      ('mus','mus','One note, held, thinning.')]),
  fr('6C','1:58 – 2:00 · wide · live action inside animation',
     'Manan considers it, hand to chin. The Muscle sags, Coach Brain slumps against the base of the lever. Two exhausted characters and one boy who has just understood something. Cut to black.',
     '<span class="nm">END CARD</span>\nTHE STRONGEST FINISH MIGHT BEGIN WITH THE SMARTEST BRAKE.',
     [('cam','cam','SETUP C. Hand to chin, thinking, looking slightly up and off. No line. Shoot it long and use the quietest moment.'),
      ('anim','anim','Both characters visibly spent. After two minutes of arguing about fatigue, the joke is that they are the ones who are tired.'),
      ('snd','snd','One last breath, then nothing. Cut hard to black on silence.'),
      ('mus','mus','Final note rings out into the black and is allowed to decay fully.')]),
 ]))

def scene_block(s, show_img=True):
    b = f'<div class="sc"><div class="sc-head"><h2>Scene {s["n"]} — {s["title"]}</h2><span class="tc">{s["tc"]}</span></div>'
    b += f'<p class="sc-log">{s["log"]}</p>'
    if show_img:
        b += f'<img class="board" src="assets/sb/{s["img"]}.jpg" alt="Storyboard, scene {s["n"]}" loading="lazy">'
        b += f'<div class="board-cap">Board {s["n"]} · three frames · tap to enlarge</div>'
    b += '<div class="frames">' + ''.join(s['frames']) + '</div></div>'
    return b

# ---------- 5. storyboard pane ----------
board_pane = """
      <!-- ===== STORYBOARD ===== -->
      <section class="pane" id="p-board">
        <div class="eyebrow">Boards</div>
        <h1 class="pane-t">Storyboard</h1>
        <p class="standfirst">Six boards, eighteen frames, two minutes exactly. Every frame carries its own words and its own instruction for each department, so nobody has to guess what happens either side of their own work.</p>

        <div class="grid">
          <div class="stat"><div class="k">Boards</div><div class="v">6</div><div class="n">One per scene, three frames each</div></div>
          <div class="stat"><div class="k">Live action frames</div><div class="v">10</div><div class="n">Three camera setups, one day</div></div>
          <div class="stat"><div class="k">Pure animation</div><div class="v">8</div><div class="n">No camera required</div></div>
        </div>

        __SCENES__

        <div class="foot">Storyboard · 18 frames · locked to 2:00</div>
      </section>
"""
board_pane = board_pane.replace('__SCENES__', '\n'.join(scene_block(s) for s in SCENES))
h = h.replace('      <!-- ===== CHARACTERS ===== -->', board_pane + '\n      <!-- ===== CHARACTERS ===== -->')

# ---------- 6. Venkatesh: add his frames ----------
def dept_block(scene_nums, tag_keep, heading, intro):
    out = f'<h2 style="font-family:\'Barlow Condensed\',sans-serif;font-weight:700;font-size:26px;text-transform:uppercase;letter-spacing:.04em;color:#eef3f8;margin:44px 0 8px">{heading}</h2>'
    out += f'<p class="standfirst" style="margin-bottom:6px">{intro}</p>'
    for s in SCENES:
        if s['n'] not in scene_nums: continue
        out += scene_block(s)
    return out

ven = dept_block([1,2,3,4,6], 'cam', 'Your boards',
  'These are the five scenes you shoot. Scene 5 needs nothing from you. Read the CAM line under each frame, that is your instruction. The other lines are there so you can see what happens around your work.')
h = h.replace('        <div class="foot">Venkatesh Aurovenkatesh · Auroville · +91 81488 97033</div>',
              ven + '\n        <div class="foot">Venkatesh Aurovenkatesh · Auroville · +91 81488 97033</div>')

kri = dept_block([1,2,3,4,5,6], 'anim', 'Storyboard, sve scene',
  'Svih šest ploča. Pod svakim kadrom ANIM linija je tvoja uputa. CAM linija ti govori što dolazi snimljeno, da znaš gdje ide kompozit, a gdje crtaš sve od nule.')
h = h.replace('        <div class="foot">Kristijan Kaurić · Brojka Kreativna Produkcija · Zagreb</div>',
              kri + '\n        <div class="foot">Kristijan Kaurić · Brojka Kreativna Produkcija · Zagreb</div>')

# ---------- 7. lightbox ----------
h = h.replace('</div>\n\n<script>', '</div>\n<div id="lb"><img id="lb-img" alt=""></div>\n\n<script>')
h = h.replace("""  if(getCookie(C_AUTH)==='1') open();""",
"""  var lb=document.getElementById('lb'), lbi=document.getElementById('lb-img');
  document.addEventListener('click',function(e){
    var t=e.target;
    if(t && t.classList && t.classList.contains('board')){ lbi.src=t.src; lb.classList.add('on'); }
    else if(t===lb || t===lbi){ lb.classList.remove('on'); lbi.src=''; }
  });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ lb.classList.remove('on'); lbi.src=''; } });

  if(getCookie(C_AUTH)==='1') open();""")

# ---------- 8. overview + lever updates ----------
h = h.replace('<div class="lever-lbl"><span>Power output</span><b>18%</b></div>','<div class="lever-lbl"><span>Power output</span><b>31%</b></div>')
h = h.replace('<div class="fill" style','<div class="fill" style').replace('.fill{height:100%;background:var(--lever);width:18%}','.fill{height:100%;background:var(--lever);width:31%}')
h = h.replace('<div class="stat"><div class="k">Script</div><div class="v hold">In revision</div><div class="n">Manan\'s draft received. Cut from five minutes to two. Awaiting sign off.</div></div>',
              '<div class="stat"><div class="k">Script</div><div class="v go">Boarded</div><div class="n">Cut to 2:00 and storyboarded. Eighteen frames.</div></div>')

open(p,'w',encoding='utf-8').write(h)
print('written, size', len(h))
