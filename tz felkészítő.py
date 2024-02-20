"""
Egy Skodákat forgalmazó vállalatnak 5 telephelye van az országban. Az elmúlt
évben havonta eladott Octavia RS modellek darabszámát egy fájlban tartja nyilván.
"""

"""
1. feladat:
Olvas be a fájl tartalmát egy megfelelő adatszerkezetbe! Ügyelj arra, hogy
a numrikus értékek számként legyenek tárolva.
"""

OctaviaRS =[]
f = open("adat.txt", "r", encoding="UTF-8")

for sor in f:
    OctaviaRS.append(sor.replace("\n", "").strip().split())

f.close()

#Adatok konvertálása
i = 0
while i < len(OctaviaRS):
    j = 1
    while j < len(OctaviaRS[i]):
        OctaviaRS[i][j] = int(OctaviaRS[i][j])
        j += 1
    i += 1
print(OctaviaRS)

"""
2.feladat:
A példában látható módon írjuk ki az adatokat!
PÉLDA :
város: Budapest
Január: 0 db
Február: 0 db
Március: 3 db
...

Város : Szeged
Január: 0 db
Február: 0 db

...
"""

hónapok = ("Január", "Február", "Március", "Április", "Május", "Június", "Július", "Agusztus", "Szeptember", "Október", "November", "December")

i = 0
while i < len(OctaviaRS):
    print(f"\nVáros: {OctaviaRS[i][0]}")
    j = 1
    while j < len(OctaviaRS)



"""
3.feladat
A példában látható módon írjuk ki a képernyőre, hogy az egyes városokban
hány olyan hónap volt, amikor egy autót sem adtak el!
PÉLDA:
eladásmentes hónapok városonként:
Budapest: 5 hónap
Szeged: 6 hónap
...
Kaposvár: 4 hónap
Összesen: 25 hónap
"""

teljesDb = 0
i = 0
while i < len(OctaviaRS):
    db = 0 
    j = 0
    while j < len(OctaviaRS[i]):
        if OctaviaRS[i][j] == 0:
            db += 1
        j += 1
    print(f"{OctaviaRS[i][0]}: {db} hónap")
    teljesDb += 1
    i += 1
print(f"összesen: {teljesDb} hónap")




"""
4.feladat:
A példában látható módon írjuk ki a képernyőre, hogy az elmúlt évben melyik
hónapban adták el a legtöbb autót a kereskedés összes telephelyét!
PÉLDA:
Havonta eladott Octavia RS autók száma:
Január 4 db
Február : 3db
...
December : 12 db
Összesen 98 db
Legsikeresebb hónap: Agusztus (27 db)
"""

i = 0
teljesösszeg = 0
print("\n Havonta eladott Octavia RS autó száma:")
segéd = []
while i < len(hónapok):
    összeg = 0
    j = 1
    while j < len(OctaviaRS):
        összeg += OctaviaRS[j][i + 1]
        j += 1
    teljesösszeg += összeg
    segéd.append(összeg)
    print(f"{hónapok[i]}: {összeg} db")
    i += 1
print(f"összesen: {teljesösszeg} db")

maxÉrték = segéd[0]
maxHely = 0
i = 1
while i < len(segéd):
    if segéd[i] > maxÉrték:
        maxÉrték = segéd[i]
        maxHely = i
    i += 1
print(f"Legsikeresebb hónap: {hónapok[maxHely].lower()} ({maxÉrték} db)")


"""
5.feladat(HF):
Igaz-e az az állítás, hogy minden telephelyen volt legalább 3 db olyan hónap, amikor legalább 3 autót eladtak?
PÉLDA:
Feltételnek megfelelő eladások városonként:
Budapest : 6 hónap
Szeged: 5 hónap
...
Kaposvár: 5 hónap
Igaz az állítás.
"""