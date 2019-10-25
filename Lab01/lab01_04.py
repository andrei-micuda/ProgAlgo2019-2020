'''
Se citește un șir format din n numere reale strict pozitive (n≥2), reprezentând
cursul de schimb valutar RON/EURO din n zile consecutive. Să se afișeze
zilele între care a avut loc cea mai mare creștere a cursului valutar, precum și
cuantumul acesteia. De exemplu, pentru n=6 zile și cursul valutar dat de șirul
4.25,4.05,4.25,4.48,4.30,4.40, cea mai mare creștere a fost de 0.23 RON,
între zilele 3 și 4.
'''

n = int(input('n: '))

mx = None
ant = float(input())

for i in range(1, n):
    tmp = float(input())
    if mx is None or tmp-ant > mx:
        mx = tmp-ant
        day = i+1

mx *= 100
mx = int(mx)
mx /= 100
print('Crestere: ', mx, 'RON')
print('Zilele: ', day-1, day)
