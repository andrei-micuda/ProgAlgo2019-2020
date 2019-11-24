# Magazine și produse
# Fișierul text “inventar.txt” conține pe fiecare rând, cu spațiu între ele, un șir de litere reprezentând
# numele unui magazin, urmat de numere naturale reprezentând codurile produselor aflate în stoc
# la acel magazin.
# a) Stocați informațiile citite din fișier într-un dicționar având ca chei numele magazinelor și ca
# valori un set cu codurile produselor din acel magazin.
# b) Afișați codurile acelor produse care există în stocul tuturor magazinelor (intersecție de seturi).
# c) Afișați codurile tuturor produselor (reuniune de seturi).
# d) Afișați pentru fiecare magazin: numele magazinului și codurile produselor exclusiviste (produse
# care se află doar în acel magazin, nu și în altele) (diferență de seturi).

fhandle = open("inventar.txt")

data = fhandle.readlines()

mag = dict()

for entry in data:
    entry = entry.split()
    mag[entry[0]] = set()
    for tmp in entry:
        if tmp.isnumeric():
            mag[entry[0]].add(tmp)

# a
for k, v in mag.items():
    print(k, end = ": ")
    print(v)

print()

# c
union = set()

for v in mag.values():
    union = union.union(v)

print(union)
print()

# b
intersection = union.copy()

for v in mag.values():
    intersection = intersection.intersection(v)

print(intersection)
print()

# d
print("DIFF")
for k, entry in mag.items():
    diff = entry.copy()
    print(k, end = ": ")
    for v in mag.values():
        if entry != v:
            diff -= v
    print(diff)
