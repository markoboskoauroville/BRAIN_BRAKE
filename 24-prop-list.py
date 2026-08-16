from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import os, sys
sys.path.insert(0,'/home/claude')
from shrink import small

for n,f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DO','DejaVuSans-Oblique.ttf'),
            ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))

W,H=A4; ML,MR=46,46; CW=W-ML-MR
PAPER=HexColor("#f2ebda"); INK=HexColor("#2b2822"); SOFT=HexColor("#6f6757")
ACC=HexColor("#8a6b2e"); RULE=HexColor("#c9bfa4"); LIVE=HexColor("#8a3b2e"); BOX=HexColor("#e6dcc4")
P='/home/claude/props'
OUT='/home/claude/out/THE BRAIN BRAKE - PROP LIST.pdf'
c=canvas.Canvas(OUT,pagesize=A4); pg=[0]

def bg(): c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def foot():
    pg[0]+=1
    c.setFont('M',7); c.setFillColor(SOFT)
    c.drawString(ML,28,"THE BRAIN BRAKE  ·  prop list  ·  for Neha and Venkatesh")
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

bg()
# ---------------------------------------------------------------- cover
y=H-96
c.setFont('DB',28); c.setFillColor(INK); c.drawString(ML,y,"THE PROP LIST")
y-=24; c.setFont('DO',12); c.setFillColor(SOFT)
c.drawString(ML,y,"Every real object that has to exist on the day.")
y-=34
c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y,W-MR,y); y-=26
y=para(ML,y,"Sizes are approximate and none of them are critical to the centimetre. What matters is "
            "that things read correctly on camera, and there are only three where the size genuinely "
            "changes the shot. Those are marked.",'D',10,14)
y-=18
c.setFillColor(BOX); c.rect(ML,y-96,CW,92,fill=1,stroke=0)
c.setStrokeColor(ACC); c.setLineWidth(2); c.line(ML,y-96,ML,y-4)
yy=para(ML+16,y-24,"Ask Venkatesh first. He is a working cinematographer and may already own the "
                   "backdrop, the stands and the lights. That will take most of this list off you "
                   "in one message.",'DB',10,13.6,CW-32)
para(ML+16,yy-4,"Anything he has is good enough. Nothing here needs to be bought new.",'D',9.6,13,CW-32)
y-=116

c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"THE THREE THAT MATTER"); y-=18
for t,d in [("The grey background","It must be about one stop darker than his grey hoodie or he "
             "cannot be cut out cleanly. Neutral, matte, no blue and no green."),
            ("The magnifying glass","The lens must be big, about the width of his head. It is the "
             "film's transition object, so a small one will not work."),
            ("The ball on a stand","Hard and smooth, roughly a cricket ball. Not a tennis ball. His "
             "fingers must sit on a firm curve the way they would on a real lever.")]:
    c.setFont('DB',10); c.setFillColor(INK); c.drawString(ML,y,t); y-=13
    y=para(ML,y,d,'D',9.4,12.8,CW,SOFT); y-=12
newpage()

# ---------------------------------------------------------------- backdrop
y=H-78
c.setFont('MB',8); c.setFillColor(ACC); c.drawString(ML,y+21,"01")
c.setFont('DB',20); c.setFillColor(INK); c.drawString(ML,y,"The grey background")
c.setStrokeColor(RULE); c.line(ML,y-13,W-MR,y-13); y-=36
c.setFillColor(HexColor("#3A3B3D")); c.rect(ML,y-120,CW*0.46,116,fill=1,stroke=0)
c.setFont('MB',13); c.setFillColor(HexColor("#f2ebda")); c.drawString(ML+18,y-70,"#3A3B3D")
c.setFont('D',9); c.drawString(ML+18,y-88,"neutral mid dark grey")
tx=ML+CW*0.50
ty=para(tx,y-14,"Savage Thunder Gray, Colorama Storm Grey, or a flat wall painted in that shade.",
        'D',9.6,13,CW*0.50)
ty-=8
ty=para(tx,ty,"At least 3 by 3 metres so he has room to stand well clear of it.",'D',9.6,13,CW*0.50,SOFT)
y-=140
for t in ["Truly neutral. No blue and no green in it. A colour cast throws that colour onto the edges "
          "of his hair and shoulders and it is very hard to remove afterwards.",
          "Matte, not shiny. A little texture is fine, a sheen is not.",
          "Lit evenly across the whole surface, no bright patch in the middle.",
          "He stands at least a metre and a half in front of it, ideally two. This is the one people "
          "get wrong. If he stands close, his shadow lands on the wall and he cannot be cut out."]:
    c.setFillColor(ACC); c.circle(ML+3,y+3.5,2.4,fill=1,stroke=0)
    y=para(ML+15,y,t,'D',9.6,13.2,CW-15); y-=9
y-=10
c.setFont('MB',8); c.setFillColor(LIVE); c.drawString(ML,y,"NOT GREEN"); y-=13
para(ML,y,"There is no chroma key on this film. He is cut out against neutral grey and composited "
          "into drawn panels. A green screen would spill green light onto his hair and shoulders and "
          "we would lose the soft edges.",'D',9.4,12.8,CW,SOFT)
newpage()

# ---------------------------------------------------------------- the sheets
sheets=sorted(f for f in os.listdir(P) if f.endswith('.jpg'))
SLOT_H=(H-150)/2.0
slot=0
for fn in sheets:
    p=os.path.join(P,fn)
    im=Image.open(p); ar=im.size[0]/im.size[1]
    ih=SLOT_H-14; iw=ih*ar
    if iw>CW: iw=CW; ih=iw/ar
    if slot==0:
        top=H-56
    else:
        top=H-56-SLOT_H
    c.drawImage(ImageReader(small(p,1200)), ML+(CW-iw)/2, top-ih, iw, ih, mask=None)
    slot+=1
    if slot==2:
        newpage(); slot=0
if slot==1: newpage()

# ---------------------------------------------------------------- wardrobe and checklist
y=H-78
c.setFont('DB',20); c.setFillColor(INK); c.drawString(ML,y,"Wardrobe")
c.setStrokeColor(RULE); c.line(ML,y-13,W-MR,y-13); y-=34
y=para(ML,y,"The grey hoodie everywhere, except on the stationary bike where he is in a plain dark "
            "t shirt. He rides the road in the hoodie, comes back sweating, takes it off, and races "
            "the recording in a t shirt. The change reads as time passing between the outdoor ride "
            "and the indoor session, which is exactly the gap the scene needs and never states.")
y-=14
y=para(ML,y,"Plain mid grey, no logos, no stripes, nothing written on it. Dark jeans. Ordinary shoes.",
       'D',9.6,13.4,CW,SOFT)
y-=30
c.setFont('DB',20); c.setFillColor(INK); c.drawString(ML,y,"The whole list")
c.setStrokeColor(RULE); c.line(ML,y-13,W-MR,y-13); y-=32
items=[("Grey background, about 3 by 3 m","#3A3B3D, matte, neutral"),
 ("Magnifying glass","brass, lens about 15 cm, head sized"),
 ("Ball on a stand","8 cm hard ball, top at chest height 130 cm"),
 ("Tennis ball on a stand","eyeline marker, seated head height 115 cm"),
 ("Blackboard and white chalk","about 90 by 70 cm, matte slate, leaning"),
 ("Stationary exercise bike","any, in his room"),
 ("Bicycle and plain dark helmet","for the road, no logos on the helmet"),
 ("Small gold or brass key on a chain","the only colour in the film"),
 ("Music stand","90 to 140 cm"),
 ("Microphone on a stand with pop shield","only has to look right on camera"),
 ("Headphones","his own are fine"),
 ("Script pages printed","white paper, one side, they catch the light"),
 ("His own phone and laptop","already in the film"),
 ("Grey hoodie and plain dark t shirt","no logos"),
]
for t,d in items:
    c.setStrokeColor(RULE); c.setLineWidth(1)
    c.rect(ML,y-2,9,9,fill=0,stroke=1)
    c.setFont('D',9.6); c.setFillColor(INK); c.drawString(ML+18,y,t)
    c.setFont('D',8.6); c.setFillColor(SOFT); c.drawRightString(W-MR,y,d)
    y-=17
foot(); c.showPage(); c.save()
print("written",OUT,os.path.getsize(OUT),"pages",pg[0])
