# Negociere
# Se cere prelucrarea unui discuții dintre persoana A, care vinde un obiect, și persoana B, care oferă bani pentru el. O astfel de
# discuție se poate desfășura în modul următor:
# • “Eu am de gând să vând vaza aceasta pentru $5. Ce plăcut, chiar mi-ar plăcea să o achiziționez, doar că am numai $3 la mine.
# Este suficient? Nu, insist să obțin $5 pe ea. Bine, atunci voi scoate niște bani și-ți aduc cei $5.”
# • “Salut, am văzut în acel anunț că vindeți o mașină second-hand. M-ar interesa s-o achiziționez pentru suma de $2700.
# Vă amintesc că suma din anunț este de $3000, sir. Desigur. Și totuși, n-am putea ajunge la mijloc? $2850? $2850 de dolari,
# spuneți? Mi se pare corect, s-a făcut.”
# După cum se poate observa din exemple, regulile sunt acestea:
# • se știe că fiecare persoană face câte o ofertă, pe rând, iar suma se apropie spre o valoare aflată între primele două oferte.
# • Considerăm că persoana A este cea care oferă, cum este și logic :), prețul mai mare dintre primele două oferte.
# • Când ultimele două oferte sunt egale, știm că cele două persoane au ajuns la un acord comun (*).
# Cerințe:
# a) Extrageți din text primele două valori. (hint: orice sumă este un număr după semnul $ în șir)
# b) Decideți dacă cele două persoane “s-au înțeles” :). (vezi (*))

s = input()

words = s.split()

sume = list()

for word in words:
    if word.startswith('$'):
        i = 1
        suma = ""
        while i < len(word) and word[i].isdigit():
            suma += word[i]
            i += 1

        sume.append(int(suma))

print("A: $", max(sume[0], sume[1]), sep='')
print("B: $", min(sume[0], sume[1]), sep='')

if sume[len(sume)-1] == sume[len(sume)-2]:
    print("Cele două persoane au ajuns la un acord comun.")
else:
    print("Cele două persoane nu au ajuns la un acord comun.")
