#Se citește un șir format din n numere întregi (n≥2). Să se afișeze cele mai mari
#două valori distincte din șir sau mesajul "Imposibil", dacă acestea nu există.

n = int(input('n: '))
mx1 = None
mx2 = int(input())
n -= 1

while mx1 is None and n:
    x = int(input())
    if x != mx2:
        mx1 = x
    n -= 1

if mx1 > mx2:
    mx1, mx2 = mx2, mx1

for i in range(n):
    x = int(input())
    if x > mx2:
        mx2 = x
    elif x > mx1 and x != mx2:
        mx1 = x

if mx1 is None:
    print('Imposibil')
else:
    print(mx1, mx2)
