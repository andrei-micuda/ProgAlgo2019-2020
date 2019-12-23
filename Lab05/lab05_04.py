def solve_greedy(lst, sum):
    nr = 0
    lst_sol = []
    for c in lst:
        if c <= sum:
            nr_curr = sum // c
            sum -= c*nr_curr
            nr += nr_curr
            lst_sol.append((c, nr_curr))

    return nr, lst_sol


with open("cuburi.txt") as fin:
    L = [int(x) for x in fin.readline().split()]
    s = int(fin.readline())

for i in range(s//L[-1]+1):
    s_copy = s
    nr_curr = i + (s-i*L[-1])//L[-2]
    s_copy -= (i*L[-1] + ((s-i*L[-1])//L[-2])*L[-2])
    print(i, (s-i*L[-1])//L[-2], s_copy)
