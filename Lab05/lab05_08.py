def find_spot(lst, x):
    deadline = x[1]
    for i in range(deadline-1, -1, -1):
        if lst[i] == 0:
            lst[i] = x
            break


with open("proiecte.txt") as fin:
    lst_proiecte = []
    for line in fin:
        nume, deadline, profit = line.split()
        lst_proiecte.append((nume, int(deadline), int(profit)))

nr_proiecte = max([x[1] for x in lst_proiecte])
schedule = [0] * nr_proiecte
for p in sorted(lst_proiecte, key=lambda e: e[2], reverse=True):
    find_spot(schedule, p)

with open("profit.txt", 'w') as fout:
    fout.write(f"T = {nr_proiecte}\n")
    tmp = ", ".join([str(x[0]) for x in schedule])
    fout.write(f"Proiecte: {tmp}\n")
    tmp = " + ".join([str(x[2]) for x in schedule])
    fout.write(f"Profit: {tmp} = {sum([x[2] for x in schedule])}")
