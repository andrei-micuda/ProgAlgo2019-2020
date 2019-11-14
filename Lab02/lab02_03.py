#Scrieți un program care să înlocuiască într-o propoziție toate aparițiile unui cuvânt 𝑠 cu un cuvânt 𝑡.

str = input('sir: ')
s = input('s: ')
t = input('t: ')

words = str.split()
str_new = ''

for x in words:
    if s == x:
        str_new += t + ' '
    else:
        str_new += x + ' '

print(str_new)
