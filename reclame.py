from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    aanbieding = prijs-(prijs*korting)
    text = (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbieding:.2f} euro.")
    print(text)

aanbieding_1("aardbei", 4, 0.1)

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btwbedrag = totaal * btw 
    return(totaal, btwbedrag)

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

print(f"Het totaal van alle inkomsten van deze week is {inkomsten_totaal(inkomsten,btw)[0]} euro, waarover {inkomsten_totaal(inkomsten, btw)[1]} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    maximum = max(mijn_lijst)
    minimum = min(mijn_lijst)
    return [maximum, minimum]

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print(laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    berekening = sum(mijn_lijst)/len(mijn_lijst)
    return berekening

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

print(f"De gemiddelde inkomsten deze week zijn {(gemiddelde(mijn_lijst))} euro.")

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

print(meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(*korte_lijst)

invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]

print(combinatie(invoer_lijst_2))
