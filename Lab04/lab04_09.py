def read_list():
    n = int(input())
    lst = [int(x) for x in input().split()]
    return lst, n


def find_elem(lst, i, j, x):
    for index, elem in enumerate(lst[i:j+1]):
        if elem > x:
            return i+index

    return -1


l, n = read_list()
sorted_desc = True
for i in range(1, n):
    if find_elem(l, i, n-1, l[i-1]) != -1:
        sorted_desc = False

if sorted_desc:
    print("Da")
else:
    print("Nu")
