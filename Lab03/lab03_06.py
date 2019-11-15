# Grupuri de cuvinte care rimează
# Se citește un text format din cuvinte de lungime minim 3, despărțite prin spațiu.
# a) Să se creeze un dicționar “rime” care are ca chei sufixe de lungime 2 ale cuvintelor din text, iar ca valori liste
# cu cuvintele din text care au ca acel sufix.
# b) Folosind “secvențe de inițializare” = ”dictionary comprehensions”, să se creeze un alt dicționar “final”, care
# preia din dicționarul “rime” doar acele perechi pentru care lista conține cel puțin 2 cuvinte pentru respectivul sufix.

s = input()

words = s.split()

# a
rime = dict()

for word in words:
    rime[word[-2:]] = rime.get(word[-2:], []) + [word]

print(rime)


# b

final = {k: v for k, v in rime.items() if len(v) >= 2}

print(final)
