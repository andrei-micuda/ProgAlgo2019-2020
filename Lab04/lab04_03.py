def min_max(*args):
    if len(args) < 1:
        return None
    for x in args:
        if type(x) is not int:
            return None
        if type(x) is int and x < 0:
            return None

    return min(args), max(args)


try:
    fin = open("numere.txt", 'r')
except FileNotFoundError:
    print("Nu exista un fisier cu acest nume.")
    quit()

data = fin.read()
fin.close()
try:
    lst = list(map(int, data.split()))
except ValueError:
    print("Datele din fisier nu sunt numere intregi.")
    quit()

nr_min, nr_max = min_max(*lst)
print(nr_min, nr_max)
try:
    rez = nr_max / nr_min
except ZeroDivisionError:
    print("Nu se poate realiza impartirea.")
    quit()

try:
    fout = open("impartire.txt", 'w')
    fout.write(str(rez))
except PermissionError:
    print("Nu se poate folosi fisierul de iesire.")
    quit()
fout.close()
