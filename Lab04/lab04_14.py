def fisier_dict(nume_fisier):
    fin = open(nume_fisier, 'r')
    lst = []
    for line in fin:
        parts = line.split()
        lst.append({"plecare": parts[0], "sosire": parts[2], "ora_plecare": parts[3], "ora_sosire": parts[4]})
    fin.close()
    return lst


def timp_calatorie(ora_plecare, ora_sosire):
    if ora_sosire < ora_plecare:
        print("Timpul calatoriei nu poate fi calculat. Returning None.")
        return None
    h_plecare, min_plecare = map(int, ora_plecare.split(":"))
    h_sosire, min_sosire = map(int, ora_sosire.split(":"))
    rez_min = (60-min_plecare) + min_sosire
    h_plecare += 1
    rez_h = h_sosire - h_plecare + rez_min // 60
    rez_min %= 60

    return rez_h, rez_min


def calatorie(lista_program, start, finish):
    lst_trasee = []
    lst_gen = []
    gen(lista_program, lst_trasee, lst_gen, start, "00:00", start, finish)
    return lst_trasee


def gen(lst_prog, lst_trasee, lst_gen, curr, ora_minima, start, finish):
    lst_gen.append(curr)
    for d in lst_prog:
        if d["plecare"] == curr:
            if d["ora_plecare"] >= ora_minima:
                gen(lst_prog, lst_trasee, lst_gen, d["sosire"], d["ora_sosire"], start, finish)

    if len(lst_gen) > 1 and lst_gen[0] == start and lst_gen[-1] == finish:
        lst_trasee.append(lst_gen.copy())
    lst_gen.pop(-1)


def scrie_fisier(lista_program, start, finish):
    fout = open("traseu.txt", 'w')
    tmp_min = (100, 100)
    for traseu in calatorie(lista_program, start, finish):
        for d in lista_program:
            if d["plecare"] == traseu[0] and d["sosire"] == traseu[1]:
                h_plecare = d["ora_plecare"]
            if d["sosire"] == traseu[-1] and d["plecare"] == traseu[-2]:
                h_sosire = d["ora_sosire"]

        fout.write(f"Plecare la ora {h_plecare}, sosire la ora {h_sosire}. ")
        if len(traseu) > 2:
            tmp = ", ".join([traseu[i] for i in range(1, len(traseu)-1)])
            fout.write(f"Schimbare tren la {tmp}. ")
        tmp_calatorie = timp_calatorie(h_plecare, h_sosire)
        fout.write(f"Durata: {tmp_calatorie[0]}h {tmp_calatorie[1]}min.\n")
        if tmp_calatorie < tmp_min:
            tmp_min = tmp_calatorie
            traseu_min = traseu
    tmp = ' - '.join([*traseu_min])
    fout.write(f"Timp minim: {tmp}.")
    fout.close()


lst = fisier_dict("program.txt")
scrie_fisier(lst, "Bucuresti", "Brasov")
