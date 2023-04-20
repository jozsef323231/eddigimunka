aszam = int(input("Adjon meg egy számot: "))
bszam = int(input("Adjon meg egy számot: "))
valasz = int(input("Csökkenő vagy Növekvő sorrend legyen (1, 2): "))

if valasz == 1:

    if aszam > bszam:
        while aszam > bszam:
            aszam = aszam - 1
            print(aszam)

    else:
        while bszam > aszam:
            bszam = bszam - 1
            print(bszam)

elif valasz == 2:

    if aszam > bszam:
        while aszam > bszam:
            bszam = bszam + 1
            print(bszam)

    else:
        while aszam < bszam:
            aszam = aszam + 1
            print(aszam)