#Se citește de la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat astfel: după fiecare vocală se adaugă
#litera p și încă o dată acea vocală (după a, e, i, o, u se adaugă respectiv pa, pe, pi, po, pu). Exemplu: “Ana are mere.” devine
#“Apanapa aparepe meperepe.”
#Fiind dat un astfel de text în limba păsărească, se poate obține textul original? Dacă da, faceți asta.

vocale = ("a", "e", "i", "o", "u")

s = input()

new_s = ""

i = 0
while i < len(s):
    new_s += s[i]
    if s[i].lower() in vocale and s[i+1:].startswith("p"+s[i].lower()):
        i += 2
    i += 1

print(new_s)
