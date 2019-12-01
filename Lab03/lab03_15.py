fin = open("test.in", 'r')
data = fin.readlines()
fin.close()

fout = open("test.out", 'w')
nota = 1
for entry in data:
    fout.write(entry.strip() + ' ')
    tmp, rez = entry.split('=')
    n1, n2 = map(int, tmp.split('*'))
    if n1*n2 == int(rez):
        nota += 1
        fout.write("Corect\n")
    else:
        fout.write("Gresit " + str(n1*n2) + '\n')

fout.write("Nota " + str(nota))
fout.close()
