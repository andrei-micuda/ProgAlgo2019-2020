# Să se unifice două dicționare în care cheile sunt șiruri de caractere, iar valorile sunt de tip numeric.
# Astfel, în rezultat va apărea fiecare cheie distinctă, iar pentru o cheie care apare în ambele dicționare inițiale
# valoarea corespunzătoare va fi egală cu suma valorilor asociate cheii respective în cele două dicționare.

def dict_merge(d1, d2):
    if type(d1) is not dict or type(d2) is not dict:
        print("Error, parameters are not dictionaries.")
        quit()

    for k, v in d2.items():
        d1[k] = d1.get(k, 0) + v

    return d1


d1 = {"ana": 3, "are": 2, "mere": 5}
d2 = {"ion": 2, "are": 1, "pere": 2, "si": 2, "mere": 2}

d3 = dict_merge(d1, d2)
print(d3)
