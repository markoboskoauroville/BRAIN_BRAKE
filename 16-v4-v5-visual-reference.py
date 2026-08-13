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
CW = W - ML - MR
PAPER = HexColor("#f2ebda")
INK = HexColor("#2b2822")
SOFT = HexColor("#6f6757")
ACC = HexColor("#8a6b2e")
RULE = HexColor("#c9bfa4")
A = "/home/claude/BRAIN_BRAKE/assets"

V4 = [
 ("V4/V4_1A_web.jpg", "Trkač na kraju snage. Broj 27."),
 ("V4/V4_1B_web.jpg", "Njegovo lice. Ništa mu nije ostalo."),
 ("V4/V4_1C_web.jpg", "I onda, bez najave, eksplozija u sprint."),
 ("V4/V4_2A_web.jpg", "Ciklus koraka. Isti čovjek koji posustaje i isti koji leti."),
 ("V4/V4_2B_web.jpg", "Znoj s brade. Kadar traje i ništa se ne objašnjava."),
 ("V4/V4_2C_web.jpg", "Manan se pojavljuje unutar kapi znoja. Detektiv."),
 ("V4/V4_3A_web.jpg", "Trkač sam u praznini."),
 ("V4/V4_3B_web.jpg", "Manan ga promatra kroz povećalo."),
 ("V4/V4_3C_web.jpg", "Povećalo na listu, a unutra radna soba iz 1923."),
 ("V4/V4_4A_web.jpg", "Radna soba. Hill za stolom."),
 ("V4/V4_4B_web.jpg", "Uljanica, papiri, anatomske ploče."),
 ("V4/V4_4C_web.jpg", "Ista soba, toplije svjetlo. Kraj sekvence."),
]

V5 = [
 ("V5/V5_1_1.jpg", "Manan za svojim stolom, u svojoj sobi, govori u kameru."),
 ("V5/V5_1_2.jpg", "Na laptopu prava snimka maratona."),
 ("V5/V5_1_3.jpg", "Trkač ubrzava. Manan to gleda s nama."),
 ("V5/V5_1_4.jpg", "Reagira na ono što je vidio."),
 ("V5/V5_1_5.jpg", "Objašnjava. Rukama, svojim riječima."),
 ("V5/V5_1_6.jpg", "Poseže za starom knjigom na stolu."),
 ("V5/V5_2_1.jpg", "Knjiga otvorena pod njegovim rukama."),
 ("V5/V5_2_2.jpg", "Iz knjige se diže pop up soba. Crtež ulazi u njegov stvarni svijet."),
 ("V5/V5_2_3.jpg", "Pop up radna soba, bliže. Najbolji predmet koji je ijedna verzija našla."),
 ("V5/V5_2_4.jpg", "Unutar crteža. Hill piše."),
 ("V5/V5_2_5.jpg", "Manan gleda u knjigu. Dvije razine u istom kadru."),
 ("V5/V5_2_6.jpg", "Krupni plan. On je taj koji objašnjava."),
 ("V5/V5_3_1.jpg", "Krivulja na papiru."),
]

DOCS = [
 ("10 - v4 nijemi film - vizualna referenca.pdf", "VERZIJA ČETIRI", "Nijemi film",
  "Devet scena, dvije minute, nijedne riječi. Grafit na kremastom papiru. Jedan fotografiran dječak u "
  "nacrtanom svijetu.\n"
  "Ovo je vizualno najjača stvar napravljena na ovoj produkciji i mislim da to i dalje stoji.\n"
  "I ovo je točno mjesto gdje sam se zanio. Manan je u ovoj verziji na ekranu otprilike osam sekundi od "
  "sto dvadeset. Ne govori. Pojavljuje se u kadrovima. Radio sam svoj film, ne njegov, i on je od "
  "protagonista postao gost u mojoj vizualnoj priči.\n"
  "Dvanaest gotovih kadrova, od dvadeset sedam koliko ih postoji.", V4),

 ("11 - v5 pop up knjiga - vizualna referenca.pdf", "VERZIJA PET", "Pop up knjiga, Yoda verzija",
  "Šest scena. Manan je na kameri u svakoj, u svojoj sobi, u svojoj majici, i govori svojim riječima.\n"
  "Struktura je otvoreno Star Wars. Coach Brain je Yoda: malen, komičan, naizgled beznačajan, i potpuno u "
  "pravu. Manan je učenik. Učenik kojeg se na kameri podučava je učenik koji na kameri pokazuje da "
  "razumije, pa oblik priče i kriteriji natjecanja traže istu stvar.\n"
  "Iz knjige na njegovom stolu diže se pop up svijet i crtež ulazi u njegovu stvarnu sobu. To je najbolji "
  "predmet koji je ijedna verzija našla.\n"
  "Trinaest kadrova.", V5),
]


def build(fn, kicker, title, intro, frames):
    out = "/home/claude/out/" + fn
    c = canvas.Canvas(out, pagesize=A4)
    page = [0]

    def bg():
        c.setFillColor(PAPER)
        c.rect(0, 0, W, H, fill=1, stroke=0)

    def foot():
        page[0] += 1
        c.setFont('M', 7)
        c.setFillColor(SOFT)
        c.drawString(ML, 30, "THE BRAIN BRAKE  ·  " + title.lower())
        c.drawRightString(W - MR, 30, str(page[0]))

    def newpage():
        foot()
        c.showPage()
        bg()

    def wrap(t, f, s, mw):
        o = []
        for p in t.split("\n"):
            w = p.split()
            if not w:
                o.append("")
                continue
            l = w[0]
            for x in w[1:]:
                if pdfmetrics.stringWidth(l + " " + x, f, s) <= mw:
                    l += " " + x
                else:
                    o.append(l)
                    l = x
            o.append(l)
        return o

    bg()
    y = H - 100
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML, y + 26, kicker)
    c.setFont('DB', 28)
    c.setFillColor(INK)
    c.drawString(ML, y, title)
    y -= 30
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(ML, y, W - MR, y)
    y -= 26
    c.setFont('D', 9.6)
    c.setFillColor(INK)
    for ln in wrap(intro, 'D', 9.6, CW):
        c.drawString(ML, y, ln)
        y -= 13.4
    newpage()

    for i, (img, cap) in enumerate(frames):
        p = os.path.join(A, img)
        im = Image.open(p)
        ar = im.size[0] / im.size[1]
        iw = CW
        ih = iw / ar
        if ih > 560:
            ih = 560
            iw = ih * ar
        top = H - 90
        c.drawImage(ImageReader(p), ML + (CW - iw) / 2, top - ih, iw, ih, mask=None)
        yy = top - ih - 20
        c.setFont('MB', 8)
        c.setFillColor(ACC)
        c.drawString(ML, yy, "%d / %d" % (i + 1, len(frames)))
        c.setFont('D', 10)
        c.setFillColor(INK)
        for ln in wrap(cap, 'D', 10, CW - 46):
            c.drawString(ML + 46, yy, ln)
            yy -= 13
        newpage()

    c.save()
    print("written", out, os.path.getsize(out))


os.makedirs("/home/claude/out", exist_ok=True)
for fn, k, t, intro, fr in DOCS:
    build(fn, k, t, intro, fr)
