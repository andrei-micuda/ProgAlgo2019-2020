from fractions import Fraction

with open("obiecte.txt") as fin:
    n = int(fin.readline())
    obiecte = []
    for i in range(n):
        v, g = fin.readline().split()
        obiecte.append((int(v), int(g), int(v)/int(g)))
    G = int(fin.readline())

rez = []
for v, g, rap in sorted(obiecte, key=lambda e: e[2], reverse=True):
    if g <= G:
        rez.append((v, g, 1))
        G -= g
    else:
        rez.append((v, g, G/g))
        G = 0
        break

with open("rucsac.txt", 'w') as fout:
    greutate = " + ".join(str(x[1]) for x in rez if x[2] == 1)
    if rez[-1][2] != 1:
        if greutate:
            greutate += f" + ({Fraction(rez[-1][2]).limit_denominator()}) x {g}"
        else:
            greutate += f"({Fraction(rez[-1][2]).limit_denominator()}) x {g}"
    fout.write(f"Greutate: {greutate} = {sum([ob[1] * ob[2] for ob in rez])}\n")
    valoare = " + ".join(str(x[0]) for x in rez if x[2] == 1)
    if rez[-1][2] != 1:
        if valoare:
            valoare += f" + ({Fraction(rez[-1][2]).limit_denominator()}) x {v}"
        else:
            valoare = f"({Fraction(rez[-1][2]).limit_denominator()}) x {v}"
    fout.write(f"Valoare: {valoare} = {sum([ob[0] * ob[2] for ob in rez])}")
