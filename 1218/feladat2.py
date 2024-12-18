import random

fegyverek={
    "Piros": ["Támadás", "Lerohanás", "Gyógyulás"],
    "Zöld": ["Támadás", "Fejlövés", "Csúszás"],
    "Lila": ["Támadás", "Lassítás", "Térmanipuláció"],
    "Kék": ["Támadás", "Felrobbantás", "Szórás"],
    "Fehér": ["Támadás", "Löveg helyezés", "Dobás"]
}

nextgun=random.choice(list(fegyverek.keys()))

print(f"A választott fegyver: {nextgun}")
print("Lépések:")
for i, lépés in enumerate(fegyverek[nextgun],1):
    print(f"{i}. lépés: {lépés}")