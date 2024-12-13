#A set_alap() függvény első paramétere egy halmaz
#és ezen kívül még három egész szám. Ha ezen egész számok közül pontosan kettő benne van 
#a halmazban, akkor törli a halmazból ezt a két számot,
#beleteszi a halmazba az összegüket és a harmadik számot. Ellenkező
#esetben nem csinál semmit. Ha mindeközben megváltozott a halmaz elem száma akkor True
#értékkel tér vissza egyébként False értékkel.

"Függvényargumentumok: {1,2,3,4,5}2, 3,6"
"Módosult halmaz: {1,4,5,6}"
"Return: True"

halmaz1= set([1,2,3,4,5])
halmaz1.add(6)
halmaz1.discard(2)
halmaz1.discard(3)

print(halmaz1)

    
