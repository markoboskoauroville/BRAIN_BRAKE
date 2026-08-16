from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import json, os, sys
sys.path.insert(0,'/home/claude')
from tc import tc, FPS
from shrink import small

for n,f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DO','DejaVuSans-Oblique.ttf'),
            ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFont(TTFont('H','/home/claude/Caveat.ttf'))

W,H=A4; ML,MR=44,44; CW=W-ML-MR
PAPER=HexColor("#f2ebda"); INK=HexColor("#2b2822"); SOFT=HexColor("#6f6757")
ACC=HexColor("#8a6b2e"); RULE=HexColor("#c9bfa4"); LIVE=HexColor("#8a3b2e")
DRAWN=HexColor("#6f6757"); STRIP=HexColor("#3d6b4a"); BOX=HexColor("#e6dcc4")
BOOTH=HexColor("#4a3a6b")

V='/home/claude/BRAIN_BRAKE/assets/V7'; P='/home/claude/BRAIN_BRAKE/assets/V6/panels'
A3='/home/claude/BRAIN_BRAKE/assets/V3A'; TR='/home/claude/train/img'
def find(fn):
    for d in (V,P,A3,TR):
        p=os.path.join(d,fn)
        if os.path.exists(p): return p
    return None

OUT="/home/claude/out/THE BRAIN BRAKE V4.pdf"
c=canvas.Canvas(OUT,pagesize=A4); pg=[0]

def bg(): c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def foot():
    pg[0]+=1
    c.setFont('M',7); c.setFillColor(SOFT)
    c.drawString(ML,28,"THE BRAIN BRAKE  ·  version four  ·  comic strip")
    c.drawRightString(W-MR,28,str(pg[0]))
def newpage(): foot(); c.showPage(); bg()
def wrap(t,f,s,mw):
    o=[]
    for p in t.split("\n"):
        w=p.split()
        if not w: o.append(""); continue
        l=w[0]
        for x in w[1:]:
            if pdfmetrics.stringWidth(l+" "+x,f,s)<=mw: l+=" "+x
            else: o.append(l); l=x
        o.append(l)
    return o
def para(x,y,t,f='D',s=9.6,lead=13.4,mw=CW,col=INK):
    c.setFont(f,s); c.setFillColor(col)
    for ln in wrap(t,f,s,mw): c.drawString(x,y,ln); y-=lead
    return y
def head(t,kick=None,y=None):
    y=y or H-76
    if kick: c.setFont('MB',8); c.setFillColor(ACC); c.drawString(ML,y+22,kick)
    c.setFont('DB',22); c.setFillColor(INK); c.drawString(ML,y,t)
    c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y-14,W-MR,y-14)
    return y-36

F=json.load(open('/home/claude/train/frames.json'))

# ---- timing, driven by the words -------------------------------------------
cursor=0
for f in F:
    f['in']=cursor; f['out']=cursor+f['fr']; cursor=f['out']
TOTAL=cursor

SCENES={1:"THE MYSTERY",2:"THE OLD THEORY",3:"THE FULL TANK",4:"THE GATEKEEPER",
        5:"THE EXPERIMENT",6:"THE RELEASE",7:"THE VERDICT",8:"THE INVITATION"}
LAYER_COL={"DRAWN":DRAWN,"LIVE":LIVE,"STRIP":STRIP,"BOOTH":BOOTH}
LAYER_LBL={"DRAWN":"DRAWN","LIVE":"LIVE ACTION IN A DRAWN PANEL","STRIP":"STRIP PANEL, BUBBLE",
           "BOOTH":"THE BOOTH"}

bg()
# ============================================================ 1 NUMBERS
y=H-92
c.setFont('DB',30); c.setFillColor(INK); c.drawString(ML,y,"THE BRAIN BRAKE")
y-=26; c.setFont('DO',12); c.setFillColor(SOFT)
c.drawString(ML,y,"Version four. The comic strip. Shooting and animation document.")
y-=38
c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y,W-MR,y); y-=24
for k,v in [("RUNNING TIME",tc(TOTAL/FPS)+"   (limit 2:00)"),("TIMEBASE","25 fps non drop, HH:MM:SS:FF"),
            ("FORMAT","16:9, 2731 x 1536"),("ENTRY","Breakthrough Junior Challenge 2026"),
            ("PRESENTER","Manan Periwal"),("CAMERA","Venkatesh, Pondicherry"),
            ("ANIMATION","Kristijan Kaurić, Brojka, Zagreb"),("PRODUCER","Neha Sonthalia Periwal")]:
    c.setFont('MB',7.4); c.setFillColor(SOFT); c.drawString(ML,y,k)
    c.setFont('D',9.6); c.setFillColor(INK); c.drawString(ML+112,y,v); y-=15
y-=18
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"THE FILM IN NUMBERS"); y-=19
from collections import Counter
cnt=Counter(f['layer'] for f in F)
rows=[(str(len(F)),"frames"),
      (str(cnt['DRAWN']),"drawn frames, animation only"),
      (str(cnt['LIVE']),"frames with Manan filmed and placed in a drawn panel"),
      (str(cnt['STRIP']),"strip panels where a character speaks in a bubble"),
      (str(len([f for f in F if f['mode']=='CAM'])),"lines Manan speaks to camera"),
      (str(len([f for f in F if f['mode']=='VO'])),"lines Manan speaks in the booth"),
      (str(len([f for f in F if f['mode']=='BUB'])),"speech bubbles, already recorded"),
      (str(len([f for f in F if not f['mode']])),"frames with no words at all")]
for a,b in rows:
    c.setFont('MB',13); c.setFillColor(INK); c.drawRightString(ML+28,y,a)
    c.setFont('D',9.4); c.setFillColor(SOFT); c.drawString(ML+40,y+1,b); y-=19
y-=14
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"BY SCENE"); y-=6
c.setStrokeColor(RULE); c.setLineWidth(0.5); c.line(ML,y,W-MR,y); y-=13
c.setFont('MB',6.8); c.setFillColor(SOFT)
for l,x in [("SCENE",0),("FRAMES",240),("DRAWN",300),("LIVE",352),("IN",404),("OUT",470)]:
    c.drawString(ML+x,y,l)
y-=11
for s in range(1,9):
    fr=[f for f in F if f['scene']==s]
    d=len([f for f in fr if f['layer']=='DRAWN'])
    c.setFont('D',8.4); c.setFillColor(INK); c.drawString(ML,y,"%d  %s"%(s,SCENES[s].title()))
    c.setFont('M',8.4)
    c.drawString(ML+240,y,str(len(fr)))
    c.setFillColor(SOFT); c.drawString(ML+300,y,str(d))
    c.setFillColor(LIVE); c.drawString(ML+352,y,str(len(fr)-d))
    c.setFillColor(SOFT); c.drawString(ML+404,y,tc(fr[0]['in']/FPS)[3:])
    c.drawString(ML+470,y,tc(fr[-1]['out']/FPS)[3:])
    y-=12
c.setStrokeColor(RULE); c.line(ML,y+4,W-MR,y+4); y-=12
c.setFont('MB',8.4); c.setFillColor(INK)
c.drawString(ML,y,"TOTAL"); c.drawString(ML+240,y,str(len(F)))
c.drawString(ML+300,y,str(cnt['DRAWN'])); c.drawString(ML+352,y,str(len(F)-cnt['DRAWN']))
c.drawString(ML+470,y,tc(TOTAL/FPS)[3:])
newpage()

# ============================================================ 2 THREE LAYERS
y=head("The three layers","THE IDEA THE WHOLE FILM RESTS ON")
y=para(ML,y,"Nobody in the audience is told any of this. They absorb it in the first twenty seconds.")
y-=16
blocks=[("DRAWN","Everything imagined","Pencil on warm cream paper. The factory inside the muscle, "
  "the hall of tanks, Coach Brain, the lever. This layer is the explanation, the model people built "
  "in their heads to make sense of the body.",DRAWN),
 ("LIVE ACTION","Everything true","Manan. Real skin, real hoodie, real hands, photographed against "
  "grey and placed inside the drawings, casting a real shadow onto the paper. This is the evidence, "
  "and the person who came to look.",LIVE),
 ("THE BOOTH","The film being made","A dark room, a music stand, a microphone, one warm light "
  "behind him. He is a silhouette and the only lit thing in frame is the page in his hands. A "
  "shadow, reading, which is exactly what a narrator is. It opens the fourth wall: for a few "
  "seconds we are behind the film, in the room where a boy is making it.",BOOTH)]
for t,sub,d,col in blocks:
    c.setFont('MB',9); c.setFillColor(col); c.drawString(ML,y,t)
    c.setFont('DO',9.4); c.setFillColor(SOFT); c.drawString(ML+130,y,sub)
    y-=13
    y=para(ML,y,d,'D',9.4,13,CW); y-=16
p=find("vo_booth.jpg")
if p:
    im=Image.open(p); ar=im.size[0]/im.size[1]; iw=CW; ih=iw/ar
    if ih>250: ih=250; iw=ih*ar
    c.drawImage(ImageReader(small(p,1500)), ML+(CW-iw)/2, y-ih, iw, ih, mask=None); y-=ih+14
para(ML,y,"The booth shots are cutaways, three or four across the film, dropped in when it wants you "
          "to remember somebody is telling you this.",'DO',9.4,13,CW,SOFT)
newpage()

# ============================================================ 3 WHAT CHANGED
y=head("What changed from version three","FOR KRISTIJAN AND VENKATESH")
items=[("The runner","New character, and the film now opens on his face in close up rather than a wide. Empathy before curiosity: the audience feels him before they wonder about him."),
 ("The format","Fifty composite shots became a moving comic strip. Characters speak in bubbles "
  "instead of being animated. No lip sync, no walk cycles, no character animation."),
 ("The script","Cut from 311 words to 192. Where the picture already said it, the voice stopped "
  "saying it. The chalkboard writes the chain, so nobody narrates the chain. The stamp reads CASE "
  "CLOSED, so nobody says case closed."),
 ("The silence","There are now 25 frames with no words at all. In version two the film was 157 "
  "seconds of speech in a 120 second film, which was impossible."),
 ("The bubbles","Every bubble is also spoken aloud, so nobody has to read anything on screen. The "
  "character voices are cast, directed and already recorded."),
 ("The booth","A new setup and a new layer. See the previous page."),
 ("Delivery","Artwork arrives finished and in separate layers: background alone, each character as "
  "a transparent PNG, bubbles empty so the font is yours, and a placeholder marking where Manan goes.")]
for t,d in items:
    c.setFont('DB',10); c.setFillColor(INK); c.drawString(ML,y,t); y-=13
    y=para(ML,y,d,'D',9.4,13,CW,SOFT); y-=13
newpage()

# ============================================================ 4 THE DAY
y=head("The shooting day","ONE DAY, PLUS ONE SHORT EXTERIOR")
setups=[("A","Grey backdrop, walking and reacting",
  "Eye level on sticks, locked off. Soft key from camera left at forty five degrees. Fill from the "
  "right at half strength. Frames 1.5, 1.6, 2.6, 3.2, 3.3, 3.4, 3.6."),
 ("B","Seated eyeline, reacting to Coach Brain",
  "Same lighting as A, unchanged. Tennis ball on a stand at seated height, camera left. Do not "
  "relight, only move the mark. Frames 4.2, 4.7."),
 ("C","White void, still, to lens",
  "Flat even light both sides, no modelling, no shadow on the backdrop. Frames 7.3, 7.6, 8.1, 8.3, "
  "8.5, 8.6, 8.7."),
 ("D","Jump, high frame rate. Optional, five minutes.","Same as C, wider, room above his head."),
 ("E","His room, at his desk","Warm window light, no lamps fighting it. Frames 2.3, 4.5, 5.4."),
 ("F","His room, at the blackboard","Same light, standing. A real blackboard, shot completely clean. Frame 2.1."),
 ("G","His room, on the stationary bike","Same light. Wide, closer, close. Frames 5.6, 5.7, 5.8, 5.9."),
 ("H","THE BOOTH. New.",
  "A small room made dark. Music stand with the script pages, microphone on a stand, headphones. "
  "One warm light low and behind him, everything else falling away. He reads as a silhouette and "
  "the page in his hands is the only lit thing. His face does not need to read. Three or four shots."),
 ("EXT","One quiet road, early morning","Riding hard, side on. Thirty minutes. Frame 5.5.")]
for k,t,d in setups:
    if y<106: newpage(); y=H-76
    c.setFont('MB',10); c.setFillColor(ACC if k!="H" else BOOTH); c.drawString(ML,y,k)
    c.setFont('DB',9.4); c.setFillColor(INK); c.drawString(ML+30,y,t); y-=13
    y=para(ML+30,y,d,'D',8.6,11.4,CW-30,SOFT); y-=12
y-=6
if y<150: newpage(); y=H-76
c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=20
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"PROPS"); y-=15
y=para(ML,y,"Neutral mid dark grey background, about hex 3A3B3D, matte, one stop darker than his "
            "hoodie, and he stands at least a metre and a half in front of it. Tennis ball on a stand. "
            "Brass magnifying glass. A real blackboard and white chalk. A stationary exercise bike. A "
            "bicycle and a plain dark helmet. A small gold key. A ball at chest height for the lever "
            "insert. His own phone and laptop. Music stand, microphone on a stand, headphones, printed "
            "script pages.",'D',9.2,12.6)
y-=14
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"WARDROBE"); y-=15
para(ML,y,"Grey hoodie everywhere, except on the stationary bike where he is in a plain dark t "
          "shirt. He rides the road in the hoodie, comes back sweating, takes it off. Plain mid grey, "
          "no logos.",'D',9.2,12.6)
newpage()

# ============================================================ FRAMES
IMGW=248.0; TXTX=ML+IMGW+16; TXTW=W-MR-TXTX; BOT=48

cur=None
def row_height(f, ih):
    """measure the text column so rows never collide"""
    h = 0
    if f['text']:
        h += 13
        sz = 13 if len(f['text'])<80 else 11
        h += len(wrap(f['text'],'DB',sz,TXTW))*sz*1.28 + 8
        if f['mode']=="BUB": h += 11
    else:
        h += 13 + 16
    notes={"DRAWN":"Animation only. Nobody on the shooting day.",
           "LIVE":"Manan filmed against grey, cut out, placed in the drawn panel. His shadow is drawn onto the paper.",
           "STRIP":"Background, character and bubble are delivered as separate layers.",
           "BOOTH":"The booth setup. Silhouette, backlit, page lit."}
    h += 9.6 + len(wrap(notes[f['layer']],'D',7.8,TXTW))*10.4
    return max(h, ih+30) + 16

for i,f in enumerate(F):
    p=find(f['img'])
    ih=IMGW*9/16
    if p:
        im=Image.open(p); ih=IMGW/(im.size[0]/im.size[1])
    need=row_height(f, ih)

    if f['scene']!=cur or top-need<BOT:
        if f['scene']!=cur:
            if cur is not None: newpage()
            cur=f['scene']
            y=H-72
            sc=[x for x in F if x['scene']==cur]
            c.setFont('MB',8.6); c.setFillColor(ACC)
            c.drawString(ML,y+21,"SCENE %d OF 8   ·   %s  to  %s" % (cur, tc(sc[0]['in']/FPS), tc(sc[-1]['out']/FPS)))
            c.setFont('DB',21); c.setFillColor(INK); c.drawString(ML,y,SCENES[cur])
            c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y-13,W-MR,y-13)
            top=y-34
        else:
            newpage(); top=H-72

    ytop=top
    if p: c.drawImage(ImageReader(small(p,1400)), ML, ytop-ih, IMGW, ih, mask=None)

    col=LAYER_COL[f['layer']]
    c.setFont('MB',8.4); c.setFillColor(col); c.drawString(ML,ytop-ih-12,f['id'])
    c.setFont('D',7.2); c.drawString(ML+30,ytop-ih-12,LAYER_LBL[f['layer']])
    c.setFont('M',7.2); c.setFillColor(SOFT)
    c.drawString(ML,ytop-ih-24,"%s  %s  %d fr" % (tc(f['in']/FPS), tc(f['out']/FPS), f['fr']))

    ty=ytop
    if f['text']:
        c.setFont('MB',7); c.setFillColor(col)
        c.drawString(TXTX,ty,{"CAM":"MANAN, TO CAMERA","VO":"MANAN, VOICE OVER",
                              "BUB":"%s, SPEECH BUBBLE"%f['who']}[f['mode']])
        ty-=13
        sz=13 if len(f['text'])<80 else 11
        c.setFont('DB',sz); c.setFillColor(INK)
        for ln in wrap(f['text'],'DB',sz,TXTW): c.drawString(TXTX,ty,ln); ty-=sz*1.28
        ty-=8
        if f['mode']=="BUB":
            c.setFont('D',7.6); c.setFillColor(SOFT)
            c.drawString(TXTX,ty,"recorded. bubble empty in the artwork, set the type yourself."); ty-=11
    else:
        c.setFont('MB',7); c.setFillColor(SOFT); c.drawString(TXTX,ty,"NO WORDS"); ty-=13
        c.setFont('DO',10); c.setFillColor(SOFT)
        c.drawString(TXTX,ty,"Let it hold. The picture is doing it."); ty-=16

    notes={"DRAWN":"Animation only. Nobody on the shooting day.",
           "LIVE":"Manan filmed against grey, cut out, placed in the drawn panel. His shadow is drawn onto the paper.",
           "STRIP":"Background, character and bubble are delivered as separate layers.",
           "BOOTH":"The booth setup. Silhouette, backlit, page lit."}
    c.setFont('MB',6.6); c.setFillColor(ACC); c.drawString(TXTX,ty,"BUILD"); ty-=9.6
    para(TXTX,ty,notes[f['layer']],'D',7.8,10.4,TXTW)
    top=ytop-need

newpage()
# ============================================================ END CARD
c.setFillColor(HexColor("#f2ebda")); c.rect(0,0,W,H,fill=1,stroke=0)
ep=find("V7_ENDCARD.jpg")
if ep:
    im=Image.open(ep); ar=im.size[0]/im.size[1]
    iw=W-56; ih=iw/ar
    c.drawImage(ImageReader(small(ep,1600)), 28, H/2-ih/2+30, iw, ih, mask=None)
c.setFont('MB',7.4); c.setFillColor(ACC)
c.drawCentredString(W/2, H/2-ih/2+8, "THE LAST FRAME BUT ONE   ·   then the sheet goes blank")
c.setFont('DO',9.6); c.setFillColor(SOFT)
for i,ln in enumerate(["Everything collapses into one plane. The drawn boy breathing, the two theories",
                       "ghosted at the edges, and the real boy's shadow reading it into being.",
                       "The sentence is hand drawn, because everything explained in this film is drawn.",
                       "Then the sheet goes blank, and we are back at the beginning."]):
    c.drawCentredString(W/2, H/2-ih/2-16-i*14, ln)
c.setFont('M',7); c.setFillColor(SOFT)
c.drawString(ML,28,"THE BRAIN BRAKE  ·  version four  ·  comic strip")
c.drawRightString(W-MR,28,str(pg[0]+1))
c.showPage(); c.save()
print("written",OUT,os.path.getsize(OUT),"pages",pg[0]+1,"runtime",tc(TOTAL/FPS))
