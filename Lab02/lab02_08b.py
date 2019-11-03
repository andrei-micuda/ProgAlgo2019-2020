'''
Se citește de la tastatură un text în care cuvintele sunt despărțite în silabe cu ajutorul cratimelor. Se cere să se “traducă”
textul dat în limba păsărească astfel: după fiecare silabă se adaugă litera p și se repetă ultima literă din acea silabă.
Afișați traducerea și cu cratime, dar și fără.
Exemplu: “A-na a-re mul-te me-re ro-sii si de-li-cioa-se.” devine
“Apa-napa apa-repe mulpl-tepe mepe-repe ropo-siipi sipi depe-lipi-cioapa-sepe.” și
“Apanapa aparepe mulpltepe meperepe roposiipi sipi depelipicioapasepe.”
Fiind dat un astfel de text în limba păsărească (cel care conține și cratime), se poate obține textul original?
Dacă da, faceți asta.
'''

def reverse(s):
    rev = ""

    j = 0
    while j < len(s):
        if s[j] == '-' or s[j] == ' ':
            rev = rev[:len(rev)-2]
        rev += s[j]
        j += 1

    return rev


s = input()

new_s = ""

i = 0
while i < len(s):
    if s[i] == '-' or s[i] == ' ':
        new_s += 'p' + s[i-1].lower()
    new_s += s[i]
    i += 1

print(new_s)
print(new_s.replace('-', ''))
print(reverse(new_s))
