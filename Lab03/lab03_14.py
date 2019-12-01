import random

def gen_pass():
    password = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password += ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=3))
    password += ''.join(random.choices("0123456789", k=4))
    return password


fin = open("date.in", 'r')
data = fin.readlines()
fin.close()

fout = open("date.out", "w")
for entry in data:
    nume, prenume = entry.split()
    nume = nume.lower()
    prenume = prenume.lower()

    str_out = prenume + '.' + nume + "@myfmi.unibuc.ro,"
    str_out += gen_pass()
    fout.write(str_out + '\n')

fout.close()
