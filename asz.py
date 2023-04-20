import random
i = 0
szamok = 0

while i < 20:
    veletlen_szamok = random.randint(1, 20)
    if veletlen_szamok % 3 == 0:
        print(veletlen_szamok)
        szamok = szamok + 1
    i = i + 1
print("Darabszám",szamok)