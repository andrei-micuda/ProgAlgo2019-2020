'''
Un greiere se deplasează efectuând câte o săritură, lungimea inițială a
săriturii fiind de x cm. După fiecare n sărituri, lungimea săriturii greierului se
micșorează cu p procente. Cunoscându-se valorile x,n,p, precum și numărul
de sărituri m pe care le face greierele, să se scrie un program care să afișeze
distanța parcursă de greiere. De exemplu, pentru x=20,n=10, p=10 și m=20
distanța parcursă de greiere este egală cu 380 cm, deoarece primele 10
sărituri efectuate au, fiecare, lungimea de 20 cm, iar următoarele 10 au,
fiecare, lungimea de 18 cm.
'''

x = int(input('x: '))
n = int(input('n: '))
p = int(input('p: '))
m = int(input('m: '))

dist = 0
while m >= n:
    dist += x*n
    m -= n
    x -= p/100*x

dist += m*x

print(dist)
