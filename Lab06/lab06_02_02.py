def bkt(k):
    global nr, s
    for v in range(1 if k==0 else nr[k-1] + 1, s+1):
        nr[k] = v
        if sum(nr[:k+1]) <= s:
            if sum(nr[:k+1]) == s:
                fout.write(' '.join(map(str, nr[:k+1])) + '\n')
            else:
                bkt(k+1)


with open("generare.in") as fin:
    s = int(fin.read())

nr = [0] * s
with open("generare.out", 'w') as fout:
    bkt(0)
