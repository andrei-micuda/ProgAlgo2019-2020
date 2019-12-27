import random


def solve(i1, j1, i2, j2, lst_obstacole):
    global rez
    lst_tmp = []
    for (i, j) in lst_obstacole:
        if i1 < i < i2 and j1 < j < j2:
            lst_tmp.append((i, j))

    if len(lst_tmp) == 0:
        arie_curr = (i2-i1)*(j2-j1)
        if arie_curr > rez[2]:
            rez = [(i1, j1), (i2, j2), arie_curr]
    else:
        coord = random.choice(lst_tmp)
        solve(coord[0], j1, i2, j2, lst_obstacole)
        solve(i1, j1, coord[0], j2, lst_obstacole)
        solve(i1, coord[1], i2, j2, lst_obstacole)
        solve(i1, j1, i2, coord[1], lst_obstacole)


with open("copaci.in") as fin:
    st_i, st_j = map(int, fin.readline().split())
    fn_i, fn_j = map(int, fin.readline().split())
    n = int(fin.readline())
    lst_obstacole = []
    for line in fin:
        i, j = map(int, line.split())
        lst_obstacole.append((i, j))

rez = [(0, 0), (0, 0), 0]
solve(st_i, st_j, fn_i, fn_j, lst_obstacole)

with open("copaci.out", 'w') as fout:
    fout.write("Dreptunghiul: ")
    fout.write(f"{rez[0]} x {rez[1]}\n")
    fout.write("Aria maxima: ")
    fout.write(str(rez[2]))
