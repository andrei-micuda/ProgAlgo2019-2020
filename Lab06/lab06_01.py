def mm_pivot(lst):
    if len(lst) <= 5:
        return sorted(lst)[len(lst)//2]
    sublst = [lst[i:i+5] for i in range(0, len(lst), 5)]
    new_lst = [sorted(l)[len(l)//2] for l in sublst]
    return mm_pivot(new_lst)


def quickselect(lst_rez, lst, G, pick_pivot):
    pivot = pick_pivot([x[3] for x in lst])
    L = [x for x in lst if x[3] < pivot]
    E = [x for x in lst if x[3] == pivot]
    H = [x for x in lst if x[3] > pivot]
    if G < sum([x[1] for x in H]):
        return quickselect(lst_rez, H, G, mm_pivot)
    else:
        lst_rez += [(ob, 1) for ob in H]
        G -= sum([x[1] for x in H])
        for ob in E:
            if G > ob[1]:
                lst_rez.append((ob, 1))
                G -= ob[1]
            else:
                lst_rez.append((ob, G/ob[1]))
                G = 0
                break

        if G != 0:
            return quickselect(lst_rez, L, G, mm_pivot)


with open("rucsac.in") as fin:
    G = int(fin.readline())
    lst_ob = []
    for i, line in enumerate(fin):
        g, v = line.split()
        lst_ob.append((i+1, int(g), int(v), int(v)/int(g)))

lst_rez = []
quickselect(lst_rez, lst_ob, G, mm_pivot)

with open("rucsac.out", 'w') as fout:
    for ob in lst_rez:
        fout.write(str(ob[0][0]).center(5) + str(ob[0][1]).center(5) + str(ob[0][2]).center(5) + str(ob[0][3]).center(5) + f"{ob[1]: .3f}\n")
