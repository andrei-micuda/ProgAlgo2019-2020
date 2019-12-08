def citire():
    v = [int(x) for x in input().split()]

    return v


def afisare(v):
    for x in v:
        print(x, end=' ')
    print()


def valpoz(v):
    return [x for x in v if x >= 0]


def semn(v):
    i = 0
    while i < len(v):
        v[i] = -v[i]
        i += 1
