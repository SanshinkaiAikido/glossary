## Script (Python) "translateGlossary"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=list, item
##title=return translation for given glossary list item and item item
##
# This Python file uses the following encoding: utf-8
if context.REQUEST['LANGUAGE'] == 'nl':
    if list == 'ryu':
        if item == '':
            return "type"
        if item == 'a':
            return "weg van harmoniseren van ki"
        if item == '':
            return "type"
        if item == 'b':
            return "lichaamstechnieken die aiki-principe gebruiken"
        if item == '':
            return "type"
        if item == 'j':
            return "jô technieken die aiki-principe gebruiken"
        if item == '':
            return "type"
        if item == 'k':
            return "ken technieken die aiki-principe gebruiken"
        if item == '':
            return "type"
        if item == 'h':
            return "eerste kata van specifieke zwaardstijl"
        if item == '':
            return "type"
        if item == 'j':
            return "zwaardstijl"
        if item == '':
            return "type"
        if item == 'g':
            return "groep van gezondheisoefeningen"
        if item == '':
            return "type"
        if item == 's':
            return "correct geordend lichaam"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOgeest"
        if item == 'a':
            return "één voor één aanvallen [continu oefening]"
        if item == '':
            return "TODOgeest"
        if item == 'k':
            return "vloeiende aanvallen, tori laat zich niet vastpakken [energetische vorm]"
        if item == '':
            return "TODOgeest"
        if item == 't':
            return "gedisciplineerde training, tori laat zich vastpakken [gedisciplineerd]"
        if item == '':
            return "TODOgeest"
        if item == 's':
            return "realistische training [serieus]"
        if item == '':
            return "TODOgeest"
        if item == 'k':
            return "balansverstoring"
        if item == '':
            return "TODOgeest"
        if item == 'j':
            return "technieken voor aanvallen van achter"
        if item == '':
            return "TODOgeest"
        if item == 'j':
            return "vrije vorm techniek"
        if item == '':
            return "TODOgeest"
        if item == 'r':
            return "technieken met meerdere aanvallers"
        if item == '':
            return "TODOgeest"
        if item == 's':
            return "herhaaldeijke oefening"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "positie"
        if item == 's':
            return "zittende techniek"
        if item == '':
            return "positie"
        if item == 'h':
            return "techniek voor zittende tori en staande uke"
        if item == '':
            return "positie"
        if item == 't':
            return "staande techniek"
        if item == '':
            return "positie"
        if item == '2':
            return "zittend"
        if item == '':
            return "positie"
        if item == '3':
            return "op knieën zittend met voeten plat op grond"
        if item == '':
            return "positie"
        if item == '4':
            return "op knieën zittend met tenen in mat"
        if item == '':
            return "positie"
        if item == '5':
            return "op knieën zittend met heupen tussen voeten op grond"
        if item == '':
            return "positie"
        if item == '6':
            return "zittend met benen vooruitgestrekt"
        if item == '':
            return "positie"
        if item == '7':
            return "zittend met benen gestrekt en geopend"
        if item == '':
            return "positie"
        if item == '8':
            return "zittend met knieën tegen borst en voeten op grond"
        if item == '':
            return "positie"
        if item == '9':
            return "zittend met voetzolen tegen elkaar en knieën op grond"
        if item == '':
            return "positie"
        if item == '0':
            return "kleermakerszit zonder benen te kruisen"
        if item == '':
            return "positie"
        if item == 'j':
            return "positie als een acht [hassôgamae]"
        if item == '':
            return "positie"
        if item == 'z':
            return "lotuspositie"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == 't':
            return "drie of meer uke die continue aanvallen, alleen begin techniek doen"
        if item == '':
            return "partner"
        if item == 'k':
            return "twee of meer uke die om de beurt aanvallen"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "wapen"
        if item == 'j':
            return "stok of korte houten staf"
        if item == '':
            return "wapen"
        if item == 'o':
            return "lange houten staf"
        if item == '':
            return "wapen"
        if item == 'b':
            return "gebogen houten zwaard"
        if item == '':
            return "wapen"
        if item == 't':
            return "mes of dolk (kling korter dan 30 cm)"
        if item == '':
            return "wapen"
        if item == 'w':
            return "gebogen metalen kort zwaard (kling 30 - 60 cm)"
        if item == '':
            return "wapen"
        if item == 'k':
            return "gebogen metalen zwaard (kling 60 - 70 cm)"
        if item == '':
            return "wapen"
        if item == 'a':
            return "gebogen metalen lang zwaard (kling langer dan 70 cm)"
        if item == '':
            return "wapen"
        if item == 'e':
            return "kort recht metalen tweesnijdend zwaard"
        if item == '':
            return "wapen"
        if item == 'n':
            return "Japans zwaard"
        if item == '':
            return "wapen"
        if item == 'n':
            return "hellebaard"
        if item == '':
            return "wapen"
        if item == 'y':
            return "speer"
        if item == '':
            return "wapen"
        if item == 's':
            return "stootplaat"
        if item == '':
            return "wapen"
        if item == 's':
            return "schede"
        if item == '':
            return "wapen"
        if item == 'u':
            return "wapenrek"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "aanval"
        if item == 'a':
            return "directe slag met open hand vanuit heupen naar voorkant hoofd [energetisch ontmoeten voorkant-gezicht slag]"
        if item == '':
            return "aanval"
        if item == 'b':
            return "greep naar één pols aan zelfde kant (identiek) [één-kant-hand greep zelfde kant]"
        if item == '':
            return "aanval"
        if item == 'c':
            return "greep naar één pols aan andere kant (spiegel) [één-kant-hand greep andere kant]"
        if item == '':
            return "aanval"
        if item == 'd':
            return "beide polsen grijpen [beide-polsen grijpen]"
        if item == '':
            return "aanval"
        if item == 'e':
            return "slag tegen voorkant hoofd [voorkant-gezicht slag]"
        if item == '':
            return "aanval"
        if item == 'f':
            return "greep naar één pols met beide handen [één-kant-hand beide-handen greep]"
        if item == '':
            return "aanval"
        if item == 'g':
            return "greep naar één schouder [schouder greep]"
        if item == '':
            return "aanval"
        if item == 'h':
            return "greep naar beide polsen van achter [achter beide-handen greep]"
        if item == '':
            return "aanval"
        if item == 'i':
            return "slag tegen zijkant hoofd [zijkant-gezicht slag]"
        if item == '':
            return "aanval"
        if item == 'j':
            return "stoot of steek naar middelste deel lichaam [midden lichaam steek]"
        if item == '':
            return "aanval"
        if item == 'k':
            return "greep naar schouder en slag tegen voorkant hoofd [schouder greep hoofd slag]"
        if item == '':
            return "aanval"
        if item == 'l':
            return "greep naar beide schouders van achter [achter beide-schouders greep]"
        if item == '':
            return "aanval"
        if item == 'm':
            return "stoot of steek naar bovenste deel lichaam [boven-lichaam steek]"
        if item == '':
            return "aanval"
        if item == 'n':
            return "ssk newsletter 3XXX [beide-kragen greep]"
        if item == '':
            return "aanval"
        if item == 'o':
            return "trap"
        if item == '':
            return "aanval"
        if item == 'p':
            return "nekverwurging van achter [achter nek wurg]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "binnen/buiten"
        if item == 'u':
            return "beweging naar binnenkant"
        if item == '':
            return "binnen/buiten"
        if item == 's':
            return "beweging naar buitenkant"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'a':
            return "ingaan met voorste voet"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'b':
            return "ingaan met achterste voet"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'c':
            return "wegdraaien op voorste voet"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'd':
            return "wegdraaien op achterste voet"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'e':
            return "uitwijken met voorste voet"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'f':
            return "uitwijken met achterste voet"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'g':
            return "ingaan met voorste voet en daarmee wegdraaien"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'h':
            return "ingaan met achterste voet en daarmee wegdraaien"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'i':
            return "ingaan met voorste voet, daarmee wegdraaien en uitwijken"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'j':
            return "ingaan met achterste voet, daarmee wegdraaien en uitwijken"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'k':
            return "wegdraaien op voorste voet en uitwijken"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'l':
            return "wegdraaien op achterste voet en uitwijken"
        if item == '':
            return "lichaamsverplaatsing"
        if item == 'm':
            return "ingaan met voorste voet en hele lichaam op de plek draaien"
        if item == '':
            return "lichaamsverplaatsing"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "handbeweging"
        if item == 'k':
            return "halve cirkel bovenlangs"
        if item == '':
            return "handbeweging"
        if item == 's':
            return "cirkel onderlangs"
        if item == '':
            return "handbeweging"
        if item == 't':
            return "onderarmen parallel"
        if item == '':
            return "handbeweging"
        if item == 'y':
            return "onderarmen gekruisd"
        if item == '':
            return "handbeweging"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "hand"
        if item == 'u':
            return "slaghand"
        if item == '':
            return "hand"
        if item == 'k':
            return "hand bij schouder"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "hoogte"
        if item == 'g':
            return "laag"
        if item == '':
            return "hoogte"
        if item == 'c':
            return "midden"
        if item == '':
            return "hoogte"
        if item == 'j':
            return "hoog"
        if item == '':
            return "hoogte"
        if item == '1':
            return "kleine houding"
        if item == '':
            return "hoogte"
        if item == '2':
            return "lage houding"
        if item == '':
            return "hoogte"
        if item == '3':
            return "midden houden"
        if item == '':
            return "hoogte"
        if item == '5':
            return "hoge houding"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "techniek"
        if item == 'a':
            return "eerste onderricht"
        if item == '':
            return "techniek"
        if item == 'b':
            return "tweede onderricht"
        if item == '':
            return "techniek"
        if item == 'c':
            return "derde onderricht"
        if item == '':
            return "techniek"
        if item == 'd':
            return "vierde onderricht"
        if item == '':
            return "techniek"
        if item == 'e':
            return "hoek worp"
        if item == '':
            return "techniek"
        if item == 'f':
            return "pols verdraaiïng"
        if item == '':
            return "techniek"
        if item == 'g':
            return "ingaande worp"
        if item == '':
            return "techniek"
        if item == 'h':
            return "vier richtingen worp"
        if item == '':
            return "techniek"
        if item == 'i':
            return "vijfde onderricht"
        if item == '':
            return "techniek"
        if item == 'j':
            return "elleboog controle klem"
        if item == '':
            return "techniek"
        if item == 'k':
            return "binnenlangs raddraai sankyo"
        if item == '':
            return "techniek"
        if item == 'l':
            return "arm verstrengeling"
        if item == '':
            return "techniek"
        if item == 'm':
            return "heupworp met hoofd van binnen naar buiten onderlangs gyaku hanmi"
        if item == '':
            return "techniek"
        if item == 'n':
            return "vermengend laten vallen"
        if item == '':
            return "techniek"
        if item == 'o':
            return "raddraai worp"
        if item == '':
            return "techniek"
        if item == 'p':
            return "arm breek worp"
        if item == '':
            return "techniek"
        if item == 'q':
            return "voorwaarste worp"
        if item == '':
            return "techniek"
        if item == 'r':
            return "trek worp"
        if item == '':
            return "techniek"
        if item == 's':
            return "houw worp"
        if item == '':
            return "techniek"
        if item == 't':
            return "draai worp"
        if item == '':
            return "techniek"
        if item == 'u':
            return "hemel aarde worp"
        if item == '':
            return "techniek"
        if item == 'v':
            return "archetype ademworp"
        if item == '':
            return "techniek"
        if item == 'w':
            return "binnenlangs raddraai worp"
        if item == '':
            return "techniek"
        if item == 'x':
            return "slingerende stomp ademworp"
        if item == '':
            return "techniek"
        if item == 'y':
            return "kruis knoop verstrengeling"
        if item == '':
            return "techniek"
        if item == 'z':
            return "roeioefening ademworp"
        if item == '':
            return "techniek"
        if item == '0':
            return "vier richtingen trappen ademworp"
        if item == '':
            return "techniek"
        if item == '1':
            return "arm verstrengeling sankyo worp"
        if item == '':
            return "techniek"
        if item == '2':
            return "arm verstrengeling yonkyo worp"
        if item == '':
            return "techniek"
        if item == '3':
            return "heupworp"
        if item == '':
            return "techniek"
        if item == '4':
            return "buitenlangs raddraai worp"
        if item == '':
            return "techniek"
        if item == '5':
            return "?"
        if item == '':
            return "techniek"
        if item == '6':
            return "arm verstrengeling klem"
        if item == '':
            return "techniek"
        if item == '7':
            return "hand rad"
        if item == '':
            return "techniek"
        if item == '8':
            return "schouder rad"
        if item == '':
            return "techniek"
        if item == '9':
            return "heup ?"
        if item == '':
            return "techniek"
        if item == '~':
            return "zinkend lichaam heup wiel"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "voor/achter"
        if item == 'o':
            return "voor partner"
        if item == '':
            return "voor/achter"
        if item == 'u':
            return "achter partner"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        if item == '':
            return "nummer"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "yin/yang"
        if item == '1':
            return "yin"
        if item == '':
            return "yin/yang"
        if item == '2':
            return "yang"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "principe"
        if item == '1':
            return "water, boven-onder, oost"
        if item == '':
            return "principe"
        if item == '2':
            return "aarde, links-rechts, zuid"
        if item == '':
            return "principe"
        if item == '3':
            return "wind, voor-achter, west"
        if item == '':
            return "principe"
        if item == '4':
            return "vuur, spiraal, noord"
        if item == '':
            return "principe"
        if item == '5':
            return "mens"
        if item == '':
            return "principe"
        if item == 'h':
            return "lente"
        if item == '':
            return "principe"
        if item == 'n':
            return "zomer"
        if item == '':
            return "principe"
        if item == 'a':
            return "herfst"
        if item == '':
            return "principe"
        if item == 'f':
            return "winter"
        if item == '':
            return "principe"
        if item == 'k':
            return "theorie van aanval en verdediging"
        if item == '':
            return "principe"
        if item == 'u':
            return "stoot principe"
        if item == '':
            return "principe"
        if item == 'o':
            return "klem principe"
        if item == '':
            return "principe"
        if item == 'g':
            return "werp principe"
        if item == '':
            return "principe"
        if item == 'z':
            return "snij principe"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "worp"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "klem"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "geklemd werpen"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "ontvangen met het lichaam"
        if item == '1':
            return "boven onder ukemi"
        if item == '':
            return "ontvangen met het lichaam"
        if item == '2':
            return "voorwaartse ukemi"
        if item == '':
            return "ontvangen met het lichaam"
        if item == '3':
            return "achterwaartse ukemi"
        if item == '':
            return "ontvangen met het lichaam"
        if item == '4':
            return "zijwaartse ukemi"
        if item == '':
            return "ontvangen met het lichaam"
        if item == 'c':
            return "valbreken door op de plaats af te slaan"
        if item == '':
            return "ontvangen met het lichaam"
        if item == '':
            return "ontvangen met het lichaam"
        if item == 't':
            return "vrije val"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "persoon"
        if item == '1':
            return "wijlen oprichter van aikidô, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "persoon"
        if item == '2':
            return "wijlen zoon van ôsensei, tweede dôshu (27-06-1921 - 04-01-1999)"
        if item == '':
            return "persoon"
        if item == '3':
            return "kleinzoon van ôsensei, derde dôshu (02-04-1951)"
        if item == '':
            return "persoon"
        if item == 't':
            return "leerling van ôsensei, shihan (13-12-1929)"
        if item == '':
            return "persoon"
        if item == 'i':
            return "leerling van Tada sensei, shihan (08-04-1940)"
        if item == '':
            return "persoon"
        if item == '':
            return "persoon"
        if item == '':
            return "persoon"
        if item == '':
            return "persoon"
        if item == '':
            return "persoon"
        if item == '':
            return "persoon"
        if item == '':
            return "persoon"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "tellen"
        if item == '0':
            return "nul, leeg"
        if item == '':
            return "tellen"
        if item == '1':
            return "een"
        if item == '':
            return "tellen"
        if item == '2':
            return "twee"
        if item == '':
            return "tellen"
        if item == '3':
            return "drie"
        if item == '':
            return "tellen"
        if item == '4':
            return "vier"
        if item == '':
            return "tellen"
        if item == '5':
            return "vijf"
        if item == '':
            return "tellen"
        if item == '6':
            return "zes"
        if item == '':
            return "tellen"
        if item == '7':
            return "zeven"
        if item == '':
            return "tellen"
        if item == '8':
            return "acht"
        if item == '':
            return "tellen"
        if item == '9':
            return "negen"
        if item == '':
            return "tellen"
        if item == 'a':
            return "tien"
        if item == '':
            return "tellen"
        if item == 'b':
            return "elf"
        if item == '':
            return "tellen"
        if item == 'c':
            return "twintig"
        if item == '':
            return "tellen"
        if item == 'd':
            return "eenentwintig"
        if item == '':
            return "tellen"
        if item == 'e':
            return "honderd"
        if item == '':
            return "tellen"
        if item == 'f':
            return "duizend"
        if item == '':
            return "tellen"
        if item == 'e':
            return "tienduizend"
        if item == '':
            return "tellen"
        if item == 'h':
            return "eerste deel"
        if item == '':
            return "tellen"
        if item == 'i':
            return "tweede deel"
        if item == '':
            return "tellen"
        if item == 'j':
            return "derde deel"
        if item == '':
            return "tellen"
        if item == 'k':
            return "vierde deel"
        if item == '':
            return "tellen"
        if item == 'l':
            return "vijfde deel"
        if item == '':
            return "tellen"
        if item == 'm':
            return "zesde deel"
        if item == '':
            return "tellen"
        if item == 'n':
            return "zevende deel"
        if item == '':
            return "tellen"
        if item == 'o':
            return "achtste deel"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "gradaties"
        if item == 'n':
            return "dangraad"
        if item == '':
            return "gradaties"
        if item == 'k':
            return "kyûgraad"
        if item == '':
            return "gradaties"
        if item == '0':
            return "zonder kyû"
        if item == '':
            return "gradaties"
        if item == '6':
            return "zesde kyû"
        if item == '':
            return "gradaties"
        if item == '5':
            return "vijfde kyû"
        if item == '':
            return "gradaties"
        if item == '4':
            return "vierde kyû"
        if item == '':
            return "gradaties"
        if item == '3':
            return "derde kyû"
        if item == '':
            return "gradaties"
        if item == '2':
            return "tweede kyû"
        if item == '':
            return "gradaties"
        if item == '1':
            return "eerste kyû, beginnerskyû"
        if item == '':
            return "gradaties"
        if item == 'y':
            return "met dan"
        if item == '':
            return "gradaties"
        if item == 'o':
            return "zonder dan"
        if item == '':
            return "gradaties"
        if item == 'a':
            return "eerste dan, beginnersdan"
        if item == '':
            return "gradaties"
        if item == 'b':
            return "tweede dan"
        if item == '':
            return "gradaties"
        if item == 'c':
            return "derde dan"
        if item == '':
            return "gradaties"
        if item == 'd':
            return "vierde dan"
        if item == '':
            return "gradaties"
        if item == 'e':
            return "vijfde dan"
        if item == '':
            return "gradaties"
        if item == 'f':
            return "zesde dan"
        if item == '':
            return "gradaties"
        if item == 'g':
            return "zevende dan"
        if item == '':
            return "gradaties"
        if item == 'h':
            return "achtste dan"
        if item == '':
            return "gradaties"
        if item == 'i':
            return "negende dan"
        if item == '':
            return "gradaties"
        if item == 'j':
            return "tiende dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "algemeen"
        if item == '1':
            return "harmonie, eenwording"
        if item == '':
            return "algemeen"
        if item == '2':
            return "levenskracht, levensenergie"
        if item == '':
            return "algemeen"
        if item == '3':
            return "weg, leer, discipline"
        if item == '':
            return "algemeen"
        if item == '3':
            return "weg van harmoniseren van ki"
        if item == '':
            return "algemeen"
        if item == '4':
            return "beoefenaar van aikido"
        if item == '':
            return "algemeen"
        if item == '5':
            return "organisatie voor de beoefening en verspreiding van aikidô"
        if item == '':
            return "algemeen"
        if item == '8':
            return "aanvaller [ontvanger]"
        if item == '':
            return "algemeen"
        if item == '9':
            return "verdediger [pakken, opnemen, kiezen]"
        if item == '':
            return "algemeen"
        if item == 'n':
            return "werper"
        if item == '':
            return "algemeen"
        if item == 'u':
            return "ouder, leraar [slaand zwaard]"
        if item == '':
            return "algemeen"
        if item == 's':
            return "kind, leerling [uitvoerend zwaard]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "instructies"
        if item == '1':
            return "wij groeten u beleeft ?/ alstublieft (aan begin van les of oefening)"
        if item == '':
            return "instructies"
        if item == '2':
            return "dank u wel (aan einde van les of oefening)"
        if item == '':
            return "instructies"
        if item == '3':
            return "ja"
        if item == '':
            return "instructies"
        if item == '':
            return "instructies"
        if item == '5':
            return "stop (en ga aan de kant zitten)"
        if item == '':
            return "instructies"
        if item == '6':
            return "begin, start"
        if item == '':
            return "instructies"
        if item == '6':
            return "wacht, stop"
        if item == '':
            return "instructies"
        if item == '8':
            return "sta op"
        if item == '':
            return "instructies"
        if item == '9':
            return "ga zitten"
        if item == '':
            return "instructies"
        if item == 'a':
            return "draai"
        if item == '':
            return "instructies"
        if item == 'b':
            return "wissel van partner [persoon]"
        if item == '':
            return "instructies"
        if item == 'c':
            return "herhaal de oefening"
        if item == '':
            return "instructies"
        if item == 'd':
            return "gebruik de andere kant"
        if item == '':
            return "instructies"
        if item == 'e':
            return "zoek een andere partner"
        if item == '':
            return "instructies"
        if item == 'f':
            return "groeten, buigen [respect]"
        if item == '':
            return "instructies"
        if item == 'g':
            return "staande buiging"
        if item == '':
            return "instructies"
        if item == 'h':
            return "zittende buiging"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "titels"
        if item == 's':
            return "grote leraar"
        if item == '':
            return "titels"
        if item == 'o':
            return "leraar, instructeur"
        if item == '':
            return "titels"
        if item == 'd':
            return "degene die de weg wijst"
        if item == '':
            return "titels"
        if item == '7':
            return "hoofdinstructeur (minimaal 6e dan)"
        if item == '':
            return "titels"
        if item == '8':
            return "instructeur, shihan-in-opleiding (4e of 5e dan)"
        if item == '':
            return "titels"
        if item == '9':
            return "assistent instructeur (2e of 3e dan)"
        if item == '':
            return "titels"
        if item == 'a':
            return "iemands senior"
        if item == '':
            return "titels"
        if item == 'b':
            return "iemands junior"
        if item == '':
            return "titels"
        if item == 'c':
            return "persoon zonder graad"
        if item == '':
            return "titels"
        if item == 'd':
            return "persoon met graad"
        if item == '':
            return "titels"
        if item == 'e':
            return "dôjô-hoofd"
        if item == '':
            return "titels"
        if item == 'f':
            return "leerling"
        if item == '':
            return "titels"
        if item == 'g':
            return "in dôjô wonende leerling, inwonende leerling"
        if item == '':
            return "titels"
        if item == 'h':
            return "buiten dôjô wonende leerling"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "voorwerpen"
        if item == '0':
            return "trainingsruimte (plaats van verlichting) [plaats van de weg]"
        if item == '':
            return "voorwerpen"
        if item == '1':
            return "altaar met portret van ôsensei (eventueel met calligrafie of bloemen) [hoge kant van de mat]"
        if item == '':
            return "voorwerpen"
        if item == '2':
            return "(lage) achterkant van de mat"
        if item == '':
            return "voorwerpen"
        if item == '3':
            return "(hoge) rechterzijde van de mat"
        if item == '':
            return "voorwerpen"
        if item == '4':
            return "(lage) linkerzijde van de mat"
        if item == '':
            return "voorwerpen"
        if item == '5':
            return "matten"
        if item == '':
            return "voorwerpen"
        if item == '6':
            return "hoofdkwartier"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "kleding"
        if item == '1':
            return "oefenkleding, trainingspak"
        if item == '':
            return "kleding"
        if item == '2':
            return "band"
        if item == '':
            return "kleding"
        if item == '3':
            return "witte band"
        if item == '':
            return "kleding"
        if item == '4':
            return "zwarte band"
        if item == '':
            return "kleding"
        if item == '5':
            return "soort van sokken met apparte grote teen"
        if item == '':
            return "kleding"
        if item == '6':
            return "slippers"
        if item == '':
            return "kleding"
        if item == '7':
            return "traditionele Japanse broek"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "anatomie"
        if item == 'a':
            return "centrum, buik"
        if item == '':
            return "anatomie"
        if item == 'b':
            return "lichaam"
        if item == '':
            return "anatomie"
        if item == 'c':
            return "voorkant hoofd"
        if item == '':
            return "anatomie"
        if item == 'd':
            return "zijkand hoofd"
        if item == '':
            return "anatomie"
        if item == 'e':
            return "knie"
        if item == '':
            return "anatomie"
        if item == 'f':
            return "nek"
        if item == '':
            return "anatomie"
        if item == 'g':
            return "borst"
        if item == '':
            return "anatomie"
        if item == 'e':
            return "schouder"
        if item == '':
            return "anatomie"
        if item == 'h':
            return "elleboog"
        if item == '':
            return "anatomie"
        if item == 'i':
            return "arm"
        if item == '':
            return "anatomie"
        if item == 'j':
            return "pols"
        if item == '':
            return "anatomie"
        if item == 'k':
            return "hand"
        if item == '':
            return "anatomie"
        if item == 'k':
            return "handzwaard"
        if item == '':
            return "anatomie"
        if item == 'l':
            return "been, voet"
        if item == '':
            return "anatomie"
        if item == 'm':
            return "enkel"
        if item == '':
            return "anatomie"
        if item == 'n':
            return "heupen, onderrug"
        if item == '':
            return "anatomie"
        if item == 'o':
            return "kraag"
        if item == '':
            return "anatomie"
        if item == 'p':
            return "lichaam"
        if item == '':
            return "anatomie"
        if item == 's':
            return "mouw"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "diversen"
        if item == 'a':
            return "gezamelijk ontsnappen"
        if item == '':
            return "diversen"
        if item == 'b':
            return "elkaar tegelijkertijd doden"
        if item == '':
            return "diversen"
        if item == 'c':
            return "?"
        if item == '':
            return "diversen"
        if item == 'd':
            return "martiale weg"
        if item == '':
            return "diversen"
        if item == 'e':
            return "stafoefeneningen met partner"
        if item == '':
            return "diversen"
        if item == 'f':
            return "zwaardoefeneningen met partner"
        if item == '':
            return "diversen"
        if item == 'g':
            return "zwaard afpakken"
        if item == '':
            return "diversen"
        if item == 'h':
            return "mes afpakken"
        if item == '':
            return "diversen"
        if item == 'i':
            return "wijzend naar het oog"
        if item == '':
            return "diversen"
        if item == 'j':
            return "?"
        if item == '':
            return "diversen"
        if item == 'm':
            return "juiste dynamische afstand [interval]"
        if item == '':
            return "diversen"
        if item == 's':
            return "lopen op knieën"
        if item == '':
            return "diversen"
        if item == 't':
            return "Japanse trommel die begin en einde van training aangeeft"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "richting"
        if item == 'h':
            return "links"
        if item == '':
            return "richting"
        if item == 'm':
            return "rechts"
        if item == '':
            return "richting"
        if item == 'i':
            return "ingaan"
        if item == '':
            return "richting"
        if item == 'k':
            return "wegdraaiend"
        if item == '':
            return "richting"
        if item == '1':
            return "voorwaards"
        if item == '':
            return "richting"
        if item == '2':
            return "achterwaards"
        if item == '':
            return "richting"
        if item == '3':
            return "zijwaards"
        if item == '':
            return "richting"
        if item == 'a':
            return "binnen, inwaarts"
        if item == '':
            return "richting"
        if item == 'b':
            return "buiten, buitenwaarts"
        if item == '':
            return "richting"
        if item == 'n':
            return "diagonaal"
        if item == '':
            return "richting"
        if item == 'c':
            return "verticaal"
        if item == '':
            return "richting"
        if item == 's':
            return "horizontaal"
        if item == '':
            return "richting"
        if item == 't':
            return "staand"
        if item == '':
            return "richting"
        if item == 'x':
            return "tegenover"
        if item == '':
            return "richting"
        if item == '8':
            return "alle richtingen [acht richtingen]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "oefening"
        if item == '1':
            return "ikkyô oefening"
        if item == '':
            return "oefening"
        if item == '2':
            return "basis lichaamsmenging"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "fundamentele principes"
        if item == '1':
            return "lente zwaard"
        if item == '':
            return "fundamentele principes"
        if item == '2':
            return "zomer zwaard"
        if item == '':
            return "fundamentele principes"
        if item == '3':
            return "herfst zwaard"
        if item == '':
            return "fundamentele principes"
        if item == '4':
            return "winter zwaard"
        if item == '':
            return "fundamentele principes"
        if item == '5':
            return "acht richtingen"
        if item == '':
            return "fundamentele principes"
        if item == '6':
            return "houw je ego doormidden"
        if item == '':
            return "fundamentele principes"
        if item == '7':
            return "veranderlijke tijden"
        if item == '':
            return "fundamentele principes"
        if item == '8':
            return "lang en kort zijn één"
        if item == '':
            return "fundamentele principes"
        if item == '9':
            return "ontvangen"
        if item == '':
            return "fundamentele principes"
        if item == 'a':
            return "lichaam zwaard"
        if item == '':
            return "fundamentele principes"
        if item == 'b':
            return "knikkende groet zonder oogcontact te verbreken of te spreken"
        if item == '':
            return "fundamentele principes"
        if item == 'c':
            return "eigen zwaard trekken"
        if item == '':
            return "fundamentele principes"
        if item == 'd':
            return "harmonieus wijzend naar het oog"
        if item == '':
            return "fundamentele principes"
        if item == 'e':
            return "versnellen, haasten"
        if item == '':
            return "fundamentele principes"
        if item == 'g':
            return "tempelbeschermer zwaard"
        if item == '':
            return "fundamentele principes"
        if item == 'h':
            return "schaduw"
        if item == '':
            return "fundamentele principes"
        if item == 'i':
            return "harmonieuze jôdan"
        if item == '':
            return "fundamentele principes"
        if item == 'j':
            return "?"
        if item == '':
            return "fundamentele principes"
        if item == 'k':
            return "herhaaldelijk oefenen [binnen ontelbaar]"
        if item == '':
            return "fundamentele principes"
        if item == 'l':
            return "beide armen"
        if item == '':
            return "fundamentele principes"
        if item == 'm':
            return "duw oefening"
        if item == '':
            return "fundamentele principes"
        if item == 'n':
            return "rechte lijn"
        if item == '':
            return "fundamentele principes"
        if item == 'o':
            return "blokkeer lichaam"
        if item == '':
            return "fundamentele principes"
        if item == 'p':
            return "bodycheck [lichaam stoot]"
        if item == '':
            return "fundamentele principes"
        if item == 'q':
            return "niet slaan"
        if item == '':
            return "fundamentele principes"
        if item == 'r':
            return "slaap [mist]"
        if item == '':
            return "fundamentele principes"
        if item == 's':
            return "lichaam zijwaarts naar opponent gedraaid"
        if item == '':
            return "fundamentele principes"
        if item == 't':
            return "aankijken, hoofd draaien"
        if item == '':
            return "fundamentele principes"
        if item == 'u':
            return "snijden"
        if item == '':
            return "fundamentele principes"
        if item == 'v':
            return "stoppen"
        if item == '':
            return "fundamentele principes"
        if item == 'w':
            return "rug slaan"
        if item == '':
            return "fundamentele principes"
        if item == 'x':
            return "ochtendgloren, dageraad"
        if item == '':
            return "fundamentele principes"
        if item == 'y':
            return "groot"
        if item == '':
            return "fundamentele principes"
        if item == 'z':
            return "wegdoen"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '~':
            return "ademhaling in grote cirkels [grote cirkel ademhalingsoefeningen]"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '0':
            return "?"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '1':
            return "ademhaling met handen in yang [?]"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '2':
            return "ademhaling met handen in ying [?]"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '3':
            return "ademhaling van de energie van handen die een kruis maken [energie menging ademhaling]"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '4':
            return "ademhaling 'om één te worden met het omniversum' [aum ademhaling]"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '5':
            return "breathing with principles"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == '6':
            return "liggende oefeningen"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == 'a':
            return "oscillatiemethode"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == 'b':
            return "?"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == 'c':
            return "?"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == 'd':
            return "goudvis oefening"
        if item == '':
            return "groep van gezondheisoefeningen"
        if item == 'u':
            return "paard oefening"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'de':
    if list == 'ryu':
        if item == '':
            return "Type"
        if item == 'a':
            return "Weg des harmoniseren von Ki"
        if item == '':
            return "Type"
        if item == 'b':
            return "Korpertechniken die aiki Prinzipien verwenden"
        if item == '':
            return "Type"
        if item == 'j':
            return "jô Techniken die aiki Prinzipien verwenden"
        if item == '':
            return "Type"
        if item == 'k':
            return "ken Techniken die aiki Prinzipien verwenden"
        if item == '':
            return "Type"
        if item == 'h':
            return "ersten Kata der spezifischen Schwert-Stil"
        if item == '':
            return "Type"
        if item == 'j':
            return "Schwertstil"
        if item == '':
            return "Type"
        if item == 'g':
            return "Gruppe der gesundheits Übungen"
        if item == '':
            return "Type"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOGeist"
        if item == 'a':
            return "angreifen einer nach dem anderen [fortwährend üben]"
        if item == '':
            return "TODOGeist"
        if item == 'k':
            return "fliessende form, tori lässt sich nicht festhalten [energetische form]"
        if item == '':
            return "TODOGeist"
        if item == 't':
            return "dizipliniertes training, tori lässt sich fessthalten [diszipliniert]"
        if item == '':
            return "TODOGeist"
        if item == 's':
            return "realistisches training [ernst]"
        if item == '':
            return "TODOGeist"
        if item == 'k':
            return "das Gleichgewicht brechen"
        if item == '':
            return "TODOGeist"
        if item == 'j':
            return "techniken bei denen man von hinten angegriffen wird"
        if item == '':
            return "TODOGeist"
        if item == 'j':
            return "freie Technik"
        if item == '':
            return "TODOGeist"
        if item == 'r':
            return "techniken mit mehreren Angreifer"
        if item == '':
            return "TODOGeist"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Position"
        if item == 's':
            return "sitzende Technik"
        if item == '':
            return "Position"
        if item == 'h':
            return "Technik für sitzender tori und stehender uke"
        if item == '':
            return "Position"
        if item == 't':
            return "stehende Technik"
        if item == '':
            return "Position"
        if item == '2':
            return "sitzend"
        if item == '':
            return "Position"
        if item == '3':
            return "auf der Knien sitzend mit Füßen flach auf dem Boden"
        if item == '':
            return "Position"
        if item == '4':
            return "auf der Knien sitzend mit Zehen in dem Boden"
        if item == '':
            return "Position"
        if item == '5':
            return "auf den Knien sitzend mit Hüften zwischen dem Füßen auf dem Boden"
        if item == '':
            return "Position"
        if item == '6':
            return "sitzend mit Beine vorausgestreckt"
        if item == '':
            return "Position"
        if item == '7':
            return "sitzend mit Beine gestreckt und geöffnet"
        if item == '':
            return "Position"
        if item == '8':
            return "sitzend mit Knien gegen die Brust und Füßen auf dem Boden"
        if item == '':
            return "Position"
        if item == '9':
            return "sitzend mit Fußsohlen gegeneinander und Knien auf dem Bodem"
        if item == '':
            return "Position"
        if item == '0':
            return "Schneidersitz ohne die Beinen zu kreuzen"
        if item == '':
            return "Position"
        if item == 'j':
            return "Haltung wie eine Acht [hassôgamae]"
        if item == '':
            return "Position"
        if item == 'z':
            return "Lotusposition"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == '':
            return "Partner"
        if item == 't':
            return "Drei oder mehr uke die fortlaufend angreifen, mache nur begin der Techik"
        if item == '':
            return "Partner"
        if item == 'k':
            return "zwei oder mehr uke die abwechselend angreifen"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "Waffe"
        if item == 'j':
            return "Stock, kurzer holzen Stab"
        if item == '':
            return "Waffe"
        if item == 'o':
            return "langer Holzstab"
        if item == '':
            return "Waffe"
        if item == 'b':
            return "gebogenes Holzschwert"
        if item == '':
            return "Waffe"
        if item == 't':
            return "Messer oder Dolch"
        if item == '':
            return "Waffe"
        if item == 'w':
            return "gebogenes Kurzschwert aus Metall"
        if item == '':
            return "Waffe"
        if item == 'k':
            return "gebogenes Metallschwert"
        if item == '':
            return "Waffe"
        if item == 'a':
            return "Langschwert aus Metall"
        if item == '':
            return "Waffe"
        if item == 'e':
            return "kurzes, grades zweischnediges Metallschwert"
        if item == '':
            return "Waffe"
        if item == 'n':
            return "Japanische Schwert"
        if item == '':
            return "Waffe"
        if item == 'n':
            return "Hellebarde"
        if item == '':
            return "Waffe"
        if item == 'y':
            return "Speer"
        if item == '':
            return "Waffe"
        if item == 's':
            return "?"
        if item == '':
            return "Waffe"
        if item == 's':
            return "Scheide"
        if item == '':
            return "Waffe"
        if item == 'u':
            return "Waffenreck?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "Angriff"
        if item == 'a':
            return "Stoß mit geöffneter Hand von den Hüften nach vorne zum Kopf"
        if item == '':
            return "Angriff"
        if item == 'b':
            return "eine Hand fasst das selbe Handgelenk des Gegenübers (identisch) [eine Hand fasst die selbe Hand des Gegenübers (identisch)]"
        if item == '':
            return "Angriff"
        if item == 'c':
            return "eine Hand fasst das andere Handgelenk des Gegenübers (spiegel) [eine Hand fasst das andere Handgelenk des Gegenübers (spiegel)]"
        if item == '':
            return "Angriff"
        if item == 'd':
            return "beide Handgelenke fassen [beide Handgelenke fassen]"
        if item == '':
            return "Angriff"
        if item == 'e':
            return "Schlag gegen Vorne von Kopf [fracesco]"
        if item == '':
            return "Angriff"
        if item == 'f':
            return "?"
        if item == '':
            return "Angriff"
        if item == 'g':
            return "die Schulter fassen"
        if item == '':
            return "Angriff"
        if item == 'h':
            return "dem Partner von hinten an die Handgelenke fassen"
        if item == '':
            return "Angriff"
        if item == 'i':
            return "Schlag gegen die Schläfe"
        if item == '':
            return "Angriff"
        if item == 'j':
            return "Stoß nach dem Mittelteil des Körpers"
        if item == '':
            return "Angriff"
        if item == 'k':
            return "Schulter fassen und Schlag zum Gesicht"
        if item == '':
            return "Angriff"
        if item == 'l':
            return "von Hinten beide Schulter fassen"
        if item == '':
            return "Angriff"
        if item == 'm':
            return "Stoß nach dem oberen Teil des Körpers"
        if item == '':
            return "Angriff"
        if item == 'n':
            return "ssk newsletter 3XXX"
        if item == '':
            return "Angriff"
        if item == 'o':
            return "Tritt"
        if item == '':
            return "Angriff"
        if item == 'p':
            return "Würgen von hinten"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "innen/ausen"
        if item == 'u':
            return "Bewegung nach innen"
        if item == '':
            return "innen/ausen"
        if item == 's':
            return "Bewegung nach draussen"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "Korperbewegung"
        if item == 'a':
            return "eintreten mit vorderem Fuß"
        if item == '':
            return "Korperbewegung"
        if item == 'b':
            return "eintreten mit hinterem Fuß"
        if item == '':
            return "Korperbewegung"
        if item == 'c':
            return "wegdrehen auf vorderem Fuß"
        if item == '':
            return "Korperbewegung"
        if item == 'd':
            return "wegdrehen auf hinterem Fuß"
        if item == '':
            return "Korperbewegung"
        if item == 'e':
            return "ausweichen mit vorderem Fuß"
        if item == '':
            return "Korperbewegung"
        if item == 'f':
            return "ausweichen mit hinterem Fuß"
        if item == '':
            return "Korperbewegung"
        if item == 'g':
            return "eintreten mit Vorderfuss mit anschliessender Drehung"
        if item == '':
            return "Korperbewegung"
        if item == 'h':
            return "eintreten mit Hinterfuss mit anschliessender Drehung"
        if item == '':
            return "Korperbewegung"
        if item == 'i':
            return "eintreten mit Vorderfuss,Körperdrehung und ausweichen"
        if item == '':
            return "Korperbewegung"
        if item == 'j':
            return "eintreten mit Hinterfuss,Körperdrehung und ausweichen"
        if item == '':
            return "Korperbewegung"
        if item == 'k':
            return "Körperdrehung mit dem Vorderfuss und ausweichen"
        if item == '':
            return "Korperbewegung"
        if item == 'l':
            return "Körperdrehung mit dem Hinterfuss und ausweichen"
        if item == '':
            return "Korperbewegung"
        if item == 'm':
            return "eintreten mit Hinterfuss und anschliessender Körperdrehung"
        if item == '':
            return "Korperbewegung"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "Handbewegung"
        if item == 'k':
            return "halber Kreis gegen oben"
        if item == '':
            return "Handbewegung"
        if item == 's':
            return "Halbkreis gegen unten"
        if item == '':
            return "Handbewegung"
        if item == 't':
            return "?"
        if item == '':
            return "Handbewegung"
        if item == 'y':
            return "?"
        if item == '':
            return "Handbewegung"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "Hand"
        if item == 'u':
            return "Schlaghand"
        if item == '':
            return "Hand"
        if item == 'k':
            return "Hand bei Schulter"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "Höhe"
        if item == 'g':
            return "Länge"
        if item == '':
            return "Höhe"
        if item == 'c':
            return "?"
        if item == '':
            return "Höhe"
        if item == 'j':
            return "hoch"
        if item == '':
            return "Höhe"
        if item == '1':
            return "schmale Haltung"
        if item == '':
            return "Höhe"
        if item == '2':
            return "tiefe Haltung"
        if item == '':
            return "Höhe"
        if item == '3':
            return "mittlere Haltung"
        if item == '':
            return "Höhe"
        if item == '5':
            return "hohe Haltung"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "Technik"
        if item == 'a':
            return "Lektion Nummer eins"
        if item == '':
            return "Technik"
        if item == 'b':
            return "Lektion Nummer zwei"
        if item == '':
            return "Technik"
        if item == 'c':
            return "Lektion Nummer drei"
        if item == '':
            return "Technik"
        if item == 'd':
            return "Lektion Nummer vier"
        if item == '':
            return "Technik"
        if item == 'e':
            return "?"
        if item == '':
            return "Technik"
        if item == 'f':
            return "Handgelenk verdrehen"
        if item == '':
            return "Technik"
        if item == 'g':
            return "?"
        if item == '':
            return "Technik"
        if item == 'h':
            return "schneiden in vier Richtungen"
        if item == '':
            return "Technik"
        if item == 'i':
            return "Lektion Nummer fünf"
        if item == '':
            return "Technik"
        if item == 'j':
            return "Ellbogen controllierende blockieren"
        if item == '':
            return "Technik"
        if item == 'k':
            return "?"
        if item == '':
            return "Technik"
        if item == 'l':
            return "?"
        if item == '':
            return "Technik"
        if item == 'm':
            return "?"
        if item == '':
            return "Technik"
        if item == 'n':
            return "?"
        if item == '':
            return "Technik"
        if item == 'o':
            return "?"
        if item == '':
            return "Technik"
        if item == 'p':
            return "?"
        if item == '':
            return "Technik"
        if item == 'q':
            return "?"
        if item == '':
            return "Technik"
        if item == 'r':
            return "?"
        if item == '':
            return "Technik"
        if item == 's':
            return "Wurf mit Schnitt"
        if item == '':
            return "Technik"
        if item == 't':
            return "Drehwurf"
        if item == '':
            return "Technik"
        if item == 'u':
            return "Himmel-Erde Wurf"
        if item == '':
            return "Technik"
        if item == 'v':
            return "?"
        if item == '':
            return "Technik"
        if item == 'w':
            return "?"
        if item == '':
            return "Technik"
        if item == 'x':
            return "?"
        if item == '':
            return "Technik"
        if item == 'y':
            return "?"
        if item == '':
            return "Technik"
        if item == 'z':
            return "?"
        if item == '':
            return "Technik"
        if item == '0':
            return "?"
        if item == '':
            return "Technik"
        if item == '1':
            return "?"
        if item == '':
            return "Technik"
        if item == '2':
            return "?"
        if item == '':
            return "Technik"
        if item == '3':
            return "Hüftwurf"
        if item == '':
            return "Technik"
        if item == '4':
            return "?"
        if item == '':
            return "Technik"
        if item == '5':
            return "?"
        if item == '':
            return "Technik"
        if item == '6':
            return "?"
        if item == '':
            return "Technik"
        if item == '7':
            return "?"
        if item == '':
            return "Technik"
        if item == '8':
            return "?"
        if item == '':
            return "Technik"
        if item == '9':
            return "?"
        if item == '':
            return "Technik"
        if item == '~':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "?"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        if item == '':
            return "Nummer"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "Yin/Yang"
        if item == '1':
            return "Yin"
        if item == '':
            return "Yin/Yang"
        if item == '2':
            return "Yang"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "Prinzip"
        if item == '1':
            return "Wasser, oben-unten, Ost"
        if item == '':
            return "Prinzip"
        if item == '2':
            return "Erde, links-rechts, Süd"
        if item == '':
            return "Prinzip"
        if item == '3':
            return "LuftXXX, vorne-hinten, West"
        if item == '':
            return "Prinzip"
        if item == '4':
            return "Feuer, Spirale, Nord"
        if item == '':
            return "Prinzip"
        if item == '5':
            return "Mensch"
        if item == '':
            return "Prinzip"
        if item == 'h':
            return "Frühling"
        if item == '':
            return "Prinzip"
        if item == 'n':
            return "Sommer"
        if item == '':
            return "Prinzip"
        if item == 'a':
            return "Herbst"
        if item == '':
            return "Prinzip"
        if item == 'f':
            return "Winter"
        if item == '':
            return "Prinzip"
        if item == 'k':
            return "?"
        if item == '':
            return "Prinzip"
        if item == 'u':
            return "Prinzip des schlagens"
        if item == '':
            return "Prinzip"
        if item == 'o':
            return "?"
        if item == '':
            return "Prinzip"
        if item == 'g':
            return "Prinzip des Wurfes"
        if item == '':
            return "Prinzip"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "Wurf"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "festhalten"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "Wurf festhalten"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "empfangen mit dem Körper"
        if item == '1':
            return "?"
        if item == '':
            return "empfangen mit dem Körper"
        if item == '2':
            return "forwärts rollen"
        if item == '':
            return "empfangen mit dem Körper"
        if item == '3':
            return "nach Hinten rollen"
        if item == '':
            return "empfangen mit dem Körper"
        if item == '4':
            return "seitwärts ukemi vom links nach rechts(Prinzip der Spyrale)"
        if item == '':
            return "empfangen mit dem Körper"
        if item == 'c':
            return "?"
        if item == '':
            return "empfangen mit dem Körper"
        if item == '':
            return "empfangen mit dem Körper"
        if item == 't':
            return "freie Fall"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Person"
        if item == '1':
            return "ehemaliger Gründer von aikidô, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "Person"
        if item == '2':
            return "ehemaliger Sohn von ôsensei, zweite dôshu (27-06-1921 - 04-01-1999)"
        if item == '':
            return "Person"
        if item == '3':
            return "Enkelkind von ôsensei, dritte dôshu (02-04-1951)"
        if item == '':
            return "Person"
        if item == 't':
            return "Student von ôsensei, shihan (13-12-1929)"
        if item == '':
            return "Person"
        if item == 'i':
            return "Student von Tada sensei, shihan (08-04-1940)"
        if item == '':
            return "Person"
        if item == '':
            return "Person"
        if item == '':
            return "Person"
        if item == '':
            return "Person"
        if item == '':
            return "Person"
        if item == '':
            return "Person"
        if item == '':
            return "Person"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "zehlen"
        if item == '0':
            return "null, leer"
        if item == '':
            return "zehlen"
        if item == '1':
            return "eins"
        if item == '':
            return "zehlen"
        if item == '2':
            return "zwei"
        if item == '':
            return "zehlen"
        if item == '3':
            return "drei"
        if item == '':
            return "zehlen"
        if item == '4':
            return "vier"
        if item == '':
            return "zehlen"
        if item == '5':
            return "fünf"
        if item == '':
            return "zehlen"
        if item == '6':
            return "sechs"
        if item == '':
            return "zehlen"
        if item == '7':
            return "sieben"
        if item == '':
            return "zehlen"
        if item == '8':
            return "acht"
        if item == '':
            return "zehlen"
        if item == '9':
            return "neun"
        if item == '':
            return "zehlen"
        if item == 'a':
            return "zehn"
        if item == '':
            return "zehlen"
        if item == 'b':
            return "elf"
        if item == '':
            return "zehlen"
        if item == 'c':
            return "zwanzig"
        if item == '':
            return "zehlen"
        if item == 'd':
            return "einundzwanzig"
        if item == '':
            return "zehlen"
        if item == 'e':
            return "hundert"
        if item == '':
            return "zehlen"
        if item == 'f':
            return "tausent"
        if item == '':
            return "zehlen"
        if item == 'e':
            return "zehntausent"
        if item == '':
            return "zehlen"
        if item == 'h':
            return "erste Teil"
        if item == '':
            return "zehlen"
        if item == 'i':
            return "tweite Teil"
        if item == '':
            return "zehlen"
        if item == 'j':
            return "dritte Teil"
        if item == '':
            return "zehlen"
        if item == 'k':
            return "fierte Teil"
        if item == '':
            return "zehlen"
        if item == 'l':
            return "fünfte Teil"
        if item == '':
            return "zehlen"
        if item == 'm':
            return "zechste Teil"
        if item == '':
            return "zehlen"
        if item == 'n':
            return "siebenste Teil"
        if item == '':
            return "zehlen"
        if item == 'o':
            return "achtste Teil"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "Graden"
        if item == 'n':
            return "dan grad"
        if item == '':
            return "Graden"
        if item == 'k':
            return "kyû ?"
        if item == '':
            return "Graden"
        if item == '0':
            return "ohne kyû"
        if item == '':
            return "Graden"
        if item == '6':
            return "segste kyû"
        if item == '':
            return "Graden"
        if item == '5':
            return "fünfte kyû"
        if item == '':
            return "Graden"
        if item == '4':
            return "vierte kyû"
        if item == '':
            return "Graden"
        if item == '3':
            return "dritten kyû"
        if item == '':
            return "Graden"
        if item == '2':
            return "zweiter kyû"
        if item == '':
            return "Graden"
        if item == '1':
            return "erste kyû, Anfengerkyû"
        if item == '':
            return "Graden"
        if item == 'y':
            return "mit Dan"
        if item == '':
            return "Graden"
        if item == 'o':
            return "ohne Dan"
        if item == '':
            return "Graden"
        if item == 'a':
            return "erste Dan, Anfengerdan"
        if item == '':
            return "Graden"
        if item == 'b':
            return "zweiter Dan"
        if item == '':
            return "Graden"
        if item == 'c':
            return "dritten Dan"
        if item == '':
            return "Graden"
        if item == 'd':
            return "vierte Dan"
        if item == '':
            return "Graden"
        if item == 'e':
            return "funfte Dan"
        if item == '':
            return "Graden"
        if item == 'f':
            return "segste Dan"
        if item == '':
            return "Graden"
        if item == 'g':
            return "sieben Dan"
        if item == '':
            return "Graden"
        if item == 'h':
            return "achtste Dan"
        if item == '':
            return "Graden"
        if item == 'i':
            return "neunte Dan"
        if item == '':
            return "Graden"
        if item == 'j':
            return "zhente Dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Algemein"
        if item == '1':
            return "Harmonie, vereinend"
        if item == '':
            return "Algemein"
        if item == '2':
            return "Lebenskraft, Lebensenergie"
        if item == '':
            return "Algemein"
        if item == '3':
            return "Weg, ?, Disciplin"
        if item == '':
            return "Algemein"
        if item == '3':
            return "Weg des harmoniseren von Ki"
        if item == '':
            return "Algemein"
        if item == '4':
            return "Eingeweihter"
        if item == '':
            return "Algemein"
        if item == '5':
            return "Organisation fur die ubing und ? von aikidô"
        if item == '':
            return "Algemein"
        if item == '8':
            return "Angreifer [entfanger]"
        if item == '':
            return "Algemein"
        if item == '9':
            return "Verteitiger [?]"
        if item == '':
            return "Algemein"
        if item == 'n':
            return "?"
        if item == '':
            return "Algemein"
        if item == 'u':
            return "Elter, Lehrer [?]"
        if item == '':
            return "Algemein"
        if item == 's':
            return "Kind, Schuler [?]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Instruktionen"
        if item == '1':
            return "bitte (am Anfang vom Trainung oder einer Übung)"
        if item == '':
            return "Instruktionen"
        if item == '2':
            return "danke (am Ende vom Training oder einer Übung)"
        if item == '':
            return "Instruktionen"
        if item == '3':
            return "ja"
        if item == '':
            return "Instruktionen"
        if item == '':
            return "Instruktionen"
        if item == '5':
            return "halt (und setzt Euch auf die Seite)"
        if item == '':
            return "Instruktionen"
        if item == '6':
            return "fangt an, startet"
        if item == '':
            return "Instruktionen"
        if item == '6':
            return "wartet, stopt"
        if item == '':
            return "Instruktionen"
        if item == '8':
            return "steht auf"
        if item == '':
            return "Instruktionen"
        if item == '9':
            return "setz Euch"
        if item == '':
            return "Instruktionen"
        if item == 'a':
            return "dreht Euch"
        if item == '':
            return "Instruktionen"
        if item == 'b':
            return "Partnerwechseln"
        if item == '':
            return "Instruktionen"
        if item == 'c':
            return "wiederholt die Übung"
        if item == '':
            return "Instruktionen"
        if item == 'd':
            return "braucht die andere Seite"
        if item == '':
            return "Instruktionen"
        if item == 'e':
            return "finde einen anderen Partner"
        if item == '':
            return "Instruktionen"
        if item == 'f':
            return "grüssen [Respect]"
        if item == '':
            return "Instruktionen"
        if item == 'g':
            return "stehend grüssen"
        if item == '':
            return "Instruktionen"
        if item == 'h':
            return "sitzend grüssen"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Titels"
        if item == 's':
            return "Grossmeister Lehrer"
        if item == '':
            return "Titels"
        if item == 'o':
            return "Lehrer, Instructor"
        if item == '':
            return "Titels"
        if item == 'd':
            return "der jenige der den Weg weist"
        if item == '':
            return "Titels"
        if item == '7':
            return "Haubtinstruktor (minimal 6e dan)"
        if item == '':
            return "Titels"
        if item == '8':
            return "Instructor, shihan-in-Ausbildung (4e oder 5e dan)"
        if item == '':
            return "Titels"
        if item == '9':
            return "assistent Instructor (2e oder 3e dan)"
        if item == '':
            return "Titels"
        if item == 'a':
            return "jemands Senior"
        if item == '':
            return "Titels"
        if item == 'b':
            return "jemands Junior"
        if item == '':
            return "Titels"
        if item == 'c':
            return "Person ohne Grad"
        if item == '':
            return "Titels"
        if item == 'd':
            return "Person mit Grad"
        if item == '':
            return "Titels"
        if item == 'e':
            return "dôjô-Haubt"
        if item == '':
            return "Titels"
        if item == 'f':
            return "Student"
        if item == '':
            return "Titels"
        if item == 'g':
            return "im dôjô lebender Student"
        if item == '':
            return "Titels"
        if item == 'h':
            return "auserhald dem dôjô lebender Student"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Objecten"
        if item == '0':
            return "Trennungsraum (Platz von Erleuchtung) [buchstäblich Platz von dem Weg]"
        if item == '':
            return "Objecten"
        if item == '1':
            return "Altar mit Portret von ôsensei (eventuel mit Kalligrafie oder Blume)"
        if item == '':
            return "Objecten"
        if item == '2':
            return "?"
        if item == '':
            return "Objecten"
        if item == '3':
            return "?"
        if item == '':
            return "Objecten"
        if item == '4':
            return "?"
        if item == '':
            return "Objecten"
        if item == '5':
            return "Matte"
        if item == '':
            return "Objecten"
        if item == '6':
            return "Hauptkwartier"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "Kleider"
        if item == '1':
            return "?"
        if item == '':
            return "Kleider"
        if item == '2':
            return "Gürtel"
        if item == '':
            return "Kleider"
        if item == '3':
            return "Weißer Gürtel"
        if item == '':
            return "Kleider"
        if item == '4':
            return "Schwarzer Gürtel"
        if item == '':
            return "Kleider"
        if item == '5':
            return "Halbstrumpf mit aprte großes Zehe"
        if item == '':
            return "Kleider"
        if item == '6':
            return "Flipflops"
        if item == '':
            return "Kleider"
        if item == '7':
            return "traditionelle japanische Hose"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "Anatomie"
        if item == 'a':
            return "Zentrum"
        if item == '':
            return "Anatomie"
        if item == 'b':
            return "Körper"
        if item == '':
            return "Anatomie"
        if item == 'c':
            return "Stirne"
        if item == '':
            return "Anatomie"
        if item == 'd':
            return "Schläfe"
        if item == '':
            return "Anatomie"
        if item == 'e':
            return "Knie"
        if item == '':
            return "Anatomie"
        if item == 'f':
            return "Nacken"
        if item == '':
            return "Anatomie"
        if item == 'g':
            return "Brust"
        if item == '':
            return "Anatomie"
        if item == 'e':
            return "Schulter"
        if item == '':
            return "Anatomie"
        if item == 'h':
            return "Ellbogen"
        if item == '':
            return "Anatomie"
        if item == 'i':
            return "Arm"
        if item == '':
            return "Anatomie"
        if item == 'j':
            return "Handgelenk"
        if item == '':
            return "Anatomie"
        if item == 'k':
            return "Hand"
        if item == '':
            return "Anatomie"
        if item == 'k':
            return "Schwerthand"
        if item == '':
            return "Anatomie"
        if item == 'l':
            return "Bein, Fuß"
        if item == '':
            return "Anatomie"
        if item == 'm':
            return "Knöchel"
        if item == '':
            return "Anatomie"
        if item == 'n':
            return "Hüfte"
        if item == '':
            return "Anatomie"
        if item == 'o':
            return "Kragen"
        if item == '':
            return "Anatomie"
        if item == 'p':
            return "Körper"
        if item == '':
            return "Anatomie"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Diversen"
        if item == 'a':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'b':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'c':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'd':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'e':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'f':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'g':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'h':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'i':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'j':
            return "?"
        if item == '':
            return "Diversen"
        if item == 'm':
            return "?"
        if item == '':
            return "Diversen"
        if item == 's':
            return "?"
        if item == '':
            return "Diversen"
        if item == 't':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "Richtung"
        if item == 'h':
            return "links"
        if item == '':
            return "Richtung"
        if item == 'm':
            return "rechts"
        if item == '':
            return "Richtung"
        if item == 'i':
            return "eintreten"
        if item == '':
            return "Richtung"
        if item == 'k':
            return "wegdrehen"
        if item == '':
            return "Richtung"
        if item == '1':
            return "vorwärts"
        if item == '':
            return "Richtung"
        if item == '2':
            return "rückwärts"
        if item == '':
            return "Richtung"
        if item == '3':
            return "seitwärts"
        if item == '':
            return "Richtung"
        if item == 'a':
            return "innen, inwärts"
        if item == '':
            return "Richtung"
        if item == 'b':
            return "außen, außerwärts"
        if item == '':
            return "Richtung"
        if item == 'n':
            return "?"
        if item == '':
            return "Richtung"
        if item == 'c':
            return "Vetikal"
        if item == '':
            return "Richtung"
        if item == 's':
            return "Horizontal"
        if item == '':
            return "Richtung"
        if item == 't':
            return "?"
        if item == '':
            return "Richtung"
        if item == 'x':
            return "gegenuber"
        if item == '':
            return "Richtung"
        if item == '8':
            return "alle Richtungen [acht Richtungen]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "Übung"
        if item == '1':
            return "ikkyô Übung"
        if item == '':
            return "Übung"
        if item == '2':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "?"
        if item == '1':
            return "Früling Schwert"
        if item == '':
            return "?"
        if item == '2':
            return "Sommer Schwert"
        if item == '':
            return "?"
        if item == '3':
            return "Herbst Schwert"
        if item == '':
            return "?"
        if item == '4':
            return "Winter Schwert"
        if item == '':
            return "?"
        if item == '5':
            return "acht Directionen"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == '7':
            return "?"
        if item == '':
            return "?"
        if item == '8':
            return "Kurz und Lang sind eins"
        if item == '':
            return "?"
        if item == '9':
            return "entfangen"
        if item == '':
            return "?"
        if item == 'a':
            return "Körper Schwert"
        if item == '':
            return "?"
        if item == 'b':
            return "fracesco"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "fracesco"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        if item == '':
            return "?"
        if item == 'i':
            return "?"
        if item == '':
            return "?"
        if item == 'j':
            return "?"
        if item == '':
            return "?"
        if item == 'k':
            return "?"
        if item == '':
            return "?"
        if item == 'l':
            return "?"
        if item == '':
            return "?"
        if item == 'm':
            return "?"
        if item == '':
            return "?"
        if item == 'n':
            return "?"
        if item == '':
            return "?"
        if item == 'o':
            return "?"
        if item == '':
            return "?"
        if item == 'p':
            return "?"
        if item == '':
            return "?"
        if item == 'q':
            return "?"
        if item == '':
            return "?"
        if item == 'r':
            return "?"
        if item == '':
            return "?"
        if item == 's':
            return "?"
        if item == '':
            return "?"
        if item == 't':
            return "?"
        if item == '':
            return "?"
        if item == 'u':
            return "?"
        if item == '':
            return "?"
        if item == 'v':
            return "?"
        if item == '':
            return "?"
        if item == 'w':
            return "?"
        if item == '':
            return "?"
        if item == 'x':
            return "?"
        if item == '':
            return "?"
        if item == 'y':
            return "groß"
        if item == '':
            return "?"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '~':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '0':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '1':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '2':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '3':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '4':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '5':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == '6':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == 'a':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == 'b':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == 'c':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == 'd':
            return "?"
        if item == '':
            return "Gruppe der gesundheits Übungen"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'en':
    if list == 'ryu':
        if item == '':
            return "type"
        if item == 'a':
            return "way to harmonise ki"
        if item == '':
            return "type"
        if item == 'b':
            return "body techniques that utilise aiki principle"
        if item == '':
            return "type"
        if item == 'j':
            return "jô techniques which utilise aiki principle"
        if item == '':
            return "type"
        if item == 'k':
            return "ken techniques which utilise aiki principle"
        if item == '':
            return "type"
        if item == 'h':
            return "first kata of specific sword style"
        if item == '':
            return "type"
        if item == 'j':
            return "sword style"
        if item == '':
            return "type"
        if item == 'g':
            return "group of health exercises"
        if item == '':
            return "type"
        if item == 's':
            return "properly ordered body"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOspirit"
        if item == 'a':
            return "attack one by one [continuous excercise]"
        if item == '':
            return "TODOspirit"
        if item == 'k':
            return "fluent attacks, tori will not allow to be grabbed [energetic form]"
        if item == '':
            return "TODOspirit"
        if item == 't':
            return "disciplined training, tori will allow to be grabbed [disciplined]"
        if item == '':
            return "TODOspirit"
        if item == 's':
            return "realistic training [seriously]"
        if item == '':
            return "TODOspirit"
        if item == 'k':
            return "disturbance of balance"
        if item == '':
            return "TODOspirit"
        if item == 'j':
            return "techniques for attackes from the rear"
        if item == '':
            return "TODOspirit"
        if item == 'j':
            return "freeform technique"
        if item == '':
            return "TODOspirit"
        if item == 'r':
            return "techniques with multiple attackers"
        if item == '':
            return "TODOspirit"
        if item == 's':
            return "repeating exercise"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "position"
        if item == 's':
            return "sitting technique"
        if item == '':
            return "position"
        if item == 'h':
            return "technique with sitting tori and standing uke"
        if item == '':
            return "position"
        if item == 't':
            return "standing technique"
        if item == '':
            return "position"
        if item == '2':
            return "sitting"
        if item == '':
            return "position"
        if item == '3':
            return "sitting on knees, feet flat on floor"
        if item == '':
            return "position"
        if item == '4':
            return "sitting on knees with toes in mat"
        if item == '':
            return "position"
        if item == '5':
            return "sitting on knees and hips between feet on floor"
        if item == '':
            return "position"
        if item == '6':
            return "sitting with legs extended to front"
        if item == '':
            return "position"
        if item == '7':
            return "sitting with legs extended and openend"
        if item == '':
            return "position"
        if item == '8':
            return "sitting with knees against chest and feet on floor"
        if item == '':
            return "position"
        if item == '9':
            return "sitting with feet againt each other and knees on floor"
        if item == '':
            return "position"
        if item == '0':
            return "sitting with legs flat and bend on floor"
        if item == '':
            return "position"
        if item == 'j':
            return "posture like an eight [hassôgamae]"
        if item == '':
            return "position"
        if item == 'z':
            return "lotus position"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == 't':
            return "three or more uke which attack continuously, only do begin of technique"
        if item == '':
            return "partner"
        if item == 'k':
            return "two or more uke which attack in turns, end technique and directly go to next uke"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "weapon"
        if item == 'j':
            return "stick or short wooden staff"
        if item == '':
            return "weapon"
        if item == 'o':
            return "long wooden staff"
        if item == '':
            return "weapon"
        if item == 'b':
            return "curved wooden sword"
        if item == '':
            return "weapon"
        if item == 't':
            return "knive or dagger"
        if item == '':
            return "weapon"
        if item == 'w':
            return "curved metal short sword"
        if item == '':
            return "weapon"
        if item == 'k':
            return "curved metal sword"
        if item == '':
            return "weapon"
        if item == 'a':
            return "metal long sword"
        if item == '':
            return "weapon"
        if item == 'e':
            return "short straight metal twosided sword"
        if item == '':
            return "weapon"
        if item == 'n':
            return "Japanese sword"
        if item == '':
            return "weapon"
        if item == 'n':
            return "hellbeard"
        if item == '':
            return "weapon"
        if item == 'y':
            return "spear"
        if item == '':
            return "weapon"
        if item == 's':
            return "sword guard"
        if item == '':
            return "weapon"
        if item == 's':
            return "scabbard"
        if item == '':
            return "weapon"
        if item == 'u':
            return "rack of arms"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "attack"
        if item == 'a':
            return "strike with open hand from hips to front of head [direct hit on the head in energetical union]"
        if item == '':
            return "attack"
        if item == 'b':
            return "grab one wrist on same side (identical) [one-side-hand grab same side]"
        if item == '':
            return "attack"
        if item == 'c':
            return "grab one wrist on reverse side (mirror) [one-side-hand grab other side]"
        if item == '':
            return "attack"
        if item == 'd':
            return "grab both wrists [both-wrists take]"
        if item == '':
            return "attack"
        if item == 'e':
            return "strike to front of head [front-face hit]"
        if item == '':
            return "attack"
        if item == 'f':
            return "grab one wrist with both hands [one-side-hand both wrists grab]"
        if item == '':
            return "attack"
        if item == 'g':
            return "grab one shoulder"
        if item == '':
            return "attack"
        if item == 'h':
            return "grab both wrists from rear"
        if item == '':
            return "attack"
        if item == 'i':
            return "strike to side of head"
        if item == '':
            return "attack"
        if item == 'j':
            return "punch or stab to middle part body"
        if item == '':
            return "attack"
        if item == 'k':
            return "grab one shoulder and strike to fornt of head"
        if item == '':
            return "attack"
        if item == 'l':
            return "grab both shoulders from rear"
        if item == '':
            return "attack"
        if item == 'm':
            return "punch or stab to upper part body"
        if item == '':
            return "attack"
        if item == 'n':
            return "ssk newsletter 3XXX"
        if item == '':
            return "attack"
        if item == 'o':
            return "kick"
        if item == '':
            return "attack"
        if item == 'p':
            return "neck choke from rear"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "inside/outside"
        if item == 'u':
            return "movement to inside"
        if item == '':
            return "inside/outside"
        if item == 's':
            return "movement to outside"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "body movement"
        if item == 'a':
            return "enter with front foot"
        if item == '':
            return "body movement"
        if item == 'b':
            return "enter with rear foot"
        if item == '':
            return "body movement"
        if item == 'c':
            return "turn on front foot"
        if item == '':
            return "body movement"
        if item == 'd':
            return "turn on rear foot"
        if item == '':
            return "body movement"
        if item == 'e':
            return "evade with front foor"
        if item == '':
            return "body movement"
        if item == 'f':
            return "evade with rear foot"
        if item == '':
            return "body movement"
        if item == 'g':
            return "enter with front foor and turn on it"
        if item == '':
            return "body movement"
        if item == 'h':
            return "enter with rear foot and turn on it"
        if item == '':
            return "body movement"
        if item == 'i':
            return "enter with front foor, turn on it and evade"
        if item == '':
            return "body movement"
        if item == 'j':
            return "enter with rear foot, turn on it and evade"
        if item == '':
            return "body movement"
        if item == 'k':
            return "turn on fron foot and evade"
        if item == '':
            return "body movement"
        if item == 'l':
            return "turn on rear foot and evade"
        if item == '':
            return "body movement"
        if item == 'm':
            return "enter with front foor and then turn entire body on the spot"
        if item == '':
            return "body movement"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "hand movements"
        if item == 'k':
            return "half circle along above"
        if item == '':
            return "hand movements"
        if item == 's':
            return "circle along bottom"
        if item == '':
            return "hand movements"
        if item == 't':
            return "underarms parallel"
        if item == '':
            return "hand movements"
        if item == 'y':
            return "underarms crossed"
        if item == '':
            return "hand movements"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "hand"
        if item == 'u':
            return "striking hand"
        if item == '':
            return "hand"
        if item == 'k':
            return "hand at shoulder"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "height"
        if item == 'g':
            return "low"
        if item == '':
            return "height"
        if item == 'c':
            return "middle"
        if item == '':
            return "height"
        if item == 'j':
            return "high"
        if item == '':
            return "height"
        if item == '1':
            return "small stance"
        if item == '':
            return "height"
        if item == '2':
            return "low stance"
        if item == '':
            return "height"
        if item == '3':
            return "middle stance"
        if item == '':
            return "height"
        if item == '5':
            return "high stance"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "technique"
        if item == 'a':
            return "first teaching"
        if item == '':
            return "technique"
        if item == 'b':
            return "second teaching"
        if item == '':
            return "technique"
        if item == 'c':
            return "third teaching"
        if item == '':
            return "technique"
        if item == 'd':
            return "fourth teaching"
        if item == '':
            return "technique"
        if item == 'e':
            return "corner throw"
        if item == '':
            return "technique"
        if item == 'f':
            return "wrist twist"
        if item == '':
            return "technique"
        if item == 'g':
            return "entering throw"
        if item == '':
            return "technique"
        if item == 'h':
            return "four directions throw"
        if item == '':
            return "technique"
        if item == 'i':
            return "fifth teaching"
        if item == '':
            return "technique"
        if item == 'j':
            return "elbow control lock"
        if item == '':
            return "technique"
        if item == 'k':
            return "inwards turn sankyo"
        if item == '':
            return "technique"
        if item == 'l':
            return "arm entanglement"
        if item == '':
            return "technique"
        if item == 'm':
            return "aiki hip throw"
        if item == '':
            return "technique"
        if item == 'n':
            return "blending drop"
        if item == '':
            return "technique"
        if item == 'o':
            return "rotary throw"
        if item == '':
            return "technique"
        if item == 'p':
            return "arm break throw"
        if item == '':
            return "technique"
        if item == 'q':
            return "forward throw"
        if item == '':
            return "technique"
        if item == 'r':
            return "pulling throw"
        if item == '':
            return "technique"
        if item == 's':
            return "cutting throw"
        if item == '':
            return "technique"
        if item == 't':
            return "turn throw"
        if item == '':
            return "technique"
        if item == 'u':
            return "heaven earth throw"
        if item == '':
            return "technique"
        if item == 'v':
            return "profound form breath throw"
        if item == '':
            return "technique"
        if item == 'w':
            return "inwards turn throw"
        if item == '':
            return "technique"
        if item == 'x':
            return "swinging thrust breath throw"
        if item == '':
            return "technique"
        if item == 'y':
            return "cross knot entanglement"
        if item == '':
            return "technique"
        if item == 'z':
            return "rowing excercise breath throw"
        if item == '':
            return "technique"
        if item == '0':
            return "four directions kicking breath throw"
        if item == '':
            return "technique"
        if item == '1':
            return "arm entanglement sankyo throw"
        if item == '':
            return "technique"
        if item == '2':
            return "arm entanglement yonkyo throw"
        if item == '':
            return "technique"
        if item == '3':
            return "hip throw"
        if item == '':
            return "technique"
        if item == '4':
            return "outwards turn throw"
        if item == '':
            return "technique"
        if item == '5':
            return "cutting sword breath throw"
        if item == '':
            return "technique"
        if item == '6':
            return "arm entanglement control"
        if item == '':
            return "technique"
        if item == '7':
            return "hand wheel"
        if item == '':
            return "technique"
        if item == '8':
            return "shoulder wheel"
        if item == '':
            return "technique"
        if item == '9':
            return "hip wheel"
        if item == '':
            return "technique"
        if item == '~':
            return "sinking body hip wheel"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "front/back"
        if item == 'o':
            return "in front of partner"
        if item == '':
            return "front/back"
        if item == 'u':
            return "behind partner"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        if item == '':
            return "number"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "yin/yang"
        if item == '1':
            return "yin"
        if item == '':
            return "yin/yang"
        if item == '2':
            return "yang"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "principle"
        if item == '1':
            return "water, up-down, east"
        if item == '':
            return "principle"
        if item == '2':
            return "earth, left-right, south"
        if item == '':
            return "principle"
        if item == '3':
            return "wind, front-behind, west"
        if item == '':
            return "principle"
        if item == '4':
            return "fire, spiral, north"
        if item == '':
            return "principle"
        if item == '5':
            return "human"
        if item == '':
            return "principle"
        if item == 'h':
            return "spring"
        if item == '':
            return "principle"
        if item == 'n':
            return "summer"
        if item == '':
            return "principle"
        if item == 'a':
            return "autumn, fall"
        if item == '':
            return "principle"
        if item == 'f':
            return "winter"
        if item == '':
            return "principle"
        if item == 'k':
            return "theory of offense and defense"
        if item == '':
            return "principle"
        if item == 'u':
            return "hitting principle"
        if item == '':
            return "principle"
        if item == 'o':
            return "control principle"
        if item == '':
            return "principle"
        if item == 'g':
            return "throw principle"
        if item == '':
            return "principle"
        if item == 'z':
            return "cutting principle"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "throw"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "control"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "throw control"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "receive with the body"
        if item == '1':
            return "?"
        if item == '':
            return "receive with the body"
        if item == '2':
            return "?"
        if item == '':
            return "receive with the body"
        if item == '3':
            return "?"
        if item == '':
            return "receive with the body"
        if item == '4':
            return "?"
        if item == '':
            return "receive with the body"
        if item == 'c':
            return "?"
        if item == '':
            return "receive with the body"
        if item == '':
            return "receive with the body"
        if item == 't':
            return "free fall"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "person"
        if item == '1':
            return "late founder of aikidô, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "person"
        if item == '2':
            return "late son of ôsensei, second dôshu (27-06-1921 - 04-01-1999)"
        if item == '':
            return "person"
        if item == '3':
            return "grandson of ôsensei, third dôshu  (02-04-1951)"
        if item == '':
            return "person"
        if item == 't':
            return "student of ôsensei, shihan (13-12-1929)"
        if item == '':
            return "person"
        if item == 'i':
            return "student of Tada sensei, shihan (08-04-1940)"
        if item == '':
            return "person"
        if item == '':
            return "person"
        if item == '':
            return "person"
        if item == '':
            return "person"
        if item == '':
            return "person"
        if item == '':
            return "person"
        if item == '':
            return "person"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "counting"
        if item == '0':
            return "zero, empty"
        if item == '':
            return "counting"
        if item == '1':
            return "one"
        if item == '':
            return "counting"
        if item == '2':
            return "two"
        if item == '':
            return "counting"
        if item == '3':
            return "three"
        if item == '':
            return "counting"
        if item == '4':
            return "four"
        if item == '':
            return "counting"
        if item == '5':
            return "five"
        if item == '':
            return "counting"
        if item == '6':
            return "six"
        if item == '':
            return "counting"
        if item == '7':
            return "seven"
        if item == '':
            return "counting"
        if item == '8':
            return "eight"
        if item == '':
            return "counting"
        if item == '9':
            return "nine"
        if item == '':
            return "counting"
        if item == 'a':
            return "ten"
        if item == '':
            return "counting"
        if item == 'b':
            return "eleven"
        if item == '':
            return "counting"
        if item == 'c':
            return "twenty"
        if item == '':
            return "counting"
        if item == 'd':
            return "twenty one"
        if item == '':
            return "counting"
        if item == 'e':
            return "hunderd"
        if item == '':
            return "counting"
        if item == 'f':
            return "thousand"
        if item == '':
            return "counting"
        if item == 'e':
            return "ten thousand"
        if item == '':
            return "counting"
        if item == 'h':
            return "first stage"
        if item == '':
            return "counting"
        if item == 'i':
            return "second stage"
        if item == '':
            return "counting"
        if item == 'j':
            return "third stage"
        if item == '':
            return "counting"
        if item == 'k':
            return "fourth stage"
        if item == '':
            return "counting"
        if item == 'l':
            return "fifth stage"
        if item == '':
            return "counting"
        if item == 'm':
            return "sixth stage"
        if item == '':
            return "counting"
        if item == 'n':
            return "seventh stage"
        if item == '':
            return "counting"
        if item == 'o':
            return "eight stage"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "grades"
        if item == 'n':
            return "dan grade"
        if item == '':
            return "grades"
        if item == 'k':
            return "kyû grade (? rank/rang=dan, level/graad=kyu)"
        if item == '':
            return "grades"
        if item == '0':
            return "without kyû"
        if item == '':
            return "grades"
        if item == '6':
            return "sixth kyû"
        if item == '':
            return "grades"
        if item == '5':
            return "fifth kyû"
        if item == '':
            return "grades"
        if item == '4':
            return "fourth kyû"
        if item == '':
            return "grades"
        if item == '3':
            return "third kyû"
        if item == '':
            return "grades"
        if item == '2':
            return "second kyû"
        if item == '':
            return "grades"
        if item == '1':
            return "first kyû, beginner kyû"
        if item == '':
            return "grades"
        if item == 'y':
            return "with dan"
        if item == '':
            return "grades"
        if item == 'o':
            return "without dan"
        if item == '':
            return "grades"
        if item == 'a':
            return "first, beginner dan (starting rank?)"
        if item == '':
            return "grades"
        if item == 'b':
            return "second dan"
        if item == '':
            return "grades"
        if item == 'c':
            return "third dan"
        if item == '':
            return "grades"
        if item == 'd':
            return "fourth dan"
        if item == '':
            return "grades"
        if item == 'e':
            return "fifth dan"
        if item == '':
            return "grades"
        if item == 'f':
            return "sixth dan"
        if item == '':
            return "grades"
        if item == 'g':
            return "seventh dan"
        if item == '':
            return "grades"
        if item == 'h':
            return "eighth dan"
        if item == '':
            return "grades"
        if item == 'i':
            return "ninth dan"
        if item == '':
            return "grades"
        if item == 'j':
            return "tenth dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "general"
        if item == '1':
            return "harmony, unification"
        if item == '':
            return "general"
        if item == '2':
            return "life power, life energy"
        if item == '':
            return "general"
        if item == '3':
            return "Way, ?, discipline"
        if item == '':
            return "general"
        if item == '3':
            return "way to harmonise ki"
        if item == '':
            return "general"
        if item == '4':
            return "practitioner"
        if item == '':
            return "general"
        if item == '5':
            return "organisation for the practitioning and distribution of aikidô"
        if item == '':
            return "general"
        if item == '8':
            return "attacker [receiver]"
        if item == '':
            return "general"
        if item == '9':
            return "defender [to take, to pick up, to choose]"
        if item == '':
            return "general"
        if item == 'n':
            return "thrower"
        if item == '':
            return "general"
        if item == 'u':
            return "parent, teacher [striking sword]"
        if item == '':
            return "general"
        if item == 's':
            return "child, student [working sword]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "instructions"
        if item == '1':
            return "please (at begin of lesson or exercise)"
        if item == '':
            return "instructions"
        if item == '2':
            return "thank you (at the end of lesson or excercise)"
        if item == '':
            return "instructions"
        if item == '3':
            return "yes"
        if item == '':
            return "instructions"
        if item == '':
            return "instructions"
        if item == '5':
            return "stop (and go sit on the side)"
        if item == '':
            return "instructions"
        if item == '6':
            return "begin, start"
        if item == '':
            return "instructions"
        if item == '6':
            return "wait, stop"
        if item == '':
            return "instructions"
        if item == '8':
            return "stand up"
        if item == '':
            return "instructions"
        if item == '9':
            return "sit down"
        if item == '':
            return "instructions"
        if item == 'a':
            return "turn"
        if item == '':
            return "instructions"
        if item == 'b':
            return "change partner [person]"
        if item == '':
            return "instructions"
        if item == 'c':
            return "repeat the excercise"
        if item == '':
            return "instructions"
        if item == 'd':
            return "use te other side"
        if item == '':
            return "instructions"
        if item == 'e':
            return "find another partner"
        if item == '':
            return "instructions"
        if item == 'f':
            return "greet, bow [respect]"
        if item == '':
            return "instructions"
        if item == 'g':
            return "standing bow"
        if item == '':
            return "instructions"
        if item == 'h':
            return "sitting bow"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "titles"
        if item == 's':
            return "great teacher"
        if item == '':
            return "titles"
        if item == 'o':
            return "teacher, instructor"
        if item == '':
            return "titles"
        if item == 'd':
            return "the one pointing the way"
        if item == '':
            return "titles"
        if item == '7':
            return "head instructor (minimal 6th dan)"
        if item == '':
            return "titles"
        if item == '8':
            return "instructor, shihan-in-training (4th or 5th dan)"
        if item == '':
            return "titles"
        if item == '9':
            return "assistent instructor (2nd of 3rd dan)"
        if item == '':
            return "titles"
        if item == 'a':
            return "somebodies senior"
        if item == '':
            return "titles"
        if item == 'b':
            return "somebodies junior"
        if item == '':
            return "titles"
        if item == 'c':
            return "person without grade (no rank person?)"
        if item == '':
            return "titles"
        if item == 'd':
            return "person with grade"
        if item == '':
            return "titles"
        if item == 'e':
            return "head of dôjô"
        if item == '':
            return "titles"
        if item == 'f':
            return "student"
        if item == '':
            return "titles"
        if item == 'g':
            return "in dôjô living student, live-in student"
        if item == '':
            return "titles"
        if item == 'h':
            return "outsite dôjô living student"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "objects"
        if item == '0':
            return "traininghal (place of enlightenment) [place of the way]"
        if item == '':
            return "objects"
        if item == '1':
            return "shrine with portrait of ôsensei (optionally with calligraphy or flowers) [high side of the mat]"
        if item == '':
            return "objects"
        if item == '2':
            return "(low) backside of the mat"
        if item == '':
            return "objects"
        if item == '3':
            return "(high) right side of mat"
        if item == '':
            return "objects"
        if item == '4':
            return "(low) left side of mat"
        if item == '':
            return "objects"
        if item == '5':
            return "mats"
        if item == '':
            return "objects"
        if item == '6':
            return "headquarters"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "clothes"
        if item == '1':
            return "training suite"
        if item == '':
            return "clothes"
        if item == '2':
            return "belt"
        if item == '':
            return "clothes"
        if item == '3':
            return "white belt"
        if item == '':
            return "clothes"
        if item == '4':
            return "black belt"
        if item == '':
            return "clothes"
        if item == '5':
            return "kind of socks with separate big toe"
        if item == '':
            return "clothes"
        if item == '6':
            return "flip-flops"
        if item == '':
            return "clothes"
        if item == '7':
            return "traditional Japanese trouwsers"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "anathomy"
        if item == 'a':
            return "center, belly"
        if item == '':
            return "anathomy"
        if item == 'b':
            return "body"
        if item == '':
            return "anathomy"
        if item == 'c':
            return "front of head"
        if item == '':
            return "anathomy"
        if item == 'd':
            return "side of head"
        if item == '':
            return "anathomy"
        if item == 'e':
            return "knee"
        if item == '':
            return "anathomy"
        if item == 'f':
            return "neck"
        if item == '':
            return "anathomy"
        if item == 'g':
            return "chest"
        if item == '':
            return "anathomy"
        if item == 'e':
            return "shoulder"
        if item == '':
            return "anathomy"
        if item == 'h':
            return "elbow"
        if item == '':
            return "anathomy"
        if item == 'i':
            return "arm"
        if item == '':
            return "anathomy"
        if item == 'j':
            return "wrist"
        if item == '':
            return "anathomy"
        if item == 'k':
            return "hand"
        if item == '':
            return "anathomy"
        if item == 'k':
            return "hand sword"
        if item == '':
            return "anathomy"
        if item == 'l':
            return "leg, foot"
        if item == '':
            return "anathomy"
        if item == 'm':
            return "ankle"
        if item == '':
            return "anathomy"
        if item == 'n':
            return "hips, lower back"
        if item == '':
            return "anathomy"
        if item == 'o':
            return "collar"
        if item == '':
            return "anathomy"
        if item == 'p':
            return "body"
        if item == '':
            return "anathomy"
        if item == 's':
            return "sleeve"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "miscellanious"
        if item == 'a':
            return "mutual escape"
        if item == '':
            return "miscellanious"
        if item == 'b':
            return "mutual kill"
        if item == '':
            return "miscellanious"
        if item == 'c':
            return "striking/hitting the body"
        if item == '':
            return "miscellanious"
        if item == 'd':
            return "martial way"
        if item == '':
            return "miscellanious"
        if item == 'e':
            return "staff partnership practice"
        if item == '':
            return "miscellanious"
        if item == 'f':
            return "sword partnership practice"
        if item == '':
            return "miscellanious"
        if item == 'g':
            return "sword takeaways"
        if item == '':
            return "miscellanious"
        if item == 'h':
            return "knive takeaways"
        if item == '':
            return "miscellanious"
        if item == 'i':
            return "pointing at the eye"
        if item == '':
            return "miscellanious"
        if item == 'j':
            return "stance"
        if item == '':
            return "miscellanious"
        if item == 'm':
            return "proper dynamic distance [interval]"
        if item == '':
            return "miscellanious"
        if item == 's':
            return "walking on knees"
        if item == '':
            return "miscellanious"
        if item == 't':
            return "Japanese drum signalling beginning and end of training"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "direction"
        if item == 'h':
            return "left"
        if item == '':
            return "direction"
        if item == 'm':
            return "right"
        if item == '':
            return "direction"
        if item == 'i':
            return "entering"
        if item == '':
            return "direction"
        if item == 'k':
            return "turning"
        if item == '':
            return "direction"
        if item == '1':
            return "from, to the front"
        if item == '':
            return "direction"
        if item == '2':
            return "from, to the rear"
        if item == '':
            return "direction"
        if item == '3':
            return "sideways"
        if item == '':
            return "direction"
        if item == 'a':
            return "inside, inwards"
        if item == '':
            return "direction"
        if item == 'b':
            return "outside, outwards"
        if item == '':
            return "direction"
        if item == 'n':
            return "diagonal"
        if item == '':
            return "direction"
        if item == 'c':
            return "vertical"
        if item == '':
            return "direction"
        if item == 's':
            return "horizontal"
        if item == '':
            return "direction"
        if item == 't':
            return "standing"
        if item == '':
            return "direction"
        if item == 'x':
            return "opposite, against"
        if item == '':
            return "direction"
        if item == '8':
            return "all directions [eight directions]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "exercise"
        if item == '1':
            return "ikkyô exercise"
        if item == '':
            return "exercise"
        if item == '2':
            return "basic body blend"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "fundamental principles"
        if item == '1':
            return "spring sword"
        if item == '':
            return "fundamental principles"
        if item == '2':
            return "summer sword"
        if item == '':
            return "fundamental principles"
        if item == '3':
            return "autumn sword"
        if item == '':
            return "fundamental principles"
        if item == '4':
            return "winter sword"
        if item == '':
            return "fundamental principles"
        if item == '5':
            return "eight directions"
        if item == '':
            return "fundamental principles"
        if item == '6':
            return "cutting your ego"
        if item == '':
            return "fundamental principles"
        if item == '7':
            return "times of change"
        if item == '':
            return "fundamental principles"
        if item == '8':
            return "long and short are one"
        if item == '':
            return "fundamental principles"
        if item == '9':
            return "to receive"
        if item == '':
            return "fundamental principles"
        if item == 'a':
            return "body sword"
        if item == '':
            return "fundamental principles"
        if item == 'b':
            return "nodding bow without breaking eye contact or speaking"
        if item == '':
            return "fundamental principles"
        if item == 'c':
            return "drawing one's sword"
        if item == '':
            return "fundamental principles"
        if item == 'd':
            return "harmoniously pointing at the eye"
        if item == '':
            return "fundamental principles"
        if item == 'e':
            return "to quicken, to urge"
        if item == '':
            return "fundamental principles"
        if item == 'g':
            return "temple-guardian sword"
        if item == '':
            return "fundamental principles"
        if item == 'h':
            return "shade"
        if item == '':
            return "fundamental principles"
        if item == 'i':
            return "harmonious jôdan"
        if item == '':
            return "fundamental principles"
        if item == 'j':
            return "?"
        if item == '':
            return "fundamental principles"
        if item == 'k':
            return "repetitive practise [inside uncountable]"
        if item == '':
            return "fundamental principles"
        if item == 'l':
            return "both arms"
        if item == '':
            return "fundamental principles"
        if item == 'm':
            return "push practise"
        if item == '':
            return "fundamental principles"
        if item == 'n':
            return "straight line"
        if item == '':
            return "fundamental principles"
        if item == 'o':
            return "block body"
        if item == '':
            return "fundamental principles"
        if item == 'p':
            return "bodycheck [body hit]"
        if item == '':
            return "fundamental principles"
        if item == 'q':
            return "not hitting"
        if item == '':
            return "fundamental principles"
        if item == 'r':
            return "temple [mist]"
        if item == '':
            return "fundamental principles"
        if item == 's':
            return "body turned sideways to opponent"
        if item == '':
            return "fundamental principles"
        if item == 't':
            return "to face, to turn head"
        if item == '':
            return "fundamental principles"
        if item == 'u':
            return "to cut"
        if item == '':
            return "fundamental principles"
        if item == 'v':
            return "to stop"
        if item == '':
            return "fundamental principles"
        if item == 'w':
            return "back hitting"
        if item == '':
            return "fundamental principles"
        if item == 'x':
            return "dawn, daybreak"
        if item == '':
            return "fundamental principles"
        if item == 'y':
            return "big"
        if item == '':
            return "fundamental principles"
        if item == 'z':
            return "to put away"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "group of health exercises"
        if item == '~':
            return "respiration in big circles [big circle breathing exercises]"
        if item == '':
            return "group of health exercises"
        if item == '0':
            return "?"
        if item == '':
            return "group of health exercises"
        if item == '1':
            return "respiration with hands in yang [yang of hands breathing]"
        if item == '':
            return "group of health exercises"
        if item == '2':
            return "respiration with hands in ying [yin of hands breathing]"
        if item == '':
            return "group of health exercises"
        if item == '3':
            return "respiration of the energy of hands drawing a cross [energy mixing with hands breathing]"
        if item == '':
            return "group of health exercises"
        if item == '4':
            return "respiration 'to become one with universe' [aum breathing]"
        if item == '':
            return "group of health exercises"
        if item == '5':
            return "?"
        if item == '':
            return "group of health exercises"
        if item == '6':
            return "lying exercises"
        if item == '':
            return "group of health exercises"
        if item == 'a':
            return "oscillation method"
        if item == '':
            return "group of health exercises"
        if item == 'b':
            return "?"
        if item == '':
            return "group of health exercises"
        if item == 'c':
            return "?"
        if item == '':
            return "group of health exercises"
        if item == 'd':
            return "goldfish excercise"
        if item == '':
            return "group of health exercises"
        if item == 'u':
            return "horse exerecise"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'fr':
    if list == 'ryu':
        if item == '':
            return "type"
        if item == 'a':
            return "la voie d`harmoniser le ki"
        if item == '':
            return "type"
        if item == 'b':
            return "technique de crops avec utilisation des principies aiki"
        if item == '':
            return "type"
        if item == 'j':
            return "technique de jo avec utilisation des principies aiki"
        if item == '':
            return "type"
        if item == 'k':
            return "technique de ken avec utilisation des principies aiki"
        if item == '':
            return "type"
        if item == 'h':
            return "le stile du sarbre"
        if item == '':
            return "type"
        if item == 'j':
            return "le stile du sarbre"
        if item == '':
            return "type"
        if item == 'g':
            return "le group d`excercis de la santé"
        if item == '':
            return "type"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOesprit"
        if item == 'a':
            return "attaquer un après l`autre [excercices continuell]"
        if item == '':
            return "TODOesprit"
        if item == 'k':
            return "form courrent, tori ne se fait pas tenir [form energetique]"
        if item == '':
            return "TODOesprit"
        if item == 't':
            return "entrainement discipliné, tori se fait tenir [discipliné]"
        if item == '':
            return "TODOesprit"
        if item == 's':
            return "entrainement realistique [serieux]"
        if item == '':
            return "TODOesprit"
        if item == 'k':
            return "detruire la balance"
        if item == '':
            return "TODOesprit"
        if item == 'j':
            return "technique ou on attaque de derrier"
        if item == '':
            return "TODOesprit"
        if item == 'j':
            return "techniques libre"
        if item == '':
            return "TODOesprit"
        if item == 'r':
            return "technique avec multiples attacquants"
        if item == '':
            return "TODOesprit"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "position"
        if item == 's':
            return "tecnicque assise"
        if item == '':
            return "position"
        if item == 'h':
            return "tecnicque pour uke assis et tori de bout"
        if item == '':
            return "position"
        if item == 't':
            return "tecnique de boue"
        if item == '':
            return "position"
        if item == '2':
            return "assis"
        if item == '':
            return "position"
        if item == '3':
            return "assis par terre sur les genouilles avec le pied aus solle"
        if item == '':
            return "position"
        if item == '4':
            return "asiss sur le genouilles avec le point du pied sur le solle"
        if item == '':
            return "position"
        if item == '5':
            return "assis sur les genouilles avec les hanches entre le pied"
        if item == '':
            return "position"
        if item == '6':
            return "assis acec les jambes allongé"
        if item == '':
            return "position"
        if item == '7':
            return "assis acec les jambes allongé et ouvertes"
        if item == '':
            return "position"
        if item == '8':
            return "assis avec les genouilles contre la poitrine et les pieds sur le solle"
        if item == '':
            return "position"
        if item == '9':
            return "?"
        if item == '':
            return "position"
        if item == '0':
            return "assis en lotus sans croiser les jambes"
        if item == '':
            return "position"
        if item == 'j':
            return "position comme une 8 [hassôgamae]"
        if item == '':
            return "position"
        if item == 'z':
            return "position lotus"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == '':
            return "partener"
        if item == 't':
            return "trois oû plus uke qui attaques  continuellesment,seullement le commençement de la tecnique"
        if item == '':
            return "partener"
        if item == 'k':
            return "deux oû plus uke qui attaques un après l`autrse"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "armes"
        if item == 'j':
            return "batton"
        if item == '':
            return "armes"
        if item == 'o':
            return "long batton de bois"
        if item == '':
            return "armes"
        if item == 'b':
            return "?"
        if item == '':
            return "armes"
        if item == 't':
            return "couteau"
        if item == '':
            return "armes"
        if item == 'w':
            return "sarbre court de metal"
        if item == '':
            return "armes"
        if item == 'k':
            return "sarbre courbe de metal"
        if item == '':
            return "armes"
        if item == 'a':
            return "sarbre long de metal"
        if item == '':
            return "armes"
        if item == 'e':
            return "court sabre de metall a deux coupes"
        if item == '':
            return "armes"
        if item == 'n':
            return "sarbre japponais"
        if item == '':
            return "armes"
        if item == 'n':
            return "?"
        if item == '':
            return "armes"
        if item == 'y':
            return "javelot"
        if item == '':
            return "armes"
        if item == 's':
            return "?"
        if item == '':
            return "armes"
        if item == 's':
            return "?"
        if item == '':
            return "armes"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "attaque"
        if item == 'a':
            return "frappe avec la main ouverte de l`hanche a la tête"
        if item == '':
            return "attaque"
        if item == 'b':
            return "une main tiens le même poignet de l`attaquantes (identique) [une main tiens le même poignet de l`attaquantes (identique)]"
        if item == '':
            return "attaque"
        if item == 'c':
            return "une main tiens le poignet contraire de l`attaquantes (mirroir) [une main tiens le poignet contraire de l`attaquantes (mirroir)]"
        if item == '':
            return "attaque"
        if item == 'd':
            return "tenir les deux poignet [tenir les deux poignet]"
        if item == '':
            return "attaque"
        if item == 'e':
            return "? [?]"
        if item == '':
            return "attaque"
        if item == 'f':
            return "?"
        if item == '':
            return "attaque"
        if item == 'g':
            return "tenir l`èpaule"
        if item == '':
            return "attaque"
        if item == 'h':
            return "tenir les poignets de derrière"
        if item == '':
            return "attaque"
        if item == 'i':
            return "frapper contre les tempes"
        if item == '':
            return "attaque"
        if item == 'j':
            return "coup contre le centre du corps"
        if item == '':
            return "attaque"
        if item == 'k':
            return "tenir l`epaule e frapper contre la tête"
        if item == '':
            return "attaque"
        if item == 'l':
            return "tenir les épaules de derrière"
        if item == '':
            return "attaque"
        if item == 'm':
            return "coup contre le haut du corps"
        if item == '':
            return "attaque"
        if item == 'n':
            return "tenir le collet"
        if item == '':
            return "attaque"
        if item == 'o':
            return "coup de piedetrangler de drrière"
        if item == '':
            return "attaque"
        if item == 'p':
            return "etrangler de derrière"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "intérieur/extérieur"
        if item == 'u':
            return "mouvement à l`intérieur"
        if item == '':
            return "intérieur/extérieur"
        if item == 's':
            return "mouvement à l`extérieur"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "mouvement du corps"
        if item == 'a':
            return "entrer avec le pied avant"
        if item == '':
            return "mouvement du corps"
        if item == 'b':
            return "entrer avec le pied arriére"
        if item == '':
            return "mouvement du corps"
        if item == 'c':
            return "turner sur le pied avant"
        if item == '':
            return "mouvement du corps"
        if item == 'd':
            return "turner sur le pied arriére"
        if item == '':
            return "mouvement du corps"
        if item == 'e':
            return "éviter avec le pied devant"
        if item == '':
            return "mouvement du corps"
        if item == 'f':
            return "éviter avec le pied arriére"
        if item == '':
            return "mouvement du corps"
        if item == 'g':
            return "entrer avec le pied avant avec tournement"
        if item == '':
            return "mouvement du corps"
        if item == 'h':
            return "entrer avec le pied arrière avec tournement"
        if item == '':
            return "mouvement du corps"
        if item == 'i':
            return "entrer avec le pied avant,turner et éviter"
        if item == '':
            return "mouvement du corps"
        if item == 'j':
            return "entrer avec le pied arriére,turner et éviter"
        if item == '':
            return "mouvement du corps"
        if item == 'k':
            return "turner sur le pied avant et éviter"
        if item == '':
            return "mouvement du corps"
        if item == 'l':
            return "turner sur le pied arriére et éviter"
        if item == '':
            return "mouvement du corps"
        if item == 'm':
            return "entrer avec le pied arriére avec tournement"
        if item == '':
            return "mouvement du corps"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "movement des mains"
        if item == 'k':
            return "demicercle vers le haut"
        if item == '':
            return "movement des mains"
        if item == 's':
            return "demicercle vers le bas"
        if item == '':
            return "movement des mains"
        if item == 't':
            return "?"
        if item == '':
            return "movement des mains"
        if item == 'y':
            return "?"
        if item == '':
            return "movement des mains"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "main"
        if item == 'u':
            return "main qui frappe"
        if item == '':
            return "main"
        if item == 'k':
            return "main sur l`épaule"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "hauteur"
        if item == 'g':
            return "loungeur"
        if item == '':
            return "hauteur"
        if item == 'c':
            return "?"
        if item == '':
            return "hauteur"
        if item == 'j':
            return "haut"
        if item == '':
            return "hauteur"
        if item == '1':
            return "tenue étroit"
        if item == '':
            return "hauteur"
        if item == '2':
            return "tenue bas"
        if item == '':
            return "hauteur"
        if item == '3':
            return "tenue moyenne"
        if item == '':
            return "hauteur"
        if item == '5':
            return "tenue haute"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "technique"
        if item == 'a':
            return "premier leçon"
        if item == '':
            return "technique"
        if item == 'b':
            return "second leçon"
        if item == '':
            return "technique"
        if item == 'c':
            return "troisiemme leçon"
        if item == '':
            return "technique"
        if item == 'd':
            return "quatriemme leçon"
        if item == '':
            return "technique"
        if item == 'e':
            return "cinquiemme leçon"
        if item == '':
            return "technique"
        if item == 'f':
            return "tournement de poignet"
        if item == '':
            return "technique"
        if item == 'g':
            return "?"
        if item == '':
            return "technique"
        if item == 'h':
            return "couper en quattre direction"
        if item == '':
            return "technique"
        if item == 'i':
            return "cinquiemme leçon"
        if item == '':
            return "technique"
        if item == 'j':
            return "bloquage controlle du coude"
        if item == '':
            return "technique"
        if item == 'k':
            return "?"
        if item == '':
            return "technique"
        if item == 'l':
            return "?"
        if item == '':
            return "technique"
        if item == 'm':
            return "?"
        if item == '':
            return "technique"
        if item == 'n':
            return "?"
        if item == '':
            return "technique"
        if item == 'o':
            return "?"
        if item == '':
            return "technique"
        if item == 'p':
            return "?"
        if item == '':
            return "technique"
        if item == 'q':
            return "?"
        if item == '':
            return "technique"
        if item == 'r':
            return "?"
        if item == '':
            return "technique"
        if item == 's':
            return "lancer avec coup"
        if item == '':
            return "technique"
        if item == 't':
            return "?"
        if item == '':
            return "technique"
        if item == 'u':
            return "?"
        if item == '':
            return "technique"
        if item == 'v':
            return "?"
        if item == '':
            return "technique"
        if item == 'w':
            return "?"
        if item == '':
            return "technique"
        if item == 'x':
            return "?"
        if item == '':
            return "technique"
        if item == 'y':
            return "?"
        if item == '':
            return "technique"
        if item == 'z':
            return "?"
        if item == '':
            return "technique"
        if item == '0':
            return "?"
        if item == '':
            return "technique"
        if item == '1':
            return "?"
        if item == '':
            return "technique"
        if item == '2':
            return "?"
        if item == '':
            return "technique"
        if item == '3':
            return "?"
        if item == '':
            return "technique"
        if item == '4':
            return "?"
        if item == '':
            return "technique"
        if item == '5':
            return "?"
        if item == '':
            return "technique"
        if item == '6':
            return "?"
        if item == '':
            return "technique"
        if item == '7':
            return "?"
        if item == '':
            return "technique"
        if item == '8':
            return "?"
        if item == '':
            return "technique"
        if item == '9':
            return "?"
        if item == '':
            return "technique"
        if item == '~':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "?"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "yin/yang"
        if item == '1':
            return "yin"
        if item == '':
            return "yin/yang"
        if item == '2':
            return "yang"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "principe"
        if item == '1':
            return "eau, haut-bas, est"
        if item == '':
            return "principe"
        if item == '2':
            return "terre, gauche-droit, sud"
        if item == '':
            return "principe"
        if item == '3':
            return "vent, XXX, ouest"
        if item == '':
            return "principe"
        if item == '4':
            return "Feu, XXX, nord"
        if item == '':
            return "principe"
        if item == '5':
            return "homme"
        if item == '':
            return "principe"
        if item == 'h':
            return "printemps"
        if item == '':
            return "principe"
        if item == 'n':
            return "ete"
        if item == '':
            return "principe"
        if item == 'a':
            return "autumn"
        if item == '':
            return "principe"
        if item == 'f':
            return "hiver"
        if item == '':
            return "principe"
        if item == 'k':
            return "?"
        if item == '':
            return "principe"
        if item == 'u':
            return "princip de frappes"
        if item == '':
            return "principe"
        if item == 'o':
            return "pricip d`immobilation"
        if item == '':
            return "principe"
        if item == 'g':
            return "princip du lancement"
        if item == '':
            return "principe"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "?"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "immobiliser"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "? ? immobiliser"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "recevoir avec le corp"
        if item == '1':
            return "?"
        if item == '':
            return "recevoir avec le corp"
        if item == '2':
            return "rouler en avant"
        if item == '':
            return "recevoir avec le corp"
        if item == '3':
            return "rouler en arrière"
        if item == '':
            return "recevoir avec le corp"
        if item == '4':
            return "ukemi sur le côte de la  droite à la gauche (avec le princip de la spyralle)"
        if item == '':
            return "recevoir avec le corp"
        if item == 'c':
            return "?"
        if item == '':
            return "recevoir avec le corp"
        if item == '':
            return "recevoir avec le corp"
        if item == 't':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "personne"
        if item == '1':
            return "ancien fondateur de l`aikidô, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "personne"
        if item == '2':
            return "ancien fils de ôsensei, second dôshu (27-06-1921 - 04-01-1999)"
        if item == '':
            return "personne"
        if item == '3':
            return "petit-enfant de ôsensei, troisiemme dôshu"
        if item == '':
            return "personne"
        if item == 't':
            return "étudiant de ôsensei, shihan (13-12-1929)"
        if item == '':
            return "personne"
        if item == 'i':
            return "étudiant de Tada sensei, shihan (08-04-1940)"
        if item == '':
            return "personne"
        if item == '':
            return "personne"
        if item == '':
            return "personne"
        if item == '':
            return "personne"
        if item == '':
            return "personne"
        if item == '':
            return "personne"
        if item == '':
            return "personne"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "conter"
        if item == '0':
            return "zero,vide"
        if item == '':
            return "conter"
        if item == '1':
            return "un"
        if item == '':
            return "conter"
        if item == '2':
            return "deux"
        if item == '':
            return "conter"
        if item == '3':
            return "trois"
        if item == '':
            return "conter"
        if item == '4':
            return "quattre"
        if item == '':
            return "conter"
        if item == '5':
            return "cinq"
        if item == '':
            return "conter"
        if item == '6':
            return "six"
        if item == '':
            return "conter"
        if item == '7':
            return "sept"
        if item == '':
            return "conter"
        if item == '8':
            return "houit"
        if item == '':
            return "conter"
        if item == '9':
            return "neuf"
        if item == '':
            return "conter"
        if item == 'a':
            return "dix"
        if item == '':
            return "conter"
        if item == 'b':
            return "onze"
        if item == '':
            return "conter"
        if item == 'c':
            return "vingt"
        if item == '':
            return "conter"
        if item == 'd':
            return "vingt-et-un"
        if item == '':
            return "conter"
        if item == 'e':
            return "cent"
        if item == '':
            return "conter"
        if item == 'f':
            return "mille"
        if item == '':
            return "conter"
        if item == 'e':
            return "dix-mille"
        if item == '':
            return "conter"
        if item == 'h':
            return "première ?forme"
        if item == '':
            return "conter"
        if item == 'i':
            return "seconde ?forme"
        if item == '':
            return "conter"
        if item == 'j':
            return "troisiemme ?forme"
        if item == '':
            return "conter"
        if item == 'k':
            return "quattrieme ?forme"
        if item == '':
            return "conter"
        if item == 'l':
            return "cinquieme ?forme"
        if item == '':
            return "conter"
        if item == 'm':
            return "sixieme ?forme"
        if item == '':
            return "conter"
        if item == 'n':
            return "septieme ?forme"
        if item == '':
            return "conter"
        if item == 'o':
            return "huitieme ?forme"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "grades"
        if item == 'n':
            return "grades dan"
        if item == '':
            return "grades"
        if item == 'k':
            return "kyû grade"
        if item == '':
            return "grades"
        if item == '0':
            return "sans kyû"
        if item == '':
            return "grades"
        if item == '6':
            return "sixieme kyû"
        if item == '':
            return "grades"
        if item == '5':
            return "cinquieme kyû"
        if item == '':
            return "grades"
        if item == '4':
            return "qutrieme kyû"
        if item == '':
            return "grades"
        if item == '3':
            return "troisieme kyû"
        if item == '':
            return "grades"
        if item == '2':
            return "second kyû"
        if item == '':
            return "grades"
        if item == '1':
            return "premier kyû"
        if item == '':
            return "grades"
        if item == 'y':
            return "avec dan"
        if item == '':
            return "grades"
        if item == 'o':
            return "sans dan"
        if item == '':
            return "grades"
        if item == 'a':
            return "premier dan"
        if item == '':
            return "grades"
        if item == 'b':
            return "deuxième dan"
        if item == '':
            return "grades"
        if item == 'c':
            return "troisieme dan"
        if item == '':
            return "grades"
        if item == 'd':
            return "quatrieme dan"
        if item == '':
            return "grades"
        if item == 'e':
            return "cinquieme dan"
        if item == '':
            return "grades"
        if item == 'f':
            return "sixieme dan"
        if item == '':
            return "grades"
        if item == 'g':
            return "septeme dan"
        if item == '':
            return "grades"
        if item == 'h':
            return "huitieme dan"
        if item == '':
            return "grades"
        if item == 'i':
            return "neufieme dan"
        if item == '':
            return "grades"
        if item == 'j':
            return "dixieme dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "généralement"
        if item == '1':
            return "harmonieux, unificant"
        if item == '':
            return "généralement"
        if item == '2':
            return "force de vis"
        if item == '':
            return "généralement"
        if item == '3':
            return "chemin"
        if item == '':
            return "généralement"
        if item == '3':
            return "moyen pour harmoniser le ki"
        if item == '':
            return "généralement"
        if item == '4':
            return "initié"
        if item == '':
            return "généralement"
        if item == '5':
            return "?"
        if item == '':
            return "généralement"
        if item == '8':
            return "?"
        if item == '':
            return "généralement"
        if item == '9':
            return "? [fracesco]"
        if item == '':
            return "généralement"
        if item == 'n':
            return "?"
        if item == '':
            return "généralement"
        if item == 'u':
            return "? [fracesco]"
        if item == '':
            return "généralement"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        if item == '':
            return "?"
        if item == '3':
            return "?"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == '8':
            return "?"
        if item == '':
            return "?"
        if item == '9':
            return "?"
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'f':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "?"
        if item == '':
            return "?"
        if item == 'o':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == '7':
            return "?"
        if item == '':
            return "?"
        if item == '8':
            return "?"
        if item == '':
            return "?"
        if item == '9':
            return "?"
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'f':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "?"
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        if item == '':
            return "?"
        if item == '3':
            return "?"
        if item == '':
            return "?"
        if item == '4':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        if item == '':
            return "?"
        if item == '3':
            return "?"
        if item == '':
            return "?"
        if item == '4':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == '7':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'f':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        if item == '':
            return "?"
        if item == 'i':
            return "?"
        if item == '':
            return "?"
        if item == 'j':
            return "?"
        if item == '':
            return "?"
        if item == 'k':
            return "?"
        if item == '':
            return "?"
        if item == 'k':
            return "?"
        if item == '':
            return "?"
        if item == 'l':
            return "?"
        if item == '':
            return "?"
        if item == 'm':
            return "?"
        if item == '':
            return "?"
        if item == 'n':
            return "?"
        if item == '':
            return "?"
        if item == 'o':
            return "?"
        if item == '':
            return "?"
        if item == 'p':
            return "?"
        if item == '':
            return "?"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'f':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        if item == '':
            return "?"
        if item == 'i':
            return "?"
        if item == '':
            return "?"
        if item == 'j':
            return "?"
        if item == '':
            return "?"
        if item == 'm':
            return "?"
        if item == '':
            return "?"
        if item == 's':
            return "?"
        if item == '':
            return "?"
        if item == 't':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        if item == '':
            return "?"
        if item == 'm':
            return "?"
        if item == '':
            return "?"
        if item == 'i':
            return "?"
        if item == '':
            return "?"
        if item == 'k':
            return "?"
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        if item == '':
            return "?"
        if item == '3':
            return "?"
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'n':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 's':
            return "?"
        if item == '':
            return "?"
        if item == 't':
            return "?"
        if item == '':
            return "?"
        if item == 'x':
            return "?"
        if item == '':
            return "?"
        if item == '8':
            return "tout directions [huit directions]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "exercise"
        if item == '1':
            return "?"
        if item == '':
            return "exercise"
        if item == '2':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        if item == '':
            return "?"
        if item == '3':
            return "?"
        if item == '':
            return "?"
        if item == '4':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == '7':
            return "?"
        if item == '':
            return "?"
        if item == '8':
            return "?"
        if item == '':
            return "?"
        if item == '9':
            return "?"
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        if item == '':
            return "?"
        if item == 'i':
            return "?"
        if item == '':
            return "?"
        if item == 'j':
            return "?"
        if item == '':
            return "?"
        if item == 'k':
            return "?"
        if item == '':
            return "?"
        if item == 'l':
            return "?"
        if item == '':
            return "?"
        if item == 'm':
            return "?"
        if item == '':
            return "?"
        if item == 'n':
            return "?"
        if item == '':
            return "?"
        if item == 'o':
            return "?"
        if item == '':
            return "?"
        if item == 'p':
            return "?"
        if item == '':
            return "?"
        if item == 'q':
            return "?"
        if item == '':
            return "?"
        if item == 'r':
            return "?"
        if item == '':
            return "?"
        if item == 's':
            return "?"
        if item == '':
            return "?"
        if item == 't':
            return "?"
        if item == '':
            return "?"
        if item == 'u':
            return "?"
        if item == '':
            return "?"
        if item == 'v':
            return "?"
        if item == '':
            return "?"
        if item == 'w':
            return "?"
        if item == '':
            return "?"
        if item == 'x':
            return "?"
        if item == '':
            return "?"
        if item == 'y':
            return "grand"
        if item == '':
            return "?"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "le group d`excercis de la santé"
        if item == '~':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '0':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '1':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '2':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '3':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '4':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '5':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == '6':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == 'a':
            return "method d'oscillation [oscillation method]"
        if item == '':
            return "le group d`excercis de la santé"
        if item == 'b':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == 'c':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == 'd':
            return "?"
        if item == '':
            return "le group d`excercis de la santé"
        if item == 'u':
            return "exercise d'chaval [cheval exercise]"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'cz':
    if list == 'ryu':
        if item == '':
            return "typy"
        if item == 'a':
            return "cesta harmonie s ki"
        if item == '':
            return "typy"
        if item == 'b':
            return "?"
        if item == '':
            return "typy"
        if item == 'j':
            return "techniky s jo využívající ai-ki principy"
        if item == '':
            return "typy"
        if item == 'k':
            return "techniky s kenem využívající ai-ki principy"
        if item == '':
            return "typy"
        if item == 'h':
            return "jedna z kat školy Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "typy"
        if item == 'j':
            return "japonská škola meče původem z 16. století"
        if item == '':
            return "typy"
        if item == 'g':
            return "skupina ozdravných cvičení"
        if item == '':
            return "typy"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOduch"
        if item == 'a':
            return "útočit jeden po druhém [?]"
        if item == '':
            return "TODOduch"
        if item == 'k':
            return "plynulá forma, tori se nenechá pevně chytit [?]"
        if item == '':
            return "TODOduch"
        if item == 't':
            return "způsob tréninku, kdy se tori nechá pevně chytit [?]"
        if item == '':
            return "TODOduch"
        if item == 's':
            return "reálný trénink [?]"
        if item == '':
            return "TODOduch"
        if item == 'k':
            return "?"
        if item == '':
            return "TODOduch"
        if item == 'j':
            return "?"
        if item == '':
            return "TODOduch"
        if item == 'j':
            return "?"
        if item == '':
            return "TODOduch"
        if item == 'r':
            return "?"
        if item == '':
            return "TODOduch"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "pozice"
        if item == 's':
            return "techniky v sedě"
        if item == '':
            return "pozice"
        if item == 'h':
            return "techniky, ve kterých je tori v sedě a uke stojí"
        if item == '':
            return "pozice"
        if item == 't':
            return "techniky ve stoje"
        if item == '':
            return "pozice"
        if item == '2':
            return "sezení"
        if item == '':
            return "pozice"
        if item == '3':
            return "sezení na patách"
        if item == '':
            return "pozice"
        if item == '4':
            return "sezení na prstech"
        if item == '':
            return "pozice"
        if item == '5':
            return "sezení na kolenou, zadek na zemi mezi nohama"
        if item == '':
            return "pozice"
        if item == '6':
            return "sezení s nataženýma nohama dopředu"
        if item == '':
            return "pozice"
        if item == '7':
            return "sezení s nataženýma roztaženýma nohama"
        if item == '':
            return "pozice"
        if item == '8':
            return "sezení s pokrčenýma nohama, s koleny u hrudě a s chodidly na zemi"
        if item == '':
            return "pozice"
        if item == '9':
            return "sezení s pokrčenýma nohama, kdy jsou chodidla proti sobě a kolena na zemi"
        if item == '':
            return "pozice"
        if item == '0':
            return "krejčovský posed, aniž by se zkřížili nohy"
        if item == '':
            return "pozice"
        if item == 'j':
            return "držení jako osmička"
        if item == '':
            return "pozice"
        if item == 'z':
            return "pozice lotosu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == '':
            return "partner"
        if item == 't':
            return "tři a více uke útočí neustále, provádí se jen začátek technik"
        if item == '':
            return "partner"
        if item == 'k':
            return "dva a více uke se střídají v útoku, čekají na dokončení techniky"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "zbraně"
        if item == 'j':
            return "tyč, krátká hůl"
        if item == '':
            return "zbraně"
        if item == 'o':
            return "dlouhá hůl"
        if item == '':
            return "zbraně"
        if item == 'b':
            return "dřevěný meč"
        if item == '':
            return "zbraně"
        if item == 't':
            return "nůž nebo dýka"
        if item == '':
            return "zbraně"
        if item == 'w':
            return "krátký zahnutý železný meč"
        if item == '':
            return "zbraně"
        if item == 'k':
            return "zahnutý železný meč"
        if item == '':
            return "zbraně"
        if item == 'a':
            return "dlouhý železný meč"
        if item == '':
            return "zbraně"
        if item == 'e':
            return "krátký, rovný dvousečný železný meč"
        if item == '':
            return "zbraně"
        if item == 'n':
            return "japonský meč"
        if item == '':
            return "zbraně"
        if item == 'n':
            return "japonské kopí se zahnutým ostřím"
        if item == '':
            return "zbraně"
        if item == 'y':
            return "kopí"
        if item == '':
            return "zbraně"
        if item == 's':
            return "záštita meče"
        if item == '':
            return "zbraně"
        if item == 's':
            return "pochva"
        if item == '':
            return "zbraně"
        if item == 'u':
            return "police, regál na zbraně"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "útoky"
        if item == 'a':
            return "útok na hlavu otevřenou rukou s pohybem boků vpřed"
        if item == '':
            return "útoky"
        if item == 'b':
            return "jedna ruka chytá to samé zápěstí protivníka (stejně) [?]"
        if item == '':
            return "útoky"
        if item == 'c':
            return "jedna ruka chytá opačné zápěstí protivníka (zrcadlově) [?]"
        if item == '':
            return "útoky"
        if item == 'd':
            return "úchop za obě zápěstí [?]"
        if item == '':
            return "útoky"
        if item == 'e':
            return "sek přímo na hlavu [?]"
        if item == '':
            return "útoky"
        if item == 'f':
            return "úchop jednoho zápěstí oběma rukama"
        if item == '':
            return "útoky"
        if item == 'g':
            return "úchop ramene"
        if item == '':
            return "útoky"
        if item == 'h':
            return "úchop obou zápěstí protivníka ze zadu"
        if item == '':
            return "útoky"
        if item == 'i':
            return "sek na spánek"
        if item == '':
            return "útoky"
        if item == 'j':
            return "úder do středu těla"
        if item == '':
            return "útoky"
        if item == 'k':
            return "úchop ramene a úder do obličeje"
        if item == '':
            return "útoky"
        if item == 'l':
            return "úchop obou ramen protivníka ze zadu"
        if item == '':
            return "útoky"
        if item == 'm':
            return "úder do horní části těla"
        if item == '':
            return "útoky"
        if item == 'n':
            return "úchop za oba límce"
        if item == '':
            return "útoky"
        if item == 'o':
            return "kop"
        if item == '':
            return "útoky"
        if item == 'p':
            return "škrcení ze zadu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uvnitř/vně"
        if item == 'u':
            return "pohyb dovnitř"
        if item == '':
            return "uvnitř/vně"
        if item == 's':
            return "pohyb ven"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "pohyb těla"
        if item == 'a':
            return "krok vpřed z přední nohy"
        if item == '':
            return "pohyb těla"
        if item == 'b':
            return "krok vpřed ze zadní nohy"
        if item == '':
            return "pohyb těla"
        if item == 'c':
            return "otočení na zadní noze s úhybem přední"
        if item == '':
            return "pohyb těla"
        if item == 'd':
            return "otočení na přední noze s úhybem zadní"
        if item == '':
            return "pohyb těla"
        if item == 'e':
            return "úhyb se stažením přední nohy"
        if item == '':
            return "pohyb těla"
        if item == 'f':
            return "úhyb se stažením zadní nohy"
        if item == '':
            return "pohyb těla"
        if item == 'g':
            return "krok z přední nohy s následným otočením"
        if item == '':
            return "pohyb těla"
        if item == 'h':
            return "krok ze zadní nohy s následným otočením"
        if item == '':
            return "pohyb těla"
        if item == 'i':
            return "krok z přední nohy, otočení a úhyb"
        if item == '':
            return "pohyb těla"
        if item == 'j':
            return "krok ze zadní nohy, otočení a úhyb"
        if item == '':
            return "pohyb těla"
        if item == 'k':
            return "otočení těla na zadní noze s úhybem přední a úhyb"
        if item == '':
            return "pohyb těla"
        if item == 'l':
            return "otočení těla na přední noze s úhybem zadní a úhyb"
        if item == '':
            return "pohyb těla"
        if item == 'm':
            return "krok vpřed ze zadní nohy s následným otočením"
        if item == '':
            return "pohyb těla"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "pohyby rukou"
        if item == 'k':
            return "horní půlkruh"
        if item == '':
            return "pohyby rukou"
        if item == 's':
            return "dolní půlkruh"
        if item == '':
            return "pohyby rukou"
        if item == 't':
            return "ruce paralelně"
        if item == '':
            return "pohyby rukou"
        if item == 'y':
            return "ruce zkřížené"
        if item == '':
            return "pohyby rukou"
        if item == 'u':
            return "úhyb do strany před útokem, kontrola útoku"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "ruce"
        if item == 'u':
            return "útočící ruka"
        if item == '':
            return "ruce"
        if item == 'k':
            return "ruka chytající rameno"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "úrovně"
        if item == 'g':
            return "nízko"
        if item == '':
            return "úrovně"
        if item == 'c':
            return "středně"
        if item == '':
            return "úrovně"
        if item == 'j':
            return "vysoko"
        if item == '':
            return "úrovně"
        if item == '1':
            return "úzký postoj"
        if item == '':
            return "úrovně"
        if item == '2':
            return "nízký postoj"
        if item == '':
            return "úrovně"
        if item == '3':
            return "střední postoj"
        if item == '':
            return "úrovně"
        if item == '5':
            return "vysoký postoj"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "techniky"
        if item == 'a':
            return "lekce číslo jedna"
        if item == '':
            return "techniky"
        if item == 'b':
            return "lekce číslo dva"
        if item == '':
            return "techniky"
        if item == 'c':
            return "lekce číslo tři"
        if item == '':
            return "techniky"
        if item == 'd':
            return "lekce číslo čtyři"
        if item == '':
            return "techniky"
        if item == 'e':
            return "hod do rohu"
        if item == '':
            return "techniky"
        if item == 'f':
            return "stočení zápěstí"
        if item == '':
            return "techniky"
        if item == 'g':
            return "hod se vstupem"
        if item == '':
            return "techniky"
        if item == 'h':
            return "seknutí do čtyř směrů"
        if item == '':
            return "techniky"
        if item == 'i':
            return "lekce číslo pět"
        if item == '':
            return "techniky"
        if item == 'j':
            return "prolomit a blokovat loket"
        if item == '':
            return "techniky"
        if item == 'k':
            return "?"
        if item == '':
            return "techniky"
        if item == 'l':
            return "?"
        if item == '':
            return "techniky"
        if item == 'm':
            return "hod přes boky"
        if item == '':
            return "techniky"
        if item == 'n':
            return "?"
        if item == '':
            return "techniky"
        if item == 'o':
            return "rotační hod"
        if item == '':
            return "techniky"
        if item == 'p':
            return "hod s prolomením lokte"
        if item == '':
            return "techniky"
        if item == 'q':
            return "hod dopředu"
        if item == '':
            return "techniky"
        if item == 'r':
            return "hod se zatažením"
        if item == '':
            return "techniky"
        if item == 's':
            return "hod se sekem"
        if item == '':
            return "techniky"
        if item == 't':
            return "hod s otočením"
        if item == '':
            return "techniky"
        if item == 'u':
            return "hod nebe-země"
        if item == '':
            return "techniky"
        if item == 'v':
            return "hod silou dechu"
        if item == '':
            return "techniky"
        if item == 'w':
            return "hod s otočením dovnitř"
        if item == '':
            return "techniky"
        if item == 'x':
            return "?"
        if item == '':
            return "techniky"
        if item == 'y':
            return "hod se zkříženýma rukama"
        if item == '':
            return "techniky"
        if item == 'z':
            return "hod silou dechu veslováním"
        if item == '':
            return "techniky"
        if item == '0':
            return "?"
        if item == '':
            return "techniky"
        if item == '1':
            return "?"
        if item == '':
            return "techniky"
        if item == '2':
            return "?"
        if item == '':
            return "techniky"
        if item == '3':
            return "hod přes boky"
        if item == '':
            return "techniky"
        if item == '4':
            return "hod s otočením vně"
        if item == '':
            return "techniky"
        if item == '5':
            return "?"
        if item == '':
            return "techniky"
        if item == '6':
            return "?"
        if item == '':
            return "techniky"
        if item == '7':
            return "?"
        if item == '':
            return "techniky"
        if item == '8':
            return "?"
        if item == '':
            return "techniky"
        if item == '9':
            return "?"
        if item == '':
            return "techniky"
        if item == '~':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "před partnera"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "za partnera"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        if item == '':
            return "čísla"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "jin/jang"
        if item == '1':
            return "jin"
        if item == '':
            return "jin/jang"
        if item == '2':
            return "jang"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "principy"
        if item == '1':
            return "voda, nahoru-dolů, východ"
        if item == '':
            return "principy"
        if item == '2':
            return "země, vlevo-vpravo, jih"
        if item == '':
            return "principy"
        if item == '3':
            return "vzduch, dopředu-dozadu, západ"
        if item == '':
            return "principy"
        if item == '4':
            return "oheň, spirála, sever"
        if item == '':
            return "principy"
        if item == '5':
            return "člověk"
        if item == '':
            return "principy"
        if item == 'h':
            return "jaro"
        if item == '':
            return "principy"
        if item == 'n':
            return "léto"
        if item == '':
            return "principy"
        if item == 'a':
            return "podzim"
        if item == '':
            return "principy"
        if item == 'f':
            return "zima"
        if item == '':
            return "principy"
        if item == 'k':
            return "principy protiútoku v obranných technikách"
        if item == '':
            return "principy"
        if item == 'u':
            return "principy úderů"
        if item == '':
            return "principy"
        if item == 'o':
            return "principy znehybnění"
        if item == '':
            return "principy"
        if item == 'g':
            return "principy hodů"
        if item == '':
            return "principy"
        if item == 'z':
            return "principy seků"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "hod"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "znehybnění"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "hod znehybnění"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "přijetí s tělem (pád)"
        if item == '1':
            return "?"
        if item == '':
            return "přijetí s tělem (pád)"
        if item == '2':
            return "pád vpřed"
        if item == '':
            return "přijetí s tělem (pád)"
        if item == '3':
            return "pád vzad"
        if item == '':
            return "přijetí s tělem (pád)"
        if item == '4':
            return "pád do boku"
        if item == '':
            return "přijetí s tělem (pád)"
        if item == 'c':
            return "?"
        if item == '':
            return "přijetí s tělem (pád)"
        if item == '':
            return "přijetí s tělem (pád)"
        if item == 't':
            return "volný pád"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "osoby"
        if item == '1':
            return "zakladatel aikido, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "osoby"
        if item == '2':
            return "syn zakladatele aikido, druhý doshu (27-06-1921 - 04-01-1999)"
        if item == '':
            return "osoby"
        if item == '3':
            return "vnuk zakladatele aikido, třetí doshu (02-04-1951)"
        if item == '':
            return "osoby"
        if item == 't':
            return "přímý žák ôsensei (13-12-1929)"
        if item == '':
            return "osoby"
        if item == 'i':
            return "žák senseie Tady, shihan (08-04-1940)"
        if item == '':
            return "osoby"
        if item == '':
            return "osoby"
        if item == '':
            return "osoby"
        if item == '':
            return "osoby"
        if item == '':
            return "osoby"
        if item == '':
            return "osoby"
        if item == '':
            return "osoby"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "počítání"
        if item == '0':
            return "nula"
        if item == '':
            return "počítání"
        if item == '1':
            return "jedna"
        if item == '':
            return "počítání"
        if item == '2':
            return "dvě"
        if item == '':
            return "počítání"
        if item == '3':
            return "tři"
        if item == '':
            return "počítání"
        if item == '4':
            return "čtyři"
        if item == '':
            return "počítání"
        if item == '5':
            return "pět"
        if item == '':
            return "počítání"
        if item == '6':
            return "šest"
        if item == '':
            return "počítání"
        if item == '7':
            return "sedm"
        if item == '':
            return "počítání"
        if item == '8':
            return "osm"
        if item == '':
            return "počítání"
        if item == '9':
            return "devět"
        if item == '':
            return "počítání"
        if item == 'a':
            return "deset"
        if item == '':
            return "počítání"
        if item == 'b':
            return "jedenáct"
        if item == '':
            return "počítání"
        if item == 'c':
            return "dvacet"
        if item == '':
            return "počítání"
        if item == 'd':
            return "dvacet jedna"
        if item == '':
            return "počítání"
        if item == 'e':
            return "sto"
        if item == '':
            return "počítání"
        if item == 'f':
            return "tisíc"
        if item == '':
            return "počítání"
        if item == 'e':
            return "deset tisíc"
        if item == '':
            return "počítání"
        if item == 'h':
            return "první forma"
        if item == '':
            return "počítání"
        if item == 'i':
            return "druhá forma"
        if item == '':
            return "počítání"
        if item == 'j':
            return "třetí forma"
        if item == '':
            return "počítání"
        if item == 'k':
            return "čtvrtá forma"
        if item == '':
            return "počítání"
        if item == 'l':
            return "pátá forma"
        if item == '':
            return "počítání"
        if item == 'm':
            return "šestá forma"
        if item == '':
            return "počítání"
        if item == 'n':
            return "sedmá forma"
        if item == '':
            return "počítání"
        if item == 'o':
            return "osmá forma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "stupně"
        if item == 'n':
            return "danový stupeň"
        if item == '':
            return "stupně"
        if item == 'k':
            return "žákovský stupeň"
        if item == '':
            return "stupně"
        if item == '0':
            return "bez kyu"
        if item == '':
            return "stupně"
        if item == '6':
            return "šesté kyu"
        if item == '':
            return "stupně"
        if item == '5':
            return "páté kyu"
        if item == '':
            return "stupně"
        if item == '4':
            return "čtvrté kyu"
        if item == '':
            return "stupně"
        if item == '3':
            return "třetí kyu"
        if item == '':
            return "stupně"
        if item == '2':
            return "druhé kyu"
        if item == '':
            return "stupně"
        if item == '1':
            return "první kyu, začátečnické kyu"
        if item == '':
            return "stupně"
        if item == 'y':
            return "s danem"
        if item == '':
            return "stupně"
        if item == 'o':
            return "bez danu"
        if item == '':
            return "stupně"
        if item == 'a':
            return "první dan, počáteční dan"
        if item == '':
            return "stupně"
        if item == 'b':
            return "druhý dan"
        if item == '':
            return "stupně"
        if item == 'c':
            return "třetí dan"
        if item == '':
            return "stupně"
        if item == 'd':
            return "čtvrtý dan"
        if item == '':
            return "stupně"
        if item == 'e':
            return "pátý dan"
        if item == '':
            return "stupně"
        if item == 'f':
            return "šestý dan"
        if item == '':
            return "stupně"
        if item == 'g':
            return "sedmý dan"
        if item == '':
            return "stupně"
        if item == 'h':
            return "osmý dan"
        if item == '':
            return "stupně"
        if item == 'i':
            return "devátý dan"
        if item == '':
            return "stupně"
        if item == 'j':
            return "desátý dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "obecné"
        if item == '1':
            return "harmonie, sjednocení"
        if item == '':
            return "obecné"
        if item == '2':
            return "životní síla, energie"
        if item == '':
            return "obecné"
        if item == '3':
            return "cesta, disciplína"
        if item == '':
            return "obecné"
        if item == '3':
            return "cesta harmonie s KI"
        if item == '':
            return "obecné"
        if item == '4':
            return "aikidista, člověk praktikující aikido"
        if item == '':
            return "obecné"
        if item == '5':
            return "organizace starající se o provoz a rozšiřování aikido"
        if item == '':
            return "obecné"
        if item == '8':
            return "útočník"
        if item == '':
            return "obecné"
        if item == '9':
            return "obránce [?]"
        if item == '':
            return "obecné"
        if item == 'n':
            return "obránce (jiné pojmenování), také hod"
        if item == '':
            return "obecné"
        if item == 'u':
            return "rodič, učitel [?]"
        if item == '':
            return "obecné"
        if item == 's':
            return "dítě, žák"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "instrukce"
        if item == '1':
            return "prosím (na začátku tréninku nebo cvičení)"
        if item == '':
            return "instrukce"
        if item == '2':
            return "děkuji (na konci tréninku nebo cvičení)"
        if item == '':
            return "instrukce"
        if item == '3':
            return "ano"
        if item == '':
            return "instrukce"
        if item == '':
            return "instrukce"
        if item == '5':
            return "stop (a posaď se na stranu)"
        if item == '':
            return "instrukce"
        if item == '6':
            return "začněte"
        if item == '':
            return "instrukce"
        if item == '6':
            return "počkat, zastavte"
        if item == '':
            return "instrukce"
        if item == '8':
            return "postav se"
        if item == '':
            return "instrukce"
        if item == '9':
            return "posaďte se"
        if item == '':
            return "instrukce"
        if item == 'a':
            return "otočte se"
        if item == '':
            return "instrukce"
        if item == 'b':
            return "výměna osob"
        if item == '':
            return "instrukce"
        if item == 'c':
            return "opakujte cvičení"
        if item == '':
            return "instrukce"
        if item == 'd':
            return "používej druhou stranu"
        if item == '':
            return "instrukce"
        if item == 'e':
            return "najdi si jiného partnera"
        if item == '':
            return "instrukce"
        if item == 'f':
            return "pozdrav"
        if item == '':
            return "instrukce"
        if item == 'g':
            return "pozdrav ve stoje"
        if item == '':
            return "instrukce"
        if item == 'h':
            return "pozdrav vsedě"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "tituly"
        if item == 's':
            return "velký učitel"
        if item == '':
            return "tituly"
        if item == 'o':
            return "učitel, instruktor"
        if item == '':
            return "tituly"
        if item == 'd':
            return "ten, jenž ukazuje cestu"
        if item == '':
            return "tituly"
        if item == '7':
            return "hlavní instruktor (minimálně 6. dan)"
        if item == '':
            return "tituly"
        if item == '8':
            return "instruktor, příprava na shihan (4. nebo 5. dan)"
        if item == '':
            return "tituly"
        if item == '9':
            return "asistent instruktora (2. nebo 3. dan)"
        if item == '':
            return "tituly"
        if item == 'a':
            return "senior, příslušník starší generace"
        if item == '':
            return "tituly"
        if item == 'b':
            return "junior, mladý student"
        if item == '':
            return "tituly"
        if item == 'c':
            return "osoba bez stupně"
        if item == '':
            return "tituly"
        if item == 'd':
            return "osoba se stupněm dan"
        if item == '':
            return "tituly"
        if item == 'e':
            return "vedoucí dojo"
        if item == '':
            return "tituly"
        if item == 'f':
            return "student"
        if item == '':
            return "tituly"
        if item == 'g':
            return "student žijící v dojo"
        if item == '':
            return "tituly"
        if item == 'h':
            return "student žijící mimo dojo"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "objekty"
        if item == '0':
            return "prostor k tréninku (místo osvícení, slabičně místo cesty)"
        if item == '':
            return "objekty"
        if item == '1':
            return "místo, kde visí portrét zakladatele aikidó, přední stěna Dojo"
        if item == '':
            return "objekty"
        if item == '2':
            return "zadní stěna dojo"
        if item == '':
            return "objekty"
        if item == '3':
            return "vrchní sezení - strana dojo, kde sedí vyšší stupně"
        if item == '':
            return "objekty"
        if item == '4':
            return "spodní sezení - strana dojo, kde sedí nižší stupně"
        if item == '':
            return "objekty"
        if item == '5':
            return "žíněnka"
        if item == '':
            return "objekty"
        if item == '6':
            return "hlavní ústředí"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "oblečení"
        if item == '1':
            return "tréninková souprava"
        if item == '':
            return "oblečení"
        if item == '2':
            return "pásek"
        if item == '':
            return "oblečení"
        if item == '3':
            return "bílý pásek"
        if item == '':
            return "oblečení"
        if item == '4':
            return "černý pásek"
        if item == '':
            return "oblečení"
        if item == '5':
            return "druh vysokých ponožek s odděleným palcem"
        if item == '':
            return "oblečení"
        if item == '6':
            return "nazouváky"
        if item == '':
            return "oblečení"
        if item == '7':
            return "tradiční japonská kalhotová suknice"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "anatomie"
        if item == 'a':
            return "centrum"
        if item == '':
            return "anatomie"
        if item == 'b':
            return "tělo"
        if item == '':
            return "anatomie"
        if item == 'c':
            return "čelo"
        if item == '':
            return "anatomie"
        if item == 'd':
            return "spánek"
        if item == '':
            return "anatomie"
        if item == 'e':
            return "koleno"
        if item == '':
            return "anatomie"
        if item == 'f':
            return "krk"
        if item == '':
            return "anatomie"
        if item == 'g':
            return "hruď"
        if item == '':
            return "anatomie"
        if item == 'e':
            return "rameno"
        if item == '':
            return "anatomie"
        if item == 'h':
            return "loket"
        if item == '':
            return "anatomie"
        if item == 'i':
            return "paže"
        if item == '':
            return "anatomie"
        if item == 'j':
            return "zápěstí"
        if item == '':
            return "anatomie"
        if item == 'k':
            return "ruka"
        if item == '':
            return "anatomie"
        if item == 'k':
            return "mečová ruka, ruka jako meč"
        if item == '':
            return "anatomie"
        if item == 'l':
            return "noha"
        if item == '':
            return "anatomie"
        if item == 'm':
            return "kotník"
        if item == '':
            return "anatomie"
        if item == 'n':
            return "boky"
        if item == '':
            return "anatomie"
        if item == 'o':
            return "límec"
        if item == '':
            return "anatomie"
        if item == 'p':
            return "tělo"
        if item == '':
            return "anatomie"
        if item == 's':
            return "rukáv"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "různé"
        if item == 'a':
            return "vzájemný únik"
        if item == '':
            return "různé"
        if item == 'b':
            return "oboustranné zabití"
        if item == '':
            return "různé"
        if item == 'c':
            return "udeřit tělo"
        if item == '':
            return "různé"
        if item == 'd':
            return "cesta boje"
        if item == '':
            return "různé"
        if item == 'e':
            return "společné cvičení s jo"
        if item == '':
            return "různé"
        if item == 'f':
            return "společné cvičení s mečem"
        if item == '':
            return "různé"
        if item == 'g':
            return "odebírání meče"
        if item == '':
            return "různé"
        if item == 'h':
            return "odebírání nože"
        if item == '':
            return "různé"
        if item == 'i':
            return "míření do oka"
        if item == '':
            return "různé"
        if item == 'j':
            return "postoj"
        if item == '':
            return "různé"
        if item == 'm':
            return "?"
        if item == '':
            return "různé"
        if item == 's':
            return "?"
        if item == '':
            return "různé"
        if item == 't':
            return "japonský buben (mj. signalizující začátek a konec trénink)"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "směry"
        if item == 'h':
            return "doleva"
        if item == '':
            return "směry"
        if item == 'm':
            return "doprava"
        if item == '':
            return "směry"
        if item == 'i':
            return "vstoupit"
        if item == '':
            return "směry"
        if item == 'k':
            return "otočit se"
        if item == '':
            return "směry"
        if item == '1':
            return "dopředu, přední"
        if item == '':
            return "směry"
        if item == '2':
            return "dozadu, zadní"
        if item == '':
            return "směry"
        if item == '3':
            return "do boku, boční"
        if item == '':
            return "směry"
        if item == 'a':
            return "uvnitř, dovnitř"
        if item == '':
            return "směry"
        if item == 'b':
            return "vně, ven"
        if item == '':
            return "směry"
        if item == 'n':
            return "diagonálně"
        if item == '':
            return "směry"
        if item == 'c':
            return "vertikálně"
        if item == '':
            return "směry"
        if item == 's':
            return "horizontálně"
        if item == '':
            return "směry"
        if item == 't':
            return "ve stoje"
        if item == '':
            return "směry"
        if item == 'x':
            return "naproti sobě"
        if item == '':
            return "směry"
        if item == '8':
            return "osm směrů"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "cvičení"
        if item == '1':
            return "opakování ikkyô"
        if item == '':
            return "cvičení"
        if item == '2':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "základní principy"
        if item == '1':
            return "jarní meč"
        if item == '':
            return "základní principy"
        if item == '2':
            return "letní meč"
        if item == '':
            return "základní principy"
        if item == '3':
            return "podzimní meč"
        if item == '':
            return "základní principy"
        if item == '4':
            return "zimní meč"
        if item == '':
            return "základní principy"
        if item == '5':
            return "osm směrů"
        if item == '':
            return "základní principy"
        if item == '6':
            return "proseknutí vlastního ego"
        if item == '':
            return "základní principy"
        if item == '7':
            return "doba změn"
        if item == '':
            return "základní principy"
        if item == '8':
            return "krátký či dlouhý jsou nyní stejné"
        if item == '':
            return "základní principy"
        if item == '9':
            return "přijmout"
        if item == '':
            return "základní principy"
        if item == 'a':
            return "meč u těla"
        if item == '':
            return "základní principy"
        if item == 'b':
            return "pozdrav lehkou úklonou bez přerušení očního kontaktu bez mluvení"
        if item == '':
            return "základní principy"
        if item == 'c':
            return "nakreslit jeden meč"
        if item == '':
            return "základní principy"
        if item == 'd':
            return "harmonicky směřovat do oka"
        if item == '':
            return "základní principy"
        if item == 'e':
            return "podnítit, urychlit"
        if item == '':
            return "základní principy"
        if item == 'g':
            return "strážce chrámu s mečem"
        if item == '':
            return "základní principy"
        if item == 'h':
            return "stín"
        if item == '':
            return "základní principy"
        if item == 'i':
            return "harmonický jodan"
        if item == '':
            return "základní principy"
        if item == 'j':
            return "?"
        if item == '':
            return "základní principy"
        if item == 'k':
            return "opakované cvičení"
        if item == '':
            return "základní principy"
        if item == 'l':
            return "obě ruce"
        if item == '':
            return "základní principy"
        if item == 'm':
            return "tlačení"
        if item == '':
            return "základní principy"
        if item == 'n':
            return "linie"
        if item == '':
            return "základní principy"
        if item == 'o':
            return "zastavené tělo"
        if item == '':
            return "základní principy"
        if item == 'p':
            return "kontrola těla"
        if item == '':
            return "základní principy"
        if item == 'q':
            return "neudeření"
        if item == '':
            return "základní principy"
        if item == 'r':
            return "spánek"
        if item == '':
            return "základní principy"
        if item == 's':
            return "tělo se otočí na stranu k protivníkovi"
        if item == '':
            return "základní principy"
        if item == 't':
            return "do obličeje, otočit hlavu"
        if item == '':
            return "základní principy"
        if item == 'u':
            return "seknout"
        if item == '':
            return "základní principy"
        if item == 'v':
            return "zastavit"
        if item == '':
            return "základní principy"
        if item == 'w':
            return "udeřit na zadní stranu"
        if item == '':
            return "základní principy"
        if item == 'x':
            return "úsvit"
        if item == '':
            return "základní principy"
        if item == 'y':
            return "velký"
        if item == '':
            return "základní principy"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '~':
            return "dýchání ve velkých kruzích"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '0':
            return "?"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '1':
            return "dýchání s dlaněmi v jang"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '2':
            return "dýchání s dlaněmi v jin"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '3':
            return "dýchání energie s rukama kreslícíma kříž"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '4':
            return "dýchání sjednocení se s vesmírem"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '5':
            return "?"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == '6':
            return "?"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == 'a':
            return "oscilační metoda, převalování se ze strany na stranu"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == 'b':
            return "?"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == 'c':
            return "?"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == 'd':
            return "pohyb zlaté rybky"
        if item == '':
            return "skupina ozdravných cvičení"
        if item == 'u':
            return "cvičení koně"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'mk':
    if list == 'ryu':
        if item == '':
            return "тип, начин"
        if item == 'a':
            return "начин да ја хармонизираш ки енергијата"
        if item == '':
            return "тип, начин"
        if item == 'b':
            return "?"
        if item == '':
            return "тип, начин"
        if item == 'j':
            return "техники со стап каде што се употрбува аики принципот"
        if item == '':
            return "тип, начин"
        if item == 'k':
            return "техники со меч каде што се употрбува аики принципот"
        if item == '':
            return "тип, начин"
        if item == 'h':
            return "стил на мечување"
        if item == '':
            return "тип, начин"
        if item == 'j':
            return "стил на мечување"
        if item == '':
            return "тип, начин"
        if item == 'g':
            return "?"
        if item == '':
            return "тип, начин"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOдух"
        if item == 'a':
            return "наизменично вежбање со два напаѓачи без пауза?"
        if item == '':
            return "TODOдух"
        if item == 'k':
            return "меко изведување на техники"
        if item == '':
            return "TODOдух"
        if item == 't':
            return "тврдо, стегнато изведување на техники"
        if item == '':
            return "TODOдух"
        if item == 's':
            return "реалистично изведување на техники"
        if item == '':
            return "TODOдух"
        if item == 'k':
            return "?"
        if item == '':
            return "TODOдух"
        if item == 'j':
            return "?"
        if item == '':
            return "TODOдух"
        if item == 'j':
            return "?"
        if item == '':
            return "TODOдух"
        if item == 'r':
            return "?"
        if item == '':
            return "TODOдух"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "позиција"
        if item == 's':
            return "техники кои се изведуваат движејќи се на колена"
        if item == '':
            return "позиција"
        if item == 'h':
            return "техники при кои тори-то седи а уке-то стои"
        if item == '':
            return "позиција"
        if item == 't':
            return "техники кои се изведуваат во стоечки став"
        if item == '':
            return "позиција"
        if item == '2':
            return "седење"
        if item == '':
            return "позиција"
        if item == '3':
            return "седење на колена, подколениците и стапалата со предната страна залепени за подот"
        if item == '':
            return "позиција"
        if item == '4':
            return "седење на колена, стапалата подигнати на прсти"
        if item == '':
            return "позиција"
        if item == '5':
            return "седење на колена а колковите на подот меѓу стопалата"
        if item == '':
            return "позиција"
        if item == '6':
            return "седење со нозете испружени напред"
        if item == '':
            return "позиција"
        if item == '7':
            return "седење со испружени и раширени нозе"
        if item == '':
            return "позиција"
        if item == '8':
            return "седење со колената допрени на гради а стапалата на под"
        if item == '':
            return "позиција"
        if item == '9':
            return "седење со споени стопала а колената странично на под"
        if item == '':
            return "позиција"
        if item == '0':
            return "турско седење"
        if item == '':
            return "позиција"
        if item == 'j':
            return "?"
        if item == '':
            return "позиција"
        if item == 'z':
            return "јога седење, позиција лотус"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == 't':
            return "тројца или повеќе напаѓаат истовремено, а се изведува само почетокот од техниката"
        if item == '':
            return "партнер"
        if item == 'k':
            return "наизменично вежбање со два напаѓачи без пауза"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "оружје"
        if item == 'j':
            return "дрвен стап"
        if item == '':
            return "оружје"
        if item == 'o':
            return "долг дрвен стап"
        if item == '':
            return "оружје"
        if item == 'b':
            return "закривен дрвен меч"
        if item == '':
            return "оружје"
        if item == 't':
            return "нож"
        if item == '':
            return "оружје"
        if item == 'w':
            return "краток самурајски закривен меч"
        if item == '':
            return "оружје"
        if item == 'k':
            return "долг самурајски закривен меч"
        if item == '':
            return "оружје"
        if item == 'a':
            return "долг меч"
        if item == '':
            return "оружје"
        if item == 'e':
            return "меч"
        if item == '':
            return "оружје"
        if item == 'n':
            return "Јапонски меч"
        if item == '':
            return "оружје"
        if item == 'n':
            return "хелебарда, вид на копје со широко сечиво на врвот"
        if item == '':
            return "оружје"
        if item == 'y':
            return "копје"
        if item == '':
            return "оружје"
        if item == 's':
            return "штитник пред дршката на мечот"
        if item == '':
            return "оружје"
        if item == 's':
            return "?"
        if item == '':
            return "оружје"
        if item == 'u':
            return "држач за оружје"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "напад"
        if item == 'a':
            return "удар во глава со отворена дланка поаѓајќи од колковите"
        if item == '':
            return "напад"
        if item == 'b':
            return "фат за зглобот над дланката на соодветно истата рака, десна за десна и лева за лева"
        if item == '':
            return "напад"
        if item == 'c':
            return "фат за зглобот над дланката на соодветно спротивната рака, десна за лева и лева за десна"
        if item == '':
            return "напад"
        if item == 'd':
            return "фат со две раце за двете раце"
        if item == '':
            return "напад"
        if item == 'e':
            return "удар во предниот дел на главата од горе"
        if item == '':
            return "напад"
        if item == 'f':
            return "фат со двете раце за една рака"
        if item == '':
            return "напад"
        if item == 'g':
            return "фат за рамо"
        if item == '':
            return "напад"
        if item == 'h':
            return "фат со две раце за двете раце од зад грб"
        if item == '':
            return "напад"
        if item == 'i':
            return "удар во главата од страна"
        if item == '':
            return "напад"
        if item == 'j':
            return "директен удар во средишниот дел на телото"
        if item == '':
            return "напад"
        if item == 'k':
            return "фат за рамо со едната рака и удар со другата во глава"
        if item == '':
            return "напад"
        if item == 'l':
            return "фат со две раце за двете рамења од зад грб"
        if item == '':
            return "напад"
        if item == 'm':
            return "директен удар во горниот дел на телото"
        if item == '':
            return "напад"
        if item == 'n':
            return "фат со две раце за крагната"
        if item == '':
            return "напад"
        if item == 'o':
            return "удар со нога"
        if item == '':
            return "напад"
        if item == 'p':
            return "давење од зад грб"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "одвнатре/однадвор"
        if item == 'u':
            return "движење кон внатре"
        if item == '':
            return "одвнатре/однадвор"
        if item == 's':
            return "движење кон надвор"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "движење на телото"
        if item == 'a':
            return "директен влез право напред со предната нога"
        if item == '':
            return "движење на телото"
        if item == 'b':
            return "директен влез право напред со задната нога"
        if item == '':
            return "движење на телото"
        if item == 'c':
            return "избегнувачко движење, предната нога прави полукруг"
        if item == '':
            return "движење на телото"
        if item == 'd':
            return "избегнувачко движење со свртување на предната нога, задната нога прави полукруг"
        if item == '':
            return "движење на телото"
        if item == 'e':
            return "избегнувачко движење со повлекување на предната нога"
        if item == '':
            return "движење на телото"
        if item == 'f':
            return "избегнувачко движење со повлекување на задната нога"
        if item == '':
            return "движење на телото"
        if item == 'g':
            return "комбинирано движење за избегнување, започнато со предната нога"
        if item == '':
            return "движење на телото"
        if item == 'h':
            return "комбинирано движење за избегнување, започнато со задната нога"
        if item == '':
            return "движење на телото"
        if item == 'i':
            return "комбинирано движење за двојно избегнување, започнато со предната нога и завршува со повлекување на задната нога"
        if item == '':
            return "движење на телото"
        if item == 'j':
            return "комбинирано движење за двојно избегнување, започнато со задната нога и завршува со повлекување на задната нога"
        if item == '':
            return "движење на телото"
        if item == 'k':
            return "комбинирано движење"
        if item == '':
            return "движење на телото"
        if item == 'l':
            return "комбинирано движење"
        if item == '':
            return "движење на телото"
        if item == 'm':
            return "?"
        if item == '':
            return "движење на телото"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "?"
        if item == 'k':
            return "горен вертикален полукруг"
        if item == '':
            return "?"
        if item == 's':
            return "долен вертикален полукруг"
        if item == '':
            return "?"
        if item == 't':
            return "?"
        if item == '':
            return "?"
        if item == 'y':
            return "?"
        if item == '':
            return "?"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "рака"
        if item == 'u':
            return "рака што удира"
        if item == '':
            return "рака"
        if item == 'k':
            return "рака што фаќа за рамо"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "ниво, височина"
        if item == 'g':
            return "долно"
        if item == '':
            return "ниво, височина"
        if item == 'c':
            return "средишно"
        if item == '':
            return "ниво, височина"
        if item == 'j':
            return "горно"
        if item == '':
            return "ниво, височина"
        if item == '1':
            return "долно"
        if item == '':
            return "ниво, височина"
        if item == '2':
            return "долно"
        if item == '':
            return "ниво, височина"
        if item == '3':
            return "средишно"
        if item == '':
            return "ниво, височина"
        if item == '5':
            return "горно"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "техника"
        if item == 'a':
            return "прво учење, прв принцип"
        if item == '':
            return "техника"
        if item == 'b':
            return "второ учење, втор принцип"
        if item == '':
            return "техника"
        if item == 'c':
            return "трето учење, трет принцип"
        if item == '':
            return "техника"
        if item == 'd':
            return "четврто учење, четврт принцип"
        if item == '':
            return "техника"
        if item == 'e':
            return "спуштање во агол, техника на фрлање"
        if item == '':
            return "техника"
        if item == 'f':
            return "фрлање со завртување на раката во спротивна насока"
        if item == '':
            return "техника"
        if item == 'g':
            return "фрлање со директен влез"
        if item == '':
            return "техника"
        if item == 'h':
            return "фрлање во четири правци"
        if item == '':
            return "техника"
        if item == 'i':
            return "петто учење, петти принцип"
        if item == '':
            return "техника"
        if item == 'j':
            return "фиксација со лост на лактот"
        if item == '':
            return "техника"
        if item == 'k':
            return "третиот принцип со поминување под рака"
        if item == '':
            return "техника"
        if item == 'l':
            return "начин на лост на раката"
        if item == '':
            return "техника"
        if item == 'm':
            return "фрлање преку колкови со искористување на инерцијата на уке-то"
        if item == '':
            return "техника"
        if item == 'n':
            return "спуштање со потфаќање и подигнување на нозете"
        if item == '':
            return "техника"
        if item == 'o':
            return "кружно, ротирачко фрлање"
        if item == '':
            return "техника"
        if item == 'p':
            return "фрлање корисејќи лост на лактот"
        if item == '':
            return "техника"
        if item == 'q':
            return "напредно спуштање / горе-долу"
        if item == '':
            return "техника"
        if item == 'r':
            return "напредно спуштање / лево-десно"
        if item == '':
            return "техника"
        if item == 's':
            return "напредно спуштање / напред-назад"
        if item == '':
            return "техника"
        if item == 't':
            return "напредно спуштање / спирално"
        if item == '':
            return "техника"
        if item == 'u':
            return "небо-земја фрлање"
        if item == '':
            return "техника"
        if item == 'v':
            return "фрлање со издишување спротивно на небо-земја фрлањето"
        if item == '':
            return "техника"
        if item == 'w':
            return "кружно, ротирачко фрлање со поминување под рака"
        if item == '':
            return "техника"
        if item == 'x':
            return "фрлање произлезено од директен влез со рака во лице"
        if item == '':
            return "техника"
        if item == 'y':
            return "фрлање со вкрстување на рацете"
        if item == '':
            return "техника"
        if item == 'z':
            return "икјо фрлање"
        if item == '':
            return "техника"
        if item == '0':
            return "?"
        if item == '':
            return "техника"
        if item == '1':
            return "фрлање со лостот удегарами во санкјо варијација"
        if item == '':
            return "техника"
        if item == '2':
            return "фрлање со лостот удегарами во јонкјо варијација"
        if item == '':
            return "техника"
        if item == '3':
            return "фрлање преку колкови"
        if item == '':
            return "техника"
        if item == '4':
            return "надворешмо кружно фрлање"
        if item == '':
            return "техника"
        if item == '5':
            return "занто фрлање со издишна сила"
        if item == '':
            return "техника"
        if item == '6':
            return "уде гарами фиксација"
        if item == '':
            return "техника"
        if item == '7':
            return "форма на завртено фрлање со рака"
        if item == '':
            return "техника"
        if item == '8':
            return "форма на завртено фрлање преку рамо"
        if item == '':
            return "техника"
        if item == '9':
            return "форма на завртено фрлање преку колкови"
        if item == '':
            return "техника"
        if item == '~':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "од лице/од опачина"
        if item == 'o':
            return "од лице (предна страна)"
        if item == '':
            return "од лице/од опачина"
        if item == 'u':
            return "од опачина (задна страна)"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "јин/јанг"
        if item == '1':
            return "јин"
        if item == '':
            return "јин/јанг"
        if item == '2':
            return "јанг"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "принцип"
        if item == '1':
            return "вода, горе-доле, исток"
        if item == '':
            return "принцип"
        if item == '2':
            return "земја, лево-десно, југ"
        if item == '':
            return "принцип"
        if item == '3':
            return "ветер, напред-назад, запад"
        if item == '':
            return "принцип"
        if item == '4':
            return "оган, спирала, север"
        if item == '':
            return "принцип"
        if item == '5':
            return "човек"
        if item == '':
            return "принцип"
        if item == 'h':
            return "пролет"
        if item == '':
            return "принцип"
        if item == 'n':
            return "лето"
        if item == '':
            return "принцип"
        if item == 'a':
            return "есен"
        if item == '':
            return "принцип"
        if item == 'f':
            return "зима"
        if item == '':
            return "принцип"
        if item == 'k':
            return "?"
        if item == '':
            return "принцип"
        if item == 'u':
            return "?"
        if item == '':
            return "принцип"
        if item == 'o':
            return "?"
        if item == '':
            return "принцип"
        if item == 'g':
            return "?"
        if item == '':
            return "принцип"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "фрлање/фиксација"
        if item == 'n':
            return "фрлање"
        if item == '':
            return "фрлање/фиксација"
        if item == 'o':
            return "фиксација"
        if item == '':
            return "фрлање/фиксација"
        if item == 'x':
            return "фиксација фиксација"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "примање со телото, пад"
        if item == '1':
            return "?"
        if item == '':
            return "примање со телото, пад"
        if item == '2':
            return "пад напред"
        if item == '':
            return "примање со телото, пад"
        if item == '3':
            return "пад назад"
        if item == '':
            return "примање со телото, пад"
        if item == '4':
            return "пад на страна"
        if item == '':
            return "примање со телото, пад"
        if item == 'c':
            return "?"
        if item == '':
            return "примање со телото, пад"
        if item == '':
            return "примање со телото, пад"
        if item == 't':
            return "слободен пад"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "личност"
        if item == '1':
            return "основачот на аикидото, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "личност"
        if item == '2':
            return "син на основачот, втор дошу (27-06-1921 - 04-01-1999)"
        if item == '':
            return "личност"
        if item == '3':
            return "внук на основачот, трет дошу (02-04-1951)"
        if item == '':
            return "личност"
        if item == 't':
            return "ученик на ôsensei (13-12-1929)"
        if item == '':
            return "личност"
        if item == 'i':
            return "ученик на Тада шиханот, shihan (08-04-1940)"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "броење"
        if item == '0':
            return "нула"
        if item == '':
            return "броење"
        if item == '1':
            return "еден"
        if item == '':
            return "броење"
        if item == '2':
            return "два"
        if item == '':
            return "броење"
        if item == '3':
            return "три"
        if item == '':
            return "броење"
        if item == '4':
            return "четири"
        if item == '':
            return "броење"
        if item == '5':
            return "пет"
        if item == '':
            return "броење"
        if item == '6':
            return "шест"
        if item == '':
            return "броење"
        if item == '7':
            return "седум"
        if item == '':
            return "броење"
        if item == '8':
            return "осум"
        if item == '':
            return "броење"
        if item == '9':
            return "девет"
        if item == '':
            return "броење"
        if item == 'a':
            return "десет"
        if item == '':
            return "броење"
        if item == 'b':
            return "единаесет"
        if item == '':
            return "броење"
        if item == 'c':
            return "дваесет"
        if item == '':
            return "броење"
        if item == 'd':
            return "дваесет и еден"
        if item == '':
            return "броење"
        if item == 'e':
            return "сто"
        if item == '':
            return "броење"
        if item == 'f':
            return "илјада"
        if item == '':
            return "броење"
        if item == 'e':
            return "десет илјади"
        if item == '':
            return "броење"
        if item == 'h':
            return "?"
        if item == '':
            return "броење"
        if item == 'i':
            return "?"
        if item == '':
            return "броење"
        if item == 'j':
            return "?"
        if item == '':
            return "броење"
        if item == 'k':
            return "?"
        if item == '':
            return "броење"
        if item == 'l':
            return "?"
        if item == '':
            return "броење"
        if item == 'm':
            return "?"
        if item == '':
            return "броење"
        if item == 'n':
            return "?"
        if item == '':
            return "броење"
        if item == 'o':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "степени"
        if item == 'n':
            return "мајсторски степен - дан"
        if item == '':
            return "степени"
        if item == 'k':
            return "ученички степен - кју"
        if item == '':
            return "степени"
        if item == '0':
            return "без степен"
        if item == '':
            return "степени"
        if item == '6':
            return "шести кју"
        if item == '':
            return "степени"
        if item == '5':
            return "петти кју"
        if item == '':
            return "степени"
        if item == '4':
            return "четврти кју"
        if item == '':
            return "степени"
        if item == '3':
            return "трети кју"
        if item == '':
            return "степени"
        if item == '2':
            return "втори кју"
        if item == '':
            return "степени"
        if item == '1':
            return "прв кју"
        if item == '':
            return "степени"
        if item == 'y':
            return "носител на дан степен"
        if item == '':
            return "степени"
        if item == 'o':
            return "без дан"
        if item == '':
            return "степени"
        if item == 'a':
            return "прв дан"
        if item == '':
            return "степени"
        if item == 'b':
            return "втор дан"
        if item == '':
            return "степени"
        if item == 'c':
            return "трет дан"
        if item == '':
            return "степени"
        if item == 'd':
            return "четврт дан"
        if item == '':
            return "степени"
        if item == 'e':
            return "петти дан"
        if item == '':
            return "степени"
        if item == 'f':
            return "шести дан"
        if item == '':
            return "степени"
        if item == 'g':
            return "седми дан"
        if item == '':
            return "степени"
        if item == 'h':
            return "осми дан"
        if item == '':
            return "степени"
        if item == 'i':
            return "девети дан"
        if item == '':
            return "степени"
        if item == 'j':
            return "десети дан"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "општо"
        if item == '1':
            return "хармонија, здружување"
        if item == '':
            return "општо"
        if item == '2':
            return "енергија, сила"
        if item == '':
            return "општо"
        if item == '3':
            return "пат, наука"
        if item == '':
            return "општо"
        if item == '3':
            return "наука за силоускладување"
        if item == '':
            return "општо"
        if item == '4':
            return "вежбач на аикидо"
        if item == '':
            return "општо"
        if item == '5':
            return "Организација за промоција на аикидото(институт за силоускладување)"
        if item == '':
            return "општо"
        if item == '8':
            return "напаѓач [примач]"
        if item == '':
            return "општо"
        if item == '9':
            return "? [?]"
        if item == '':
            return "општо"
        if item == 'n':
            return "?"
        if item == '':
            return "општо"
        if item == 'u':
            return "?"
        if item == '':
            return "општо"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "упатства"
        if item == '1':
            return "ве молам повелете"
        if item == '':
            return "упатства"
        if item == '2':
            return "благодарам (на крај на вежбањето)"
        if item == '':
            return "упатства"
        if item == '3':
            return "да"
        if item == '':
            return "упатства"
        if item == '':
            return "упатства"
        if item == '5':
            return "сопри"
        if item == '':
            return "упатства"
        if item == '6':
            return "почни"
        if item == '':
            return "упатства"
        if item == '6':
            return "шести кју"
        if item == '':
            return "упатства"
        if item == '8':
            return "стани"
        if item == '':
            return "упатства"
        if item == '9':
            return "седни"
        if item == '':
            return "упатства"
        if item == 'a':
            return "сврти се"
        if item == '':
            return "упатства"
        if item == 'b':
            return "смени партнер"
        if item == '':
            return "упатства"
        if item == 'c':
            return "повтори ја вежбата"
        if item == '':
            return "упатства"
        if item == 'd':
            return "од другата страна"
        if item == '':
            return "упатства"
        if item == 'e':
            return "најди друг партнер"
        if item == '':
            return "упатства"
        if item == 'f':
            return "почит, поклони се"
        if item == '':
            return "упатства"
        if item == 'g':
            return "стоечко поклонување"
        if item == '':
            return "упатства"
        if item == 'h':
            return "седечко поклонување"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "наслови, титули"
        if item == 's':
            return "големиот учител"
        if item == '':
            return "наслови, титули"
        if item == 'o':
            return "учител, инструктор"
        if item == '':
            return "наслови, титули"
        if item == 'd':
            return "оној кој го покажува патот, првиот човек на дисциплината"
        if item == '':
            return "наслови, титули"
        if item == '7':
            return "главен учител (со најмалку 6-ти дан)"
        if item == '':
            return "наслови, титули"
        if item == '8':
            return "пошмик главен учител (4-ти или 5-ти дан)"
        if item == '':
            return "наслови, титули"
        if item == '9':
            return "пошник на шидоинот (2-ор или 3-ти дан)"
        if item == '':
            return "наслови, титули"
        if item == 'a':
            return "старешина"
        if item == '':
            return "наслови, титули"
        if item == 'b':
            return "јуниор"
        if item == '':
            return "наслови, титули"
        if item == 'c':
            return "без дан"
        if item == '':
            return "наслови, титули"
        if item == 'd':
            return "со дан"
        if item == '':
            return "наслови, титули"
        if item == 'e':
            return "глава на доџото"
        if item == '':
            return "наслови, титули"
        if item == 'f':
            return "ученик"
        if item == '':
            return "наслови, титули"
        if item == 'g':
            return "ученик кој живее во доџото"
        if item == '':
            return "наслови, титули"
        if item == 'h':
            return "ученик кој не живее во доџото"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "објекти"
        if item == '0':
            return "салата за вежбање (место за одредена дисциплина)"
        if item == '':
            return "објекти"
        if item == '1':
            return "челото на салата каде што стои сликата на основачот"
        if item == '':
            return "објекти"
        if item == '2':
            return "?"
        if item == '':
            return "објекти"
        if item == '3':
            return "?"
        if item == '':
            return "објекти"
        if item == '4':
            return "?"
        if item == '':
            return "објекти"
        if item == '5':
            return "душеци"
        if item == '':
            return "објекти"
        if item == '6':
            return "штаб"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "облека"
        if item == '1':
            return "облека за вежбање"
        if item == '':
            return "облека"
        if item == '2':
            return "поајс"
        if item == '':
            return "облека"
        if item == '3':
            return "бел појас"
        if item == '':
            return "облека"
        if item == '4':
            return "црн појас"
        if item == '':
            return "облека"
        if item == '5':
            return "чевли со одвоен палец"
        if item == '':
            return "облека"
        if item == '6':
            return "влечки"
        if item == '':
            return "облека"
        if item == '7':
            return "широки пантолоно од старојапонската носија"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "анатомија"
        if item == 'a':
            return "стомак, тежиште"
        if item == '':
            return "анатомија"
        if item == 'b':
            return "тело"
        if item == '':
            return "анатомија"
        if item == 'c':
            return "преден дел на главата"
        if item == '':
            return "анатомија"
        if item == 'd':
            return "страничен дел на главата"
        if item == '':
            return "анатомија"
        if item == 'e':
            return "колено"
        if item == '':
            return "анатомија"
        if item == 'f':
            return "врат"
        if item == '':
            return "анатомија"
        if item == 'g':
            return "гради"
        if item == '':
            return "анатомија"
        if item == 'e':
            return "рамо"
        if item == '':
            return "анатомија"
        if item == 'h':
            return "лакт"
        if item == '':
            return "анатомија"
        if item == 'i':
            return "рака"
        if item == '':
            return "анатомија"
        if item == 'j':
            return "зглоб"
        if item == '':
            return "анатомија"
        if item == 'k':
            return "дланка"
        if item == '':
            return "анатомија"
        if item == 'k':
            return "дланка меч"
        if item == '':
            return "анатомија"
        if item == 'l':
            return "нога, стопало"
        if item == '':
            return "анатомија"
        if item == 'm':
            return "глужд"
        if item == '':
            return "анатомија"
        if item == 'n':
            return "колкови"
        if item == '':
            return "анатомија"
        if item == 'o':
            return "крагна"
        if item == '':
            return "анатомија"
        if item == 'p':
            return "тело"
        if item == '':
            return "анатомија"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "разно"
        if item == 'a':
            return "взаемно избегнување"
        if item == '':
            return "разно"
        if item == 'b':
            return "вземен погодок"
        if item == '':
            return "разно"
        if item == 'c':
            return "удар"
        if item == '':
            return "разно"
        if item == 'd':
            return "воена наука"
        if item == '':
            return "разно"
        if item == 'e':
            return "вежби со стап со партнер"
        if item == '':
            return "разно"
        if item == 'f':
            return "вежби со меч со партнер"
        if item == '':
            return "разно"
        if item == 'g':
            return "одземање на меч"
        if item == '':
            return "разно"
        if item == 'h':
            return "одземање на нож"
        if item == '':
            return "разно"
        if item == 'i':
            return "покажување кон окото"
        if item == '':
            return "разно"
        if item == 'j':
            return "став"
        if item == '':
            return "разно"
        if item == 'm':
            return "?"
        if item == '':
            return "разно"
        if item == 's':
            return "?"
        if item == '':
            return "разно"
        if item == 't':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "правци"
        if item == 'h':
            return "лево"
        if item == '':
            return "правци"
        if item == 'm':
            return "десно"
        if item == '':
            return "правци"
        if item == 'i':
            return "влез"
        if item == '':
            return "правци"
        if item == 'k':
            return "одзади"
        if item == '':
            return "правци"
        if item == '1':
            return "напред"
        if item == '':
            return "правци"
        if item == '2':
            return "наназад"
        if item == '':
            return "правци"
        if item == '3':
            return "странично"
        if item == '':
            return "правци"
        if item == 'a':
            return "внатрешно"
        if item == '':
            return "правци"
        if item == 'b':
            return "надворешно"
        if item == '':
            return "правци"
        if item == 'n':
            return "?"
        if item == '':
            return "правци"
        if item == 'c':
            return "?"
        if item == '':
            return "правци"
        if item == 's':
            return "?"
        if item == '':
            return "правци"
        if item == 't':
            return "?"
        if item == '':
            return "правци"
        if item == 'x':
            return "спротивно"
        if item == '':
            return "правци"
        if item == '8':
            return "осум правци"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "?"
        if item == '1':
            return "?"
        if item == '':
            return "?"
        if item == '2':
            return "?"
        if item == '':
            return "?"
        if item == '3':
            return "?"
        if item == '':
            return "?"
        if item == '4':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == '7':
            return "?"
        if item == '':
            return "?"
        if item == '8':
            return "?"
        if item == '':
            return "?"
        if item == '9':
            return "?"
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'e':
            return "?"
        if item == '':
            return "?"
        if item == 'g':
            return "?"
        if item == '':
            return "?"
        if item == 'h':
            return "?"
        if item == '':
            return "?"
        if item == 'i':
            return "?"
        if item == '':
            return "?"
        if item == 'j':
            return "?"
        if item == '':
            return "?"
        if item == 'k':
            return "?"
        if item == '':
            return "?"
        if item == 'l':
            return "?"
        if item == '':
            return "?"
        if item == 'm':
            return "?"
        if item == '':
            return "?"
        if item == 'n':
            return "?"
        if item == '':
            return "?"
        if item == 'o':
            return "?"
        if item == '':
            return "?"
        if item == 'p':
            return "?"
        if item == '':
            return "?"
        if item == 'q':
            return "?"
        if item == '':
            return "?"
        if item == 'r':
            return "?"
        if item == '':
            return "?"
        if item == 's':
            return "?"
        if item == '':
            return "?"
        if item == 't':
            return "?"
        if item == '':
            return "?"
        if item == 'u':
            return "?"
        if item == '':
            return "?"
        if item == 'v':
            return "?"
        if item == '':
            return "?"
        if item == 'w':
            return "?"
        if item == '':
            return "?"
        if item == 'x':
            return "?"
        if item == '':
            return "?"
        if item == 'y':
            return "големи"
        if item == '':
            return "?"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "?"
        if item == '~':
            return "дишење во големи кругови [?]"
        if item == '':
            return "?"
        if item == '0':
            return "основна вежба за дишење [?]"
        if item == '':
            return "?"
        if item == '1':
            return "дишење со рацете во јанг позиција [?]"
        if item == '':
            return "?"
        if item == '2':
            return "дишење со рацете во јин позиција [?]"
        if item == '':
            return "?"
        if item == '3':
            return "дишење со рацете формирајќи крстесто движење [?]"
        if item == '':
            return "?"
        if item == '4':
            return "дишење 'да се стане едно со вселената' [?]"
        if item == '':
            return "?"
        if item == '5':
            return "?"
        if item == '':
            return "?"
        if item == '6':
            return "?"
        if item == '':
            return "?"
        if item == 'a':
            return "?"
        if item == '':
            return "?"
        if item == 'b':
            return "?"
        if item == '':
            return "?"
        if item == 'c':
            return "?"
        if item == '':
            return "?"
        if item == 'd':
            return "?"
        if item == '':
            return "?"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'sr':
    if list == 'ryu':
        if item == '':
            return "тип, начин"
        if item == 'a':
            return "начин да балансираш ки енергију"
        if item == '':
            return "тип, начин"
        if item == 'b':
            return "?"
        if item == '':
            return "тип, начин"
        if item == 'j':
            return "технике са штапом у којима се користи аики принцип"
        if item == '':
            return "тип, начин"
        if item == 'k':
            return "технике са мачем у којима се користи аики принцип"
        if item == '':
            return "тип, начин"
        if item == 'h':
            return "мач стил (мачевање)"
        if item == '':
            return "тип, начин"
        if item == 'j':
            return "мач стил (мачевање)"
        if item == '':
            return "тип, начин"
        if item == 'g':
            return "група здравствених вежби"
        if item == '':
            return "тип, начин"
        if item == 's':
            return "правилно усмерено тело"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "TODOдух"
        if item == 'a':
            return "наизменично вежбање нападањем два укеа без паузе"
        if item == '':
            return "TODOдух"
        if item == 'k':
            return "меко извођење технике"
        if item == '':
            return "TODOдух"
        if item == 't':
            return "тврдо, стегнуто извођење технике"
        if item == '':
            return "TODOдух"
        if item == 's':
            return "реалистично извођење технике"
        if item == '':
            return "TODOдух"
        if item == 'k':
            return "поремећај равнотеже"
        if item == '':
            return "TODOдух"
        if item == 'j':
            return "технике које се раде када напад долази rear?"
        if item == '':
            return "TODOдух"
        if item == 'j':
            return "слободне технике (тори ради технике по избору)"
        if item == '':
            return "TODOдух"
        if item == 'r':
            return "технике са више нападача"
        if item == '':
            return "TODOдух"
        if item == 's':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "позиција"
        if item == 's':
            return "технике које се изводе на коленима"
        if item == '':
            return "позиција"
        if item == 'h':
            return "технике при којим тори седи а уке стоји"
        if item == '':
            return "позиција"
        if item == 't':
            return "технике које се изводе у стојећем положају"
        if item == '':
            return "позиција"
        if item == '2':
            return "седење"
        if item == '':
            return "позиција"
        if item == '3':
            return "седење на коленима, стопала положена на поду"
        if item == '':
            return "позиција"
        if item == '4':
            return "седење на коленима, стопала подигнута у прстима"
        if item == '':
            return "позиција"
        if item == '5':
            return "седење на коленима док су кукови на поду, између стопала"
        if item == '':
            return "позиција"
        if item == '6':
            return "седење са ногама испруженим напред"
        if item == '':
            return "позиција"
        if item == '7':
            return "седење са испруженим и раширеним ногама"
        if item == '':
            return "позиција"
        if item == '8':
            return "седење са коленима наслоњеним на груди и стопалима на поду"
        if item == '':
            return "позиција"
        if item == '9':
            return "седење са спојеним стопалима и коленима на поду"
        if item == '':
            return "позиција"
        if item == '0':
            return "турско седење"
        if item == '':
            return "позиција"
        if item == 'j':
            return "позиција у облику броја 8"
        if item == '':
            return "позиција"
        if item == 'z':
            return "јога седење, позиција лотус"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == '':
            return "партнер"
        if item == 't':
            return "три или више нападача нападају континуирано, изводи се само почетак технике"
        if item == '':
            return "партнер"
        if item == 'k':
            return "наизменично вежбање са два или више нападача"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "оружје"
        if item == 'j':
            return "дрвени штап"
        if item == '':
            return "оружје"
        if item == 'o':
            return "дугачак дрвени штап"
        if item == '':
            return "оружје"
        if item == 'b':
            return "увијен дрвени мач"
        if item == '':
            return "оружје"
        if item == 't':
            return "нож"
        if item == '':
            return "оружје"
        if item == 'w':
            return "кратак самурајски увијен мач"
        if item == '':
            return "оружје"
        if item == 'k':
            return "дугачак самурајски увијен мач"
        if item == '':
            return "оружје"
        if item == 'a':
            return "дуг мач"
        if item == '':
            return "оружје"
        if item == 'e':
            return "мач"
        if item == '':
            return "оружје"
        if item == 'n':
            return "Јапански мач"
        if item == '':
            return "оружје"
        if item == 'n':
            return "?"
        if item == '':
            return "оружје"
        if item == 'y':
            return "копље"
        if item == '':
            return "оружје"
        if item == 's':
            return "штитник испред дршке на мачу"
        if item == '':
            return "оружје"
        if item == 's':
            return "корица оружја"
        if item == '':
            return "оружје"
        if item == 'u':
            return "држач за оружје"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "напад"
        if item == 'a':
            return "ударац са отвореним дланом који креће од кукова према глави"
        if item == '':
            return "напад"
        if item == 'b':
            return "хват за један ручни зглоб са исте (идентичне) стране. (десна на десну, лева на леву руку)"
        if item == '':
            return "напад"
        if item == 'c':
            return "хват за ручни зглоб са супротних страна. (лева на десну, десна на леву)"
        if item == '':
            return "напад"
        if item == 'd':
            return "хват на оба ручна зглоба"
        if item == '':
            return "напад"
        if item == 'e':
            return "ударац према предњем делу главе"
        if item == '':
            return "напад"
        if item == 'f':
            return "хват са две за једну руку"
        if item == '':
            return "напад"
        if item == 'g':
            return "хват за раме"
        if item == '':
            return "напад"
        if item == 'h':
            return "хват са обе руке на (from rear)"
        if item == '':
            return "напад"
        if item == 'i':
            return "ударац према једној страни главе (слепоочница)"
        if item == '':
            return "напад"
        if item == 'j':
            return "директан ударац ка средишњем делу тела"
        if item == '':
            return "напад"
        if item == 'k':
            return "хват за раме са једном руком, ударац са другом"
        if item == '':
            return "напад"
        if item == 'l':
            return "хавт са обе руке за рамена (from rear)"
        if item == '':
            return "напад"
        if item == 'm':
            return "директан ударац ка горњем делу тела"
        if item == '':
            return "напад"
        if item == 'n':
            return "хват са обе руке за крагну"
        if item == '':
            return "напад"
        if item == 'o':
            return "ударац са ногом"
        if item == '':
            return "напад"
        if item == 'p':
            return "дављење (from rear)"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "унутра/споља"
        if item == 'u':
            return "кретање са унутрашње стране"
        if item == '':
            return "унутра/споља"
        if item == 's':
            return "кретање са спољашње стране"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "кретање тела"
        if item == 'a':
            return "искорак са предњом ногом"
        if item == '':
            return "кретање тела"
        if item == 'b':
            return "искорак са задњом ногом"
        if item == '':
            return "кретање тела"
        if item == 'c':
            return "окрет око предње ноге"
        if item == '':
            return "кретање тела"
        if item == 'd':
            return "окрет око задње ноге"
        if item == '':
            return "кретање тела"
        if item == 'e':
            return "избегавајуће кретање повлачењем предње ноге у страну"
        if item == '':
            return "кретање тела"
        if item == 'f':
            return "избегавајуће кретање повлаћењем задње ноге у страну"
        if item == '':
            return "кретање тела"
        if item == 'g':
            return "искорак предњом ногом и окрет око ње"
        if item == '':
            return "кретање тела"
        if item == 'h':
            return "искорак задњом ногом и окрет око ње"
        if item == '':
            return "кретање тела"
        if item == 'i':
            return "избегавајуђе кретање, искорак предњом ногом и окрет око ње, затим повлађење задње ноге у страну"
        if item == '':
            return "кретање тела"
        if item == 'j':
            return "избегавајуће кретање, искорак задњом ногом и окрет око ње, затим повлаћење задње ноге у страну"
        if item == '':
            return "кретање тела"
        if item == 'k':
            return "комбиновано кретање"
        if item == '':
            return "кретање тела"
        if item == 'l':
            return "комбиновано кретање"
        if item == '':
            return "кретање тела"
        if item == 'm':
            return "?"
        if item == '':
            return "кретање тела"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "кретање руку"
        if item == 'k':
            return "половина круга уз горе"
        if item == '':
            return "кретање руку"
        if item == 's':
            return "круг уз доле (дно)"
        if item == '':
            return "кретање руку"
        if item == 't':
            return "?"
        if item == '':
            return "кретање руку"
        if item == 'y':
            return "?"
        if item == '':
            return "кретање руку"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "рука"
        if item == 'u':
            return "рука која удара"
        if item == '':
            return "рука"
        if item == 'k':
            return "рука која хвата за раме"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "ниво, висина"
        if item == 'g':
            return "ниско"
        if item == '':
            return "ниво, висина"
        if item == 'c':
            return "средиште (средина)"
        if item == '':
            return "ниво, висина"
        if item == 'j':
            return "високо"
        if item == '':
            return "ниво, висина"
        if item == '1':
            return "мали став"
        if item == '':
            return "ниво, висина"
        if item == '2':
            return "низак став"
        if item == '':
            return "ниво, висина"
        if item == '3':
            return "средишњи став"
        if item == '':
            return "ниво, висина"
        if item == '5':
            return "високи став"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "техника"
        if item == 'a':
            return "прво учење, први принцип"
        if item == '':
            return "техника"
        if item == 'b':
            return "друго учење, други принцип"
        if item == '':
            return "техника"
        if item == 'c':
            return "треће учење, трећи принцип"
        if item == '':
            return "техника"
        if item == 'd':
            return "четврто учење, четврти принцип"
        if item == '':
            return "техника"
        if item == 'e':
            return "?"
        if item == '':
            return "техника"
        if item == 'f':
            return "окретање зглоба"
        if item == '':
            return "техника"
        if item == 'g':
            return "пребацити споља?"
        if item == '':
            return "техника"
        if item == 'h':
            return "пребацивање у четири правца"
        if item == '':
            return "техника"
        if item == 'i':
            return "пето учење, пети принцип"
        if item == '':
            return "техника"
        if item == 'j':
            return "полуга блокирања лакта"
        if item == '':
            return "техника"
        if item == 'k':
            return "?"
        if item == '':
            return "техника"
        if item == 'l':
            return "?"
        if item == '':
            return "техника"
        if item == 'm':
            return "пребацивање укеа преко кукова са једне на другу страну"
        if item == '':
            return "техника"
        if item == 'n':
            return "спуштање испод нивоа нападача (укеа) и бацање подизањем његових ногу"
        if item == '':
            return "техника"
        if item == 'o':
            return "кружно бацање"
        if item == '':
            return "техника"
        if item == 'p':
            return "бацање користећи полугу на лакту"
        if item == '':
            return "техника"
        if item == 'q':
            return "спуштање руке у напред"
        if item == '':
            return "техника"
        if item == 'r':
            return "спуштање / лево-десно"
        if item == '':
            return "техника"
        if item == 's':
            return "спуштање / напред-назад"
        if item == '':
            return "техника"
        if item == 't':
            return "спуштање / спирална путања руке"
        if item == '':
            return "техника"
        if item == 'u':
            return "?"
        if item == '':
            return "техника"
        if item == 'v':
            return "?"
        if item == '':
            return "техника"
        if item == 'w':
            return "кружно кретање са полугом на руци"
        if item == '':
            return "техника"
        if item == 'x':
            return "?"
        if item == '':
            return "техника"
        if item == 'y':
            return "полуга са укрштеним рукама"
        if item == '':
            return "техника"
        if item == 'z':
            return "вежба дисања, покрети руку као за бацање"
        if item == '':
            return "техника"
        if item == '0':
            return "?"
        if item == '':
            return "техника"
        if item == '1':
            return "?"
        if item == '':
            return "техника"
        if item == '2':
            return "?"
        if item == '':
            return "техника"
        if item == '3':
            return "бацање преко кукова"
        if item == '':
            return "техника"
        if item == '4':
            return "?"
        if item == '':
            return "техника"
        if item == '5':
            return "?"
        if item == '':
            return "техника"
        if item == '6':
            return "уде гарами полуга"
        if item == '':
            return "техника"
        if item == '7':
            return "форма бацања преко руке?"
        if item == '':
            return "техника"
        if item == '8':
            return "форма бацања преко рамена?"
        if item == '':
            return "техника"
        if item == '9':
            return "форма бацања преко кукова?"
        if item == '':
            return "техника"
        if item == '~':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "испред нападача/иза нападача"
        if item == 'o':
            return "испред нападача"
        if item == '':
            return "испред нападача/иза нападача"
        if item == 'u':
            return "иза нападача"
        else:
            return 'unknown item %s for list %s' %(item, list)
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        if item == '':
            return "број"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'yin/yang':
        if item == '':
            return "јин/јанг"
        if item == '1':
            return "јин"
        if item == '':
            return "јин/јанг"
        if item == '2':
            return "јанг"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ri':
        if item == '':
            return "принцип"
        if item == '1':
            return "вода, горе-доле, исток"
        if item == '':
            return "принцип"
        if item == '2':
            return "земља, лево-десно, југ"
        if item == '':
            return "принцип"
        if item == '3':
            return "ветар, напред-назад, запад"
        if item == '':
            return "принцип"
        if item == '4':
            return "ватра, спирала, север"
        if item == '':
            return "принцип"
        if item == '5':
            return "човек"
        if item == '':
            return "принцип"
        if item == 'h':
            return "пролеће"
        if item == '':
            return "принцип"
        if item == 'n':
            return "лето"
        if item == '':
            return "принцип"
        if item == 'a':
            return "јесен"
        if item == '':
            return "принцип"
        if item == 'f':
            return "зима"
        if item == '':
            return "принцип"
        if item == 'k':
            return "?"
        if item == '':
            return "принцип"
        if item == 'u':
            return "?"
        if item == '':
            return "принцип"
        if item == 'o':
            return "?"
        if item == '':
            return "принцип"
        if item == 'g':
            return "?"
        if item == '':
            return "принцип"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "бацање/полуга"
        if item == 'n':
            return "бацање"
        if item == '':
            return "бацање/полуга"
        if item == 'o':
            return "полуга"
        if item == '':
            return "бацање/полуга"
        if item == 'x':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "пад у напред"
        if item == '1':
            return "?"
        if item == '':
            return "пад у напред"
        if item == '2':
            return "пад у напред"
        if item == '':
            return "пад у напред"
        if item == '3':
            return "пад у назад"
        if item == '':
            return "пад у напред"
        if item == '4':
            return "пад на страну"
        if item == '':
            return "пад у напред"
        if item == 'c':
            return "?"
        if item == '':
            return "пад у напред"
        if item == '':
            return "пад у напред"
        if item == 't':
            return "слободан пад"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "личност"
        if item == '1':
            return "оснивач аикидоа, ôsensei (14-12-1883 - 26-04-1969)"
        if item == '':
            return "личност"
        if item == '2':
            return "син основача, други дошу (27-06-1921 - 04-01-1999)"
        if item == '':
            return "личност"
        if item == '3':
            return "унук основача, трећи дошу (02-04-1951)"
        if item == '':
            return "личност"
        if item == 't':
            return "ученик ôsensei (13-12-1929)"
        if item == '':
            return "личност"
        if item == 'i':
            return "ученик Таде шихан, shihan(08-04-1940)"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        if item == '':
            return "личност"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kazueru':
        if item == '':
            return "броење"
        if item == '0':
            return "нула"
        if item == '':
            return "броење"
        if item == '1':
            return "један"
        if item == '':
            return "броење"
        if item == '2':
            return "два"
        if item == '':
            return "броење"
        if item == '3':
            return "три"
        if item == '':
            return "броење"
        if item == '4':
            return "четири"
        if item == '':
            return "броење"
        if item == '5':
            return "пет"
        if item == '':
            return "броење"
        if item == '6':
            return "шест"
        if item == '':
            return "броење"
        if item == '7':
            return "седам"
        if item == '':
            return "броење"
        if item == '8':
            return "осам"
        if item == '':
            return "броење"
        if item == '9':
            return "девет"
        if item == '':
            return "броење"
        if item == 'a':
            return "десет"
        if item == '':
            return "броење"
        if item == 'b':
            return "једанаест"
        if item == '':
            return "броење"
        if item == 'c':
            return "дванаест"
        if item == '':
            return "броење"
        if item == 'd':
            return "двадесет и један"
        if item == '':
            return "броење"
        if item == 'e':
            return "сто"
        if item == '':
            return "броење"
        if item == 'f':
            return "хиљаду"
        if item == '':
            return "броење"
        if item == 'e':
            return "десет хиљада"
        if item == '':
            return "броење"
        if item == 'h':
            return "прва форма"
        if item == '':
            return "броење"
        if item == 'i':
            return "друга форма"
        if item == '':
            return "броење"
        if item == 'j':
            return "трећа форма"
        if item == '':
            return "броење"
        if item == 'k':
            return "четврта форма"
        if item == '':
            return "броење"
        if item == 'l':
            return "пета форма"
        if item == '':
            return "броење"
        if item == 'm':
            return "шеста форма"
        if item == '':
            return "броење"
        if item == 'n':
            return "седма форма"
        if item == '':
            return "броење"
        if item == 'o':
            return "осма форма"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "степени"
        if item == 'n':
            return "мајсторски степен - дан"
        if item == '':
            return "степени"
        if item == 'k':
            return "ученички степен - кју"
        if item == '':
            return "степени"
        if item == '0':
            return "без степена"
        if item == '':
            return "степени"
        if item == '6':
            return "шести кју"
        if item == '':
            return "степени"
        if item == '5':
            return "пети кју"
        if item == '':
            return "степени"
        if item == '4':
            return "четврти кју"
        if item == '':
            return "степени"
        if item == '3':
            return "трећи кју"
        if item == '':
            return "степени"
        if item == '2':
            return "други кју"
        if item == '':
            return "степени"
        if item == '1':
            return "први кју"
        if item == '':
            return "степени"
        if item == 'y':
            return "носилац дан степена"
        if item == '':
            return "степени"
        if item == 'o':
            return "без дана"
        if item == '':
            return "степени"
        if item == 'a':
            return "први дан"
        if item == '':
            return "степени"
        if item == 'b':
            return "други дан"
        if item == '':
            return "степени"
        if item == 'c':
            return "трећи дан"
        if item == '':
            return "степени"
        if item == 'd':
            return "четврти дан"
        if item == '':
            return "степени"
        if item == 'e':
            return "пети дан"
        if item == '':
            return "степени"
        if item == 'f':
            return "шести дан"
        if item == '':
            return "степени"
        if item == 'g':
            return "седми дан"
        if item == '':
            return "степени"
        if item == 'h':
            return "осми дан"
        if item == '':
            return "степени"
        if item == 'i':
            return "девети дан"
        if item == '':
            return "степени"
        if item == 'j':
            return "десети дан"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "опште"
        if item == '1':
            return "хармонија, сједињење"
        if item == '':
            return "опште"
        if item == '2':
            return "енергија, сила"
        if item == '':
            return "опште"
        if item == '3':
            return "пут"
        if item == '':
            return "опште"
        if item == '3':
            return "наука (пут) ка усклађивању енергије"
        if item == '':
            return "опште"
        if item == '4':
            return "вежбач аикидо"
        if item == '':
            return "опште"
        if item == '5':
            return "Организација за промоције аикидоа"
        if item == '':
            return "опште"
        if item == '8':
            return "нападач [примач]"
        if item == '':
            return "опште"
        if item == '9':
            return "? [?]"
        if item == '':
            return "опште"
        if item == 'n':
            return "?"
        if item == '':
            return "опште"
        if item == 'u':
            return "родитељ, учитељ"
        if item == '':
            return "опште"
        if item == 's':
            return "дете, ученик"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "упутства"
        if item == '1':
            return "молим вас"
        if item == '':
            return "упутства"
        if item == '2':
            return "хвала"
        if item == '':
            return "упутства"
        if item == '3':
            return "да"
        if item == '':
            return "упутства"
        if item == '':
            return "упутства"
        if item == '5':
            return "стоп"
        if item == '':
            return "упутства"
        if item == '6':
            return "почни"
        if item == '':
            return "упутства"
        if item == '6':
            return "сачекајте, станите"
        if item == '':
            return "упутства"
        if item == '8':
            return "стани"
        if item == '':
            return "упутства"
        if item == '9':
            return "седни"
        if item == '':
            return "упутства"
        if item == 'a':
            return "окрени се"
        if item == '':
            return "упутства"
        if item == 'b':
            return "смена партнера"
        if item == '':
            return "упутства"
        if item == 'c':
            return "поновите вежбу"
        if item == '':
            return "упутства"
        if item == 'd':
            return "промените сртану"
        if item == '':
            return "упутства"
        if item == 'e':
            return "нађи другог партнера"
        if item == '':
            return "упутства"
        if item == 'f':
            return "почни, поклони се"
        if item == '':
            return "упутства"
        if item == 'g':
            return "стајаћи поклон"
        if item == '':
            return "упутства"
        if item == 'h':
            return "седећи поклон"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "наслови, титуле"
        if item == 's':
            return "велики учитељ"
        if item == '':
            return "наслови, титуле"
        if item == 'o':
            return "учитељ, инструктор"
        if item == '':
            return "наслови, титуле"
        if item == 'd':
            return "онај који показује пут"
        if item == '':
            return "наслови, титуле"
        if item == '7':
            return "главни учитељ (са најмање 6-тим даном)"
        if item == '':
            return "наслови, титуле"
        if item == '8':
            return "помоћни главни учитељ (4-ти или 5-ти дан)"
        if item == '':
            return "наслови, титуле"
        if item == '9':
            return "асистент инструктора (2-ги или 3-ћи дан)"
        if item == '':
            return "наслови, титуле"
        if item == 'a':
            return "старешина"
        if item == '':
            return "наслови, титуле"
        if item == 'b':
            return "млади ученик"
        if item == '':
            return "наслови, титуле"
        if item == 'c':
            return "особа без дана"
        if item == '':
            return "наслови, титуле"
        if item == 'd':
            return "оосба са даном"
        if item == '':
            return "наслови, титуле"
        if item == 'e':
            return "глава дођоа"
        if item == '':
            return "наслови, титуле"
        if item == 'f':
            return "ученик"
        if item == '':
            return "наслови, титуле"
        if item == 'g':
            return "ученик који живи у дођоу"
        if item == '':
            return "наслови, титуле"
        if item == 'h':
            return "ученик који не живи у дођоу"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "објекти"
        if item == '0':
            return "сала за вежбање"
        if item == '':
            return "објекти"
        if item == '1':
            return "место у сали на којем стоји слика оснивача"
        if item == '':
            return "објекти"
        if item == '2':
            return "?"
        if item == '':
            return "објекти"
        if item == '3':
            return "?"
        if item == '':
            return "објекти"
        if item == '4':
            return "?"
        if item == '':
            return "објекти"
        if item == '5':
            return "струњаче"
        if item == '':
            return "објекти"
        if item == '6':
            return "штаб"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "одећа"
        if item == '1':
            return "опрема за вежбање"
        if item == '':
            return "одећа"
        if item == '2':
            return "појас"
        if item == '':
            return "одећа"
        if item == '3':
            return "бели појас"
        if item == '':
            return "одећа"
        if item == '4':
            return "црни појас"
        if item == '':
            return "одећа"
        if item == '5':
            return "врста чарапа са одвојеним палцем"
        if item == '':
            return "одећа"
        if item == '6':
            return "папуче"
        if item == '':
            return "одећа"
        if item == '7':
            return "традиицоналне јапанске широке панталоне"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "анатомија"
        if item == 'a':
            return "стомак, тежиште"
        if item == '':
            return "анатомија"
        if item == 'b':
            return "тело"
        if item == '':
            return "анатомија"
        if item == 'c':
            return "предњи део главе"
        if item == '':
            return "анатомија"
        if item == 'd':
            return "једна страна главе"
        if item == '':
            return "анатомија"
        if item == 'e':
            return "колено"
        if item == '':
            return "анатомија"
        if item == 'f':
            return "врат"
        if item == '':
            return "анатомија"
        if item == 'g':
            return "груди"
        if item == '':
            return "анатомија"
        if item == 'e':
            return "раме"
        if item == '':
            return "анатомија"
        if item == 'h':
            return "лакат"
        if item == '':
            return "анатомија"
        if item == 'i':
            return "рука"
        if item == '':
            return "анатомија"
        if item == 'j':
            return "зглоб"
        if item == '':
            return "анатомија"
        if item == 'k':
            return "рука (длан, шака)"
        if item == '':
            return "анатомија"
        if item == 'k':
            return "ручни мач"
        if item == '':
            return "анатомија"
        if item == 'l':
            return "нога, стопало"
        if item == '':
            return "анатомија"
        if item == 'm':
            return "зглоб"
        if item == '':
            return "анатомија"
        if item == 'n':
            return "кукови"
        if item == '':
            return "анатомија"
        if item == 'o':
            return "крагна"
        if item == '':
            return "анатомија"
        if item == 'p':
            return "тело"
        if item == '':
            return "анатомија"
        if item == 's':
            return "рукав"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "разно"
        if item == 'a':
            return "међусобно избегавање"
        if item == '':
            return "разно"
        if item == 'b':
            return "?"
        if item == '':
            return "разно"
        if item == 'c':
            return "удар"
        if item == '':
            return "разно"
        if item == 'd':
            return "начин борења"
        if item == '':
            return "разно"
        if item == 'e':
            return "вежбе са штапом, са партнером"
        if item == '':
            return "разно"
        if item == 'f':
            return "вежбе са мачем, са партнером"
        if item == '':
            return "разно"
        if item == 'g':
            return "одузимање мача"
        if item == '':
            return "разно"
        if item == 'h':
            return "одузимање ножа"
        if item == '':
            return "разно"
        if item == 'i':
            return "показивање на око"
        if item == '':
            return "разно"
        if item == 'j':
            return "став"
        if item == '':
            return "разно"
        if item == 'm':
            return "?"
        if item == '':
            return "разно"
        if item == 's':
            return "?"
        if item == '':
            return "разно"
        if item == 't':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "правци"
        if item == 'h':
            return "лево"
        if item == '':
            return "правци"
        if item == 'm':
            return "десно"
        if item == '':
            return "правци"
        if item == 'i':
            return "улаз"
        if item == '':
            return "правци"
        if item == 'k':
            return "окрет"
        if item == '':
            return "правци"
        if item == '1':
            return "напред"
        if item == '':
            return "правци"
        if item == '2':
            return "према назад"
        if item == '':
            return "правци"
        if item == '3':
            return "са сране"
        if item == '':
            return "правци"
        if item == 'a':
            return "унутар"
        if item == '':
            return "правци"
        if item == 'b':
            return "споља"
        if item == '':
            return "правци"
        if item == 'n':
            return "диагонално"
        if item == '':
            return "правци"
        if item == 'c':
            return "вертикално"
        if item == '':
            return "правци"
        if item == 's':
            return "хоризонтално"
        if item == '':
            return "правци"
        if item == 't':
            return "стајање"
        if item == '':
            return "правци"
        if item == 'x':
            return "супротно, против"
        if item == '':
            return "правци"
        if item == '8':
            return "осам праваца"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "вежба"
        if item == '1':
            return "?"
        if item == '':
            return "вежба"
        if item == '2':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "установљени принцип"
        if item == '1':
            return "пролећни мач"
        if item == '':
            return "установљени принцип"
        if item == '2':
            return "летњи мач"
        if item == '':
            return "установљени принцип"
        if item == '3':
            return "јесењи мач"
        if item == '':
            return "установљени принцип"
        if item == '4':
            return "зимски мач"
        if item == '':
            return "установљени принцип"
        if item == '5':
            return "осам праваца"
        if item == '':
            return "установљени принцип"
        if item == '6':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == '7':
            return "доба промене"
        if item == '':
            return "установљени принцип"
        if item == '8':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == '9':
            return "примити"
        if item == '':
            return "установљени принцип"
        if item == 'a':
            return "телесни мач"
        if item == '':
            return "установљени принцип"
        if item == 'b':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'c':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'd':
            return "складно показивање (упозоравање) на око"
        if item == '':
            return "установљени принцип"
        if item == 'e':
            return "убрзати, ургирати"
        if item == '':
            return "установљени принцип"
        if item == 'g':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'h':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'i':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'j':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'k':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'l':
            return "обе руке"
        if item == '':
            return "установљени принцип"
        if item == 'm':
            return "вежба гурања"
        if item == '':
            return "установљени принцип"
        if item == 'n':
            return "линија"
        if item == '':
            return "установљени принцип"
        if item == 'o':
            return "блокирано тело"
        if item == '':
            return "установљени принцип"
        if item == 'p':
            return "контрола тела"
        if item == '':
            return "установљени принцип"
        if item == 'q':
            return "непогођен"
        if item == '':
            return "установљени принцип"
        if item == 'r':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 's':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 't':
            return "?"
        if item == '':
            return "установљени принцип"
        if item == 'u':
            return "сећи"
        if item == '':
            return "установљени принцип"
        if item == 'v':
            return "зауставити"
        if item == '':
            return "установљени принцип"
        if item == 'w':
            return "узвратити ударац"
        if item == '':
            return "установљени принцип"
        if item == 'x':
            return "зора"
        if item == '':
            return "установљени принцип"
        if item == 'y':
            return "велико"
        if item == '':
            return "установљени принцип"
        if item == 'z':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "група здравствених вежби"
        if item == '~':
            return "дисање у великим круговима [?]"
        if item == '':
            return "група здравствених вежби"
        if item == '0':
            return "основна вежба за дисање [?]"
        if item == '':
            return "група здравствених вежби"
        if item == '1':
            return "дисање са рукама у јанг позицији [?]"
        if item == '':
            return "група здравствених вежби"
        if item == '2':
            return "дисање са рукама у јин позицији [?]"
        if item == '':
            return "група здравствених вежби"
        if item == '3':
            return "дисање енергијом руку које формирају крст [?]"
        if item == '':
            return "група здравствених вежби"
        if item == '4':
            return "дицање 'постати једно са универзумом [?]"
        if item == '':
            return "група здравствених вежби"
        if item == '5':
            return "?"
        if item == '':
            return "група здравствених вежби"
        if item == '6':
            return "?"
        if item == '':
            return "група здравствених вежби"
        if item == 'a':
            return "метод осцилације"
        if item == '':
            return "група здравствених вежби"
        if item == 'b':
            return "?"
        if item == '':
            return "група здравствених вежби"
        if item == 'c':
            return "?"
        if item == '':
            return "група здравствених вежби"
        if item == 'd':
            return "?"
        if item == '':
            return "група здравствених вежби"
        if item == 'u':
            return "?"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
return 'untranslated list %s and item %s for language %s' %(list, item, context.REQUEST['LANGUAGE'])
