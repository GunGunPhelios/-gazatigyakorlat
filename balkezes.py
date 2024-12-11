import datetime
szemelyek= []

with open("ifelse/balkezesek.txt", "r",encoding= "UTF-8") as fajl:
    sorok= fajl.readlines()
elsosor=sorok[0].strip()
print(elsosor)

for sor in sorok:
    sor= sor.strip()
    sor= sor.split(";")

nev= sor[0]
elso= (datetime.datetime.strptime(sor[1], "%Y-%m-%d"))
utolso= (datetime.datetime.strptime(sor[2],"%Y-%m-%d" ))
suly= int(sor[3])
magassag= int(sor[4])

szemelyek.append([nev,elso,utolso,suly,magassag])

sz= ""

for szemely in szemelyek:
    print(f"{szemely[0]}, {szemely[1]} ,{szemely[2]},{szemely[3]} {szemely[4]}")
    if szemely[1].year== 1999 and szemely[1].month == 10 or szemely[2].year == 1999 and szemely[2].month == 10:
        ev= szemely[1]
        sz= szemely[2]
        magassag= szemely[4]* 2,54
        print(f"{sz}, {round(magassag,1)} cm")
        

while True:
    evszam= int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
    if evszam >= 1990 and evszam <= 1999:
        print(f"A megadott szám: {evszam}")
        break

    else:
        print(f"Hibás adat! Kérek egy 1990 és 1999 közötti évszámot!:")

print(f"3.feladat {len(szemelyek)}")