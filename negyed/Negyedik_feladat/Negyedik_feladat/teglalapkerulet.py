print("Válassz a megadottak közül: ")
print("1. Téglalap")
print("2. Háromszög")

while True:
    valaszt = input("Írd be választásod: ")

    if valaszt in ("1", "2"):
        
        if valaszt == "1":
         ateg = int(input("Írd be a téglalap hosszúságát: "))
         bteg = int(input("Írd be a téglalap szélességét: "))
         teruletteg = ateg * bteg
         keruletteg = 2 * (ateg + bteg)
         print(f"A téglalap területe: {teruletteg} \nA téglalap kerülete: {keruletteg}")
        
        elif valaszt == "2":
         aharsz = int(input("Írd be a háromszög A oldalát: "))
         bharsz = int(input("Írd be a háromszög B oldalát: "))
         charsz = int(input("Írd be a háromszög C oldalát: "))
         ma = bharsz
         teruletharsz = aharsz * ma / 2
         keruletharsz = aharsz + bharsz + charsz
         print(f"A háromszög területe: {teruletharsz} \nA háromszög kerülete: {keruletharsz}")
         for i in range(ma,0,-1):
          print(i* ' ' + (ma+1-i) * '*')
            
    ujszam = input("Szeretnél újat számolni? (igen/nem): ")
    if ujszam == "nem":
        break


