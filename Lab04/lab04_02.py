from math import pi


# a
def lungime_arie_cerc(r):
    return 2 * pi * r, pi * (r ** 2)


# b
r = float(input("raza: "))
l, a = lungime_arie_cerc(r)
print(l, a)
