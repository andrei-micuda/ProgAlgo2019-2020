def colour(k):
    global tari, vecini
    for c in range(1, 5):
        tari[k] = c
        if tari[k] not in [tari[i] for i in vecini[k] if i < k]:
            if k == n:
                print(tari[1:])
            else:
                colour(k+1)


with open("harti.in") as fin:
    n = int(fin.readline())
    vecini = {i: [] for i in range(1, n+1)}
    for line in fin:
        x, y = map(int, line.split())
        vecini[x].append(y)
        vecini[y].append(x)

tari = [0] * (n+1)
colour(1)
