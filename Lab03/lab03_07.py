# Total cheltuieli
# De la tastatură se citește numele unui fișier. Acel fișier conține un text în care sunt specificate cheltuielile
# efectuate de Ana într-o zi. Scrieți un program care să afișeze suma totală cheltuită de Ana în ziua respectivă.

def isnumber(x):
    if x.isdecimal():
        return True

    x = x.split(".")
    if len(x) == 2 and x[0].isdecimal() and x[1].isdecimal():
        return True

    return False


fhandle = open("cheltuieli.txt", "r")

txt = fhandle.read()
fhandle.close()

words = txt.split()
tmp = 0
total = 0

for wrd in words:
    if isnumber(wrd):
        if tmp == 0:
            tmp = float(wrd)
        else:
            total += tmp * float(wrd)
            tmp = 0

print(total)
