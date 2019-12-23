def solve_greedy(lst, sum):
    nr = 0
    lst_sol = []
    for c in sorted(lst, reverse=True):
        if c <= sum:
            nr_curr = sum // c
            sum -= c*nr_curr
            nr += nr_curr
            lst_sol.append((c, nr_curr))

    return nr, lst_sol


with open("bani.txt") as fin:
    L = [int(x) for x in fin.readline().split()]
    s = int(fin.readline())

nr_min = s + 1
for i in range(s//L[-1]+1):
    nr_curr = i + (s-i*L[-1])//L[-2]
    s_rem = s - (i*L[-1] + ((s-i*L[-1])//L[-2])*L[-2])
    tmp, lst_tmp = solve_greedy(L[:-2], s_rem)
    nr_curr += tmp
    if nr_curr < nr_min:
        L_rez = [(L[-1], i), (L[-2], ((s-i*L[-1])//L[-2]))] + lst_tmp.copy()
        nr_min = nr_curr

lst_tmp = []
for c, i in L_rez:
    if i > 0:
        lst_tmp.append('x'.join((str(c), str(i))))
str_rez = ' + '.join(lst_tmp)
with open("plata.txt", 'w') as fout:
    fout.write(f"{s} = {str_rez}")
