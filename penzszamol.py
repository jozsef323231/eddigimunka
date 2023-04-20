penz = int(input("Adja meg a pénzösszegét: "))

husz_ezer = penz // 20000
penz = penz % 20000
tiz_ezer = penz // 10000
penz = penz % 10000
ot_ezer = penz // 5000
penz = penz % 5000
ezer = penz // 1000
penz = penz % 1000
otszaz = penz // 500
penz = penz % 500

print("20000 forintos bankjegyek:", husz_ezer)
print("10000 forintos bankjegyek:", tiz_ezer)
print("5000 forintos bankjegyek:", ot_ezer)
print("1000 forintos bankjegyek:", ezer)
print("500 forintos bankjegyek:", otszaz)