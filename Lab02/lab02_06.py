'''
Jurnalul electronic al Anei conține, în fiecare zi, câte o frază cu informații desprecheltuielile pe care ea le-a efectuat în ziua
respectivă. Scrieți un program care să citească o frază de acest tip din jurnalul Anei și apoi să afișeze suma totală cheltuită de
ea în ziua respectivă. De exemplu, pentru fraza “Astăzi am cumpărat pâine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am
cumpărat niște cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!”, programul trebuie să afișeze suma totală de
80 RON. Fraza se consideră corectă, adică toate numerele care apar în ea sunt numere naturale reprezentând sume cheltuite de Ana
în ziua respectivă!
'''
s = input("Fraza: ")

words = s.split()
total = 0

for word in words:
    if word.isnumeric(): total += int(word)

print(total, "RON")
