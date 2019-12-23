with open("cuburi.txt") as fin:
    n = int(fin.readline())
    cuburi = []
    for line in fin:
        l, cul = line.split()
        cuburi.append((int(l), cul))

prev_cul = None
h = 0
with open("turn.txt", 'w') as fout:
    for cub in sorted(cuburi, key=lambda e: e[0], reverse=True):
        if cub[1] != prev_cul:
            fout.write(f"{cub[0]} {cub[1]}\n")
            prev_cul = cub[1]
            h += cub[0]
    fout.write(f"Inaltime totala: {h}.")
