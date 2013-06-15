## Script (Python) "formatRomaji"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=list, item
##title=return formatted romaji for given glossary list item and item item
##
# This Python file uses the following encoding: utf-8
if context.REQUEST['LANGUAGE'] == 'nl':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'de':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'en':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'fr':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'cz':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'mk':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
if context.REQUEST['LANGUAGE'] == 'sr':
    if list == 'ryu':
        if item == '':
            return "ryû"
        if item == 'a':
            return "ai·ki·dô"
        if item == '':
            return "ryû"
        if item == 'b':
            return "ai·ki·jutsu"
        if item == '':
            return "ryû"
        if item == 'j':
            return "ai·ki·jô"
        if item == '':
            return "ryû"
        if item == 'k':
            return "ai·ki·ken"
        if item == '':
            return "ryû"
        if item == 'h':
            return "ho·jo kata"
        if item == '':
            return "ryû"
        if item == 'j':
            return "Kashima Shinden Jikishinkage-ryû"
        if item == '':
            return "ryû"
        if item == 'g':
            return "gen·ki·kai"
        if item == '':
            return "ryû"
        if item == 's':
            return "sei·tai"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'keikoho':
        if item == '':
            return "keiko hô"
        if item == 'a':
            return "kakari kei·ko"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kigata"
        if item == '':
            return "keiko hô"
        if item == 't':
            return "tan·ren"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "shin·ken"
        if item == '':
            return "keiko hô"
        if item == 'k':
            return "kuzushi"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ushi·ro·waza"
        if item == '':
            return "keiko hô"
        if item == 'j':
            return "ji·yû waza"
        if item == '':
            return "keiko hô"
        if item == 'r':
            return "ran·do·ri"
        if item == '':
            return "keiko hô"
        if item == 's':
            return "su·bu·ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "suwa·ri waza"
        if item == '':
            return "?"
        if item == 'h':
            return "han·mi han·da·chi waza"
        if item == '':
            return "?"
        if item == 't':
            return "ta·chi waza"
        if item == '':
            return "?"
        if item == '2':
            return "za"
        if item == '':
            return "?"
        if item == '3':
            return "sei·za"
        if item == '':
            return "?"
        if item == '4':
            return "ki·za"
        if item == '':
            return "?"
        if item == '5':
            return "wari·za"
        if item == '':
            return "?"
        if item == '6':
            return "cho·za"
        if item == '':
            return "?"
        if item == '7':
            return "kai·za"
        if item == '':
            return "?"
        if item == '8':
            return "tai·za"
        if item == '':
            return "?"
        if item == '9':
            return "gaku·za"
        if item == '':
            return "?"
        if item == '0':
            return "an·za"
        if item == '':
            return "?"
        if item == 'j':
            return "hassô"
        if item == '':
            return "?"
        if item == 'z':
            return "kahuza"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'aite':
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == '':
            return "ai·te"
        if item == 't':
            return "ta·nin·zû to·ri"
        if item == '':
            return "ai·te"
        if item == 'k':
            return "ka·ka·ri gei·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'buki':
        if item == '':
            return "bu·ki"
        if item == 'j':
            return "jô"
        if item == '':
            return "bu·ki"
        if item == 'o':
            return "bô"
        if item == '':
            return "bu·ki"
        if item == 'b':
            return "bok·ken, boku·tô"
        if item == '':
            return "bu·ki"
        if item == 't':
            return "tan·tô"
        if item == '':
            return "bu·ki"
        if item == 'w':
            return "waki·zashi, shoto"
        if item == '':
            return "bu·ki"
        if item == 'k':
            return "(ken?,) katana"
        if item == '':
            return "bu·ki"
        if item == 'a':
            return "ta·chi"
        if item == '':
            return "bu·ki"
        if item == 'e':
            return "ken"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "ni·hon·tô"
        if item == '':
            return "bu·ki"
        if item == 'n':
            return "naginata"
        if item == '':
            return "bu·ki"
        if item == 'y':
            return "yari"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "tsuba"
        if item == '':
            return "bu·ki"
        if item == 's':
            return "saya"
        if item == '':
            return "bu·ki"
        if item == 'u':
            return "bugukake"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kokukegi':
        if item == '':
            return "koku·kegi"
        if item == 'a':
            return "ki·a·wa·se shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'b':
            return "kata·te do·ri ai han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'c':
            return "kata·te do·ri gyaku han·mi"
        if item == '':
            return "koku·kegi"
        if item == 'd':
            return "ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'e':
            return "shô·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'f':
            return "kata·te ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'g':
            return "kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'h':
            return "ushi·ro ryô·te do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'i':
            return "yoko·men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'j':
            return "chû·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'k':
            return "kata do·ri men u·chi"
        if item == '':
            return "koku·kegi"
        if item == 'l':
            return "ushi·ro ryô·kata do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'm':
            return "jô·dan tsu·ki"
        if item == '':
            return "koku·kegi"
        if item == 'n':
            return "ryô·eri do·ri"
        if item == '':
            return "koku·kegi"
        if item == 'o':
            return "ke·ri"
        if item == '':
            return "koku·kegi"
        if item == 'p':
            return "ushi·ro kubi jime"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'uchi/soto':
        if item == '':
            return "uchi/soto"
        if item == 'u':
            return "uchi saba·ki"
        if item == '':
            return "uchi/soto"
        if item == 's':
            return "soto saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'taisabaki':
        if item == '':
            return "tai saba·ki"
        if item == 'a':
            return "mae ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'b':
            return "ushi·ro ashi iri·mi"
        if item == '':
            return "tai saba·ki"
        if item == 'c':
            return "mae ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'd':
            return "ushi·ro ashi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'e':
            return "mae ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'f':
            return "ushi·ro ashi tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'g':
            return "mae ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'h':
            return "ushi·ro ashi iri·mi ten·kan"
        if item == '':
            return "tai saba·ki"
        if item == 'i':
            return "mae ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'j':
            return "ushi·ro ashi iri·mi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'k':
            return "mae ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'l':
            return "ushi·ro ashi ten·kan tenshin"
        if item == '':
            return "tai saba·ki"
        if item == 'm':
            return "ushi·ro ashi iri·mi tenkai"
        if item == '':
            return "tai saba·ki"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'tesabaki':
        if item == '':
            return "te saba·ki"
        if item == 'k':
            return "kami han·en"
        if item == '':
            return "te saba·ki"
        if item == 's':
            return "shimo han·en"
        if item == '':
            return "te saba·ki"
        if item == 't':
            return "te·kubi gae·shi"
        if item == '':
            return "te saba·ki"
        if item == 'y':
            return "jyû·ji musu·bi"
        if item == '':
            return "te saba·ki"
        if item == 'u':
            return "uke naga·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'note':
        if item == '':
            return "no·te"
        if item == 'u':
            return "u·chi·no·te"
        if item == '':
            return "no·te"
        if item == 'k':
            return "kata·no·te"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dan':
        if item == '':
            return "dan"
        if item == 'g':
            return "ge·dan"
        if item == '':
            return "dan"
        if item == 'c':
            return "chû·dan"
        if item == '':
            return "dan"
        if item == 'j':
            return "jô·dan"
        if item == '':
            return "dan"
        if item == '1':
            return "waki gamae"
        if item == '':
            return "dan"
        if item == '2':
            return "ge·dan no kama·e"
        if item == '':
            return "dan"
        if item == '3':
            return "chû·dan no kama·e"
        if item == '':
            return "dan"
        if item == '5':
            return "jô·dan no kamae"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'waza':
        if item == '':
            return "waza"
        if item == 'a':
            return "ik·kyô"
        if item == '':
            return "waza"
        if item == 'b':
            return "ni·kyô"
        if item == '':
            return "waza"
        if item == 'c':
            return "san·kyô"
        if item == '':
            return "waza"
        if item == 'd':
            return "yon·kyô"
        if item == '':
            return "waza"
        if item == 'e':
            return "sumi·oto·shi"
        if item == '':
            return "waza"
        if item == 'f':
            return "ko·te·gae·shi"
        if item == '':
            return "waza"
        if item == 'g':
            return "iri·mi·na·ge"
        if item == '':
            return "waza"
        if item == 'h':
            return "shi·hô·na·ge"
        if item == '':
            return "waza"
        if item == 'i':
            return "go·kyô"
        if item == '':
            return "waza"
        if item == 'j':
            return "hiji ki·me osa·e"
        if item == '':
            return "waza"
        if item == 'k':
            return "uchi·kai·ten·san·kyô"
        if item == '':
            return "waza"
        if item == 'l':
            return "ude gara·mi"
        if item == '':
            return "waza"
        if item == 'm':
            return "ai·ki·goshi"
        if item == '':
            return "waza"
        if item == 'n':
            return "ai·ki·oto·shi"
        if item == '':
            return "waza"
        if item == 'o':
            return "kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'p':
            return "ude ki·me na·ge"
        if item == '':
            return "waza"
        if item == 'q':
            return "mae·oto·shi"
        if item == '':
            return "waza"
        if item == 'r':
            return "hiki·oto·shi"
        if item == '':
            return "waza"
        if item == 's':
            return "ki·ri oto·shi"
        if item == '':
            return "waza"
        if item == 't':
            return "kai·ten·oto·shi"
        if item == '':
            return "waza"
        if item == 'u':
            return "ten chi na·ge"
        if item == '':
            return "waza"
        if item == 'v':
            return "gen·kei·ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == 'w':
            return "uchi·kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == 'x':
            return "furi·zu·ki ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == 'y':
            return "jyû·ji gara·mi"
        if item == '':
            return "waza"
        if item == 'z':
            return "to·ri fune ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '0':
            return "shi·hô ge·ri ko·kyû·na·ge"
        if item == '':
            return "waza"
        if item == '1':
            return "ude gara·mi san·kyô na·ge"
        if item == '':
            return "waza"
        if item == '2':
            return "ude gara·mi yon·kyô na·ge"
        if item == '':
            return "waza"
        if item == '3':
            return "koshi na·ge"
        if item == '':
            return "waza"
        if item == '4':
            return "soto kai·ten·na·ge"
        if item == '':
            return "waza"
        if item == '5':
            return "zan·to ko·kyû na·ge"
        if item == '':
            return "waza"
        if item == '6':
            return "ude gara·mi osa·e"
        if item == '':
            return "waza"
        if item == '7':
            return "te guruma"
        if item == '':
            return "waza"
        if item == '8':
            return "se·o·i guruma"
        if item == '':
            return "waza"
        if item == '9':
            return "koshi guruma"
        if item == '':
            return "waza"
        if item == '~':
            return "chin shin koshi guruma"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'omote/ura':
        if item == '':
            return "omote/ura"
        if item == 'o':
            return "omote"
        if item == '':
            return "omote/ura"
        if item == 'u':
            return "ura"
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
            return "ri"
        if item == '1':
            return "su, mizu"
        if item == '':
            return "ri"
        if item == '2':
            return "do, tsu"
        if item == '':
            return "ri"
        if item == '3':
            return "hu"
        if item == '':
            return "ri"
        if item == '4':
            return "ka, hi"
        if item == '':
            return "ri"
        if item == '5':
            return "complete?"
        if item == '':
            return "ri"
        if item == 'h':
            return "haru"
        if item == '':
            return "ri"
        if item == 'n':
            return "natsu"
        if item == '':
            return "ri"
        if item == 'a':
            return "aki"
        if item == '':
            return "ri"
        if item == 'f':
            return "fuyu"
        if item == '':
            return "ri"
        if item == 'k':
            return "kô·bô no gen·ri"
        if item == '':
            return "ri"
        if item == 'u':
            return "u·chi no ri"
        if item == '':
            return "ri"
        if item == 'o':
            return "osa·e no ri"
        if item == '':
            return "ri"
        if item == 'g':
            return "na·ge no ri"
        if item == '':
            return "ri"
        if item == 'z':
            return "zan no ri"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'nage/osae':
        if item == '':
            return "nage/osae"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "nage/osae"
        if item == 'o':
            return "osa·e"
        if item == '':
            return "nage/osae"
        if item == 'x':
            return "na·ge osa·e"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ukemi':
        if item == '':
            return "u·ke·mi"
        if item == '1':
            return "boven onder u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '2':
            return "mae u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '3':
            return "ushi·ro u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == '4':
            return "yoko u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 'c':
            return "chokuto"
        if item == '':
            return "u·ke·mi"
        if item == '':
            return "u·ke·mi"
        if item == 't':
            return "to·bi u·ke·mi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "Ueshiba, Morihei"
        if item == '':
            return "?"
        if item == '2':
            return "Ueshiba, Kisshomaru"
        if item == '':
            return "?"
        if item == '3':
            return "Moriteru Ueshiba"
        if item == '':
            return "?"
        if item == 't':
            return "Tada, Hiroshi"
        if item == '':
            return "?"
        if item == 'i':
            return "Ikeda, Masatomi"
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
    if list == 'kazueru':
        if item == '':
            return "kazu·e·ru"
        if item == '0':
            return "zero"
        if item == '':
            return "kazu·e·ru"
        if item == '1':
            return "ichi"
        if item == '':
            return "kazu·e·ru"
        if item == '2':
            return "ni"
        if item == '':
            return "kazu·e·ru"
        if item == '3':
            return "san"
        if item == '':
            return "kazu·e·ru"
        if item == '4':
            return "shi, yon"
        if item == '':
            return "kazu·e·ru"
        if item == '5':
            return "go"
        if item == '':
            return "kazu·e·ru"
        if item == '6':
            return "roku"
        if item == '':
            return "kazu·e·ru"
        if item == '7':
            return "shichi, nana"
        if item == '':
            return "kazu·e·ru"
        if item == '8':
            return "hachi"
        if item == '':
            return "kazu·e·ru"
        if item == '9':
            return "ku, kyû"
        if item == '':
            return "kazu·e·ru"
        if item == 'a':
            return "jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'b':
            return "jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'c':
            return "ni jû"
        if item == '':
            return "kazu·e·ru"
        if item == 'd':
            return "ni jû ichi"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "hyaku"
        if item == '':
            return "kazu·e·ru"
        if item == 'f':
            return "sen"
        if item == '':
            return "kazu·e·ru"
        if item == 'e':
            return "man"
        if item == '':
            return "kazu·e·ru"
        if item == 'h':
            return "ip·pon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'i':
            return "ni·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'j':
            return "san·bon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'k':
            return "yon·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'l':
            return "go·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'm':
            return "roku·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'n':
            return "nana·hon·me"
        if item == '':
            return "kazu·e·ru"
        if item == 'o':
            return "hachi·hon·me"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'dankai':
        if item == '':
            return "dan·kai"
        if item == 'n':
            return "dan"
        if item == '':
            return "dan·kai"
        if item == 'k':
            return "kyû"
        if item == '':
            return "dan·kai"
        if item == '0':
            return "mu·kyû"
        if item == '':
            return "dan·kai"
        if item == '6':
            return "rok·kyû"
        if item == '':
            return "dan·kai"
        if item == '5':
            return "go·kyû"
        if item == '':
            return "dan·kai"
        if item == '4':
            return "yon·kyû"
        if item == '':
            return "dan·kai"
        if item == '3':
            return "san·kyû"
        if item == '':
            return "dan·kai"
        if item == '2':
            return "ni·kyû"
        if item == '':
            return "dan·kai"
        if item == '1':
            return "ik·kyû"
        if item == '':
            return "dan·kai"
        if item == 'y':
            return "yû·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'o':
            return "mu·dan·sha"
        if item == '':
            return "dan·kai"
        if item == 'a':
            return "sho·dan"
        if item == '':
            return "dan·kai"
        if item == 'b':
            return "ni·dan"
        if item == '':
            return "dan·kai"
        if item == 'c':
            return "san·dan"
        if item == '':
            return "dan·kai"
        if item == 'd':
            return "yon·dan"
        if item == '':
            return "dan·kai"
        if item == 'e':
            return "go·dan"
        if item == '':
            return "dan·kai"
        if item == 'f':
            return "roku·dan"
        if item == '':
            return "dan·kai"
        if item == 'g':
            return "nana·dan"
        if item == '':
            return "dan·kai"
        if item == 'h':
            return "hachi·dan"
        if item == '':
            return "dan·kai"
        if item == 'i':
            return "ku·dan"
        if item == '':
            return "dan·kai"
        if item == 'j':
            return "jyû·dan"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "ai"
        if item == '':
            return "?"
        if item == '2':
            return "ki"
        if item == '':
            return "?"
        if item == '3':
            return "dô"
        if item == '':
            return "?"
        if item == '3':
            return "ai·ki·dô"
        if item == '':
            return "?"
        if item == '4':
            return "ai·ki·dô·ka"
        if item == '':
            return "?"
        if item == '5':
            return "ai·ki·kai"
        if item == '':
            return "?"
        if item == '8':
            return "u·ke"
        if item == '':
            return "?"
        if item == '9':
            return "to·ri"
        if item == '':
            return "?"
        if item == 'n':
            return "na·ge"
        if item == '':
            return "?"
        if item == 'u':
            return "uchi·da·chi"
        if item == '':
            return "?"
        if item == 's':
            return "shi·da·chi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '1':
            return "o·nega·i shi·ma·su"
        if item == '':
            return "?"
        if item == '2':
            return "do·o·mo a·ri·ga·to·o go·za·i·ma·shi·ta"
        if item == '':
            return "?"
        if item == '3':
            return "hai"
        if item == '':
            return "?"
        if item == '':
            return "?"
        if item == '5':
            return "yame"
        if item == '':
            return "?"
        if item == '6':
            return "haji·me"
        if item == '':
            return "?"
        if item == '6':
            return "ma·t·te"
        if item == '':
            return "?"
        if item == '8':
            return "ta·te"
        if item == '':
            return "?"
        if item == '9':
            return "suwatte"
        if item == '':
            return "?"
        if item == 'a':
            return "mawatte"
        if item == '':
            return "?"
        if item == 'b':
            return "ko·tai"
        if item == '':
            return "?"
        if item == 'c':
            return "mo·ri·kai"
        if item == '':
            return "?"
        if item == 'd':
            return "han·tai"
        if item == '':
            return "?"
        if item == 'e':
            return "ai·te kaite"
        if item == '':
            return "?"
        if item == 'f':
            return "rei"
        if item == '':
            return "?"
        if item == 'g':
            return "ritsu·rei"
        if item == '':
            return "?"
        if item == 'h':
            return "za·rei"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 's':
            return "ô·sen·sei"
        if item == '':
            return "?"
        if item == 'o':
            return "sen·sei"
        if item == '':
            return "?"
        if item == 'd':
            return "dô·shu"
        if item == '':
            return "?"
        if item == '7':
            return "shi·han"
        if item == '':
            return "?"
        if item == '8':
            return "shi·do·in"
        if item == '':
            return "?"
        if item == '9':
            return "fuku·shi·do·in"
        if item == '':
            return "?"
        if item == 'a':
            return "sen·pai"
        if item == '':
            return "?"
        if item == 'b':
            return "kô·hai"
        if item == '':
            return "?"
        if item == 'c':
            return "mu·dan·sha"
        if item == '':
            return "?"
        if item == 'd':
            return "yû·dan·sha"
        if item == '':
            return "?"
        if item == 'e':
            return "dô·jô·cho"
        if item == '':
            return "?"
        if item == 'f':
            return "de·shi"
        if item == '':
            return "?"
        if item == 'g':
            return "uchi·de·shi"
        if item == '':
            return "?"
        if item == 'h':
            return "soto·de·shi"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == '0':
            return "dô·jô"
        if item == '':
            return "?"
        if item == '1':
            return "kamiza"
        if item == '':
            return "?"
        if item == '2':
            return "shomiza"
        if item == '':
            return "?"
        if item == '3':
            return "joseki"
        if item == '':
            return "?"
        if item == '4':
            return "shimoseki"
        if item == '':
            return "?"
        if item == '5':
            return "tatami"
        if item == '':
            return "?"
        if item == '6':
            return "hom·bu"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'ifuku':
        if item == '':
            return "i·fuku"
        if item == '1':
            return "kei·ko·gi"
        if item == '':
            return "i·fuku"
        if item == '2':
            return "obi"
        if item == '':
            return "i·fuku"
        if item == '3':
            return "shiro·obi"
        if item == '':
            return "i·fuku"
        if item == '4':
            return "kuro·obi"
        if item == '':
            return "i·fuku"
        if item == '5':
            return "tabi"
        if item == '':
            return "i·fuku"
        if item == '6':
            return "zori"
        if item == '':
            return "i·fuku"
        if item == '7':
            return "hakama"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'kakobogaku':
        if item == '':
            return "kako·bô·gaku"
        if item == 'a':
            return "hara"
        if item == '':
            return "kako·bô·gaku"
        if item == 'b':
            return "tai"
        if item == '':
            return "kako·bô·gaku"
        if item == 'c':
            return "shô·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'd':
            return "yoko·men"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "hiza"
        if item == '':
            return "kako·bô·gaku"
        if item == 'f':
            return "kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'g':
            return "mune"
        if item == '':
            return "kako·bô·gaku"
        if item == 'e':
            return "kata"
        if item == '':
            return "kako·bô·gaku"
        if item == 'h':
            return "hiji"
        if item == '':
            return "kako·bô·gaku"
        if item == 'i':
            return "ude"
        if item == '':
            return "kako·bô·gaku"
        if item == 'j':
            return "te·kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te"
        if item == '':
            return "kako·bô·gaku"
        if item == 'k':
            return "te·gatana"
        if item == '':
            return "kako·bô·gaku"
        if item == 'l':
            return "ashi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'm':
            return "asho kubi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'n':
            return "koshi"
        if item == '':
            return "kako·bô·gaku"
        if item == 'o':
            return "eri"
        if item == '':
            return "kako·bô·gaku"
        if item == 'p':
            return "mi"
        if item == '':
            return "kako·bô·gaku"
        if item == 's':
            return "sode"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'a':
            return "ai·nuke"
        if item == '':
            return "?"
        if item == 'b':
            return "ai·uchi"
        if item == '':
            return "?"
        if item == 'c':
            return "a·te·mi"
        if item == '':
            return "?"
        if item == 'd':
            return "budo"
        if item == '':
            return "?"
        if item == 'e':
            return "kumi·jô"
        if item == '':
            return "?"
        if item == 'f':
            return "kumi·ta·chi"
        if item == '':
            return "?"
        if item == 'g':
            return "ta·chi·do·ri"
        if item == '':
            return "?"
        if item == 'h':
            return "tan·to·do·ri"
        if item == '':
            return "?"
        if item == 'i':
            return "sei·gan"
        if item == '':
            return "?"
        if item == 'j':
            return "kama·e"
        if item == '':
            return "?"
        if item == 'm':
            return "ma·a·i"
        if item == '':
            return "?"
        if item == 's':
            return "shikkou"
        if item == '':
            return "?"
        if item == 't':
            return "tai·ko"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == '?':
        if item == '':
            return "?"
        if item == 'h':
            return "hidari"
        if item == '':
            return "?"
        if item == 'm':
            return "migi"
        if item == '':
            return "?"
        if item == 'i':
            return "iri·mi"
        if item == '':
            return "?"
        if item == 'k':
            return "kai·ten"
        if item == '':
            return "?"
        if item == '1':
            return "mae"
        if item == '':
            return "?"
        if item == '2':
            return "ushi·ro"
        if item == '':
            return "?"
        if item == '3':
            return "yoko"
        if item == '':
            return "?"
        if item == 'a':
            return "uchi"
        if item == '':
            return "?"
        if item == 'b':
            return "soto"
        if item == '':
            return "?"
        if item == 'n':
            return "nana·me"
        if item == '':
            return "?"
        if item == 'c':
            return "choku·ritsu"
        if item == '':
            return "?"
        if item == 's':
            return "sui·hei"
        if item == '':
            return "?"
        if item == 't':
            return "ta·te"
        if item == '':
            return "?"
        if item == 'x':
            return "han·tai"
        if item == '':
            return "?"
        if item == '8':
            return "hap·pô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'undo':
        if item == '':
            return "un·dô"
        if item == '1':
            return "ik·kyo undo"
        if item == '':
            return "un·dô"
        if item == '2':
            return "tai no hen·kou"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'hojonokata':
        if item == '':
            return "hô·jô no kata"
        if item == '1':
            return "haru no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '2':
            return "natsu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '3':
            return "aki no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '4':
            return "fuyu no ta·chi"
        if item == '':
            return "hô·jô no kata"
        if item == '5':
            return "hassô happa"
        if item == '':
            return "hô·jô no kata"
        if item == '6':
            return "itto ryô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == '7':
            return "u·ten sa·ten"
        if item == '':
            return "hô·jô no kata"
        if item == '8':
            return "cho·tan ichi·mi"
        if item == '':
            return "hô·jô no kata"
        if item == '9':
            return "u·ke·ru"
        if item == '':
            return "hô·jô no kata"
        if item == 'a':
            return "tai·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'b':
            return "moku·rei"
        if item == '':
            return "hô·jô no kata"
        if item == 'c':
            return "bak·ken"
        if item == '':
            return "hô·jô no kata"
        if item == 'd':
            return "ai seigan"
        if item == '':
            return "hô·jô no kata"
        if item == 'e':
            return "soku·shin"
        if item == '':
            return "hô·jô no kata"
        if item == 'g':
            return "ni·ô da·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'h':
            return "kazashi"
        if item == '':
            return "hô·jô no kata"
        if item == 'i':
            return "ai jô·dan"
        if item == '':
            return "hô·jô no kata"
        if item == 'j':
            return "tsume"
        if item == '':
            return "hô·jô no kata"
        if item == 'k':
            return "u·chi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'l':
            return "morô·de"
        if item == '':
            return "hô·jô no kata"
        if item == 'm':
            return "o·shi ko·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 'n':
            return "ichi·mon·ji"
        if item == '':
            return "hô·jô no kata"
        if item == 'o':
            return "so tai"
        if item == '':
            return "hô·jô no kata"
        if item == 'p':
            return "tai ata·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'q':
            return "hi tachi"
        if item == '':
            return "hô·jô no kata"
        if item == 'r':
            return "kasumi"
        if item == '':
            return "hô·jô no kata"
        if item == 's':
            return "hi·toe·mi"
        if item == '':
            return "hô·jô no kata"
        if item == 't':
            return "muki"
        if item == '':
            return "hô·jô no kata"
        if item == 'u':
            return "ki·ri"
        if item == '':
            return "hô·jô no kata"
        if item == 'v':
            return "to·me"
        if item == '':
            return "hô·jô no kata"
        if item == 'w':
            return "ura u·chi"
        if item == '':
            return "hô·jô no kata"
        if item == 'x':
            return "sho·kô"
        if item == '':
            return "hô·jô no kata"
        if item == 'y':
            return "dai"
        if item == '':
            return "hô·jô no kata"
        if item == 'z':
            return "no·ke·n"
        else:
            return 'unknown item %s for list %s' %(item, list)
    if list == 'genkikai':
        if item == '':
            return "gen·ki·kai"
        if item == '~':
            return "dai en ko·kyû hô"
        if item == '':
            return "gen·ki·kai"
        if item == '0':
            return "su·u no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '1':
            return "yo no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '2':
            return "in no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '3':
            return "ki·musu·bi no te ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '4':
            return "a·un no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '5':
            return "gen no ko·kyû"
        if item == '':
            return "gen·ki·kai"
        if item == '6':
            return "ne un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'a':
            return "yô dô·hô"
        if item == '':
            return "gen·ki·kai"
        if item == 'b':
            return "mô·kan un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'c':
            return "gas·shô gas·seki un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'd':
            return "kin·gyo un·dô"
        if item == '':
            return "gen·ki·kai"
        if item == 'u':
            return "uma un·dô"
        else:
            return 'unknown item %s for list %s' %(item, list)
    else:
        return 'unknown list %s' %list
return 'untranslated list %s and item %s for language %s' %(list, item, context.REQUEST['LANGUAGE'])
