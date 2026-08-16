from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, os
from scipy import ndimage

FONT='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
FONTR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
INK=(58,52,44); DIM=(150,60,40)
OUT='/home/claude/props'; os.makedirs(OUT, exist_ok=True)

def bbox(path, thresh=238):
    im=Image.open(path).convert('L')
    a=np.array(im).astype(float)
    m=a<thresh
    m=ndimage.binary_opening(m, np.ones((5,5)))
    lab,n=ndimage.label(m)
    if n:
        sz=ndimage.sum(m,lab,range(1,n+1))
        keep=lab==int(np.argmax(sz))+1
        # keep anything close to the main blob
        big=ndimage.binary_dilation(keep, iterations=25)
        for i in range(1,n+1):
            c=lab==i
            if (c&big).any(): keep|=c
        ys,xs=np.nonzero(keep)
        return xs.min(),ys.min(),xs.max(),ys.max()
    return 0,0,im.size[0],im.size[1]

def arrow(d,p1,p2,col,w=4,head=16):
    d.line([p1,p2],fill=col,width=w)
    import math
    ang=math.atan2(p2[1]-p1[1],p2[0]-p1[0])
    for P,a in ((p1,ang),(p2,ang+math.pi)):
        for s in (0.42,-0.42):
            d.line([P,(P[0]+head*math.cos(a+s),P[1]+head*math.sin(a+s))],fill=col,width=w)

def sheet(src,out,label,dims,note=""):
    """dims: list of ('h'|'v', frac_start, frac_end, position_frac, text)"""
    im=Image.open(src).convert('RGB')
    W,H=im.size
    # pad for annotation
    PAD=int(W*0.17)
    canvas=Image.new('RGB',(W+PAD*2,H+PAD*2),(252,249,242))
    canvas.paste(im,(PAD,PAD))
    d=ImageDraw.Draw(canvas)
    x0,y0,x1,y1=bbox(src)
    x0+=PAD; x1+=PAD; y0+=PAD; y1+=PAD
    f=ImageFont.truetype(FONT,int(W*0.030))
    fl=ImageFont.truetype(FONT,int(W*0.038))
    fn=ImageFont.truetype(FONTR,int(W*0.026))

    for kind,a,b,pos,txt in dims:
        if kind=='h':
            xa=x0+(x1-x0)*a; xb=x0+(x1-x0)*b; yy=y0+(y1-y0)*pos
            yy = y1+int(W*0.055) if pos>1 else yy
            d.line([(xa,y0-8),(xa,yy+10)],fill=(205,195,180),width=2)
            d.line([(xb,y0-8),(xb,yy+10)],fill=(205,195,180),width=2)
            arrow(d,(xa,yy),(xb,yy),DIM)
            tw=d.textlength(txt,font=f)
            d.rectangle([ (xa+xb)/2-tw/2-8, yy-int(W*0.026), (xa+xb)/2+tw/2+8, yy+int(W*0.008)],
                        fill=(252,249,242))
            d.text(((xa+xb)/2-tw/2, yy-int(W*0.024)),txt,font=f,fill=DIM)
        else:
            ya=y0+(y1-y0)*a; yb=y0+(y1-y0)*b; xx=x0+(x1-x0)*pos
            xx = x1+int(W*0.055) if pos>1 else xx
            d.line([(x0-8,ya),(xx+10,ya)],fill=(205,195,180),width=2)
            d.line([(x0-8,yb),(xx+10,yb)],fill=(205,195,180),width=2)
            arrow(d,(xx,ya),(xx,yb),DIM)
            tw=d.textlength(txt,font=f)
            d.rectangle([xx+10, (ya+yb)/2-int(W*0.016), xx+18+tw, (ya+yb)/2+int(W*0.016)],
                        fill=(252,249,242))
            d.text((xx+14,(ya+yb)/2-int(W*0.014)),txt,font=f,fill=DIM)

    d.text((PAD*0.35, PAD*0.30), label, font=fl, fill=INK)
    if note:
        d.text((PAD*0.35, H+PAD*1.35), note, font=fn, fill=(120,110,95))
    canvas.save(out, quality=95, subsampling=0)
    return out

G='/home/claude/gen'
sheet(f'{G}/p_glass.png', f'{OUT}/01_magnifying_glass.jpg', "MAGNIFYING GLASS",
 [('h',0,1,1.1,"total 28 cm"),('v',0,0.52,1.1,"lens 15 cm")],
 "Brass rim, clear glass, wooden handle. The lens must be big, about the width of Manan's head.\nThis is the film's transition object, so a small one will not work.")
sheet(f'{G}/p_mic.png', f'{OUT}/02_microphone.jpg', "MICROPHONE AND STAND",
 [('v',0,1,1.1,"to 150 cm"),('h',0,1,1.1,"boom reach 70 cm")],
 "It only has to look like a studio microphone on camera. A pop shield in front of it reads instantly.\nNot used for the real recording, that is done separately.")
sheet(f'{G}/p_musicstand.png', f'{OUT}/03_music_stand.jpg', "MUSIC STAND",
 [('v',0,1,1.1,"90 to 140 cm"),('h',0,1,1.1,"tray 48 cm")],
 "Holds his script pages at chest height. The pages are the brightest thing in the booth frame,\nso plain white paper, printed one side.")
sheet(f'{G}/p_headphones.png', f'{OUT}/04_headphones.jpg', "HEADPHONES",
 [('h',0,1,1.1,"cup 9 cm")],
 "Over ear, dark. His own are fine. They read as a silhouette so only the shape matters.")
sheet(f'{G}/p_ballstand.png', f'{OUT}/05_ball_on_stand.jpg', "BALL ON A STAND",
 [('v',0,1,1.1,"top at chest, 130 cm"),('h',0.30,0.70,-0.12,"ball 8 cm")],
 "For frames 8.3 and 8.6. His hand rests on top of it and the lever is drawn around his hand.\nHard and smooth, roughly a cricket ball. NOT a tennis ball, it must not squash under the hand.")
sheet(f'{G}/p_tennisball.png', f'{OUT}/06_eyeline_marker.jpg', "EYELINE MARKER",
 [('v',0,1,1.1,"seated head height, 115 cm")],
 "Never appears in the film. It gives Manan something real to look at where Coach Brain will be drawn.\nAny ball. Place it just left of the camera for frames 4.2 and 4.7.")
sheet(f'{G}/p_blackboard.png', f'{OUT}/07_blackboard.jpg', "BLACKBOARD AND CHALK",
 [('h',0,1,1.1,"90 cm"),('v',0,1,1.1,"70 cm")],
 "Leaning against the wall, shot completely clean and empty. The chain and the year are added afterwards.\nReal white chalk in his hand. Matte slate, not glossy.")
sheet(f'{G}/p_key.png', f'{OUT}/08_key.jpg', "THE KEY",
 [('v',0.35,1,1.1,"key 6 cm")],
 "The only colour anywhere in the film. Brass or gold coloured, on a fine chain.\nHe receives it in 8.5 and holds it in 8.7.")
sheet(f'{G}/p_helmet.png', f'{OUT}/09_helmet.jpg', "CYCLING HELMET",
 [('h',0,1,1.1,"adjust to fit")],
 "Plain, dark, no markings or logos. For the road frame 5.5 only.")
sheet(f'{G}/p_bike.png', f'{OUT}/10_exercise_bike.jpg', "STATIONARY BIKE",
 [('v',0,1,1.1,"seat at 80 cm"),('h',0,1,1.1,"about 100 cm")],
 "In his room, frames 5.6 to 5.9. Any exercise bike. Position it so the window light is behind him\nand the laptop sits to his left.")
print("prop sheets built")
