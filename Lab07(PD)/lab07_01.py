with open("date.in") as fin:
    n = int(fin.readline())
    domino = []
    for line in fin:
        domino.append(tuple(int(x) for x in line.split()))

lmax = [0] * n  # lmax[i] = subsirul de lungime maxima care se termina pe i
pred = [-1] * n
lmax[0] = 1
for i in range(1, n):
    tmp = 0
    for j in range(0, i):
        if domino[j][1] == domino[i][0] and lmax[j] > tmp:
            tmp = lmax[j]
            pred[i] = j
    lmax[i] = 1 + tmp

rez = max(lmax)
poz = lmax.index(rez)
lst_rez = []
while poz != -1:
    lst_rez.append(domino[poz])
    poz = pred[poz]

with open("date.out", 'w') as fout:
    lst_rez.reverse()
    fout.write(' '.join([str(x) for x in lst_rez]) + '\n')
    fout.write(str(lmax.count(rez)))
