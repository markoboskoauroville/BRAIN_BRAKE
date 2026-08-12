# THE BRAIN BRAKE, version six
# Frame by frame production breakdown for Neha.
# For every one of the 48 boarded frames: what camera shoots, what animation draws,
# what Manan does and says.

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image
import os

for n, f in [('D', 'DejaVuSans.ttf'), ('DB', 'DejaVuSans-Bold.ttf'),
             ('DO', 'DejaVuSans-Oblique.ttf'), ('M', 'DejaVuSansMono.ttf'),
             ('MB', 'DejaVuSansMono-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(n, '/usr/share/fonts/truetype/dejavu/' + f))

W, H = A4
ML, MR = 46, 46
PAPER = HexColor("#f2ebda")
INK = HexColor("#2b2822")
SOFT = HexColor("#6f6757")
ACC = HexColor("#8a6b2e")
RULE = HexColor("#c9bfa4")
LIVE = HexColor("#8a3b2e")

OUT = "/home/claude/out/8 - v6 production breakdown - Neha.pdf"
os.makedirs("/home/claude/out", exist_ok=True)
c = canvas.Canvas(OUT, pagesize=A4)
page = [0]


def bg():
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def footer():
    page[0] += 1
    c.setFont('M', 7)
    c.setFillColor(SOFT)
    c.drawString(ML, 30, "THE BRAIN BRAKE  ·  version six  ·  production breakdown for Neha")
    c.drawRightString(W - MR, 30, str(page[0]))


def newpage():
    footer()
    c.showPage()
    bg()


def wrap(text, font, size, maxw):
    out = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            out.append("")
            continue
        line = words[0]
        for w in words[1:]:
            if pdfmetrics.stringWidth(line + " " + w, font, size) <= maxw:
                line += " " + w
            else:
                out.append(line)
                line = w
        out.append(line)
    return out


def para(x, y, text, font='D', size=8, lead=10.4, maxw=240, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in wrap(text, font, size, maxw):
        c.drawString(x, y, ln)
        y -= lead
    return y


# ------------------------------------------------------------------ content
# (panel file, frame title, camera, animation, manan)
# camera == "" means nothing is shot for this frame.

S = {}

S[1] = ("THE MYSTERY", "0:00 – 0:14", [
 ("S1_P1", "The runner at the end of himself",
  "",
  "Full drawn wide. He is finished: head rolling, legs gone, the crowd thin and quiet behind the barriers, "
  "the road running away to the horizon. Shot 6.4 rhymes this frame exactly, same composition and opposite "
  "feeling, so the camera position chosen here is locked for the rest of the film.",
  "Voice over only. \"For a hundred years we thought the answer was in the muscles.\""),
 ("S1_P2", "His face",
  "",
  "Drawn close up, sweat and breath. He is lean and about thirty five. He is at the end of a race, not at "
  "the end of a life, and the whole first scene fails if he reads as an old man.",
  "Voice over continues."),
 ("S1_P3", "He explodes into a sprint",
  "",
  "The impossible thing, and it happens without warning. Diagonal, violent, left to right, horizon low so "
  "he sits high in frame. Speed lines, grit lifting, the crowd coming up off the barriers.",
  "Nothing. Let the picture do it."),
 ("S1_P4", "The sprint carries",
  "",
  "Held on the sprint, a bottle thrown, the crowd on its feet. Two or three seconds of pure disbelief "
  "before the film stops dead.",
  "Nothing."),
 ("S1_P5", "Everything freezes and Manan walks in",
  "SETUP A. Grey backdrop, mid shot, camera at eye level on sticks, locked off. He walks slowly across "
  "frame looking left and right at nothing at all. Shoot thirty seconds of pure observing with no lines. "
  "One dominant key from camera left, hard enough that his shadow has a shape, because that shadow gets "
  "drawn onto the road afterwards and it is the single thing the whole look depends on.",
  "The world stops: crowd, runner, thrown bottle, all held. Manan is cut in and his shadow is drawn onto "
  "the tarmac, crossing the pencil lines so they stay visible through it. That shadow is what makes him "
  "stand in the drawing instead of on top of it.",
  "Walking through a stopped world with the magnifying glass raised, looking at things. Curious, taking "
  "his time. No line here. He is not performing for anyone, he is just looking."),
 ("S1_P6", "He turns to us and asks the question",
  "SETUP A. Close up, same light, to lens. Six takes minimum and use the most unguarded.",
  "The frozen crowd stays behind him. Title over.",
  "He lowers the glass and turns to camera.\n"
  "\"Hold on. He had nothing left. So where did THAT come from?\"\n"
  "Curious and amused, never presenting. He has just noticed something, he is not announcing it."),
])

S[2] = ("THE OLD THEORY", "0:14 – 0:30", [
 ("S2_P1", "1923, and the man who answered it",
  "",
  "A lecture room of the period, empty desks, blackboard, A. V. Hill's portrait on the wall. Warm and "
  "respectful. There is no villain in this film and this scene is where that is decided.",
  "Voice over. \"A. V. Hill, Nobel prize, 1923.\""),
 ("S2_P2", "The chain that held for a century",
  "",
  "The chain writes itself on the board one box at a time: RUN FASTER, OXYGEN, LACTATE, FATIGUE, STOP. "
  "Chalk the year 1923 at the top of the board. This panel will be screenshotted on its own, and without "
  "the year on it the board states a hundred year old theory as current fact.",
  "Voice over. \"Run hard, run out of oxygen, and the muscle stops.\""),
 ("S2_P3", "Inside the leg, a working factory",
  "",
  "The muscle as an industrial plant, gears turning, belts running, crates arriving, a delivery of glucose "
  "at the loading bay. Everything healthy and in rhythm. This is Manan's own image from his first draft "
  "and it earns its place by being the clearest picture of the old theory anyone has drawn.",
  "Voice over."),
 ("S2_P4", "The supply stops",
  "",
  "The alarm turns, a worker straightens up and shrugs, palms open. The supply is failing, the machine is "
  "not breaking. Resigned, not frightened. This is a shift ending, not a disaster.",
  "Worker's line, one voice, dry. \"That's it. We're done.\""),
 ("S2_P5", "The lactate pump",
  "",
  "Two workers at the pump with their hands on their heads, steam going up. The old theory's villain, "
  "lactate, drawn exactly as the theory imagined it.",
  "Voice over."),
 ("S2_P6", "Case closed, and the crack",
  "",
  "The stamp comes down over the whole factory with real weight. Then a fine crack runs across the face of "
  "it and the sprint replays inside the crack. The crack is the scene. Everything before it exists to make "
  "this land.",
  "Voice over. \"Case closed. For a hundred years.\"\nThen, over the crack: \"Except it doesn't explain this.\""),
])

S[3] = ("THE FULL TANK", "0:30 – 0:48", [
 ("S3_P1", "The back of the factory",
  "",
  "Wide of the plant from outside, and one door in it that nobody has opened. Quiet after the noise of "
  "scene two.",
  "Voice over."),
 ("S3_P2", "His hand on the door",
  "SETUP A. He stands with his back to camera and puts his palm flat on a mark at chest height, head "
  "tilted, listening. There is nothing really there. Hold it, then let him lean into it.",
  "The riveted door is drawn around his hand, with a keyhole beside it and light behind the keyhole. His "
  "shadow falls on the door.",
  "Back to camera, palm flat, listening. He is curious rather than cautious.\n"
  "Voice over. \"At the back of the factory there is a door nobody opens.\""),
 ("S3_P3", "The door swings",
  "SETUP A. Silhouette from behind, then turning into the light. Shoot it both ways.",
  "The door opens and warm light floods out over him. This is the first warm light in the film and it "
  "arrives as a discovery, not as a threat.",
  "He pushes and steps into the light. No line."),
 ("S3_P4", "The hall of tanks",
  "SETUP A. Back of his head and shoulder in the near foreground, held still.",
  "Row upon row of storage tanks receding into the distance. Nine tanks visible, the nearest one stencilled "
  "9. The reveal, and the first big lift in the film. Discovery, not warning.",
  "Looking. Nothing else.\nVoice over: when scientists tested athletes at the exact moment they gave up, the "
  "muscles could still produce far more power than the athlete had just produced."),
 ("S3_P5", "Every gauge full",
  "",
  "One gauge in close up, the needle hard over on FULL. This instrument governs the rest of the film, so "
  "establish it clearly here.",
  "Nothing."),
 ("S3_P6", "He turns to us",
  "SETUP A. Close up, to lens, lit by the warm light coming from the tanks. This is the most important "
  "take of the shooting day. Shoot it many times and use the most unguarded one.",
  "The hall behind him. He must be turned to the lens in this frame: as boarded, scene three never shows "
  "his face once, and this is the scene where the audience decides whether the boy understands what he is "
  "saying.",
  "Delighted rather than shocked. He has found something, and it is better than what he expected to find.\n"
  "\"It was never empty. Somebody closed that door.\""),
])

S[4] = ("THE GATEKEEPER", "0:48 – 1:14", [
 ("S4_P1", "Coach Brain, found",
  "",
  "A warm control room, monitors and dials on every wall. Coach Brain in a tracksuit in a swivel chair "
  "with a mug and a small gold key on a chain at his chest. He is not caught out. He is delighted to be "
  "found. Establish the key clearly here, it is the object the whole film turns on.",
  "Voice over hands over.\nCOACH BRAIN: \"You found me. Took you long enough.\""),
 ("S4_P2", "The two of them, level",
  "SETUP B. Seated eyeline. A tennis ball on a stand at seated height, camera left, for him to look at. "
  "Do not relight between setup A and setup B, only move the eyeline mark. Shoot the line, then ten "
  "seconds of him simply listening.",
  "The console wall behind them. The two characters are evenly matched in the frame, the same size and "
  "the same weight. Nobody is above anybody here.",
  "Facing Coach Brain, level with him.\n\"You closed that door.\"\nNot an accusation. He is working it out "
  "in the moment."),
 ("S4_P3", "The network",
  "",
  "Five readouts converging on one dial: heart, breath, temperature, water, distance. One click as each "
  "one connects, five evenly spaced. The dial carries a red arc and twenty seven tick marks.",
  "COACH BRAIN: \"Heart rate. Breath. Temperature. Water. Distance. I'm asking one question. Can we keep "
  "going safely?\""),
 ("S4_P4", "Low power mode",
  "",
  "Two seconds of a phone dimming, apps closing around the edges. A generic phone with no brand anywhere "
  "on it. This is Manan's own analogy from his first draft and it is the clearest everyday explanation in "
  "either version, so it is kept and compressed.",
  "Voice over. \"Like a phone at twenty percent. Not broken. Protecting itself.\""),
 ("S4_P5", "He is not sorry",
  "",
  "Coach Brain in close up, wide open and entirely unembarrassed. He is a teacher with a better model of "
  "the situation than his student has, and he knows it.",
  "COACH BRAIN: \"My best judgement. I'm not trying to stop you. I'm trying to get you to the finish line.\""),
 ("S4_P6", "Manan arrives at it",
  "SETUP B. Same light, same eyeline mark. He should sound like he is discovering the idea, not stating "
  "it. Shoot the thinking as well as the line.",
  "Coach Brain works the console beside him without looking up. A small subtitle low in frame, in and out "
  "in two seconds: Central Governor Theory, proposed by Prof. Tim Noakes, 1997, and that scientists still "
  "debate how brain and muscle share the work. That honesty is scored by the judges.",
  "In profile, hand at his chin, working it out.\n\"So the limit isn't my body. It's your judgement.\""),
])

S[5] = ("THE TRICK", "1:14 – 1:30", [
 ("S5_P1", "A cyclist and a ghost",
  "",
  "A clean laboratory, not a clinical one. The cyclist on a stationary bike facing a screen with a "
  "translucent version of himself on it.",
  "Voice over. \"So they let a cyclist race a recording of his own best ride.\""),
 ("S5_P2", "YOU and BEST",
  "",
  "The screen, plainly lettered, his ghost ahead of him. These two words and the figure +2% are the only "
  "lettering permitted anywhere in this scene.",
  "Voice over."),
 ("S5_P3", "The two percent",
  "",
  "The researcher at the console quietly turning the ghost up. One conspiratorial click and nothing said. "
  "+2% on the monitor, lap counter on 27.",
  "Voice over. \"Except they made the ghost two percent faster. And they didn't tell him.\""),
 ("S5_P4", "He chases",
  "",
  "The cyclist's face in close up, teeth bared, sweat coming off him. His expression is the shot.",
  "Nothing under this. Let it run."),
 ("S5_P5", "He draws level",
  "",
  "The screen again, the two riders overlapping. Cut this scene like a race. The overlap as he comes "
  "through is the money frame of the sequence.",
  "Nothing."),
 ("S5_P6", "He passes his own best",
  "",
  "He goes by, spent and astonished, and the ghost dissolves behind him.",
  "Voice over. \"He beat his own maximum. Which means it was never his maximum.\"\n"
  "Keep his laugh in the sound if there is one."),
])

S[6] = ("THE RELEASE", "1:30 – 1:46", [
 ("S6_P1", "The check comes back green",
  "",
  "Coach Brain at the console running his safety check, every reading coming back green. He chooses. He "
  "is not overpowered and he is not tricked, and this is the single most important gesture in the film.",
  "COACH BRAIN: \"All right. Everything's holding. Let's give him a little more.\""),
 ("S6_P2", "His hand on the lever",
  "",
  "The lever with his hand on it, and it must start LOW on the scale, well below 95. As boarded it already "
  "sits high, which makes the move across this panel and the next read as travelling downward and reverses "
  "the meaning of the whole scene. Low here, higher in the next frame.",
  "Nothing under this."),
 ("S6_P3", "Eased open, and never to a hundred",
  "",
  "The lever moves up and stops at 95. The gap of open track between the ball and 100 stays visible and is "
  "the moral architecture of the film. Protect it in every frame it appears.",
  "Caption, small: Never to one hundred.\nVoice over. \"More fibres recruited. Notice, still not all of them.\""),
 ("S6_P4", "Fibres lighting",
  "",
  "Muscle fibres lighting in scattered clusters inside a semi transparent leg. In sequence, never all at "
  "once, and never all of them.",
  "Voice over continues."),
 ("S6_P5", "More of them, and still not all",
  "",
  "More clusters lit, and a clear proportion still dark. The reserve is inside the runner and it was "
  "always his. Nothing is given to him from outside.",
  "Nothing."),
 ("S6_P6", "Bodies finally permitted",
  "",
  "Traceur rooftop to rooftop, a dancer turning in the air, a swimmer leaving the wall. Each one higher in "
  "frame than the last. Rapid and rising. This is where the audience gets goosebumps.",
  "Voice over. \"The brain didn't make new energy. It gave permission.\"\n"
  "OPTIONAL AND WORTH FIVE MINUTES ON THE DAY: SETUP D, Manan jumping on the spot against grey, arms out, "
  "laughing, high frame rate if the camera allows. It is not boarded, it costs almost nothing, and it "
  "gives the edit the option of putting him inside this moment."),
])

S[7] = ("THE VERDICT", "1:46 – 1:54", [
 ("S7_P1", "Everything drains to white",
  "",
  "The Muscle and Coach Brain a long way apart in a white field, facing each other. Stillness after the "
  "release. Do not rush this.",
  "Nothing. The silence is doing the work."),
 ("S7_P2", "The brake between them",
  "",
  "The lever alone in the white, standing between the two of them. The object they have been arguing "
  "about for a hundred years.",
  "Nothing."),
 ("S7_P3", "They walk toward each other",
  "",
  "Both walking in, easy and unhurried. No winner is being decided here.",
  "Voice over begins. \"Hill was right about the muscle. Noakes was right about the brain.\""),
 ("S7_P4", "The handshake",
  "",
  "They shake hands. This is the answer to the question the film opened with, and it is given as a gesture "
  "rather than as a statement.",
  "Voice over continues."),
 ("S7_P5", "1923 and 1997",
  "",
  "Two cards, an arm on one and a brain on the other, dated. Clean and plain.",
  "Voice over. \"Today the evidence says both. And researchers are still working out exactly how.\""),
 ("S7_P6", "Still being tested",
  "",
  "The two cards overlapping in the white. The most credible seconds in the film, because the film admits "
  "what is not yet settled.",
  "\"Great ideas aren't accepted because they sound convincing. They're accepted because scientists keep "
  "testing them.\"\nManan's own line, kept word for word from his first draft."),
])

S[8] = ("THE INVITATION", "1:54 – 2:00", [
 ("S8_P1", "Alone, breathing",
  "SETUP C. White void, flat even light from both sides, no modelling and no shadow on the backdrop. This "
  "is the brightest and the calmest setup of the day. Roll a full unbroken minute and use the stillest "
  "twenty frames.",
  "White all round him. Nothing drawn in this frame at all except the world he is standing in.",
  "Arms at his sides, eyes closed, simply breathing. No performance of any kind. This is the hardest thing "
  "on the call sheet and the reason it is shot last, when he has stopped trying."),
 ("S8_P2", "The finish line",
  "",
  "The runner crossing, seen down the road from scene one. The film returns to where it started and the "
  "question has been answered.",
  "Nothing."),
 ("S8_P3", "His own hand on the lever",
  "SETUP C, insert. His hand alone, resting on a real ball at chest height, so the fingers and the weight "
  "are right. A few seconds, held.",
  "The lever drawn around his hand. It must be his hand and not an adult's, and the ball must sit at 95 "
  "with the short gap open above it. A real hand from the world of evidence reaching into the world of "
  "explanation is the thesis of the film and the climax of the story at the same time.",
  "Just the hand. Steady, unhurried, no grip and no drama."),
 ("S8_P4", "Coach Brain takes off the key",
  "",
  "He lifts the small gold key from his own neck. No fanfare, no ceremony. He is handing over a job.",
  "Nothing."),
 ("S8_P5", "The key handed across",
  "SETUP C. Receiving at chest height, then looking up. Give him a real key to hold so the hand knows what "
  "to do.",
  "Coach Brain's drawn hand and Manan's photographed palm in one frame. The gold of the key is the only "
  "colour anywhere in the film.",
  "He takes it.\n\"The wall is real. But somebody set it.\"\nCertain and unhurried, never triumphant. One "
  "sentence per take."),
 ("S8_P6", "Eyes open",
  "SETUP C. Wider, to lens, key in one hand and the other resting on the lever. Shoot the last line "
  "several times and let the last take be the tired one.",
  "The lever beside him, the key in his hand. Then black, and the end card.",
  "\"And what your brain believes is safe can be trained.\"\nThen his own closing line, kept from his first "
  "draft:\n\"So the next time you watch an athlete find one last burst of speed, don't just wonder how "
  "strong their muscles are. Wonder what their brain believed was still safe.\""),
])

# ------------------------------------------------------------------ page one
bg()

y = H - 92
c.setFont('DB', 30)
c.setFillColor(INK)
c.drawString(ML, y, "THE BRAIN BRAKE")
y -= 26
c.setFont('DO', 12)
c.setFillColor(SOFT)
c.drawString(ML, y, "Version six, boarded. What each department makes, frame by frame.")
y -= 40

c.setStrokeColor(RULE)
c.setLineWidth(0.8)
c.line(ML, y, W - MR, y)
y -= 26

y = para(ML, y, "Eight scenes, forty eight frames, two minutes. Every frame in the film is on the "
                "following pages with three things beside it: what the camera has to shoot, what the "
                "animator has to draw, and what Manan has to do and say.", 'D', 10, 14, W - ML - MR)
y -= 10
y = para(ML, y, "The film separates evidence from explanation and never mentions it. Manan and his hands "
                "are photographed, because they are what is true. Everything else is drawn, because it is "
                "what is thought. Nobody in the audience is told this and everybody absorbs it in the "
                "first twenty seconds.", 'D', 10, 14, W - ML - MR)
y -= 26

c.setFont('MB', 9)
c.setFillColor(ACC)
c.drawString(ML, y, "THE SPLIT")
y -= 18

rows = [
    ("48", "frames boarded in total"),
    ("12", "frames need Manan in front of a camera"),
    ("36", "frames are drawn and need nobody on the day"),
    ("1", "shooting day, in Pondicherry, with Venkatesh"),
    ("4", "lighting setups, and two of them share one lighting state"),
    ("6", "lines he speaks to camera, the rest is voice over"),
]
for a, b in rows:
    c.setFont('MB', 13)
    c.setFillColor(INK)
    c.drawRightString(ML + 30, y, a)
    c.setFont('D', 9.5)
    c.setFillColor(SOFT)
    c.drawString(ML + 42, y + 1, b)
    y -= 20

y -= 12
y = para(ML, y, "So three quarters of the film is made in Zagreb and never needs him. The day itself is "
                "short, and almost all of it is one boy against a plain grey wall doing very little.",
         'D', 10, 14, W - ML - MR)

newpage()

# ------------------------------------------------------------------ page two
y = H - 80
c.setFont('DB', 20)
c.setFillColor(INK)
c.drawString(ML, y, "The shooting day")
y -= 30

y = para(ML, y, "Manan is filmed against a plain grey background and placed into the drawn world "
                "afterwards, so the shoot itself is simple. Lines are shot one sentence at a time and "
                "nothing is ever rushed.", 'D', 9.5, 13.4, W - ML - MR)
y -= 18

setups = [
 ("A", "Grey backdrop, mid shot, walking and reacting",
  "Camera at eye level on sticks, locked off. Soft key from camera left at forty five degrees, large "
  "source. Fill from the right at half strength. Slightly warm, because every scene in this setup ends "
  "with warm light arriving. Frames 1.5, 1.6, 3.2, 3.3, 3.4, 3.6."),
 ("B", "Seated eyeline, reacting to Coach Brain",
  "The same lighting as A, unchanged. A tennis ball on a stand at seated height, camera left, for the "
  "eyeline. Do not relight between A and B, only move the mark. Frames 4.2, 4.6."),
 ("C", "White void, still, to lens",
  "Flat even light from both sides, no modelling, no shadow on the backdrop. The brightest setup of the "
  "day and the calmest. Frames 8.1, 8.3, 8.5, 8.6."),
 ("D", "Jump, high frame rate",
  "Same as C, wider, room above his head. Not boarded, five minutes, worth having. Shoot it last when he "
  "is loose."),
]
for k, t, d in setups:
    c.setFont('MB', 11)
    c.setFillColor(ACC)
    c.drawString(ML, y, k)
    c.setFont('DB', 9.5)
    c.setFillColor(INK)
    c.drawString(ML + 18, y, t)
    y -= 13
    y = para(ML + 18, y, d, 'D', 8.4, 11, W - ML - MR - 18, SOFT)
    y -= 12

y -= 4
c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 22

c.setFont('MB', 9)
c.setFillColor(ACC)
c.drawString(ML, y, "THE ONE THING THE WHOLE LOOK DEPENDS ON")
y -= 16
y = para(ML, y, "In setups A and B, Manan is lit by a single dominant key from a consistent side, hard "
                "enough that his shadow has a shape. That shadow is drawn onto the paper afterwards, and "
                "it is what makes him stand inside the drawing instead of sitting on top of it. If the "
                "light on the day is flat, every frame in the film loses this and it cannot honestly be "
                "added back later.", 'D', 9, 12.6, W - ML - MR)
y -= 22

c.setFont('MB', 9)
c.setFillColor(ACC)
c.drawString(ML, y, "FOR MANAN, BEFORE THE DAY")
y -= 16
y = para(ML, y, "Six lines to camera, none longer than two sentences, and the voice over on top of them. He should know them well enough to "
                "forget them, because every one of them is written to sound like somebody working "
                "something out rather than somebody explaining it. The best takes on this film will be "
                "the ones where he is thinking, not the ones where he is right.", 'D', 9, 12.6, W - ML - MR)
y -= 14
y = para(ML, y, "Two moments carry more than the rest. Frame 3.6, where he turns to us in the hall of "
                "tanks, and frame 8.1, where he stands still with his eyes closed and does nothing at "
                "all. The first is the one the judges read him on. The second is the hardest thing on "
                "the call sheet.", 'D', 9, 12.6, W - ML - MR)

newpage()

# ------------------------------------------------------------------ frames
IMGW = 252.0
IMGH = IMGW * 568.0 / 740.0
TXTX = ML + IMGW + 18
TXTW = W - MR - TXTX
BOT = 50.0
FS, LEAD = 8.0, 10.4


def block_height(ftitle, cam, ani, man):
    h = len(wrap(ftitle, 'DB', 10.5, TXTW)) * 13.2 + 6
    for body in [cam if cam else "Nothing on the day. This frame is drawn.", ani, man]:
        h += 9.8 + len(wrap(body, 'D', FS, TXTW)) * LEAD + 7
    return max(h, IMGH + 16) + 11


def scene_header(sc, title, timing):
    y = H - 74
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML, y + 22, "SCENE %d OF 8   ·   %s" % (sc, timing))
    c.setFont('DB', 21)
    c.setFillColor(INK)
    c.drawString(ML, y, title)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(ML, y - 14, W - MR, y - 14)
    return y - 38


for sc in range(1, 9):
    title, timing, frames = S[sc]
    top = scene_header(sc, title, timing)

    for i, (pf, ftitle, cam, ani, man) in enumerate(frames):
        need = block_height(ftitle, cam, ani, man)
        if top - need < BOT:
            newpage()
            top = H - 74

        ytop = top
        img = ImageReader('/home/claude/panels/%s.jpg' % pf)
        c.drawImage(img, ML, ytop - IMGH, IMGW, IMGH, mask=None)

        c.setFont('MB', 8.5)
        c.setFillColor(LIVE if cam else SOFT)
        c.drawString(ML, ytop - IMGH - 13, "%d.%d" % (sc, i + 1))
        c.setFont('D', 7.8)
        c.setFillColor(SOFT)
        c.drawString(ML + 26, ytop - IMGH - 13,
                     "LIVE ACTION + DRAWN" if cam else "DRAWN, nobody needed on the day")

        ty = ytop
        c.setFont('DB', 10.5)
        c.setFillColor(INK)
        for ln in wrap(ftitle, 'DB', 10.5, TXTW):
            c.drawString(TXTX, ty, ln)
            ty -= 13.2
        ty -= 6

        blocks = [("CAMERA · VENKATESH", cam if cam else
                   "Nothing on the day. This frame is drawn.", LIVE if cam else SOFT),
                  ("ANIMATION · KRISTIJAN", ani, ACC),
                  ("MANAN", man, ACC)]
        for label, body, col in blocks:
            c.setFont('MB', 6.8)
            c.setFillColor(col)
            c.drawString(TXTX, ty, label)
            ty -= 9.8
            ty = para(TXTX, ty, body, 'D', FS, LEAD, TXTW)
            ty -= 7

        top = ytop - need

    newpage()

# ------------------------------------------------------------------ last page
y = H - 90
c.setFont('DB', 20)
c.setFillColor(INK)
c.drawString(ML, y, "Two things still open")
y -= 30

y = para(ML, y, "Scene five has no frame with Manan in it. In the earlier breakdown he turned to camera "
                "at the end of that scene and said that changing what the brain believes opens the door. "
                "It is the most cheerful line in the film. Either it becomes voice over, or one frame of "
                "scene five turns to him. Worth a decision before the shoot rather than after, because it "
                "costs nothing on the day and cannot be added later.", 'D', 9.5, 13.4, W - ML - MR)
y -= 16
y = para(ML, y, "Coach Brain has four spoken lines. He can be voiced by Manan pitched differently, or by "
                "somebody else entirely. Whoever it is, he is never sly and never a villain. He is a "
                "teacher who is pleased to have been found.", 'D', 9.5, 13.4, W - ML - MR)
y -= 34

c.setStrokeColor(RULE)
c.line(ML, y, W - MR, y)
y -= 30

c.setFont('DO', 13)
c.setFillColor(SOFT)
for ln in wrap("The wall is real. But somebody set it.", 'DO', 13, W - ML - MR):
    c.drawString(ML, y, ln)
    y -= 18

footer()
c.showPage()
c.save()
print("written", OUT, os.path.getsize(OUT))
