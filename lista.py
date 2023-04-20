print("Lista")

lista = [2, 5, 6, 7]


print(f"A lista 0. indexének értéke: {lista[0]}")

print(f"A lista hossza: {len(lista)}")

print(f"Az egész lista: {lista}")

lista.append(17)
print(f"A listához egy új elem adva: {lista}")

lista.insert(1,86)
print(f"A lista adott indexére új elem beszúrása: {lista}")



import random
most = [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
i = 0
while i < len(most):
    most[i] = 4
    i = i + 1
for valami in most:
    print(valami)
i = 0
while i < len(most):
    rszam = random.randint(1,100)
    most[i] = rszam
    i = i + 1
for valami in most:
    print(rszam)