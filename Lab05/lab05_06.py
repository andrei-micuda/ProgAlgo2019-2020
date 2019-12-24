with open("evenimente.txt") as fin:
    lst_sp = []
    for line in fin:
        interval, nume = line.split()
        ora_inceput, ora_sfarsit = interval.split('-')
        lst_sp.append((ora_inceput, ora_sfarsit, nume))

sali = []
for sp in sorted(lst_sp):
    for sala in sali:
        if sala[-1][1] <= sp[0]:
            sala.append(sp)
            break
    else:
        sali.append([sp]) # deschidem o sala noua pentru spectacolul sp

with open("sali.txt", 'w') as fout:
    fout.write(f"{len(sali)} sali:\n")
    for sala in sali:
        fout.write(", ".join((f"({st}-{fn} {nume})" for st, fn, nume in sala)))
        fout.write('\n')
