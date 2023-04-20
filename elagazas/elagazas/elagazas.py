print("Elágazások")
"""
szam = int(input("Kérek egy számot: "))
if szam > 5:
    print("A szám nagyobb mint 5!")

else:
  if szam == 5:
    print("A szám egyenlő 5-tel!")

  else:
      print("A szám kisebb mint 5!")

print("Vége a programnak! \n")

szam1 = int(input("Kérek egy számot: "))
# ezt ne tanuld 
if szam1 == 0:
    print("Ez 0")
if szam1 > 0:
    print("Ez +")
if szam1 < 0:
    print("Ez -")
"""

# egy szám pozitív negatív vagy 0

szam = int(input("Adj meg egy számot: "))

if szam == 0:
    print(f"A szám {szam}")
else:
    if szam > 0:
       print(f"A szám nagyobb mint 0, így pozitív! A szám: {szam}")
    else:
        print(f"A szám kisebb mint 0, így negatív! A szám: {szam}")

print("A programnak vége! \n")