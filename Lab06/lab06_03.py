def bin_src_first(lst, k):
    pas = 1
    r = 0
    while pas < len(lst):
        pas *= 2

    while pas:
        if r+pas < len(lst) and lst[r+pas] < k:
            r += pas
        pas //= 2
    if lst[r+1] != k:
        return -1
    return r+1


def bin_src_last(lst, k):
    pas = 1
    r = 0
    while pas < len(lst):
        pas *= 2

    while pas:
        if r + pas < len(lst) and lst[r + pas] <= k:
            r += pas
        pas //= 2
    if lst[r] != k:
        return -1
    return r


with open("data.in") as fin:
    lst = [int(x) for x in fin.read().split()]

lst.sort()
lst = [0] + lst

x = int(input())
print(bin_src_last(lst, x) - bin_src_first(lst, x) + 1)
