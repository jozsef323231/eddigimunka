print("Lista feltöltése véletlen számokkal")

import random

lista = []

i = 1
while i <= 20:
    szamok = random.randint(1,20)
    lista.append(szamok)
    i = i + 1
    
print(f"A véletlen számokból előállított lista: {lista}")