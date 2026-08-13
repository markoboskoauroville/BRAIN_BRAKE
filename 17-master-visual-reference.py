from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import sys; sys.path.insert(0,'/home/claude')
from shrink import small
import os

for n,f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DO','DejaVuSans-Oblique.ttf'),
            ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))

W,H=A4; ML,MR=46,46; CW=W-ML-MR
PAPER=HexColor("#f2ebda"); INK=HexColor("#2b2822"); SOFT=HexColor("#6f6757")
ACC=HexColor("#8a6b2e"); RULE=HexColor("#c9bfa4")

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

c=canvas.Canvas("/home/claude/out/_front.pdf", pagesize=A4)
def bg():
    c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)

bg()
y=H-110
c.setFont('DB',30); c.setFillColor(INK); c.drawString(ML,y,"THE BRAIN BRAKE")
y-=26; c.setFont('DO',12); c.setFillColor(SOFT)
c.drawString(ML,y,"Sve vizualne reference na jednom mjestu. Za Kristijana.")
y-=40
c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y,W-MR,y); y-=26
intro=("Umjesto dvadeset pet privitaka, jedan dokument. Unutra je sve što je nastalo na ovom filmu, "
 "poredano onako kako je nastajalo.\n\n"
 "Ne moraš ovo čitati od početka do kraja. Prolistaj, uzmi ono što ti koristi, ostalo preskoči. Sve "
 "je ovdje samo zato da vidiš gdje smo bili i odakle možeš krenuti.")
c.setFont('D',9.8); c.setFillColor(INK)
for ln in wrap(intro,'D',9.8,CW): c.drawString(ML,y,ln); y-=13.6
y-=26
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"ŠTO JE UNUTRA"); y-=20
items=[("1","Scenarij, verzija 2. Prva zajednička verzija. Ovdje je završetak s parkourom, plesačicom i "
            "plivačem, i rečenica koja nosi cijeli film: granica je postavka, a ne zid."),
       ("2","Verzija 4, nijemi film. Dvije minute bez ijedne riječi, grafit na papiru. Vizualno "
            "najjače, i točno ono gdje sam se zanio."),
       ("3","Verzija 5, pop up knjiga. Manan u svojoj sobi, iz knjige se diže nacrtani svijet."),
       ("4","Verzija 6, storyboard. Osam listova, 48 kadrova, zadnje što je izboardano."),
       ("5","Knjiga likova. Model sheetovi, rekviziti, lokacije, i cijeli arhiv svih 168 slika kroz "
            "četiri verzije scenarija, uključujući sve što nije prošlo.")]
for k,t in items:
    c.setFont('MB',12); c.setFillColor(ACC); c.drawString(ML,y,k)
    lines=wrap(t,'D',9.2,CW-24)
    c.setFont('D',9.2); c.setFillColor(INK)
    yy=y
    for ln in lines: c.drawString(ML+24,yy,ln); yy-=12.6
    y=yy-10
c.showPage()

# V6 boards section
bg()
y=H-100
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y+26,"VERZIJA ŠEST")
c.setFont('DB',28); c.setFillColor(INK); c.drawString(ML,y,"Storyboard")
y-=30; c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=26
t=("Osam scena, 48 kadrova, dvije minute. Ovo je zadnje što je izboardano i najrazrađenija verzija "
   "koja postoji.\n\nOsam listova, po šest kadrova na svakom.")
c.setFont('D',9.6); c.setFillColor(INK)
for ln in wrap(t,'D',9.6,CW): c.drawString(ML,y,ln); y-=13.4
c.showPage()

A='/home/claude/BRAIN_BRAKE/assets/V6/boards'
titles=["Scena 1, Misterij","Scena 2, Stara teorija","Scena 3, Pun spremnik","Scena 4, Čuvar",
        "Scena 5, Trik","Scena 6, Otpuštanje","Scena 7, Presuda","Scena 8, Poziv"]
for i in range(1,9):
    bg()
    p=f'{A}/V6_S{i}.jpg'
    im=Image.open(p); ar=im.size[0]/im.size[1]
    iw=CW; ih=iw/ar
    top=H-100
    c.drawImage(ImageReader(small(p)), ML, top-ih, iw, ih, mask=None)
    yy=top-ih-24
    c.setFont('MB',8); c.setFillColor(ACC); c.drawString(ML,yy,"%d / 8"%i)
    c.setFont('D',10); c.setFillColor(INK); c.drawString(ML+44,yy,titles[i-1])
    c.showPage()
c.save()
print("front built")
