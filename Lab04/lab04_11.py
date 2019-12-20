def f1(*args):
    rez = 0
    for x in args:
        cif_max = int(max(*str(x)))
        rez = rez*10 + cif_max
    return rez


def f2(a, b, c):
    if f1(a, b, c) <= 111:
        return 1
    else:
        return 0
