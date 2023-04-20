import random
list = [6, 12, 8, 2, 1, 7, 9, 3, 1]
jelenlegi = 0
print(f"A listában található számok: {list}")
for szam in list:
    jelenlegi += szam
    print(f"A jelenlegi összeg: {jelenlegi}")
print(f"A lista végösszege: {sum(list)}")



listapar = [random.randint(1,100) for i in range(20)]
paros = [szam for szam in listapar if szam % 2 == 0]
print(f"A páros számok: {paros}")