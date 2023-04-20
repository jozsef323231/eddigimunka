import random
lista = [random.randint(1, 100) for i in range(10)]
print(f"Az egész lista: {lista}")
print(f"A listában lévő legkisebb szám: {min(lista)}, legnagyobb szám:  {max(lista)}")

#max = lista[0]
#i = 0
#while i < len(lista):
#    if max < lista[i]:
#        max = lista[i]
#    i += 1
#print(f"A legnagyobb eleme: {max}")