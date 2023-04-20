import random
dobasok = int(input("Adja meg a dobások számát: "))
fejekszama = 0
irasokszama = 0





mitszamol = str(input("Mit számoljon, fej vagy írás: "))

if mitszamol == 'fej':
    for i in range(dobasok):
        dobasertek = random.randint(0,1)

        if dobasertek == 0:
            print("Fej")
            fejekszama = fejekszama + 1
    print(f"Fejek száma: {fejekszama}")

elif mitszamol == 'írás':
    for i in range(dobasok):
        dobasertek = random.randint(0,1)

        if dobasertek == 1:
            print("Írás")
            irasokszama = irasokszama + 1
    print(f"Írások száma: {irasokszama}")