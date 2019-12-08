fin = open("cuvinte.txt")
L = fin.read().split()
fin.close()

print(sorted(L, reverse=True))
print(sorted(L, key=lambda e: (len(e), e)))
print(sorted(L, key=len))
