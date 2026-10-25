def mijn_functie_1(mijn_lijst1):
    for nr in mijn_lijst1:
        kwadraat = nr ** 2
        print(kwadraat)

mijn_lijst1 = [2, 4, 10, 12]
mijn_functie_1(mijn_lijst1)

def mijn_functie_2(a,b):
    optellen = a+b
    aftrekken = a-b
    vermenigvuldigen = a*b
    delen = a//b
    return[optellen, aftrekken, vermenigvuldigen, delen]

print(mijn_functie_2(12,3))
print(mijn_functie_2(12,2))
print(mijn_functie_2(10,5))
print(mijn_functie_2(100,20))
