import random

lista = [random.randint(1, 100) for i in range(10)]
print(f"Az alap lista: {lista}")

lista.insert(random.randint(1, 10), random.randint(1, 100))
print(f"A lista kitöltve egy random indexen egy random számmal: {lista}")



lista1 = []

for i in range(10):
   rszam = random.randint(1, 100)
   lista1.append(rszam)

print(f"Az alap lista: {lista1}")

lista2 = []

for i in range(10):
    rszami = random.randint(0, 9)
    rszamim = random.randint(1, 100)
    print(f"A véletlen szám: {rszamim}, a véletlen index: {rszami}")
    lista2.insert(rszami, rszamim)
    
print(f"Egy üres lista kitöltve egy random indexen egy random számmal: {lista2}")