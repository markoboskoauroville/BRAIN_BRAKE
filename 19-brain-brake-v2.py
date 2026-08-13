from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import sys, os
sys.path.insert(0, '/home/claude')
from shrink import small

for n, f in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DO','DejaVuSans-Oblique.ttf'),
             ('M','DejaVuSansMono.ttf'),('MB','DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))

W, H = A4
ML, MR = 46, 46
CW = W - ML - MR
PAPER = HexColor("#f2ebda"); INK = HexColor("#2b2822"); SOFT = HexColor("#6f6757")
ACC = HexColor("#8a6b2e"); RULE = HexColor("#c9bfa4"); LIVE = HexColor("#8a3b2e")
NEW = HexColor("#3d6b4a")
R = "/home/claude/BRAIN_BRAKE/assets"
P = R + "/V6/panels"
V = R + "/V7"

OUT = "/home/claude/out/THE BRAIN BRAKE V2.pdf"
os.makedirs("/home/claude/out", exist_ok=True)
c = canvas.Canvas(OUT, pagesize=A4)
page = [0]

def bg():
    c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)

def foot():
    page[0] += 1
    c.setFont('M',7); c.setFillColor(SOFT)
    c.drawString(ML,30,"THE BRAIN BRAKE  ·  version two  ·  production breakdown")
    c.drawRightString(W-MR,30,str(page[0]))

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

def para(x,y,t,f='D',s=9.4,lead=13,mw=CW,col=INK):
    c.setFont(f,s); c.setFillColor(col)
    for ln in wrap(t,f,s,mw):
        c.drawString(x,y,ln); y-=lead
    return y

# ------------------------------------------------------------------ frames
# (image, tag, title, camera, animation, manan)
# tag: 'D' drawn, 'L' live action + drawn, 'N' new in this version
S = {}

S[1] = ("THE MYSTERY","0:00 – 0:14",[
 (P+"/S1_P1.jpg","D","The runner at the end of himself","",
  "Full drawn wide. He is finished: head rolling, legs gone, the crowd thin and quiet behind the "
  "barriers, the road running away to the horizon. Frame 6.4 rhymes this one exactly, same "
  "composition and opposite feeling, so the camera position chosen here is locked for the film.",
  "Voice over. \"For a hundred years we thought the answer was in the muscles.\"\n"
  "NEW: shoot this line as video of him too, in his room. The edit decides later."),
 (P+"/S1_P2.jpg","D","His face","",
  "Drawn close up, sweat and breath. He is lean and about thirty five. He is at the end of a race, "
  "not at the end of a life, and the whole first scene fails if he reads as an old man.",
  "Voice over continues. Also shot as video."),
 (P+"/S1_P3.jpg","D","He explodes into a sprint","",
  "The impossible thing, and it happens without warning. Diagonal, violent, left to right, horizon "
  "low so he sits high in frame. Speed lines, grit lifting, the crowd coming up off the barriers.",
  "Nothing. Let the picture do it."),
 (P+"/S1_P4.jpg","D","The sprint carries","",
  "Held on the sprint, a bottle thrown, the crowd on its feet. Two or three seconds of pure "
  "disbelief before the film stops dead.","Nothing."),
 (P+"/S1_P5.jpg","L","Everything freezes and Manan walks in",
  "SETUP A. Grey backdrop, mid shot, eye level, locked off. He walks slowly across frame looking "
  "left and right at nothing. Thirty seconds of pure observing, no lines. One dominant key from "
  "camera left, hard enough that his shadow has a shape.",
  "The world stops: crowd, runner, thrown bottle, all held. Manan is cut in and his shadow drawn "
  "onto the tarmac, crossing the pencil lines so they stay visible through it.",
  "Walking through a stopped world with the magnifying glass raised. Curious, taking his time. No "
  "line. He is not performing for anyone, he is just looking."),
 (P+"/S1_P6.jpg","L","He turns to us and asks the question",
  "SETUP A. Close up, same light, to lens. Six takes minimum, use the most unguarded.",
  "The frozen crowd stays behind him. Title over.",
  "He lowers the glass and turns to camera.\n\"Hold on. He had nothing left. So where did THAT "
  "come from?\"\nCurious and amused, never presenting."),
])

S[2] = ("THE OLD THEORY","0:14 – 0:30",[
 (V+"/V7_2_1_blackboard.jpg","N","Manan writes 1923 on the board",
  "SETUP F. His room, a real blackboard leaning against the wall, warm window light. He stands at "
  "it with real chalk in his hand and writes. The board is shot completely clean and empty.",
  "The chain and the year are composited onto the real board afterwards, in perspective, so the "
  "chalk lands only where the board actually is. His hand and arm pass in front of the writing "
  "and occlude it. The 1923 is his own hand writing it, not a caption.",
  "Your note, and it is the best change in this version. He is not narrating the old theory, he is "
  "writing it out. Writing 1923 himself is what makes the date his statement rather than a "
  "subtitle."),
 (P+"/S2_P2.jpg","D","The chain that held for a century","",
  "The chain writes itself one box at a time: RUN FASTER, OXYGEN, LACTATE, FATIGUE, STOP. This is "
  "now the close up of the board he is writing on in 2.1, so the two frames are one action.",
  "Voice over. \"Run hard, run out of oxygen, and the muscle stops.\""),
 (V+"/V7_2_3_lens.jpg","N","The factory inside the lens",
  "SETUP E. His room, at his desk, holding the brass magnifying glass up at shoulder height, lens "
  "facing camera. The glass is empty on the day.",
  "The factory is composited inside the circle of the lens afterwards, with the lens distortion "
  "and the real glass reflection kept over it.",
  "The whole argument of the film in one image, and it answers your question about how to make "
  "him more visible without a box in the corner.\nEverything outside the circle is his real room. "
  "Everything inside it is drawn. The glass is not magnifying, it is a hole punched through "
  "ordinary reality into the layer underneath."),
 (P+"/S2_P4.jpg","D","The supply stops","",
  "The alarm turns, a worker straightens up and shrugs, palms open. The supply is failing, the "
  "machine is not breaking. Resigned, not frightened. A shift ending, not a disaster.",
  "Worker's line, one voice, dry. \"That's it. We're done.\"\n"
  "NOT Manan, and no worker's costume. He is the one investigating the factory, not somebody "
  "working in it."),
 (P+"/S2_P5.jpg","D","The lactate pump","",
  "Two workers at the pump, hands on their heads, steam going up. The old theory's villain drawn "
  "exactly as the theory imagined it.",
  "Voice over. Drawn, not shot at a real pump, for the same reason as 2.4."),
 (V+"/V7_2_6_over_shoulder.jpg","N","Case closed, over his shoulder",
  "SETUP A. He is the near layer, the back of his head and shoulder in the lower left of frame, "
  "watching the stamp come down.",
  "The stamp, the crack and the paper are drawn around him. His shoulder throws a shadow across "
  "the drawing so he stands inside it.",
  "Your note from page six, and it is the shape I want everywhere instead of a corner box. Same "
  "information, opposite feeling: he is at real scale, in the same light, inside the picture.\n"
  "Voice over. \"Case closed. For a hundred years.\" Then over the crack: \"Except it doesn't "
  "explain this.\""),
])

S[3] = ("THE FULL TANK","0:30 – 0:48",[
 (P+"/S3_P1.jpg","D","The back of the factory","",
  "Wide of the plant from outside, and one door in it that nobody has opened. Quiet after the "
  "noise of scene two.","Voice over."),
 (P+"/S3_P2.jpg","L","His hand on the door",
  "SETUP A. Back to camera, palm flat on a mark at chest height, head tilted, listening. Nothing "
  "is really there. Hold it, then let him lean into it.",
  "The riveted door drawn around his hand, keyhole beside it, light behind the keyhole. His shadow "
  "falls on the door.",
  "Curious rather than cautious.\nVoice over. \"At the back of the factory there is a door nobody "
  "opens.\""),
 (P+"/S3_P3.jpg","L","The door swings",
  "SETUP A. Silhouette from behind, then turning into the light. Shoot it both ways.",
  "The door opens and warm light floods over him. The first warm light in the film, and it arrives "
  "as a discovery.","He pushes and steps into the light. No line."),
 (P+"/S3_P4.jpg","L","The hall of tanks",
  "SETUP A. Back of his head and shoulder in the near foreground, held still.",
  "Row upon row of tanks receding. Nine visible, the nearest stencilled 9. The reveal, and the "
  "first big lift in the film.",
  "Looking. Nothing else.\nVoice over: tested at the exact moment they gave up, the muscles could "
  "still produce far more power than the athlete had just produced."),
 (P+"/S3_P5.jpg","D","Every gauge full","",
  "One gauge in close up, needle hard over on FULL. This instrument governs the rest of the film.",
  "Nothing."),
 (P+"/S3_P6.jpg","L","He turns to us",
  "SETUP A. Close up, to lens, lit by the warm light from the tanks. The most important take of "
  "the day. Shoot it many times and use the most unguarded one.",
  "The hall behind him. He must be turned to the lens here: as boarded, scene three never showed "
  "his face once.",
  "Delighted rather than shocked. He found something better than what he expected.\n\"It was never "
  "empty. Somebody closed that door.\""),
])

S[4] = ("THE GATEKEEPER","0:48 – 1:12",[
 (P+"/S4_P1.jpg","D","Coach Brain, found","",
  "A warm control room. Coach Brain in a tracksuit with a mug and a small gold key on a chain. He "
  "is not caught out, he is delighted to be found. Establish the key clearly, it is the object the "
  "film turns on.",
  "COACH BRAIN: \"You found me. Took you long enough.\""),
 (P+"/S4_P2.jpg","L","The two of them, level",
  "SETUP B. Seated eyeline, tennis ball on a stand at seated height, camera left. Do not relight "
  "between A and B, only move the mark. Shoot the line, then ten seconds of him listening.",
  "The console wall behind them. Evenly matched in the frame, same size, same weight. Nobody is "
  "above anybody.",
  "\"You closed that door.\"\nNot an accusation. He is working it out in the moment."),
 (P+"/S4_P3.jpg","D","The network","",
  "Five readouts converging on one dial: heart, breath, temperature, water, distance. One click as "
  "each connects. The dial carries a red arc and twenty seven tick marks.",
  "COACH BRAIN: \"Heart rate. Breath. Temperature. Water. Distance. I'm asking one question. Can "
  "we keep going safely?\""),
 (V+"/V7_4_4_phone.jpg","N","Low power, on his own phone",
  "SETUP E. His room, at his desk, holding his own phone up, screen switched off on the day.",
  "The low power warning is composited onto the real screen afterwards, and his thumb covers part "
  "of it exactly as a thumb does.",
  "Your note, and it works. The analogy is Manan's own from his first draft, and it lands harder "
  "on a real phone in a real hand than on a drawn one.\nVoice over. \"Like a phone at twenty "
  "percent. Not broken. Protecting itself.\""),
 (P+"/S4_P5.jpg","D","He is not sorry","",
  "Coach Brain in close up, wide open and entirely unembarrassed. A teacher with a better model of "
  "the situation than his student has.",
  "COACH BRAIN: \"My best judgement. I'm not trying to stop you. I'm trying to get you to the "
  "finish line.\""),
 (P+"/S4_P6.jpg","L","Manan arrives at it",
  "SETUP B. Same light, same mark. He should sound like he is discovering the idea, not stating "
  "it. Shoot the thinking as well as the line.",
  "Coach Brain works the console beside him. Small subtitle, two seconds: Central Governor Theory, "
  "Prof. Tim Noakes, 1997, and that scientists still debate how brain and muscle share the work.",
  "In profile, hand at his chin.\n\"So the limit isn't my body. It's your judgement.\""),
])

S[5] = ("THE EXPERIMENT","1:12 – 1:34",[
 (P+"/S5_P1.jpg","D","A cyclist and a ghost","",
  "A clean laboratory, not a clinical one. The cyclist on a stationary bike facing a screen with a "
  "translucent version of himself on it. Short. This is a citation now, not a scene.",
  "Voice over. \"So they let a cyclist race a recording of his own best ride.\""),
 (P+"/S5_P2.jpg","D","YOU and BEST, and the two percent","",
  "The screen, plainly lettered, his ghost ahead of him. A researcher's hand turns a dial. +2% on "
  "the monitor, one conspiratorial click, nothing said.",
  "Voice over. \"Except they made the ghost two percent faster. And they didn't tell him.\""),
 (P+"/S5_P6.jpg","D","He passes his own best","",
  "He goes by, spent and astonished, the ghost dissolving behind him.",
  "Voice over. \"He beat his own maximum. Which means it was never his maximum.\""),
 (V+"/V7_5_4_idea_lands.jpg","N","The idea lands",
  "SETUP E. His room, at his desk, the study finishing on his laptop. He sits back, a beat, then "
  "he is already getting up, out of frame before the shot is ready to end.",
  "Nothing drawn. This frame is entirely his.",
  "The turn of the whole scene, and it is played as appetite, not understanding. He does not nod "
  "because he grasped something. He gets up because he cannot sit still.\nNo line. It is on his "
  "face and then on the empty chair."),
 (V+"/V7_5_5_road.jpg","N","Out on the road",
  "EXTERIOR, NEW LOCATION. An ordinary quiet road near the house, early morning. Manan riding hard, "
  "shot side on from a following vehicle or a fixed wide as he passes. Helmet on. Thirty minutes, "
  "and it is the only time the shoot leaves the house.",
  "Nothing drawn. This footage is what plays on the laptop for the rest of the scene.",
  "Voice over, dry and a little amused at himself. \"So I tried it.\""),
 (V+"/V7_5_1_bike.jpg","N","Racing himself",
  "SETUP G. His room, stationary bike, the road footage playing on the laptop in front of him. "
  "Wide. Three layers: him near, the screen middle, the window behind.",
  "The screen content is composited afterwards so the edit can change what is on it.",
  "Voice over. \"Same legs. Same road. Same everything.\"\n"
  "NOTE: this frame was made before the wardrobe was settled and shows the hoodie. On the day he "
  "is in a t shirt, as in 5.7 and 5.8."),
 (V+"/V7_5_7_the_wall.jpg","N","The wall",
  "SETUP G, closer. He is level with the recording and cannot get past it. Teeth, sweat, the "
  "effort completely real.",
  "Nothing drawn.",
  "Nothing spoken. Let it run. The sound carries this: breath, chain, the room.\nThis is the place "
  "where the film began, where the runner's head went back."),
 (V+"/V7_5_8_eyes_closed.jpg","N","Eyes closed",
  "SETUP G, close. He closes his eyes. Two seconds of nothing at all, just breath. Then his legs "
  "pick up, his eyes open, he is ahead of the recording, and he laughs.",
  "A brief cut away to the drawn fibres lighting, three or four frames of the 6.4 artwork arriving "
  "early. Nothing is composited onto his leg and nothing glows on him. Drawn stays drawn.",
  "Voice over, over the closed eyes. \"Nothing about my legs changed.\"\nThen, after he opens "
  "them: \"Only what I believed they had left.\"\nHe never says the words attention, or breathing, "
  "or meditation. He closes his eyes, it works, he laughs."),
])

S[6] = ("THE RELEASE","1:34 – 1:48",[
 (P+"/S6_P1.jpg","D","The check comes back green","",
  "Coach Brain at the console running his safety check, every reading green. He chooses. He is not "
  "overpowered and not tricked, and this is the single most important gesture in the film.",
  "COACH BRAIN: \"All right. Everything's holding. Let's give him a little more.\""),
 (P+"/S6_P2.jpg","D","His hand on the lever","",
  "The lever with his hand on it, and it must start LOW on the scale, well below 95. As boarded it "
  "already sits high, which makes the move across this panel and the next read as travelling "
  "downward and reverses the whole scene. Low here, higher in the next frame.",
  "Nothing under this."),
 (P+"/S6_P3.jpg","D","Eased open, and never to a hundred","",
  "The lever moves up and stops at 95. The gap of open track between the ball and 100 stays "
  "visible and is the moral architecture of the film.",
  "Caption, small: Never to one hundred.\nVoice over. \"More fibres recruited. Notice, still not "
  "all of them.\""),
 (P+"/S6_P4.jpg","D","Fibres lighting","",
  "Muscle fibres lighting in scattered clusters inside a semi transparent leg. In sequence, never "
  "all at once, and never all of them.","Voice over continues."),
 (P+"/S6_P5.jpg","D","More of them, and still not all","",
  "More clusters lit, a clear proportion still dark. The reserve is inside the runner and it was "
  "always his. Nothing is given to him from outside.","Nothing."),
 (P+"/S6_P6.jpg","D","Bodies finally permitted","",
  "Traceur rooftop to rooftop, a dancer turning in the air, a swimmer leaving the wall. Each one "
  "higher in frame than the last. Rapid and rising. This is where the audience gets goosebumps.",
  "Voice over. \"The brain didn't make new energy. It gave permission.\"\n"
  "OPTIONAL, FIVE MINUTES: SETUP D, Manan jumping on the spot, arms out, laughing, high frame "
  "rate. Not boarded, costs almost nothing, gives the edit the option of putting him inside this."),
])

S[7] = ("THE VERDICT","1:48 – 1:54",[
 (P+"/S7_P1.jpg","D","Everything drains to white","",
  "The Muscle and Coach Brain a long way apart in a white field, facing each other. Stillness "
  "after the release. Do not rush this.","Nothing. The silence is doing the work."),
 (P+"/S7_P2.jpg","D","The brake between them","",
  "The lever alone in the white, standing between the two of them. The object they have been "
  "arguing about for a hundred years.","Nothing."),
 (V+"/V7_7_3_white.jpg","N","They walk toward each other, and he is there",
  "SETUP C. The white void, the same setup as scene 8, so those two scenes share one lighting "
  "state. He stands at the left, back to camera, watching.",
  "The Muscle and Coach Brain are cut off their paper and placed in the same white field, standing "
  "on the same floor with the same contact shadows.",
  "The hardest composite in the film and it holds: a photographed boy and two drawn characters "
  "sharing one space, one light, one floor.\nVoice over. \"Hill was right about the muscle. Noakes "
  "was right about the brain.\""),
 (P+"/S7_P4.jpg","D","The handshake","",
  "They shake hands. The answer to the question the film opened with, given as a gesture rather "
  "than as a statement.","Voice over continues."),
 (P+"/S7_P5.jpg","D","1923 and 1997","",
  "Two cards, an arm on one and a brain on the other, dated. Clean and plain.",
  "Voice over. \"Today the evidence says both. And researchers are still working out exactly "
  "how.\""),
 (P+"/S7_P6.jpg","D","Still being tested","",
  "The two cards overlapping in the white. The most credible seconds in the film, because it "
  "admits what is not yet settled.",
  "\"Great ideas aren't accepted because they sound convincing. They're accepted because "
  "scientists keep testing them.\"\nManan's own line, word for word from his first draft."),
])

S[8] = ("THE INVITATION","1:54 – 2:00",[
 (P+"/S8_P1.jpg","L","Alone, breathing",
  "SETUP C. White void, flat even light from both sides, no modelling, no shadow on the backdrop. "
  "The brightest and calmest setup of the day. Roll a full unbroken minute and use the stillest "
  "twenty frames.",
  "White all round him. Nothing drawn in this frame at all.",
  "Arms at his sides, eyes closed, simply breathing. No performance of any kind. The hardest thing "
  "on the call sheet, and the reason it is shot last.\nIt is also the same gesture as 5.8, and by "
  "now the audience knows what it means without being told."),
 (P+"/S8_P2.jpg","D","The finish line","",
  "The runner crossing, seen down the road from scene one. The film returns to where it started "
  "and the question has been answered.","Nothing."),
 (V+"/V7_8_3_lever_drawn.jpg","L","His own hand on the lever",
  "SETUP C, insert. His hand alone, resting on a real ball at chest height, so the fingers and the "
  "weight are right. A few seconds, held.",
  "The lever drawn around his real hand. The ball must sit at 95 with the short gap open above it. "
  "The drawn version shown here still reads slightly under 95 and the composite will correct it "
  "exactly.",
  "Just the hand. Steady, unhurried, no grip and no drama.\nA real hand from the world of evidence "
  "reaching into the world of explanation is the thesis and the climax at the same time."),
 (P+"/S8_P4.jpg","D","Coach Brain takes off the key","",
  "He lifts the small gold key from his own neck. No fanfare, no ceremony. He is handing over a "
  "job.","Nothing."),
 (P+"/S8_P5.jpg","L","The key handed across",
  "SETUP C. Receiving at chest height, then looking up. Give him a real key so the hand knows what "
  "to do.",
  "Coach Brain's drawn hand and Manan's photographed palm in one frame. The gold of the key is the "
  "only colour anywhere in the film.",
  "He takes it.\n\"The wall is real. But somebody set it.\"\nCertain and unhurried, never "
  "triumphant. One sentence per take."),
 (P+"/S8_P6.jpg","L","Eyes open",
  "SETUP C. Wider, to lens, key in one hand and the other resting on the lever. Shoot the last "
  "line several times and let the last take be the tired one.",
  "The lever beside him, the key in his hand. Then black, and the end card.",
  "\"And what your brain believes is safe can be trained.\"\nThen his own closing line, kept from "
  "his first draft:\n\"So the next time you watch an athlete find one last burst of speed, don't "
  "just wonder how strong their muscles are. Wonder what their brain believed was still safe.\""),
])

# ------------------------------------------------------------------ counts
frames = sum(len(S[k][2]) for k in S)
live = sum(1 for k in S for f in S[k][2] if f[1] in ('L','N'))
newf = sum(1 for k in S for f in S[k][2] if f[1] == 'N')

bg()
# ---------------------------------------------------------------- cover
y = H-92
c.setFont('DB',30); c.setFillColor(INK); c.drawString(ML,y,"THE BRAIN BRAKE")
y-=26; c.setFont('DO',12); c.setFillColor(SOFT)
c.drawString(ML,y,"Version two. Your notes, built.")
y-=40
c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y,W-MR,y); y-=26
y = para(ML,y,"Neha, this is version one with everything you marked on it folded in. Where a frame "
              "changed, the change is described on the frame itself so you can see the reasoning "
              "next to the picture rather than in a covering note.",'D',10,14)
y-=12
y = para(ML,y,"You were right that Manan should be more visible. He is now in twenty two frames "
              "instead of twelve, and in almost all of the new ones he is doing something rather "
              "than saying something.",'D',10,14)
y-=24
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"THE SPLIT"); y-=18
for a,b in [(str(frames),"frames"),(str(live),"need Manan in front of a camera"),
            (str(frames-live),"are drawn and need nobody"),(str(newf),"are new since version one"),
            ("2","shooting locations, his room and one road"),
            ("7","setups, and three of them share one lighting state")]:
    c.setFont('MB',13); c.setFillColor(INK); c.drawRightString(ML+30,y,a)
    c.setFont('D',9.5); c.setFillColor(SOFT); c.drawString(ML+42,y+1,b); y-=20
y-=14
y = para(ML,y,"The day is longer than version one because he is in more of it. Most of it is his "
              "own bedroom in his own clothes, which is the cheapest kind of extra day there is.",
         'D',10,14)
newpage()

# ---------------------------------------------------------------- your notes
y = H-80
c.setFont('DB',20); c.setFillColor(INK); c.drawString(ML,y,"Your notes, one by one")
y-=12; c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=26

notes = [
 ("YES","Shoot the voice over lines as video of him talking, study room or grey wall.",
  "Agreed completely. It costs a few hours on a day we are shooting anyway and it gives the edit "
  "every option. We shoot all of it and decide later what is picture and what is voice."),
 ("YES","Can Manan write 1923 and the chain on a board. Can he hold the phone. Can he ride a bike. "
  "Can we shoot over his shoulder for the stamp.",
  "These were the best notes in the document and they are all in. Frames 2.1, 2.6, 4.4 and the "
  "whole of scene five. This is not Manan added to the film, it is Manan inside it."),
 ("NO","The small box in the corner with his talking video while the animation plays in the centre.",
  "This is the one I pushed back on. A rectangle in the corner with a talking head in it reads as "
  "a webcam, and audiences have been trained to ignore that corner. It also breaks the rule the "
  "whole look depends on: every frame is three layers and the boy is one of them. A box is not a "
  "layer, it sits on top like a sticker, and the moment he is a sticker he stops being the "
  "protagonist and becomes a caption.\nInstead there are two devices doing the same job better, "
  "the over the shoulder foreground and the magnifying glass as a window. Both are in this "
  "document, on frames 2.6 and 2.3."),
 ("NO","Does Manan need the factory worker costume. Can we shoot at a real pump with a LACTATE "
  "PUMP board.",
  "No costume, and no real pump. The factory is the old theory, the thing the film is disproving. "
  "The second he puts on overalls he stops being the person investigating it and becomes a "
  "character inside it. The workers are also cartoons two and a half heads tall, so the scale "
  "would fall apart beside a real boy.\nThe line is: he can do real things a real boy does, and he "
  "does not dress up as a drawn character or stand inside a metaphor."),
 ("ASK","Usain Bolt, written at the top of page four.",
  "I was not sure what this meant. Our runner is a marathon runner rather than a sprinter, and "
  "naming a real athlete in a competition entry brings complications. Tell me what you had in mind."),
]
for tag, note, ans in notes:
    if y < 150:
        newpage(); y = H-80
    col = NEW if tag=="YES" else (LIVE if tag=="NO" else ACC)
    c.setFont('MB',9); c.setFillColor(col); c.drawString(ML,y,tag)
    y = para(ML+40,y,note,'DB',9.4,12.8,CW-40)
    y -= 4
    y = para(ML+40,y,ans,'D',9.2,12.6,CW-40,SOFT)
    y -= 18
newpage()

# ---------------------------------------------------------------- the day
y = H-80
c.setFont('DB',20); c.setFillColor(INK); c.drawString(ML,y,"The shooting day")
y-=12; c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=24

setups = [
 ("A","Grey backdrop, walking and reacting",
  "Eye level on sticks, locked off. Soft key from camera left at forty five degrees, large source. "
  "Fill from the right at half strength. Frames 1.5, 1.6, 2.6, 3.2, 3.3, 3.4, 3.6."),
 ("B","Seated eyeline, reacting to Coach Brain",
  "The same lighting as A, unchanged. Tennis ball on a stand at seated height, camera left. Do not "
  "relight, only move the mark. Frames 4.2, 4.6."),
 ("C","White void, still, to lens",
  "Flat even light from both sides, no modelling, no shadow on the backdrop. Now serves scene "
  "seven as well as scene eight. Frames 7.3, 8.1, 8.3, 8.5, 8.6."),
 ("D","Jump, high frame rate. Optional, five minutes.",
  "Same as C, wider, room above his head. Shoot it last when he is loose."),
 ("E","His room, at his desk",
  "Warm window light, no lamps fighting it. Frames 2.3, 4.4, 5.4."),
 ("F","His room, at the blackboard",
  "Same light, standing. A real blackboard leaning on the wall, shot completely clean. Frame 2.1."),
 ("G","His room, on the stationary bike",
  "Same light. Wide, then closer, then close. Frames 5.6, 5.7, 5.8. Half an hour."),
 ("EXT","One quiet road, early morning",
  "Riding hard, side on. Thirty minutes, and the only time the shoot leaves the house. Frame 5.5."),
]
for k,t,d in setups:
    if y < 110:
        newpage(); y = H-80
    c.setFont('MB',10); c.setFillColor(ACC); c.drawString(ML,y,k)
    c.setFont('DB',9.4); c.setFillColor(INK); c.drawString(ML+30,y,t)
    y-=13
    y = para(ML+30,y,d,'D',8.6,11.4,CW-30,SOFT)
    y-=12

y -= 6
if y < 260:
    newpage(); y = H-80
c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=22
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"YOUR PROP LIST, CONFIRMED"); y-=16
y = para(ML,y,"Plain grey background. Tennis ball on a stand. Brass magnifying glass. A real "
              "blackboard and white chalk. A stationary exercise bike. A bicycle and a plain dark "
              "helmet. A small gold key. A ball at chest height for the lever insert. His own "
              "phone and his own laptop.",'D',9.2,12.6)
y-=18
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"WARDROBE"); y-=16
y = para(ML,y,"The grey hoodie everywhere, except on the stationary bike, where he is in a plain "
              "t shirt. He rides the road in the hoodie, comes back sweating, takes it off and "
              "races the recording in a t shirt. The change reads as time passing between the "
              "outdoor ride and the indoor session, which is exactly the gap the scene needs and "
              "never states. Plain mid grey, no logos, no stripes.",'D',9.2,12.6)
y-=18
c.setFont('MB',9); c.setFillColor(ACC); c.drawString(ML,y,"FOR MANAN, BEFORE THE DAY"); y-=16
y = para(ML,y,"He should know the lines well enough to forget them. Every one is written to sound "
              "like somebody working something out rather than somebody explaining it. The best "
              "takes on this film will be the ones where he is thinking, not the ones where he is "
              "right.\nThree moments carry more than the rest. Frame 3.6, where he turns to us in "
              "the hall of tanks. Frame 5.4, where the idea lands and he gets up mid shot. And "
              "frame 8.1, where he stands still with his eyes closed and does nothing at all.",
         'D',9.2,12.6)
newpage()

# ---------------------------------------------------------------- frames
IMGW = 252.0
TXTX = ML + IMGW + 18
TXTW = W - MR - TXTX
BOT = 50.0
FS, LEAD = 8.0, 10.4

def block_h(title, cam, ani, man, ih):
    h = len(wrap(title,'DB',10.5,TXTW))*13.2 + 6
    for body in [cam if cam else "Nothing on the day. This frame is drawn.", ani, man]:
        h += 9.8 + len(wrap(body,'D',FS,LEAD and FS and TXTW))*LEAD + 7
    return max(h, ih+16) + 11

for sc in range(1,9):
    title, timing, fr = S[sc]
    y = H-74
    c.setFont('MB',9); c.setFillColor(ACC)
    c.drawString(ML,y+22,"SCENE %d OF 8   ·   %s" % (sc,timing))
    c.setFont('DB',21); c.setFillColor(INK); c.drawString(ML,y,title)
    c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(ML,y-14,W-MR,y-14)
    top = y-38

    for i,(img,tag,ftitle,cam,ani,man) in enumerate(fr):
        p = small(img,1500)
        im = Image.open(p); ar = im.size[0]/im.size[1]
        ih = IMGW/ar
        need = block_h(ftitle,cam,ani,man,ih)
        if top-need < BOT:
            newpage(); top = H-74
        ytop = top
        c.drawImage(ImageReader(p), ML, ytop-ih, IMGW, ih, mask=None)
        lab = {'D':"DRAWN",'L':"DRAWN + LIVE ACTION",'N':"NEW  ·  DRAWN + LIVE ACTION"}[tag]
        col = {'D':SOFT,'L':LIVE,'N':NEW}[tag]
        c.setFont('MB',8.5); c.setFillColor(col)
        c.drawString(ML, ytop-ih-13, "%d.%d" % (sc,i+1))
        c.setFont('D',7.8); c.setFillColor(col if tag=='N' else SOFT)
        c.drawString(ML+26, ytop-ih-13, lab)

        ty = ytop
        c.setFont('DB',10.5); c.setFillColor(INK)
        for ln in wrap(ftitle,'DB',10.5,TXTW):
            c.drawString(TXTX,ty,ln); ty-=13.2
        ty-=6
        for label, body, cl in [("CAMERA · VENKATESH", cam if cam else
                                 "Nothing on the day. This frame is drawn.", LIVE if cam else SOFT),
                                ("ANIMATION · KRISTIJAN", ani, ACC),
                                ("MANAN", man, ACC)]:
            c.setFont('MB',6.8); c.setFillColor(cl); c.drawString(TXTX,ty,label); ty-=9.8
            ty = para(TXTX,ty,body,'D',FS,LEAD,TXTW)
            ty-=7
        top = ytop-need
    newpage()

# ---------------------------------------------------------------- last page
y = H-90
c.setFont('DB',20); c.setFillColor(INK); c.drawString(ML,y,"Still open")
y-=30
y = para(ML,y,"Coach Brain has four spoken lines and still needs a voice. He can be Manan pitched "
              "differently or somebody else entirely. Whoever it is, he is never sly and never a "
              "villain. He is a teacher who is pleased to have been found.",'D',9.6,13.4)
y-=14
y = para(ML,y,"Usain Bolt, from your page four. Tell me what you meant and I will build it if it "
              "fits.",'D',9.6,13.4)
y-=14
y = para(ML,y,"Frame 5.6 was made before the wardrobe was settled and shows the hoodie on the "
              "stationary bike. On the day it is a t shirt. The picture will be remade, it changes "
              "nothing about the shoot.",'D',9.6,13.4)
y-=34
c.setStrokeColor(RULE); c.line(ML,y,W-MR,y); y-=30
c.setFont('DO',13); c.setFillColor(SOFT)
c.drawString(ML,y,"The wall is real. But somebody set it.")
foot(); c.showPage(); c.save()
print("written", OUT, os.path.getsize(OUT), "frames", frames, "live", live, "new", newf)
