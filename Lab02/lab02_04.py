# Scrieți un program care să se verifice dacă două șiruri de caractere sunt anagrame sau nu. Două
# șiruri sunt anagrame dacă unul se poate obține din celălalt printr-o permutare a caracterelor sale.
# De exemplu, șirurile emerit și treime sunt anagrame, dar șirurile emerit și treimi nu sunt!

str1 = input('sir 1: ')
str2 = input('sir 2: ')

if len(str1) != len(str2):
    print('Sirurile nu sunt anagrame.')
else:
    for x in str1:
        if x in str2:
            str2 = str2.replace(x, '', 1)

    if not str2:
        print('Sirurile sunt anagrame.')
    else:
        print('Sirurile nu sunt anagrame.')
