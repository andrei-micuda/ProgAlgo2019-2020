def mat_parc(coord, dim):
    i, j = coord
    if dim-i == 0:
        return
    if dim-i == 1:
        lista_parcurgere.append((i, j))
        return
    for k in range(j, dim-1):
        lista_parcurgere.append((i, k))
    for k in range(i, dim-1):
        lista_parcurgere.append((k, dim-1))
    for k in range(dim-1, j, -1):
        lista_parcurgere.append((dim-1, k))
    for k in range(dim-1, i, -1):
        lista_parcurgere.append((k, j))

    mat_parc((i+1, j+1), dim-1)
    return


N = int(input())

mat = [[0 for j in range(N)] for i in range(N)]

# a
elem = 1
for i in range(N):
    for j in range(N):
        mat[i][j] = elem
        elem += 1

for i in range(N):
    for j in range(N):
        print(str(mat[i][j]).rjust(2), end=" ")
    print()

# b
lista_parcurgere = []
mat_parc((0, 0), N)

# c
spirala = []
for elem in lista_parcurgere:
    i, j = elem
    spirala.append(mat[i][j])

print(spirala)
