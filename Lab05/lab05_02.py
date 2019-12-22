with open("tis.txt") as fin:
    lst_sp = []
    for line in fin:
        interval, nume = line.split(maxsplit=1)
        ora_inceput, ora_sfarsit = interval.split('-')
        lst_sp.append((nume.strip(), ora_inceput, ora_sfarsit))

ora_sfarsit_curr = "00:00"
with open("programare.txt", 'w') as fout:
    for sp in sorted(lst_sp, key=lambda e: e[2]):
        nume, ora_inceput, ora_sfarsit = sp
        if ora_inceput >= ora_sfarsit_curr:
            fout.write(f"{ora_inceput}-{ora_sfarsit} {nume}\n")
            ora_sfarsit_curr = ora_sfarsit
