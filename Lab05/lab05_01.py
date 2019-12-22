def TMS(lst):
    tms = 0
    print("nr".center(5), "ti".center(5), "tt".center(5))
    for j, (i, x) in enumerate(lst):
        tt = sum([x for i, x in lst[:j+1]])
        tms += tt
        print(str(i).center(5), str(x).center(5), str(tt).center(5))
    print(f"TMS: {tms/len(lst): .2f}".center(17))
    print()


with open("tis.txt") as fin:
    L = [int(x) for x in fin.readline().split()]
for i, x in enumerate(L):
    L[i] = (i+1, x)

TMS(L)
TMS(sorted(L, key=lambda e: e[1]))
