import tkinter as tk

def szamol():
    alak = valasztas.get()
    if alak == 1:
        oldal_a = float(bevitel_a.get())
        oldal_b = float(bevitel_b.get())
        kerulet = 2 * (oldal_a + oldal_b)
        terulet = oldal_a * oldal_b
    elif alak == 2:
        sugar = float(bevitel_a.get())
        kerulet = 2 * 3.14 * sugar
        terulet = 3.14 * sugar * sugar
    elif alak == 3:
        oldal = float(bevitel_a.get())
        kerulet = 4 * oldal
        terulet = oldal * oldal
    elif alak == 4:
        oldal_a = float(bevitel_a.get())
        oldal_b = float(bevitel_b.get())
        oldal_c = float(bevitel_c.get())
        p = (oldal_a + oldal_b + oldal_c) / 2
        kerulet = oldal_a + oldal_b + oldal_c
        terulet = (p * (p - oldal_a) * (p - oldal_b) * (p - oldal_c)) ** 0.5
    eredmeny.configure(text=f'Kerület: {kerulet:.2f}\nTerület: {terulet:.2f}')

ablak = tk.Tk()
ablak.title("Kerület és terület számoló")

valasztas = tk.IntVar()

gomb_1 = tk.Radiobutton(ablak, text="Téglalap", variable=valasztas, value=1)
gomb_2 = tk.Radiobutton(ablak, text="Kör", variable=valasztas, value=2)
gomb_3 = tk.Radiobutton(ablak, text="Négyzet", variable=valasztas, value=3)
gomb_4 = tk.Radiobutton(ablak, text="Háromszög", variable=valasztas, value=4)

gomb_1.pack()
gomb_2.pack()
gomb_3.pack()
gomb_4.pack()

bevitel_a_szov = tk.Label(ablak, text="Adja meg az [A] oldalt:")
bevitel_a = tk.Entry(ablak)
bevitel_b_szov = tk.Label(ablak, text="Adja meg a [B] oldalt:")
bevitel_b = tk.Entry(ablak)
bevitel_c_szov = tk.Label(ablak, text="Adja meg a [C] oldalt:")
bevitel_c = tk.Entry(ablak)

bevitel_a_szov.pack()
bevitel_a.pack()
bevitel_b_szov.pack()
bevitel_b.pack()
bevitel_c_szov.pack()
bevitel_c.pack()

eredmeny = tk.Label(ablak, text="")
eredmeny.pack()

szamol_gomb = tk.Button(ablak, text="Számolj", command=szamol)
szamol_gomb.pack()

ablak.mainloop()
