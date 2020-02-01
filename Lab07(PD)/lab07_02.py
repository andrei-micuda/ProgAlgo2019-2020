with open("date.in") as fin:
    n, m = (int(x) for x in fin.readline().split())
    mat = [[int(x) for x in line.split()] for line in fin]

smax = [[0 for j in range(m)] for i in range(n)]  # smax[i][j] = suma maxima care se termina pe i si j
pred = [[0 for j in range(m)] for i in range(n)]
smax[0][0] = mat[0][0]
pred[0][0] = (-1, -1)
for j in range(1, m):
    smax[0][j] = smax[0][j-1] + mat[0][j]
    pred[0][j] = (0, j-1)
for i in range(1, n):
    smax[i][0] = smax[i-1][0] + mat[i][0]
    pred[i][0] = (i-1, 0)
for i in range(1, n):
    for j in range(1, m):
        smax[i][j] = mat[i][j] + max(smax[i-1][j], smax[i][j-1])
        pred[i][j] = (i-1, j) if smax[i-1][j] > smax[i][j-1] else (i, j-1)

pozi, pozj = n-1, m-1
lst_rez = []
while (pozi, pozj) != (-1, -1):
    lst_rez.append((pozi, pozj))
    pozi, pozj = pred[pozi][pozj]

with open("date.out", 'w') as fout:
    fout.write(str(smax[n - 1][m - 1]) + '\n')
    lst_rez.reverse()
    for i, j in lst_rez:
        i += 1
        j += 1
        fout.write(f"{i} {j}\n")
