import random # as veletlen

vsz = random.randint(1,10)
print(f"Az előállított véletlen szám: {vsz}")

i = 0
while i < 10:
    szamok = (random.randint(1,10))*2
    i = i + 1
    print(f"Az előállított véletlen szám: {szamok}")
        
j = 0
print("3-al és 5-el osztható számokat írja ki")
while j < 10:
    vsz1 = random.randint(1,100)
    if vsz1 % 3 == 0 and vsz1 % 5 == 0:
        print(f"A szám: {vsz1}")
        j = j + 1