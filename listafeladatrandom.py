import random
indexn = int(input("Add meg a lista nagyságát, számold bele, hogy az index a 0. elem!: "))
legnsz = int(input("Add meg, hogy maximum mekkorák legyenek a számok: "))
lista = [random.randint(0,legnsz) for indexn in range(indexn)]
print(f"Az egész lista: {lista}\nA lista legnagyobb száma: {max(lista)}\nA lista legkisebb száma: {min(lista)}")