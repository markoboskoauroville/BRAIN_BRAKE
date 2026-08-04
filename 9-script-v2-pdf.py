from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('D', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DB', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DO', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'))
pdfmetrics.registerFont(TTFont('M', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('MB', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'))

W, H = A4
ML, MR, MT, MB = 62, 62, 60, 58
PAPER = HexColor("#f2ebda")
INK = HexColor("#2b2822")
SOFT = HexColor("#6a6253")
ACC = HexColor("#8a6b2e")
RULE = HexColor("#c3b89c")

c = canvas.Canvas("assets/pdf/2-THE-BRAIN-BRAKE-script-v2-Manan-and-Marko.pdf", pagesize=A4)
state = {"y": 0, "page": 0}


def bg():
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def footer():
    c.setFont('M', 7.5)
    c.setFillColor(SOFT)
    c.drawString(ML, 32, "THE BRAIN BRAKE  ·  script v2  ·  Manan Periwal & Marko Boško")
    c.drawRightString(W - MR, 32, str(state["page"]))


def newpage():
    if state["page"]:
        footer()
        c.showPage()
    state["page"] += 1
    bg()
    state["y"] = H - MT


def need(h):
    if state["y"] - h < MB:
        newpage()


def wrap(text, font, size, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(text, font='D', size=10.5, lead=15.5, color=INK, indent=0, gap=9, width=None):
    wdt = width or (W - ML - MR - indent)
    lines = wrap(text, font, size, wdt)
    need(len(lines) * lead + gap)
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in lines:
        if state["y"] - lead < MB:
            newpage()
            c.setFont(font, size)
            c.setFillColor(color)
        c.drawString(ML + indent, state["y"], ln)
        state["y"] -= lead
    state["y"] -= gap


def rule(gap_before=6, gap_after=12):
    need(gap_before + gap_after + 2)
    state["y"] -= gap_before
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(ML, state["y"], W - MR, state["y"])
    state["y"] -= gap_after


def h1(t):
    need(44)
    c.setFont('DB', 21)
    c.setFillColor(INK)
    c.drawString(ML, state["y"], t)
    state["y"] -= 30


def scene_head(num, title, tc):
    need(56)
    state["y"] -= 10
    c.setStrokeColor(INK)
    c.setLineWidth(1.4)
    c.line(ML, state["y"] + 20, W - MR, state["y"] + 20)
    c.setFont('DB', 15)
    c.setFillColor(INK)
    c.drawString(ML, state["y"], f"SCENE {num}   {title}")
    c.setFont('MB', 10)
    c.setFillColor(ACC)
    c.drawRightString(W - MR, state["y"], tc)
    state["y"] -= 24


def slug(t):
    need(20)
    c.setFont('MB', 9)
    c.setFillColor(SOFT)
    c.drawString(ML, state["y"], t.upper())
    state["y"] -= 17


def line(who, txt):
    need(34)
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML + 40, state["y"], who.upper())
    state["y"] -= 14
    for ln in wrap(txt, 'M', 10, W - ML - MR - 110):
        if state["y"] - 14 < MB:
            newpage()
        c.setFont('M', 10)
        c.setFillColor(INK)
        c.drawString(ML + 60, state["y"], ln)
        state["y"] -= 14
    state["y"] -= 6


# ============================ COVER ============================
newpage()
state["y"] = H - 150
c.setFont('DB', 34)
c.setFillColor(INK)
c.drawString(ML, state["y"], "THE BRAIN BRAKE")
state["y"] -= 22
c.setFont('DO', 12)
c.setFillColor(SOFT)
c.drawString(ML, state["y"], "The limit is a setting, not a wall.")
state["y"] -= 50
c.setStrokeColor(INK)
c.setLineWidth(1.6)
c.line(ML, state["y"], W - MR, state["y"])
state["y"] -= 26
c.setFont('M', 9.5)
c.setFillColor(SOFT)
for k, v in [("Running time", "2:00"),
             ("Format", "16:9, live action composited into hand drawn animation"),
             ("Entry", "Breakthrough Junior Challenge 2026"),
             ("Draft", "Version 2")]:
    c.drawString(ML, state["y"], f"{k}")
    c.setFillColor(INK)
    c.drawString(ML + 130, state["y"], v)
    c.setFillColor(SOFT)
    state["y"] -= 17
state["y"] -= 26
c.setFont('MB', 9)
c.setFillColor(ACC)
c.drawString(ML, state["y"], "WRITTEN BY")
state["y"] -= 18
c.setFont('DB', 13)
c.setFillColor(INK)
c.drawString(ML, state["y"], "Manan Periwal")
state["y"] -= 17
c.setFont('D', 10)
c.setFillColor(SOFT)
c.drawString(ML, state["y"], "Concept, science and story")
state["y"] -= 26
c.setFont('DB', 13)
c.setFillColor(INK)
c.drawString(ML, state["y"], "Marko Boško")
state["y"] -= 17
c.setFont('D', 10)
c.setFillColor(SOFT)
c.drawString(ML, state["y"], "Story mentor and direction")
state["y"] -= 44

para("This draft is a collaboration. The concept, the science and the choice of subject are Manan's, taken from his "
     "first draft. The change in this version is the shape of the story rather than its substance.",
     'D', 10.5, 15.5, INK)
para("Draft one explained a mechanism: the brain applies a brake to protect the body. Accurate, and it ended in a "
     "closed case. This draft asks a different question. If the brake exists, where is the limit really, and can it "
     "move? The research says it can, and that turns an explanation into a discovery.",
     'D', 10.5, 15.5, INK)
para("The film now rises rather than settles. Curiosity, then astonishment, then release. It ends with a boy "
     "breathing calmly, understanding that what stopped him was a decision, and that decisions can be trained.",
     'D', 10.5, 15.5, INK)

# ============================ SPINE ============================
newpage()
h1("The spine")
para("A runner with nothing left produces an impossible sprint. A boy goes looking for where it came from. He "
     "expects to find an empty tank. He finds a full one, and a door that somebody closed on purpose.",
     'DO', 11, 16, INK)
rule()
para("The three findings the film is built on. Each one is real, published, and stranger than the explanation it "
     "replaces.", 'DB', 10.5, 15.5, INK)
para("One. Athletes taken to genuine exhaustion were tested immediately afterwards and could still produce far more "
     "power than they had just produced. The muscle was not the thing that stopped them.", 'D', 10.5, 15.5, INK, 16)
para("Two. Cyclists raced a ghost of their own best ride. The ghost was secretly set two percent faster. They beat "
     "it. A reserve is held back, and it is released by the belief that the effort is sustainable.",
     'D', 10.5, 15.5, INK, 16)
para("Three. Mindfulness training increased how long athletes could keep going, with no measurable change in the "
     "body. What changed was how hard it felt.", 'D', 10.5, 15.5, INK, 16)
rule()
para("So the sentence at the centre of the film is this. The wall is real. But somebody set it, and settings can "
     "move.", 'DB', 11.5, 16.5, INK)
para("Underneath, unnamed and never argued, sits an older idea: that attention and breath are the instruments by "
     "which a person meets their own limits. The film does not say this. It shows a boy going still, and then "
     "flying. The audience can take from that whatever they already carry.", 'DO', 10.5, 15.5, SOFT)

# ============================ SCENES ============================
newpage()
h1("The film")

scene_head(1, "THE MYSTERY", "0:00 – 0:18")
slug("EXT. Marathon course, day. Animation.")
para("A lean runner is failing on an open road. Head rolling, arms hanging, stride collapsed to a shuffle. He is "
     "beaten and everyone watching knows it.", 'D', 10.5, 15.5, INK)
line("COMMENTATOR (V.O.)", "He's got nothing left.")
para("He explodes into a sprint. The world freezes around him, speed lines suspended in the air. MANAN walks into "
     "the frozen frame, magnifying glass raised. Through the lens: a footprint, a stopwatch. He lowers the glass and "
     "turns to camera.", 'D', 10.5, 15.5, INK)
line("MANAN", "Hold on. He had nothing left. So where did THAT come from?")
para("Question marks bloom around him. TITLE: THE BRAIN BRAKE.", 'D', 10.5, 15.5, INK)

scene_head(2, "THE FULL TANK", "0:18 – 0:40")
slug("INT. The muscle factory. Animation with Manan composited.")
para("Inside the leg, a working factory. Gears turning where the calf would be, conveyors, tiny workers hauling "
     "crates. Manan walks through it, unhurried, the only calm figure in the room.", 'D', 10.5, 15.5, INK)
line("MANAN (V.O.)", "For a hundred years we blamed the muscles. Ran out of fuel. Ran out of air. Simple.")
para("The machines slow. A worker wipes his brow and shrugs: that's it, we're done. But Manan has stopped. At the "
     "back of the factory there is a door, and it is shut.", 'D', 10.5, 15.5, INK)
line("MANAN (V.O.)", "Except when scientists tested runners the moment they gave up, the muscles could still do far more.")
para("He pushes the door. It opens onto an enormous hall of storage tanks, and every one of them is full. Light "
     "floods his face.", 'D', 10.5, 15.5, INK)
line("MANAN", "It was never empty.")

scene_head(3, "THE GATEKEEPER", "0:40 – 1:05")
slug("INT. Mission control. Animation with Manan composited.")
para("A warm, glowing room of monitors. A chair turns. COACH BRAIN, tracksuit, whistle, coffee, and a small brass "
     "key on a chain around his neck. He is delighted to be found.", 'D', 10.5, 15.5, INK)
line("MANAN", "You closed that door.")
line("COACH BRAIN", "I keep the key.")
para("He gestures and the room lights up. Glowing lines run out to a heart, lungs, a thermometer, a water drop, a "
     "distance counter, all feeding back to a single dial marked from EASY to DANGER.", 'D', 10.5, 15.5, INK)
line("COACH BRAIN", "Every heartbeat. Every breath. Every drop of sweat. I'm asking one question. Can we keep going safely?")
line("MANAN", "So the limit isn't my body. It's your guess.")
para("Coach Brain grins, entirely unembarrassed.", 'D', 10.5, 15.5, INK)
line("COACH BRAIN", "It's my best guess. And I'd rather you finish than break.")
para("SUBTITLE, two seconds: One influential model, the Central Governor Theory, proposed by Prof. Tim Noakes, 1997. "
     "Scientists still debate exactly how brain and muscle share the work.", 'DO', 9.5, 14, SOFT, 16)

scene_head(4, "THE TRICK", "1:05 – 1:25")
slug("INT. Sports laboratory. Animation.")
para("A cyclist on a stationary bike, screen in front of him showing a translucent ghost rider. He has been told the "
     "ghost is a recording of his own best ever ride.", 'D', 10.5, 15.5, INK)
line("MANAN (V.O.)", "So scientists tried something cheeky. They let a cyclist race himself.")
para("Behind glass, a researcher quietly turns a small dial. On her screen: +2%.", 'D', 10.5, 15.5, INK)
line("MANAN (V.O.)", "Except they made the ghost slightly faster. And they didn't tell him.")
para("The cyclist chases. Strains. Draws level. Passes. The ghost falls behind.", 'D', 10.5, 15.5, INK)
line("MANAN (V.O.)", "He beat his own maximum. Which means it was never his maximum.")
para("Manan turns to camera, delighted.", 'D', 10.5, 15.5, INK)
line("MANAN", "Change what the brain believes, and the door opens.")

scene_head(5, "THE RELEASE", "1:25 – 1:50")
slug("EXT. Everywhere. Animation. The peak of the film.")
para("Coach Brain looks at his dial, then at Manan. He smiles, and eases it open.", 'D', 10.5, 15.5, INK)
para("Inside the runner's legs, muscle fibres light one after another, more and more of them. His stride opens. He "
     "flies. Speed lines. The crowd erupts.", 'D', 10.5, 15.5, INK)
para("And the film breaks loose. A traceur launching rooftop to rooftop. A dancer turning in the air. A swimmer "
     "leaving the wall. Bodies doing what they could always do, permitted at last. All of it rising.",
     'D', 10.5, 15.5, INK)
line("MANAN (V.O.)", "The brain didn't make new energy. It gave permission.")
para("Manan himself, mid air, coat flying, laughing.", 'D', 10.5, 15.5, INK)
para("CAPTION: More muscle fibres recruited. Notice: still not maximum.", 'DO', 9.5, 14, SOFT, 16)

scene_head(6, "THE INVITATION", "1:50 – 2:00")
slug("Everything settles to white. Manan alone. Live action.")
para("The motion drains away. Manan stands still, eyes closed, breathing. Calm. The dial hangs in the air beside "
     "him, and this time his own hand is on it.", 'D', 10.5, 15.5, INK)
line("MANAN", "The wall is real. But somebody set it.")
line("MANAN", "And what your brain believes is safe can be trained.")
para("Coach Brain steps up, takes the key from around his neck, and hands it over. A small, warm moment. Manan opens "
     "his eyes.", 'D', 10.5, 15.5, INK)
para("Cut to black.", 'D', 10.5, 15.5, INK)
para("END CARD: THE LIMIT IS A SETTING, NOT A WALL.", 'DB', 11, 16, INK)

# ============================ NOTES ============================
newpage()
h1("Notes on the change")
para("What was kept", 'DB', 12, 17, INK)
para("The subject, the science, the detective device, the factory, Coach Brain and the closing honesty about an "
     "unresolved debate. All of it Manan's, all of it working.", 'D', 10.5, 15.5, INK)
para("What was changed, and why", 'DB', 12, 17, INK)
para("Draft one ended on a closed case, a cracked board and a shrug. The mechanism was explained but the audience "
     "was left flat. The evidence itself offers a better ending: the reserve is real, it can be reached, and "
     "reaching it is one of the most alive experiences a person can have.", 'D', 10.5, 15.5, INK)
para("So the emotional line now climbs. Curiosity, astonishment, release, calm. Same facts, opposite feeling.",
     'D', 10.5, 15.5, INK)
para("What is deliberately not said", 'DB', 12, 17, INK)
para("The film makes no claim beyond the published findings. It does not promise that training the mind removes "
     "physical limits, and it does not stray into anything unfalsifiable. It simply shows a boy going still before "
     "he moves, and lets the audience notice.", 'D', 10.5, 15.5, INK)
para("Scientific accuracy is scored in this competition. Every claim in this draft traces to a study, and the one "
     "contested model is labelled as contested, on screen, in the film.", 'D', 10.5, 15.5, INK)

footer()
c.save()
print("written")
