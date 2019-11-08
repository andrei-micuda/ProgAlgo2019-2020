'''
Numele Pre-Nume
Scrieți un program care citește un șir de caractere și decide dacă acesta este un nume corect al unei persoane. Se consideră că un nume este corect dacă respectă următoarele proprietăți:
• Orice nume sau prenume conține doar litere și cel mult o cratimă.
• Orice nume sau prenume este format din cel puțin 3 litere.
• Orice nume sau prenume începe cu literă mare.
• Prenumele sunt cel mult două, iar dacă sunt două atunci sunt despărțite printr-o cratimă (‘-’).
'''

def isValidName(string):
    tmp = string.split('-', 1)
    names = ""
    for x in tmp:
        names += x.strip()

    print(names)
    if len(names) > 3: return False

    for x in names:
        if len(x) < 3: return False
        if not x.isalpha(): return False
        if not x[0].isupper(): return False

    return True


s = input("s= ")
print(isValidName(s))

