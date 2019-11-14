# O metodă simplă (dar nesigură!!!) de criptare a unui text o reprezintă cifrul lui Cezar, prin care
# fiecare literă dintr-un text dat este înlocuită cu litera aflată peste 𝑘 poziții la dreapta în
# alfabet în mod circular. Valoarea 𝑘 reprezintă cheia secretă comună pe care trebuie să o cunoască
# atât expeditorul, cât și destinatarul mesajului criptat. Decriptarea unui text constă în înlocuirea
# fiecărei litere din textul criptat cu litera aflată peste 𝑘 poziții la stânga în alfabet în mod
# circular. Scrieți un program care să realizeze criptarea sau decriptarea unui text folosind cifrul
# lui Cezar.

def encrypt(s, n):
    tmp = ''
    for ltr in s:
        if ltr.isupper():
            tmp += chr(((ord(ltr) - ord('A') + n) % 26) + ord('A'))
        else:
            tmp += chr(((ord(ltr) - ord('a') + n) % 26) + ord('a'))

    return tmp


def decrypt(s, n):
    tmp = ''
    for ltr in s:
        if ltr.isupper():
            tmp += chr(((ord(ltr) - ord('A') - n) % 26) + ord('A'))
        else:
            tmp += chr(((ord(ltr) - ord('a') - n) % 26) + ord('a'))

    return tmp


str = input('sir: ')
k = int(input('k: '))
action = int(input('Vrei sa criptezi sau sa decriptezi sirul? (1 - criptare, 2 - decriptare): '))

if action == 1:
    str_new = encrypt(str, k)
else:
    str_new = decrypt(str, k)

print(str_new)
