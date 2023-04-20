import random
veletlen_szamok = [random.randint(1, 20) for i in range(20)]
harmal_oszthato = [szam for szam in veletlen_szamok if szam % 3 == 0]
print("3-al osztható számok:", harmal_oszthato)
darab = len(harmal_oszthato)
print("Darabszám:", darab)