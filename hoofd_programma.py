from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")
uitvoer.append(f"Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append(f"Slagroom, spuitbus van 1 liter: 2 euro")

print()

for zin in uitvoer:
    print(zin)