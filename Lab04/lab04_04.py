def prime():
    yield 2
    n = 3
    while True:
        i = 2
        is_prime = True
        while i*i <= n:
            if n % i == 0:
                is_prime = False
            i += 1

        if is_prime:
            yield n
        n += 2


n = int(input())

# a
print("Numerele prime mai mici sau egale cu {}:".format(n))
g = prime()
curr = next(g)
while curr <= n:
    print(curr, end=' ')
    curr = next(g)

# b
print("\nPrimele {} numere prime:".format(n))
g = prime()
i = 0
while i < n:
    print(next(g), end=' ')
    i += 1
