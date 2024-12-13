#Írd meg a beolvas() metódust ami egy szöveg típusú paramétert vár, ami egy fajl neve
#A feladat, hogy olvasd be a fajl tartalmát, ami soronként egy szöveget, egy lebegőpontos számot majd egy egész számot tartalmaz pontosvesszővel
##A sorokbol alkoss egy listát, ami dictionaryket tartalmaz a lenti táblázatban kulcs érték párokkal. Térj vissza a megalkotott listával
#szín szöveg kacsa színe
#méret lebegőpntos kacsa mérete
#sebesség szám a kacsa sebessége





"[{Szín: k},  {meret: 10.1}, {sebesség: 2}, {szín:f, meret: 3.5, sebesseg:1 }, {...}]"
def beolvas(fajlnev):
    # Lista a feldolgozott sorok tárolásához
    adat_lista = []
    
    try:
        # Fájl megnyitása olvasásra
        with open(fajlnev, 'r') as f:
            # Soronkénti beolvasás és feldolgozás
            for sor in f:
                # Sor levágása, hogy ne maradjanak üres karakterek a végén
                sor = sor.strip()
                # Sor feldarabolása pontosvessző szerint
                reszek = sor.split(';')
                
                # Készítünk egy dictionary-t a darabolt elemekből
                adat = {
                    'szín': reszek[0],
                    'méret': float(reszek[1]),
                    'sebesség': int(reszek[2])
                }
                
                # A dictionary hozzáadása a listához
                adat_lista.append(adat)
        
        return adat_lista
    
    except FileNotFoundError:
        print(f"A fájl nem található: {fajlnev}")
        return []
    except Exception as e:
        print(f"Hiba történt a fájl olvasása során: {e}")
        return []

# Példa a használatra
fajlnev = "kacsa.txt"
eredmeny = beolvas(fajlnev)
print(eredmeny)

