vezetek = str(input("Add meg a Vezetékneved: "))
kereszt = str(input("Add meg a Keresztneved: "))
teljesnev = vezetek + " " + kereszt
print(f"Üdvözöllek {teljesnev}")

# Másik feladat
szam = float(input("Adj meg egy számot: "))
print(szam * szam)

# Harmadik feladat
konst = 3.142
print("Egy konstans szám: ",konst)

koratmer = float(input("Adj meg egy kör átmérőjét: "))
kerulet = koratmer * konst
r = koratmer / 2
terulet = (r * r) * konst
print(f"A kör kerülete: {kerulet} \n A kör területe: {terulet}")

# Negyedik feladat
a = 5
b = 6
print(a,b)
c = b
b = a
a = c
print(a,b)