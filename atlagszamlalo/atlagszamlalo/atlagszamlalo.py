mitszeretnel = int(input("Átlagot vagy TTI-t szeretnél számolni (1 vagy 2): "))

if mitszeretnel == 1:
    atlag = int(input("Add meg az átlagodat: "))
    if atlag < 1.4:
        print("Az átlagod: Elégtelen")
    else:
        if atlag < 2.4:
            print("Az átlagod: Elégséges")
        else:
            if atlag < 3.4:
                print("Az átlagod: Közepes")
            else:
                if atlag < 4.4:
                    print("Az átlagod: Jó")
                else:
                    if atlag >= 4.5:
                        print("Az átlagod: Jeles")


else:
    if mitszeretnel == 2:
        ttomeg = float(input("Add meg a tömegedet: "))
        tmagas = float(input("Add meg a magasságodat (pl: 1.60 = 160cm) : "))
        tti = ttomeg / (tmagas*tmagas)

if tti < 16:
    print(f"A testsúlyosztályod: Súlyos soványság \n A Testtömegindexed: {tti}")
else:
    if tti < 16.99:
        print(f"A testsúlyosztályod: Mérsékelt soványság \n A Testtömegindexed: {tti}")
    else:
        if tti < 18.49:
            print(f"A testsúlyosztályod: Enyhe soványság \n A Testtömegindexed: {tti}")
        else:
            if tti < 24.99:
                print(f"A testsúlyosztályod: Normális testsúly \n A Testtömegindexed: {tti}")
            else:
                if tti < 29.99:
                    print(f"A testsúlyosztályod: Túlsúlyos \n A Testtömegindexed: {tti}")
                else:
                    if tti < 34.99:
                        print(f"A testsúlyosztályod: 1. Fokú elhízás \n A Testtömegindexed: {tti}")
                    else:
                        if tti < 39.99:
                            print(f"A testsúlyosztályod: 2. Fokú elhízás \n A Testtömegindexed: {tti}")
                        else:
                            if tti >= 40:
                                print(f"A testsúlyosztályod: 3. Fokú elhízás \n A Testtömegindexed: {tti}")