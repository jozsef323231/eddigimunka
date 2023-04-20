import tkinter as tk

def megjelenit():
    penz = int(bevitel.get())
    
    husz_ezer = penz // 20000
    penz = penz % 20000
    tiz_ezer = penz // 10000
    penz = penz % 10000
    ot_ezer = penz // 5000
    penz = penz % 5000
    ket_ezer = penz // 2000
    penz = penz % 2000
    ezer = penz // 1000
    penz = penz % 1000
    otszaz = penz // 500
    penz = penz % 500
    ketszaz = penz // 200
    penz = penz % 200
    szaz = penz // 100
    penz = penz % 100
    otven = penz // 50
    penz = penz % 50
    husz = penz // 20
    penz = penz % 20
    tiz = penz // 10
    penz = penz % 10
    ot = penz // 5
    penz = penz % 5

    cim1["text"] = "20000 forintos bankjegyek: " + str(husz_ezer)
    cim2["text"] = "10000 forintos bankjegyek: " + str(tiz_ezer)
    cim3["text"] = "5000 forintos bankjegyek: " + str(ot_ezer)
    cim4["text"] = "2000 forintos bankjegyek: " + str(ket_ezer)
    cim5["text"] = "1000 forintos bankjegyek: " + str(ezer)
    cim6["text"] = "500 forintos bankjegyek: " + str(otszaz)
    cim7["text"] = "200 forintos bankjegyek: " + str(ketszaz)
    cim8["text"] = "100 forintos bankjegyek: " + str(szaz)
    cim9["text"] = "50 forintos bankjegyek: " + str(otven)
    cim10["text"] = "20 forintos bankjegyek: " + str(husz)
    cim11["text"] = "10 forintos bankjegyek: " + str(tiz)
    cim12["text"] = "5 forintos bankjegyek: " + str(ot)

ablak = tk.Tk()
ablak.title("Pénz felosztása")

keret = tk.Frame(ablak)
keret.pack()

cimke = tk.Label(keret, text="Adja meg a pénzösszegét:")
cimke.grid(row=0, column=0)

bevitel = tk.Entry(keret)
bevitel.grid(row=0, column=1)

gomb = tk.Button(keret, text="Felosztás", command=megjelenit)
gomb.grid(row=1, column=1, pady=10)

cim1 = tk.Label(keret, text="")
cim1.grid(row=2, column=0, columnspan=2)

cim2 = tk.Label(keret, text="")
cim2.grid(row=3, column=0, columnspan=2)

cim3 = tk.Label(keret, text="")
cim3.grid(row=4, column=0, columnspan=2)

cim4 = tk.Label(keret, text="")
cim4.grid(row=5, column=0, columnspan=2)

cim5 = tk.Label(keret, text="")
cim5.grid(row=6, column=0, columnspan=2)

cim6 = tk.Label(keret, text="")
cim6.grid(row=7, column=0, columnspan=2)

ablak.mainloop()
