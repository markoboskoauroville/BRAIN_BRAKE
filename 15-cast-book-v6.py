# THE BRAIN BRAKE, version six
# The character and model sheet book for Kristijan. Croatian and English from one source.

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
WARN = HexColor("#8a3b2e")
R = "/home/claude/BRAIN_BRAKE/assets"

# ---------------------------------------------------------------- sheets
# (image, section, title HR, title EN, body HR, body EN)
SHEETS = [
 ("REFERENCES/MANAN.jpg", "LIKOVI|THE CAST",
  "MANAN", "MANAN",
  "Snimljen, nikad crtan. On je jedino stvarno u filmu i na tome počiva cijeli vizualni ključ: sve što je "
  "nacrtano je unutrašnjost problema, sve što je fotografirano je osoba koja je došla to pogledati.\n"
  "U verziji šest više nema lovačke kape ni kaputa. Nosi svoju sivu majicu s kapuljačom.\n"
  "SJENA. Gdje god stoji na crtežu, papir ispod njega potamni, a linije olovke ostaju čitljive kroz sjenu. "
  "Sjena je dokaz da fotografija i crtež dijele isti prostor. Bez nje je zalijepljen na crtež, s njom stoji "
  "u njemu. To nije ukras, to je mehanizam cijele ideje.",
  "Photographed, never drawn. He is the only real thing in the film and the whole visual idea rests on "
  "that: everything drawn is the inside of the problem, everything photographed is the person who came to "
  "look at it.\n"
  "In version six the deerstalker and the coat are gone. He is in his own grey hoodie.\n"
  "THE SHADOW. Wherever he stands on the drawing the paper goes dark under him, and the pencil lines stay "
  "readable through the shadow. The shadow is proof that a photograph and a drawing occupy one space. "
  "Without it he is pasted on, with it he is standing in it. This is not decoration, it is the mechanism "
  "of the whole idea."),

 ("REFERENCES/MANAN_CLOSE.jpg", "LIKOVI|THE CAST",
  "MANAN, BLIZU", "MANAN, CLOSE",
  "Za usklađivanje tena, kose i pogleda u krupnim planovima. Ima četrnaest godina. Ne stari ga.",
  "For matching skin, hair and eyeline in close ups. He is fourteen years old. Do not age him."),

 ("REFERENCES/BRAIN.jpg", "LIKOVI|THE CAST",
  "COACH BRAIN", "COACH BRAIN",
  "Četiri pogleda. Trenirka, šalica, slušalice s mikrofonom i mali zlatni ključ na lančiću na prsima. "
  "Visok dvije i pol glave.\n"
  "On je učitelj, a ne negativac, i u ovom filmu negativca nema nigdje. Nikad nije lukav i nikad ne "
  "izgleda kao da je uhvaćen. Sretan je što ga je netko konačno pronašao.\n"
  "Ključ je jedina boja u cijelom filmu. Nigdje drugdje nema zlatne.",
  "Four views. Tracksuit, mug, headset, and a small gold key on a chain at his chest. Two and a half heads "
  "tall.\n"
  "He is a teacher and not a villain, and there is no villain anywhere in this film. He is never sly and "
  "he never looks caught out. He is delighted to have finally been found.\n"
  "The key is the only colour in the entire film. There is no gold anywhere else."),

 ("REFERENCES/RUNNER.jpg", "LIKOVI|THE CAST",
  "MARATONAC", "THE MARATHON RUNNER",
  "Četiri pogleda. Mršav, oko trideset pet godina, broj 27 na dresu. Nije star: on je na kraju utrke, a ne "
  "na kraju života, i prva scena pada ako izgleda kao starac.\n"
  "Pojavljuje se u prvom kadru filma i ponovno u zadnjem. Broj 27 je vrh brojanja koje teče kroz cijeli "
  "film i nikad se ne spominje naglas.",
  "Four views. Lean, about thirty five, number 27 on the vest. He is not old: he is at the end of a race, "
  "not at the end of a life, and the first scene fails if he reads as an old man.\n"
  "He appears in the first frame of the film and again in the last. The number 27 is the top of a count "
  "that runs through the whole film and is never once remarked on."),

 ("REFERENCES/RUN_CYCLE.jpg", "LIKOVI|THE CAST",
  "CIKLUS TRČANJA", "THE RUN CYCLE",
  "Četiri položaja koraka. Isti čovjek koji posustaje i isti čovjek koji leti, pa ciklus mora izdržati "
  "oba stanja. Kadar 6.4 rimuje se s kadrom 1.1 točno: ista kompozicija, suprotan osjećaj.",
  "Four positions of the stride. The same man failing and the same man flying, so the cycle has to hold in "
  "both states. Frame 6.4 rhymes frame 1.1 exactly: same composition, opposite feeling."),

 ("REFERENCES/MUSCLE.jpg", "LIKOVI|THE CAST",
  "MIŠIĆ", "THE MUSCLE",
  "Četiri pogleda. Ponosan, tvrdoglav, dvije i pol glave, frotirna traka na čelu, jednostavne konture.\n"
  "Na kraju filma rukuje se s Coachom Brainom. Hill je bio u pravu za mišić i film to izgovara naglas. "
  "Nitko ne gubi.",
  "Four views. Proud, stubborn, two and a half heads, terry sweatband, simple contours.\n"
  "At the end of the film he shakes Coach Brain's hand. Hill was right about the muscle and the film says "
  "so out loud. Nobody loses."),

 ("REFERENCES/WORKERS.jpg", "LIKOVI|THE CAST",
  "RADNICI U TVORNICI", "THE FACTORY WORKERS",
  "Posada stare teorije. Kombinezoni, čizme, rukavice, kaciga. Rekviziti: podložak za pisanje, ključ za "
  "matice, sanduk s kisikom. Poze su već nacrtane: nošenje sanduka, povlačenje poluge, panika, brisanje "
  "znoja.\n"
  "Pomireni su, a ne prestrašeni. Ovo je kraj smjene, a ne katastrofa.",
  "The crew of the old theory. Overalls, boots, gloves, hard hat. Props: clipboard, wrench, oxygen crate. "
  "The poses are already drawn: hauling the crate, pulling the lever, panicking, wiping sweat.\n"
  "They are resigned, not frightened. This is a shift ending, not a disaster."),

 ("REFERENCES/SCIENTIST.jpg", "LIKOVI|THE CAST",
  "A. V. HILL", "A. V. HILL",
  "Turnaround i tri izraza lica: udubljen, zaglavljen, spoznaja. U verziji šest visi kao portret na zidu "
  "učionice u drugoj sceni.\n"
  "Prema njemu se odnosimo s poštovanjem. Njegova teorija je nepotpuna, a ne pogrešna, i nikad mu se ne "
  "rugamo.",
  "Turnaround and three expressions: absorbed, stuck, epiphany. In version six he hangs as a portrait on "
  "the classroom wall in scene two.\n"
  "He is treated with respect. His theory is incomplete rather than wrong, and he is never mocked."),

 ("V6/cast/CAST_ALL.jpg", "LIKOVI|THE CAST",
  "CIJELA POSTAVA, ODNOS VELIČINA", "THE CAST TOGETHER, RELATIVE SCALE",
  "Ako ovo promašiš, ništa drugo na ovim stranicama ne pomaže. Coach Brain i Mišić su otprilike dvije i "
  "pol glave. Manan je stvaran četrnaestogodišnjak i mjerilo je on.",
  "Get this wrong and nothing else on these pages helps. Coach Brain and the Muscle are each about two and "
  "a half heads. Manan is a real fourteen year old boy and he is the yardstick."),

 ("REFERENCES/LEVER.jpg", "REKVIZITI|PROPS",
  "POLUGA", "THE LEVER",
  "Šest pogleda. Kugla je hvatište i sjedi NA VRHU osovine. Skala označena sa 100 i 95.\n"
  "Staje na 95 i nikad na 100. Razmak otvorene staze iznad kugle je moralna arhitektura cijelog filma i "
  "rečenica koju nitko ne izgovara. Čuvaj ga u svakom kadru u kojem se poluga pojavljuje.\n"
  "U sceni 6 kugla kreće NISKO i putuje prema gore. Ako krene visoko, cijela scena se okreće naopako.",
  "Six views. The ball is the grip and it sits ON TOP of the shaft. Scale marked 100 and 95.\n"
  "It stops at 95 and never at 100. The gap of open track above the ball is the moral architecture of the "
  "whole film and the sentence nobody speaks. Protect it in every frame the lever appears in.\n"
  "In scene 6 the ball starts LOW and travels upward. If it starts high, the whole scene reverses."),

 ("REFERENCES/GLASS.jpg", "REKVIZITI|PROPS",
  "POVEĆALO", "THE MAGNIFYING GLASS",
  "Mjed i tamno drvo, šest kutova. Ovo je stvaran predmet koji leži na crtežu: baca sjenu na papir, a ono "
  "što se vidi kroz njega je olovka.\n"
  "Stvaran instrument koji pokazuje nacrtanu unutrašnjost je argument cijelog filma sažet u jedan predmet.",
  "Brass and dark wood, six angles. This is a real object lying on a drawing: it throws a shadow onto the "
  "paper, and what you see through it is pencil.\n"
  "A real instrument showing a drawn interior is the argument of the whole film in one object."),

 ("REFERENCES/BOOK.jpg", "REKVIZITI|PROPS",
  "KNJIGA", "THE BOOK",
  "Zeleno platno. Zatvorena, otvorena i sa strane.",
  "Green cloth. Closed, open, and from the side."),

 ("REFERENCES/BRAIN_ROOM.jpg", "LOKACIJE|LOCATIONS",
  "KONTROLNA SOBA", "THE CONTROL ROOM",
  "Coach Brainova soba. Topla, a ne klinička. Monitori po svim zidovima, jedna stolica.\n"
  "Ovdje se nekoga upoznaje, a ne hvata na djelu. Svjetlo mora biti gostoljubivo.",
  "Coach Brain's room. Warm, not clinical. Monitors on every wall, one chair.\n"
  "This is meeting somebody, not catching them. The light has to be welcoming."),

 ("REFERENCES/TANKS.jpg", "LOKACIJE|LOCATIONS",
  "DVORANA SA SPREMNICIMA", "THE HALL OF TANKS",
  "Iza vrata koja nitko nije otvorio. Devet vidljivih spremnika, svaki mjerač pun.\n"
  "Ovo je otkriće i prvo veliko podizanje u filmu. Radost, a ne upozorenje. Svjetlo dolazi kao dobra "
  "vijest.",
  "Behind the door nobody opened. Nine tanks visible, every gauge full.\n"
  "This is the reveal and the first big lift in the film. Discovery, not warning. The light arrives as "
  "good news."),

 ("REFERENCES/LAB.jpg", "LOKACIJE|LOCATIONS",
  "RADNA SOBA, 1923.", "THE 1923 STUDY",
  "Tri pogleda: cijela soba, detalj stola, anatomski kut. Uljanica, papiri, anatomske ploče.\n"
  "Na anatomskim pločama ne smije biti nikakvih slova. Alat izmišlja tekst i vrati ga kao besmislice.",
  "Three views: full room, desk detail, anatomy corner. Oil lamp, papers, anatomical plates.\n"
  "There must be no lettering at all on the anatomical plates. The tool invents text and returns it as "
  "nonsense."),

 ("REFERENCES/ROOM.jpg", "LOKACIJE|LOCATIONS",
  "DJEČAKOVA SOBA, VERZIJA PET", "THE BOY'S BEDROOM, VERSION FIVE",
  "Napravljeno za verziju pet, kad se film odvijao u njegovoj sobi. Verzija šest je ne koristi: Manan se "
  "snima na sivoj pozadini i naknadno se stavlja u nacrtani svijet.\n"
  "Ostaje ovdje da je nitko slučajno ne crta ponovno i zato što se može vratiti.",
  "Built for version five, when the film played out in his room. Version six does not use it: Manan is "
  "shot against grey and placed into the drawn world afterwards.\n"
  "It stays here so nobody redraws it by accident, and because it may come back."),
]

MISSING_HR = [
 ("KLJUČ", "Mali zlatni ključ na lančiću. Nosi ga Coach Brain, predaje se Mananu u zadnjoj sceni. "
           "Pojavljuje se u pet kadrova, jedini je obojeni predmet u filmu, a nema svoj sheet."),
 ("BROJČANIK", "Okrugli mjerač s kazaljkom. Nije isto što i poluga. Osam kadrova kroz pet scena, "
               "svaki put nacrtan drugačije, što je točno ono što se dogodi bez sheeta."),
 ("VRATA", "Zakovana vrata na kraju tvornice, zatvorena i otvorena, sa svjetlom iza."),
 ("TVORNICA", "Unutrašnjost mišića kao pogon. Zupčanici, trake, sanduci, dizalica. Nosi cijelu drugu "
              "scenu i dio treće."),
]
MISSING_EN = [
 ("THE KEY", "Small gold key on a chain. Worn by Coach Brain, handed to Manan in the last scene. It "
             "appears in five frames, it is the only coloured object in the film, and it has no sheet."),
 ("THE DIAL", "The round gauge with a needle. Not the same object as the lever. Eight frames across five "
              "scenes, drawn differently every time, which is exactly what happens without a sheet."),
 ("THE DOOR", "The riveted door at the back of the factory, closed and open, with light behind it."),
 ("THE FACTORY", "The inside of the muscle as a working plant. Gears, belts, crates, gantry. It carries "
                 "the whole of scene two and part of scene three."),
]

TXT = {
 'hr': dict(
   sub="Verzija šest. Knjiga likova, rekvizita i lokacija.",
   lead="Sve što je do sada nacrtano i zaključano, na jednom mjestu. Ovo je biblija ovog filma. Crtež "
        "koji odstupa od ovih listova je off model, i to je jedina presuda koja se ovdje koristi.",
   lead2="Svaki predmet koji se ponavlja dobiva svoj model sheet s više kutova, jednako kao i lik. Bez "
         "njega alat ga prvi ispusti iz punog kadra, jer nema identitet za koji bi se uhvatio. Jedan "
         "sheet košta jedan kredit i spasi ih pet.",
   law="ZAKON KOJI STOJI IZNAD SVIH LISTOVA",
   lawtext="Sve što je nacrtano je unutrašnjost problema. Sve što je fotografirano je osoba koja je došla "
           "to pogledati. Film je trenutak u kojem ta dva svijeta prestanu biti odvojena.\n"
           "Nitko to ne izgovara i ništa u filmu to ne objašnjava. Sve nosi jedino to jesu li fotografija "
           "i crtež obasjani istim svjetlom.",
   missing="LISTOVI KOJI JOŠ NE POSTOJE",
   missinglead="Poredani po tome koliko štete radi njihov nedostatak.",
   close="Sheetovi su 3:2. Kadrovi su 16:9. Sheet se uvijek prepisuje preko vlastitog imena datoteke, "
         "zauvijek, da svaki već napisani prompt ostane važeći."),
 'en': dict(
   sub="Version six. The book of characters, props and locations.",
   lead="Everything drawn and locked so far, in one place. This is the bible for this film. A drawing that "
        "departs from these sheets is off model, and that is the only verdict used here.",
   lead2="Every recurring object gets its own model sheet with several angles, exactly like a character. "
         "Without one it is the first thing the tool drops from a busy frame, because it has no identity "
         "to hold on to. One sheet costs one credit and saves five.",
   law="THE LAW THAT SITS ABOVE EVERY SHEET",
   lawtext="Everything drawn is the inside of the problem. Everything photographed is the person who came "
           "to look at it. The film is the moment those two stop being separate.\n"
           "Nobody says this and nothing in the film explains it. It is carried entirely by whether the "
           "photograph and the drawing are lit by the same light.",
   missing="SHEETS THAT DO NOT EXIST YET",
   missinglead="Ordered by how much damage their absence does.",
   close="Sheets are 3:2. Frames are 16:9. A sheet is always overwritten at its own filename, forever, so "
         "that every prompt already written stays valid."),
}


def build(lang, out):
    c = canvas.Canvas(out, pagesize=A4)
    page = [0]
    t = TXT[lang]

    def bg():
        c.setFillColor(PAPER)
        c.rect(0, 0, W, H, fill=1, stroke=0)

    def foot():
        page[0] += 1
        c.setFont('M', 7)
        c.setFillColor(SOFT)
        c.drawString(ML, 30, "THE BRAIN BRAKE  ·  version six  ·  " +
                     ("knjiga likova za Kristijana" if lang == 'hr' else "character sheets for Kristijan"))
        c.drawRightString(W - MR, 30, str(page[0]))

    def newpage():
        foot()
        c.showPage()
        bg()

    def wrap(text, font, size, maxw):
        out = []
        for p in text.split("\n"):
            words = p.split()
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

    def para(x, y, text, font='D', size=9.4, lead=13, maxw=CW, color=INK):
        c.setFont(font, size)
        c.setFillColor(color)
        for ln in wrap(text, font, size, maxw):
            c.drawString(x, y, ln)
            y -= lead
        return y

    bg()
    # cover
    y = H - 100
    c.setFont('DB', 30)
    c.setFillColor(INK)
    c.drawString(ML, y, "THE BRAIN BRAKE")
    y -= 26
    c.setFont('DO', 12)
    c.setFillColor(SOFT)
    c.drawString(ML, y, t['sub'])
    y -= 40
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(ML, y, W - MR, y)
    y -= 26
    y = para(ML, y, t['lead'])
    y -= 12
    y = para(ML, y, t['lead2'])
    y -= 26
    c.setFont('MB', 9)
    c.setFillColor(ACC)
    c.drawString(ML, y, t['law'])
    y -= 18
    y = para(ML, y, t['lawtext'], 'D', 9.4, 13, CW, SOFT)
    y -= 30

    counts = {}
    for s in SHEETS:
        k = s[1].split("|")[0 if lang == 'hr' else 1]
        counts[k] = counts.get(k, 0) + 1
    for k, v in counts.items():
        c.setFont('MB', 13)
        c.setFillColor(INK)
        c.drawRightString(ML + 26, y, str(v))
        c.setFont('D', 9.5)
        c.setFillColor(SOFT)
        c.drawString(ML + 38, y + 1, k.lower())
        y -= 20
    newpage()

    # sheet pages
    last = None
    for img, sec, thr, ten, bhr, ben in SHEETS:
        section = sec.split("|")[0 if lang == 'hr' else 1]
        title = thr if lang == 'hr' else ten
        body = bhr if lang == 'hr' else ben

        y = H - 74
        c.setFont('MB', 9)
        c.setFillColor(ACC)
        c.drawString(ML, y + 20, section)
        c.setFont('DB', 20)
        c.setFillColor(INK)
        c.drawString(ML, y, title)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(ML, y - 13, W - MR, y - 13)
        y -= 34

        im = Image.open(os.path.join(R, img))
        ar = im.size[0] / im.size[1]
        iw = CW
        ih = iw / ar
        if ih > 400:
            ih = 400
            iw = ih * ar
        c.drawImage(ImageReader(os.path.join(R, img)), ML, y - ih, iw, ih, mask=None)
        y -= ih + 14

        c.setFont('M', 7)
        c.setFillColor(SOFT)
        c.drawString(ML, y, os.path.basename(img))
        y -= 18
        para(ML, y, body, 'D', 9.2, 12.8, CW)
        newpage()

    # missing
    y = H - 74
    c.setFont('DB', 20)
    c.setFillColor(INK)
    c.drawString(ML, y, t['missing'])
    c.setStrokeColor(RULE)
    c.line(ML, y - 13, W - MR, y - 13)
    y -= 34
    y = para(ML, y, t['missinglead'], 'DO', 9.4, 13, CW, SOFT)
    y -= 18
    for name, desc in (MISSING_HR if lang == 'hr' else MISSING_EN):
        c.setFont('MB', 10)
        c.setFillColor(WARN)
        c.drawString(ML, y, name)
        y -= 14
        y = para(ML + 14, y, desc, 'D', 9.2, 12.8, CW - 14)
        y -= 16
    y -= 20
    c.setStrokeColor(RULE)
    c.line(ML, y, W - MR, y)
    y -= 24
    para(ML, y, t['close'], 'D', 9.2, 12.8, CW, SOFT)

    foot()
    c.showPage()
    c.save()
    print("written", out, os.path.getsize(out))


os.makedirs("/home/claude/out", exist_ok=True)
build('hr', "/home/claude/out/[HR] 9 - v6 knjiga likova - Kristijan.pdf")
build('en', "/home/claude/out/[EN] 9 - v6 character sheets - Kristijan.pdf")
