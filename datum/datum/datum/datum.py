from datetime import date

szulev = int(input("Add meg a születési évedet: "))
szulho = int(input("Add meg a születési hónapod: "))
szulnap = int(input("Add meg a születési napod: "))
szuldatum = date(szulev, szulho, szulnap)

maidatum = date.today()

eletev = maidatum.year - szuldatum.year
eletho = maidatum.month - szuldatum.month
eletnap = maidatum.day - szuldatum.day
print(eletev, "éves vagy, ", abs(eletho), "hónapos, és", abs(eletnap), "napos.")

if eletev < 18:
    print("Még kiskorú vagy!")
else:
    print("Már nagykorú vagy!")