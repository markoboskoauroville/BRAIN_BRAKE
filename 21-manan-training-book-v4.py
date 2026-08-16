from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import json, os, sys
sys.path.insert(0, '/home/claude')
from tc import tc, FPS

for n, f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DO','DejaVuSans-Oblique.ttf'),
             ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))
pdfmetrics.registerFont(TTFont('H', '/home/claude/Caveat.ttf'))

W, H = A4
ML, MR = 48, 48
CW = W - ML - MR
PAPER = HexColor("#f2ebda"); INK = HexColor("#2b2822"); SOFT = HexColor("#6f6757")
ACC = HexColor("#8a6b2e"); RULE = HexColor("#c9bfa4"); LIVE = HexColor("#8a3b2e")
BOX = HexColor("#e6dcc4")
IMG = "/home/claude/train/img"
OUT = "/home/claude/out/HOW TO ACT NATURALLY v4 - Manan.pdf"
os.makedirs("/home/claude/out", exist_ok=True)

c = canvas.Canvas(OUT, pagesize=A4)
pg = [0]

def bg():
    c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)

def foot(label=""):
    pg[0] += 1
    c.setFont('M',7); c.setFillColor(SOFT)
    c.drawString(ML,28,"HOW TO ACT NATURALLY  ·  version four  ·  Manan Periwal")
    c.drawRightString(W-MR,28,str(pg[0]))

def newpage():
    foot(); c.showPage(); bg()

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

def para(x,y,t,f='D',s=10,lead=14,mw=CW,col=INK):
    c.setFont(f,s); c.setFillColor(col)
    for ln in wrap(t,f,s,mw):
        c.drawString(x,y,ln); y-=lead
    return y

def head(t,kicker=None,y=None):
    y = y or H-78
    if kicker:
        c.setFont('MB',8); c.setFillColor(ACC); c.drawString(ML,y+22,kicker)
    c.setFont('DB',22); c.setFillColor(INK); c.drawString(ML,y,t)
    c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y-14,W-MR,y-14)
    return y-38

def img(path,y,maxh=300,w=CW):
    p=os.path.join(IMG,path)
    im=Image.open(p); ar=im.size[0]/im.size[1]
    iw=w; ih=iw/ar
    if ih>maxh: ih=maxh; iw=ih*ar
    c.drawImage(ImageReader(p), ML+(CW-iw)/2, y-ih, iw, ih, mask=None)
    return y-ih-16

LINES = json.load(open('/home/claude/train/lines.json'))

# ---- one reminder per line page, sequenced easy to subtle -------------------
REMINDERS = [
 "When you hear action, do nothing. Then think. Then let it come.",
 "Say it at the volume of this room. Never louder because a camera is there.",
 "Look at something real. Never at nothing.",
 "The pause before you speak belongs to you. Nobody is waiting.",
 "Do not decide how the sentence ends before you start it.",
 "Give your hands a job or a rest. Never a hover.",
 "Breathe out longer than you breathe in, before the take.",
 "Let your shoulders be wide. Do not push them down.",
 "Talk to one person. Choose them now and keep them all week.",
 "Have the thought first. The words come out shaped by it on their own.",
 "Do not act the emotion. Do the thing, and let the feeling arrive.",
 "The end of a statement goes down, not up.",
 "Let your neck be free. Do not hold your head in place.",
 "If a take feels wrong, watch it before you decide it was wrong.",
 "One sentence per take on the hard ones. Never string them.",
 "Be wrong on purpose for the first three takes. You are looking, not performing.",
 "Think what you want from the person in front of you, not how you look.",
 "Small is bigger on camera than it feels in your body.",
 "Do not fill the silence. The silence is part of the line.",
 "Never watch yourself while you are doing it. Only afterwards.",
 "Nothing about you needs to change. Only what you believe you already have.",
 "Stop trying. Just breathe, and let it be seen.",
]

# ---- per line direction ----------------------------------------------------
DIR = {
 "1.1": ("The film has not started yet. You are telling somebody how the story begins.",
         "You already know the answer and you are not going to give it yet.",
         "the page in your hands","low and slow",
         "the weight even on both feet","the person you are telling this to",
         "you want them to lean in","for a hundred years, everyone was wrong",
         "a small pause before you blame the muscles"),
 "1.6": ("You have just walked through a world that stopped, and looked at a man through a glass.",
         "Nobody else has noticed this. You are the only one who saw.",
         "the lens, one person behind it","held",
         "weight forward, still walking a moment ago","the person behind the lens",
         "you want them to be as puzzled as you are","that is not possible, and it happened",
         "a real stop after Hold on"),
 "2.1": ("You are opening an old book.",
         "You like this man. He was not wrong, he was early.",
         "the page","low and slow",
         "still, settled","a teacher you respect",
         "you want it to sound like a fact, not a verdict","a photograph on a wall, a long time ago",
         "let the year land on its own"),
 "2.6":("The whole hundred years just closed with a stamp.",
         "And you are about to break it open.",
         "the page","held",
         "very slight lean in","the person listening",
         "you want the door reopened","except",
         "a beat before except"),
 "3.2": ("You are standing outside a building nobody goes into.",
         "You are about to open it.",
         "the page","low and slow",
         "weight even, quiet","the person listening",
         "you want them to come with you","there is a door here",
         "quiet, almost a secret"),
 "3.4": ("This is the fact that changes everything.",
         "This is the most surprising sentence in the whole film.",
         "the page","low and slow",
         "still","the person listening",
         "you want them to hear the size of it","they could still do far more",
         "slow down on could still do far more"),
 "3.6": ("A door just opened and warm light came out over you.",
         "And I think a door might be closed on me too.",
         "the lens","held then released",
         "weight forward, you have just stepped in","the person behind the lens",
         "you want to share what you found","it was full, all of it, the whole time",
         "delighted, never shocked"),
 "4.2": ("You have just found the person responsible.",
         "You are not angry. You are impressed.",
         "the tennis ball at seated height","low and slow",
         "level, standing easy","the small character in front of you",
         "you want him to admit it","so it was you",
         "not an accusation, a discovery"),
 "4.5": ("Something ordinary just explained something enormous.",
         "You have seen this on your own phone a hundred times.",
         "the page","low and slow",
         "relaxed","the person listening",
         "you want them to recognise it","my phone does this at twenty percent",
         "ordinary, like mentioning the weather"),
 "4.7": ("He has just told you fatigue is him slowing you down before real danger.",
         "So it can be changed, and now I know what it is called.",
         "the tennis ball","held",
         "in profile, hand at your chin, then you look up","the small character",
         "you want to check you have understood","then it is not my body at all",
         "the name arrives last, like remembering a street name"),
 "5.1": ("You are telling somebody about an experiment you read.",
         "You are enjoying how sneaky it was.",
         "the page","low and slow",
         "settled","the person listening",
         "you want them curious","they set him against himself",
         "light, a little amused"),
 "5.2": ("The trick just happened.",
         "This is the part that makes the whole thing work.",
         "the page","held",
         "still","the person listening",
         "you want them to catch the lie","and he never knew",
         "quiet, conspiratorial, almost whispered"),
 "5.3": ("He just went past his own best.",
         "Which means yours is not your best either.",
         "the page","low and slow",
         "still","the person listening",
         "you want the conclusion to land","so the number was never real",
         "let a beat sit before so it was never"),
 "5.5": ("You have just got up out of your chair because you could not sit still.",
         "You wanted to know if it was true for you.",
         "the page","recovering slightly",
         "as if you have just come in","the person listening",
         "you want them to know you had to","I had to find out myself",
         "dry, a little amused at yourself"),
 "5.8": ("You have just closed your eyes on a bike at your limit and your legs found more.",
         "You did not know that was in you.",
         "the page","recovering",
         "still out of breath","the person listening",
         "you want to be honest about what happened","my legs were exactly the same legs",
         "quiet, slightly amazed, not triumphant"),
 "5.9":("You have just said nothing about your legs changed.",
         "So it was in my head, and my head is mine.",
         "the lens","low and slow",
         "settled, still warm from the effort","the person behind the lens",
         "you want them to feel the size of it","only what I believed",
         "the most important pause in the film sits before only"),
 "6.3": ("Fibres are lighting one after another inside a leg.",
         "There is still more left, even now.",
         "the page","low and slow",
         "still","the person listening",
         "you want them to notice what was withheld","even now, not all of it",
         "small, almost thrown away"),
 "6.9": ("Bodies are flying across the screen doing impossible things.",
         "It was all already there.",
         "the page","low and slow",
         "still","the person listening",
         "you want the whole film to arrive in one sentence","nothing was added, something was allowed",
         "the pause between the two sentences carries the film"),
 "7.6": ("Two dated cards are lying in white space.",
         "This is what I actually admire about science.",
         "the lens","low and slow",
         "settled, calm","the person behind the lens",
         "you want them to trust you","being right is not enough, you have to keep checking",
         "unhurried, this is the most credible thing you say"),
 "8.5": ("A small gold key has just been put into your open hand.",
         "This was handed to me and now it is mine.",
         "the key in your palm, then the lens","low and slow",
         "receiving, weight even","the person behind the lens",
         "you want them to take it too","somebody set this, so it can be moved",
         "certain, never triumphant"),
 "8.6": ("You are holding the key and your hand is on the lever.",
         "This is true for you too.",
         "the lens","low and slow",
         "still, calm, both feet","the person behind the lens",
         "you want them to try it","it can be trained, it is not fixed",
         "quiet, sure, no push"),
 "8.8": ("The film is over. This is the very last thing anybody hears.",
         "I want you to leave believing this.",
         "the page in your hands, in the booth","low and slow",
         "standing still at the microphone","the person listening",
         "you want them to take it with them","a setting can be changed, a wall cannot",
         "the biggest pause in the film sits between setting and not. do not rush the second half"),
 "8.7":("The film is ending. This is the last thing anybody hears.",
         "I want you to look at people differently now.",
         "the lens","low and slow",
         "completely still","the person behind the lens",
         "you want them to carry it out of the room","next time you see it, you will know",
         "let the last take be the tired one, it will be the best"),
}

bg()

# ============================================================ COVER
y = H-140
c.setFont('DB',34); c.setFillColor(INK); c.drawString(ML,y,"HOW TO ACT")
y-=38; c.drawString(ML,y,"NATURALLY")
y-=30
c.setFont('DO',13); c.setFillColor(ACC)
c.drawString(ML,y,"What feels natural is only what you are used to.")
y-=18
c.drawString(ML,y,"Acting naturally is something you learn.")
y-=44
c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=30
y = para(ML,y,"Manan Periwal.  THE BRAIN BRAKE.  Twenty two lines.",'DB',11,15)
y-=14
y = para(ML,y,"This book is yours. Write on it. The back of every page is for your answers "
              "after you have watched yourself, and nobody marks them.",'D',10,14)
y-=180
y = img("vo_booth.jpg", y, 250)
newpage()

# ============================================================ HOW TO USE
y = head("How to use this book","START HERE")
y = para(ML,y,"There are twenty two lines in the film. Each one has a page. On the front is what "
              "you say and how to find it. On the back are four questions you answer after you "
              "have filmed yourself saying it.")
y-=12
y = para(ML,y,"At the bottom of every page there is one reminder. One. Not two. By the end of the "
              "book you will have twenty two of them, and each one arrived while you had room "
              "to take it in.")
y-=20
c.setFillColor(BOX); c.rect(ML,y-96,CW,92,fill=1,stroke=0)
c.setStrokeColor(ACC); c.setLineWidth(2); c.line(ML,y-96,ML,y-4)
yy = para(ML+16,y-24,"You will finish this book knowing more than you did at the start, so the "
                     "first lines will be your weakest. That is how it is meant to work.",'DB',10.5,14.5,CW-32)
para(ML+16,yy-4,"When you reach the end, go back to the beginning and do it again. The second "
                "time through is where the film is.",'D',10,14,CW-32)
y -= 116
y = para(ML,y,"Do all of it on your phone. Film yourself, then sit and watch it. That is the whole "
              "method. You will see things in one minute of watching that nobody could tell you "
              "in an hour.")
y-=16
y = para(ML,y,"There is no rush. You have more time than it feels like.")
newpage()

# ============================================================ PROFESSIONAL CURVE
y = head("Do not be good on the first take","THE MOST USEFUL PAGE IN THIS BOOK")
y = para(ML,y,"Here is the difference between someone who has done this before and someone who "
              "has not.")
y-=14
y = para(ML,y,"Someone who has not done it before gives everything on take one. It is the best "
              "thing they do all day. Take two is a little worse. By take ten they are tired and "
              "defending their first attempt. After an hour they want to stop.",'D',10,14)
y-=12
y = para(ML,y,"Someone who has done it before is worst on take one. They are not performing yet, "
              "they are looking for it. Take four is better. Take ten is better again. They are "
              "still improving after two hours, because they were never trying to be good.",'D',10,14)
y-=22
c.setFillColor(BOX); c.rect(ML,y-72,CW,68,fill=1,stroke=0)
c.setStrokeColor(ACC); c.setLineWidth(2); c.line(ML,y-72,ML,y-4)
para(ML+16,y-24,"So do not try to be good on the first three takes. Be wrong on purpose. Look "
                "for it. The take we use will not be one of the first three.",'DB',10.5,14.5,CW-32)
y-=92

# the curve, drawn
gx, gy, gw, gh = ML+40, y-190, CW-80, 150
c.setStrokeColor(RULE); c.setLineWidth(1)
c.line(gx,gy,gx+gw,gy); c.line(gx,gy,gx,gy+gh)
c.setFont('M',7.5); c.setFillColor(SOFT)
c.drawString(gx-4,gy-14,"take 1"); c.drawRightString(gx+gw,gy-14,"take 20")
c.saveState(); c.translate(gx-14,gy+gh/2); c.rotate(90)
c.drawCentredString(0,0,"how good it is"); c.restoreState()
import math
c.setStrokeColor(LIVE); c.setLineWidth(2.4)
p=c.beginPath(); p.moveTo(gx, gy+gh*0.82)
for i in range(1,101):
    t=i/100.0; p.lineTo(gx+gw*t, gy+gh*(0.82-0.62*t**0.7))
c.drawPath(p)
c.setStrokeColor(ACC); c.setLineWidth(2.4)
p=c.beginPath(); p.moveTo(gx, gy+gh*0.12)
for i in range(1,101):
    t=i/100.0; p.lineTo(gx+gw*t, gy+gh*(0.12+0.80*(1-math.exp(-2.6*t))))
c.drawPath(p)
c.setFont('DB',8.5); c.setFillColor(LIVE); c.drawString(gx+gw*0.55, gy+gh*0.22,"never done it before")
c.setFillColor(ACC); c.drawString(gx+gw*0.42, gy+gh*0.80,"done it before")
newpage()

# ============================================================ FIVE THINGS
y = head("Five things, in this order","EVERY SINGLE TAKE")
steps = [
 ("DO NOTHING","When you hear action, do nothing at all. Not a dramatic pause. Nothing. Wait for "
  "the urge to perform to arrive and go past you. Then begin. The camera is already running and "
  "it costs nothing."),
 ("WHAT JUST HAPPENED","One second before this shot, what happened? Not the scene, the second. "
  "Every page tells you. If you begin in the middle of something, you cannot recite."),
 ("THE THING YOU DO NOT SAY","One private thought you hold and never speak. Nobody can hear it "
  "and everybody can see it. Every page gives you one."),
 ("LOOK AT SOMETHING REAL","You will never be asked to feel something. You will be asked to look "
  "at something and want something from it. The feeling turns up by itself."),
 ("BREATHE","Out longer than in, before you start. When nothing is working, this is the thing "
  "that works."),
]
for i,(t,d) in enumerate(steps):
    c.setFont('MB',13); c.setFillColor(ACC); c.drawString(ML,y,str(i))
    c.setFont('DB',11); c.setFillColor(INK); c.drawString(ML+24,y,t)
    y-=15
    y = para(ML+24,y,d,'D',9.6,13,CW-24,SOFT)
    y-=14
newpage()

# ============================================================ SHEETS
for title, kick, fn, txt in [
 ("Your face","LOOK, DO NOT COPY","sheet_expression.jpg",
  "These are not faces to make. If you make them, they are masks and everyone sees it.\n\n"
  "They are here so that when the right thought gives you the right face, you recognise what it "
  "felt like and can find it again. Noticing. Curious and amused. Thinking. Arriving. Delighted. "
  "And the last one, completely at rest, which is not a face at all."),
 ("Your body","WEIGHT, AND WHAT THE HANDS DO","sheet_posture.jpg",
  "Where your weight sits tells the audience what you are thinking before you speak. Forward means "
  "interested. Back means considering. Even and still is the hardest and you need it at the end.\n\n"
  "Your hands need a job or a rest, never a hover. In this film they always have one: the "
  "magnifying glass, the chalk, the phone, the handlebars, the ball, the key. That was decided for "
  "you on purpose."),
 ("Your breath","THREE PATTERNS","sheet_breath.jpg",
  "Low and slow, out longer than in. Calm, thinking, arriving.\n\n"
  "Held, caught at the top for a beat. Surprise, noticing.\n\n"
  "Recovering, uneven, mouth open. After effort.\n\n"
  "Every page tells you which one. When you cannot find a line, start with the breath and the "
  "rest usually follows."),
 ("When you are nervous","WHAT IT ACTUALLY DOES","sheet_fear.jpg",
  "Nobody can be told not to be nervous. But nerves do the same thing to every body and once you "
  "can see it you can undo it.\n\n"
  "On the left, the shoulders come up toward the ears, the neck shortens, the head pulls back.\n\n"
  "On the right, the same boy released. Do not push your shoulders down, that is just more "
  "holding. Let them be wide. Let your neck be free. Breathe out longer than you breathe in.\n\n"
  "Three seconds, and it is gone."),
]:
    y = head(title, kick)
    y = img(fn, y, 320)
    para(ML,y,txt,'D',10,14)
    newpage()

# ============================================================ LINE PAGES
FRAME_FOR = {
 "1.6":"V7_1_6_turns_to_us.jpg", "3.2":"V7_3_2_door.jpg", "3.6":"V7_3_6_turns.jpg",
 "4.2":"V7_4_2_level.jpg", "4.4":"V7_4_4_phone.jpg", "4.6":"V7_4_6_arrives.jpg",
 "5.5":"V7_5_5_road.jpg", "5.8":"V7_5_8_eyes_closed.jpg", "5.8b":"V7_5_8_eyes_closed.jpg",
 "8.5":"V7_8_5_key.jpg", "8.6":"V7_8_6_eyes_open.jpg", "8.6b":"V7_8_6_eyes_open.jpg",
 "2.1":"V7_2_1_blackboard.jpg", "5.1":"V7_5_6_racing.jpg", "5.2":"V7_5_6_racing.jpg",
 "5.3":"V7_5_7_the_wall.jpg", "7.6":"V7_7_3_white.jpg", "2.6b":"V7_2_6_case_closed.jpg",
 "3.4":"V7_3_4_tanks.jpg",
}


# ---- v4. Directions for the lines added at Neha's request, and for the
# ---- ending rebuilt as the triplet from Manan's original script.
DIR.update({
 "4.4b": ("He has just told you he only ever asks one question, can we keep going safely.",
          "You are not angry any more. You are impressed, and you do not want to show it.",
          "the lens","held",
          "still, head slightly tilted","the person behind the lens",
          "you want him to admit it","so that is what has been happening the whole time",
          "a small pause before secretly. the word is the joke and the truth at once"),
 "4.8":  ("You have just named the theory. Now you have to say what it actually means.",
          "This is the one sentence the whole film exists to deliver.",
          "the lens, nowhere else","low and slow",
          "completely still, both feet, no lean","one person who has never heard this before",
          "you want them to understand it the first time",
          "in advance is the important part, not in the moment",
          "a clear beat before and keeps something in reserve. do not run the two halves together"),
 "8.6":  ("The film is ending. You are setting up the last thing you will ever say to them.",
          "I know how this lands because it happened to me.",
          "the lens","low and slow",
          "completely still","the person behind the lens",
          "you want them to picture a real race","you have all seen this happen",
          "the line does not finish. leave it open, the next one closes it"),
 "8.7":  ("You have set it up. This is the turn.",
          "Everyone gets this wrong, including me, at the start of this film.",
          "the lens","held",
          "still, no movement at all","the person behind the lens",
          "you want them to catch themselves doing it","not the muscles. never was the muscles",
          "do not lean on don't. the correction is gentle, not a telling off"),
 "8.8":  ("This is the last thing you say on camera in the whole film.",
          "I want you to look at people differently after this.",
          "the lens","low and slow",
          "completely still","the person behind the lens",
          "you want them to carry it out of the room","next time you see it, you will know",
          "let the last take be the tired one, it will be the best"),
 "8.9":  ("The film is over. This is the very last thing anybody hears.",
          "I want you to leave believing this.",
          "the page in your hands, in the booth","low and slow",
          "standing still at the microphone","the person listening",
          "you want them to take it with them","a setting can be changed, a wall cannot",
          "the biggest pause in the film sits between setting and not. do not rush the second half"),
})
FRAME_FOR.update({
 "4.4b":"V7_4_2_level.jpg", "4.8":"V7_4_6_arrives.jpg",
 "8.6":"V7_8_5_key.jpg", "8.7":"V7_8_7_closing.jpg", "8.8":"V7_8_6_eyes_open.jpg",
})

for i, L in enumerate(LINES):
    lid = L['id']; mode = L['mode']; text = L['text']
    d = DIR.get(lid)
    # ---------- FRONT
    y = H-70
    c.setFont('MB',8); c.setFillColor(ACC)
    c.drawString(ML,y,"LINE %d OF %d   ·   SCENE %d   ·   %s" % (i+1,len(LINES),L['scene'],
        "TO CAMERA" if mode=="CAM" else "VOICE OVER, IN THE BOOTH"))
    y-=8
    c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y,W-MR,y)
    y-=42

    # ---- THE LINE, ALWAYS INSIDE A MARKED BOX.
    # Neha and Manan both read the bare line at the top of the page as a heading.
    # It is not a heading. It is the only thing on the page he says out loud, so it
    # is framed, labelled and put in quotation marks, and nothing else on the page
    # is ever drawn this way.
    PAD = 18
    size = 26 if len(text)<70 else (21 if len(text)<120 else 17)
    said = "\u201c" + text + "\u201d"
    body = wrap(said,'DB',size,CW-PAD*2)
    bh = 30 + len(body)*size*1.30 + PAD
    top = y
    c.setFillColor(BOX); c.rect(ML, top-bh, CW, bh, fill=1, stroke=0)
    c.setStrokeColor(ACC); c.setLineWidth(2.6); c.line(ML, top-bh, ML, top)
    c.setStrokeColor(RULE); c.setLineWidth(0.8)
    c.rect(ML, top-bh, CW, bh, fill=0, stroke=1)
    c.setFont('MB',6.8); c.setFillColor(ACC)
    c.drawString(ML+PAD, top-19,
        "YOU SAY THIS OUT LOUD" + ("" if mode=="CAM" else "   ·   IN THE BOOTH, NOT ON CAMERA"))
    yy = top - 30 - size*0.92
    c.setFont('DB',size); c.setFillColor(INK)
    for ln in body:
        c.drawString(ML+PAD,yy,ln); yy-=size*1.30
    y = top - bh - 20

    fr = FRAME_FOR.get(lid)
    if fr and os.path.exists(os.path.join(IMG,fr)):
        y = img(fr, y, 190)
    elif mode=="VO":
        y = img("vo_booth.jpg", y, 170)
    y-=6

    if d:
        just, secret, look, breath, earth, water, fire, wind, ether = d
        rows = [("ONE SECOND BEFORE", just), ("THE THING YOU DO NOT SAY", secret),
                ("LOOK AT", look), ("BREATH", breath)]
        for lbl,val in rows:
            c.setFont('MB',6.8); c.setFillColor(ACC); c.drawString(ML,y,lbl); y-=10
            y = para(ML,y,val,'D',9.4,12.6,CW); y-=7
        c.setFont('MB',6.8); c.setFillColor(ACC); c.drawString(ML,y,"THE FIVE"); y-=11
        for k,v in [("body",earth),("who",water),("want",fire),("thought",wind),("silence",ether)]:
            c.setFont('M',7.6); c.setFillColor(SOFT); c.drawString(ML,y,k)
            yy=para(ML+52,y,v,'D',9,12.4,CW-52)
            y=yy

    # reminder box, always at the foot
    rt = REMINDERS[i % len(REMINDERS)]
    bh = 52
    c.setFillColor(BOX); c.rect(ML,52,CW,bh,fill=1,stroke=0)
    c.setStrokeColor(ACC); c.setLineWidth(2); c.line(ML,52,ML,52+bh)
    c.setFont('MB',6.8); c.setFillColor(ACC); c.drawString(ML+14,52+bh-16,"REMEMBER")
    para(ML+14,52+bh-31,rt,'DB',10,13,CW-28)
    newpage()

    # ---------- BACK
    y = H-70
    c.setFont('MB',8); c.setFillColor(SOFT)
    c.drawString(ML,y,"AFTER YOU HAVE FILMED IT   ·   LINE %d   ·   %s" % (i+1, lid))
    y-=8
    c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=30
    c.setFont('DO',11); c.setFillColor(ACC)
    c.drawString(ML,y,"Watch it back first. Then answer. Nobody reads this but you."); y-=34

    qs = ["What did you actually do that you did not know you were doing?",
          "What were you thinking about, in the second before you spoke?",
          "Which take felt worst to you? Watch that one again. What is in it?",
          "One thing to try differently next time. Only one."]
    for qi,q in enumerate(qs):
        c.setFont('MB',11); c.setFillColor(ACC); c.drawString(ML,y,str(qi+1))
        yy = para(ML+22,y,q,'DB',10.5,14,CW-22)
        y = yy-6
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        for k in range(3 if qi<3 else 2):
            c.line(ML+22,y-8,W-MR,y-8); y-=20
        y-=14
    y-=6
    c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=24
    c.setFont('MB',8); c.setFillColor(ACC); c.drawString(ML,y,"THE TAKE I KEPT")
    c.setStrokeColor(RULE); c.line(ML+120,y-3,ML+200,y-3)
    c.setFont('MB',8); c.setFillColor(ACC); c.drawString(ML+220,y,"WHY")
    c.line(ML+260,y-3,W-MR,y-3)
    newpage()

# ============================================================ ON THE DAY
y = head("On the day","READ THIS ON TUESDAY MORNING")
for t in ["Eat something before you come. Nerves and an empty stomach feel exactly the same and "
          "you will mistake one for the other.",
          "Warm your voice up by talking, not by exercises. Ten minutes of ordinary conversation "
          "with anyone.",
          "Choose the person you are talking to and keep them all day.",
          "The first take is a rehearsal that happens to be recorded. Expect nothing from it.",
          "If a take is wrong, the direction was wrong, not you. We go again and nobody comments.",
          "Do not watch yourself between takes. That is for the evening.",
          "After six takes on anything, stand up and walk about before you continue.",
          "The silence before you speak belongs to you. Nobody is waiting.",
          "When you do not know what to do: breathe out longer than in, and look at the thing."]:
    c.setFillColor(ACC); c.circle(ML+3,y+3.5,2.6,fill=1,stroke=0)
    y = para(ML+16,y,t,'D',10.5,14.6,CW-16); y-=10
newpage()

# ============================================================ END CARD
c.setFillColor(HexColor("#141110")); c.rect(0,0,W,H,fill=1,stroke=0)
ep=os.path.join(IMG,"endcard.jpg")
if os.path.exists(ep):
    im=Image.open(ep); ar=im.size[0]/im.size[1]
    iw=W-56; ih=iw/ar
    c.drawImage(ImageReader(ep), 28, H/2-ih/2+34, iw, ih, mask=None)
c.setFont('DO',12); c.setFillColor(HexColor("#a08a68"))
c.drawCentredString(W/2, H/2-ih/2+6, "This is the last thing anyone sees.")
c.setFont('DB',13); c.setFillColor(HexColor("#c9b48c"))
for i,ln in enumerate(["Nothing about you needs to change.",
                       "Only what you believe you already have."]):
    c.drawCentredString(W/2, H/2-ih/2-26-i*20, ln)
c.setFont('M',7); c.setFillColor(HexColor("#5d5346"))
c.drawString(ML,28,"HOW TO ACT NATURALLY  ·  version four  ·  Manan Periwal")
c.drawRightString(W-MR,28,str(pg[0]+1))
c.showPage(); c.save()
print("written", OUT, os.path.getsize(OUT), "pages", pg[0]+1)
