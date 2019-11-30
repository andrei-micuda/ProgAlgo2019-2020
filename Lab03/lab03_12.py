def dfs(tata):
    DFS.append(tata)
    for fiu in lst_ad.get(tata, []):
        if fiu not in DFS:
            dfs(fiu)
    return


fin = open("graf_in.txt", "r")

tip_graf = fin.readline().strip()
n = int(fin.readline())
m = int(fin.readline())

# a
lst_muchii = []
for k in range(m):
    i, j = map(int, fin.readline().split())
    lst_muchii.append((i, j))
    if tip_graf == "neorientat":
        lst_muchii.append((j, i))

s, f = map(int, fin.readline().split())
fin.close()

fout = open("graf_out.txt", "w")

fout.write(str(lst_muchii) + '\n')

# b
lst_ad = {}
for i, j in lst_muchii:
    lst_ad[i] = lst_ad.get(i, []) + [j]

# c
M = [[0 for i in range(n)] for j in range(n)]

for i, j in lst_muchii:
    M[i-1][j-1] = 1

# d
BFS = [(s, -1)]
st = dr = 0

while st <= dr:
    tata = BFS[st][0]

    for fiu in lst_ad.get(tata, []):
        if fiu not in [nod for (nod, parinte) in BFS]:
            BFS.append((fiu, tata))
            dr += 1
    st += 1

fout.write("BFS: ")
rez_str = ", ".join(map(str, [nod for (nod, parinte) in BFS]))
fout.write(rez_str + '\n')

# e
DFS = []
dfs(s)
fout.write("DFS: ")
rez_str = ", ".join(map(str, DFS))
fout.write(rez_str + '\n')

# f
i = len(BFS) - 1
nod_curent = f
drum_min = [f]
while i >= 0 and nod_curent != s:
    if BFS[i][0] == nod_curent:
        nod_curent = BFS[i][1]
        drum_min.append(nod_curent)
    i -= 1

if nod_curent != s:
    print("Nu exista un drum intre cele doua noduri.")
else:
    drum_min.reverse()
    rez_str = "->".join(map(str, drum_min))
    fout.write(rez_str + '\n')

fout.close()
