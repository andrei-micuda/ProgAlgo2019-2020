def negative_pozitive(lst):
    lst_neg = []
    lst_poz = []
    for nr in lst:
        if nr < 0:
            lst_neg.append(nr)
        elif nr > 0:
            lst_poz.append(nr)

    return lst_neg, lst_poz


lst = [int(x) for x in input().split()]
lst_neg, lst_poz = negative_pozitive(lst)

print("Negative:", lst_neg)
print("Pozitive:", lst_poz)
