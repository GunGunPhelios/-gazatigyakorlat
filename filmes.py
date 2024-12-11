filmek=[]
with open("ifelse/film.txt", "r", encoding="UTF-8") as fajl:
    sorok=fajl.readlines()
    
    for sor in sorok[1:]:
        sor= sor.strip()
        sor=sor.split(";")
        cím=sor[0]
        rendezo=sor[1]
        foszerep=sor[2].lower
        ev=int(sor[3])
        perc=int(sor[4])
        filmek.append([cím,rendezo,foszerep,ev,perc])
szinesz= input("Adj meg egy szinész nevet! ")
legrovidebb= float("inf")
legrovidebbcim=""
db=0
filmszineszek=0
for film in filmek:
    #print(f"{film[0]}, {film[1]}, {film[2]}, {film[3]}, {film[4]}")
    hossz= len(film[0])
    if hossz < legrovidebb:
        legrovidebb= len(film[0])
        legrovidebbcim= film[0]
    if film[4]>= 110:
        db+=1
    if film[2] == szinesz:
        filmszineszek.append(film[0])
if len(filmek) > 0:
    print(";". join(map(str,filmszineszek[:1])))
else:
    print("Nincs ilyen személy a listában.")
    fajl.write("Nincs ilyen személy a listában.")


print(f"A legrövidebb film címe: {legrovidebbcim}")
print(f"Legalább {db} db 110 perces film van")
print(f"{len(filmek)}")
