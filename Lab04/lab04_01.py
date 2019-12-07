from math import sqrt

# a
def ipotenuza(a, b):
    return sqrt(a**2 + b**2)


# b
fout = open("triplete_pitagoreice.txt", "w")
b = int(input("b: "))

for a in range(1, b+1):
    c = ipotenuza(a, b)
    if c.is_integer():
        fout.write(str(a) + ' ' + str(b) + ' ' + str(int(c)) + '\n')
        
fout.close()
