def my_print(l):
    for sp in l:
        fout.write(f"{sp[0]}-{sp[1]} {sp[2]}\n")
    fout.write('\n')


def bkt(k):
    global nr_sp_mx, x, lst_sp
    for sp in lst_sp if k == 0 else [tmp for tmp in lst_sp if tmp[0] >= x[k-1][1]]:
        x[k] = sp
        if k < nr_sp_mx:
            if k == nr_sp_mx - 1:
                my_print(x)
            else:
                bkt(k+1)


with open("spectacole.txt") as fin:
    lst_sp = []
    for line in fin:
        line = line.strip()
        interval, nume = line.split(maxsplit=1)
        ora_inceput, ora_sfarsit = interval.split('-')
        lst_sp.append((ora_inceput, ora_sfarsit, nume))

lst_sp.sort(key=lambda e: e[1])
ora_fin_curr = "00:00"
nr_sp_mx = 0
for sp in lst_sp:
    if sp[0] >= ora_fin_curr:
        nr_sp_mx += 1
        ora_fin_curr = sp[1]

x = [0] * nr_sp_mx
with open("programare.txt", 'w') as fout:
    bkt(0)
