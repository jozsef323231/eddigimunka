print("Összegzés, átlag, max és min")
import random
i = 0
ossz = 0
max = 0
min = 11
nagysor = 0
kissor = 0

while i < 10:
    vlt = random.randint(1,10)
    print(f"Az {i}. szám:",end=" ")
    print(vlt)
    ossz = ossz + vlt
    if max < vlt:
        max = vlt
        nagysor = i
    if min > vlt:
        min = vlt
        kissor = i
    i = i + 1
    
print(f"A számok összege: {ossz}")
print(f"A számok átlaga: {ossz/i}%")
print(f"A legnagyobb szám: {max, nagysor}")
print(f"A legkisebb szám: {min, kissor}")


print("Program vége")