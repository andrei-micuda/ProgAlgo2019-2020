'''
Se dă o ecuație de gradul II de forma generala. Realizați un algoritm care să
determine rădăcinile acesteia.
'''

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)

else:
    delta = -delta
    x1 = complex(-b/(2*a), (delta**0.5)/(2*a))
    x2 = complex(-b/(2*a), -(delta**0.5)/(2*a))

print(x1, x2)
