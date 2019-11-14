# Să se determine cele mai mari două valori distincte dintr-un șir de numere întregi.

s = input()

v = [int(x) for x in s.split()]

mx1 = max(v)

while mx1 in v:
    v.remove(mx1)

mx2 = max(v)

print(mx1, mx2)
