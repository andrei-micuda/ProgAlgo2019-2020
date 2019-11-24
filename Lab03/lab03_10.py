# Departajare

line = input()
participanti = []
punctaje = set()
nr_ord = 1

while line != "-1":
    tmp = line.split(" ", 1)
    # a
    participanti.append((int(tmp[0]), tmp[1], nr_ord))
    # b
    punctaje.add(int(tmp[0]))
    line = input()
    nr_ord += 1

print(participanti)
print(punctaje)

clasament = dict()
for entry in participanti:
    clasament[entry[0]] = clasament.get(entry[0], []) + [(entry[1], entry[2])]

clasament = sorted(clasament.items(), reverse=True)

for x in clasament:
    print(x[0], x[1], sep=": ")
