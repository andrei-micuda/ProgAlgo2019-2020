def bkt(k):
    global s, n
    for v in range(1, n+1):
        s[k] = v
        if sum(s[:k+1]) <= n and s[k] not in s[:k] and s[:k+1] == sorted(s[:k+1]):
            if sum(s[:k+1]) == n:
                fout.write(" + ".join(map(str, s[:k+1])) + '\n')
            else:
                bkt(k+1)


with open("descompunere.in") as fin:
    n = int(fin.read())

s = [0] * n
with open("descompunere.out", 'w') as fout:
    bkt(0)
