def info_angajat(nume):
    for x in lst_angajati:
        if x["nume"] == nume:
            print("Nume: {}\nVarsta: {}\nSalariu: {}".format(x["nume"], x["varsta"], x["salariu"]))


def salariu_maxim():
    mx = max([x["salariu"] for x in lst_angajati])
    print("Salariul maxim este {}.".format(mx))

    for x in lst_angajati:
        if x["salariu"] == mx:
            print(x["nume"])


def salariu_mediu():
    total = 0
    for x in lst_angajati:
        total += x["salariu"]

    print("Salariul mediu este {0: .2f}.".format(total/n))


fin = open("angajati.txt")
n = int(fin.readline())

lst_angajati = []
for entry in fin.readlines():
    nume, varsta, salariu = entry.strip().split(',')
    lst_angajati.append({
        "nume": nume,
        "varsta": int(varsta),
        "salariu": int(salariu)
    })
fin.close()

# a
nume = input()
info_angajat(nume)
print()

# b
salariu_maxim()
print()

# c
salariu_mediu()

# d
fout = open("angajati_nume.txt", 'w')
for x in sorted(lst_angajati, key=lambda e: (e["nume"].split()[0].lower(), e["nume"].split()[1].lower())):
    fout.write("{}, {}, {}.\n".format(x["nume"], x["varsta"], x["salariu"]))
fout.close()

# e
fout = open("angajati_varsta_nume.txt", 'w')
for x in sorted(lst_angajati, key=lambda e: (-e["varsta"], e["nume"].split()[0].lower(), e["nume"].split()[1].lower())):
    fout.write("{}, {}, {}.\n".format(x["nume"], x["varsta"], x["salariu"]))
fout.close()

# f
fout = open("angajati_salariu_varsta.txt", 'w')
for x in sorted(lst_angajati, key=lambda e: (-e["salariu"], e["varsta"])):
    fout.write("{}, {}, {}.\n".format(x["nume"], x["varsta"], x["salariu"]))
fout.close()
