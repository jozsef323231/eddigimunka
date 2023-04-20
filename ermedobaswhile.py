import random
dobasok = int(input("Adja meg a dobások számát: "))
fejekszama = 0
irasokszama = 0

keres = str(input("Fejet vagy írást számoljak?: "))

if keres == 'Fej':
    while dobasok > 1:
        dobasertek = random.randint(0,1)
        print("A jelenlegi dobás értéke:", end=" ")
        if dobasertek == 0:
            print("Fej")
            fejekszama = fejekszama + 1
        else:
            print("Írás")
        dobasok = dobasok - 1
    print("A fejek száma: ", fej)
else:
    if keres == 'Írás':
        while dobasok > 1:
            dobasertek = random.randint(0,1)
            print("A jelenlegi dobás értéke:", end=" ")
            if dobasertek == 0:
                print("Fej")
            else:
                print("Írás")
                irasokszama = irasokszama + 1
            dobasok = dobasok - 1
        print("Az irasok száma: ", iras)