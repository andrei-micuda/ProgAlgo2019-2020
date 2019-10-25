'''
Se citește un număr natural nenul n. Să se afișeze cel mai mic și cel mare
număr ce pot fi formate din cifrele lui n. De exemplu, pentru n=812383 trebuie
afișate numerele 883321 și 123388.
'''

n = input('n: ')
digits = list(n)

digits.sort(reverse=True)
for digit in digits:
    print(digit, end='')
print()

digits.sort()
for digit in digits:
    print(digit, end='')
