import random
dobasok = int(input("Adja meg a dobások számát: "))
fejekszama = 0
irasokszama = 0

for i in range(dobasok):
    dobasertek = random.randint(0,1)
    print("A jelenlegi dobás értéke:", end=" ")

    if dobasertek == 0:
        print("Fej")
        fejekszama = fejekszama + 1
    elif dobasertek == 1:
        print("Írás")
        irasokszama = irasokszama + 1
    

print(f"A fejek száma: {fejekszama}")
print(f"Az írások száma: {irasokszama}")

print("Több van ebből:", end=" ")
if fejekszama > irasokszama:
    print("Fej")
elif fejekszama < irasokszama:
    print("Írás")

fejekszama = fejekszama / dobasok * 100
irasokszama = irasokszama / dobasok * 100
print(f"A fejek száma százalékosan: {fejekszama}%")
print(f"A írások száma százalékosan: {irasokszama}%")