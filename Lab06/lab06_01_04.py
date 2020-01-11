def find_peak(lst, i, j):
    if j-i+1 == 1:
        return i
    elif j-i+1 == 2:
        if lst[i] < lst[j]:
            return j
        else:
            return i
    mij = (i+j)//2
    if lst[mij-1] < lst[mij] > lst[mij+1]:
        return mij
    elif lst[mij-1] < lst[mij] < lst[mij+1]:
        return find_peak(lst, mij, j)
    else:
        return find_peak(lst, i, mij)


with open("date.in") as fin:
    n = int(fin.readline())
    lst = [int(x) for x in fin.readline().split()]

with open("date.out", 'w') as fout:
    fout.write(str(lst[find_peak(lst, 0, n-1)]))
