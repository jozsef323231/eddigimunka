print("primitivek (egyszerű típusú változók)")

"""
#egész típusú változó
avalt = 13
avaltt = 123
#float (valós típusú)
bvalt = 3.56
#sztring típus
cvalt = "hello"
#karakter==sztring
c1valt = 'H'
#logikai típus bool
#dvalt = true
"""

#az alapműveletek változókkal
aszam = 6
bszam = 5
osszeg = aszam+bszam
kulonbseg = aszam-bszam
szorzat = aszam*bszam
hanyados = aszam/bszam #ez veszélyes!

print("A két szám összege: ",osszeg)
print(aszam," + ",bszam," = ",osszeg)

print("A két szám különbsége: ",kulonbseg)
print(aszam," - ",bszam," = ",kulonbseg)

print("A két szám szorzata: ",szorzat)
print(aszam," * ",bszam," = ",szorzat)

print("A két szám hanyados: ",hanyados)
print(aszam," / ",bszam," = ",hanyados)


if bszam > aszam:
  print("A második változó nagyobb mint az első")
else:
  print("A második változó kisebb mint az első")