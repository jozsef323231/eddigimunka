import math

valasztas = int(input("Kérem válasszon a megadottak közül:\n 1. Négyzet\n 2. Téglalap\n 3. Háromszög\n 4. Kör\n Választása: "))

if valasztas > 0 and valasztas < 5:
    if valasztas == 1:
        na = float(input("Add meg a négyzet oldalának hosszát: "))
        nkerulet = 4*na
        nterulet = na*na
        print(f"A négyzet kerülete: {nkerulet}\nA négyzet területe: {round(nterulet,2)}")
    elif valasztas == 2:
        ta = float(input("Add meg a téglalap \x1b[31mA\x1b[0m oldalát: "))
        tb = float(input("Add meg a téglalap \x1b[31mB\x1b[0m oldalát: "))
        tkerulet = 2*(ta+tb)
        tterulet = ta*tb
        print(f"A téglalap kerülete: {tkerulet}\nA téglalap területe: {round(tterulet,2)}")
    elif valasztas == 3:
        ha = float(input("Add meg a háromszög \x1b[31mA\x1b[0m oldalát: "))
        hb = float(input("Add meg a háromszög \x1b[31mB\x1b[0m oldalát: "))
        hc = float(input("Add meg a háromszög \x1b[31mC\x1b[0m oldalát: "))
        hma = float(input("Add meg a háromszög magasságát: "))
        hkerulet = ha+hb+hc
        hterulet = ha*hma/2
        print(f"A háromszög kerülete: {hkerulet}\nA háromszög területe: {round(hterulet,2)}")
    elif valasztas == 4:
        ks = float(input("Add meg a kör sugarát: "))
        kkerulet = 2*ks*math.pi
        kterulet = ks*ks*math.pi
        print(f"A háromszög kerülete: {kkerulet}\nA háromszög területe: {round(kterulet,2)}")
else:
    print("Nem jó adatok\nA programnak vége.")