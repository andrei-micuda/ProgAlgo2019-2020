# Scrieți un program care să furnizeze toate cuvintele dintr-un șir de caractere formate din aceleași litere cu ale unui
# cuvânt dat (fără a fi neapărat anagrame!). Dacă șirul nu conține nici un cuvânt cu proprietatea cerută, programul
# trebuie să afișeze un mesaj corespunzător. Cuvintele din șir sunt despărțite între ele prin spații și semnele de
# punctuație uzuale. De exemplu, pentru șirul “Langa o cabana, stand pe o banca, un bacan a spus un banc bun.” și
# cuvântul “bacan” funcția trebuie să furnizeze cuvintele “cabana”, “banca”, “bacan” și “banc”.

s = input() # "Langa o cabana, stand pe o banca, un bacan a spus un banc bun."
cuv = input() # "bacan"

cuv = set(cuv)
cuv.discard("-")

words = s.split()

for i in range(len(words)):
    word = ""
    for chr in words[i]:
        if chr.isalpha() or chr == '-':
            word += chr
    words[i] = word

for word in words:
    tmp = set(word)
    tmp.discard("-")
    if tmp == cuv:
        print(word)
