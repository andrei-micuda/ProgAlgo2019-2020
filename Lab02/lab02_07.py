'''
Știind că 1 ianuarie 1702 a picat într-o zi de duminică, să se citească de la tastatură o dată mai recentă, și să se spună în ce
zi a săptămânii cade aceasta. Puteți să faceți 2 cazuri - în care inputul este dat de forma "1 10 2019", sau "1 octombrie 2019". Folosiți funcția range() pentru a itera printre ani, respectiv instrucțiuni if/elif/else pentru a trata
'''


def isleap(year):
    year = int(year)
    if year % 4 != 0:
        return False #common year
    elif year % 100 != 0:
        return True #leap year
    elif year % 400 != 0:
        return False #common year
    else:
        return True #leap year


day = {
    0: "luni", 1: "marti", 2: "miercuri", 3: "joi",
    4: "vineri", 5: "sambata", 6: "duminica"
}

days_in_month = {
    1: 31, 2: 28, 3: 31,
    4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30,
    10: 31, 11: 30, 12: 31
}

month = {
    "ianuarie": 1, "februarie": 2, "martie": 3,
    "aprilie": 4, "mai": 5, "iunie": 6,
    "iulie": 7, "august": 8, "septembrie": 9,
    "octombrie": 10, "noiembrie": 11, "decembrie": 12
}

date = input("Introduceti data: ")
tmp = date.split()
if not tmp[1].isdigit():
    tmp[1] = month[tmp[1]]

d, m, y = map(int, tmp)

if y < 1702:
    print("Introduceti o data mai recenta decat 1 ianuarie 1702.")
    quit()

days = 0
for year in range(1702, y):
    if isleap(year):
        days += 366
    else:
        days += 365

for month in range(1, m):
    days += days_in_month[month]

if isleap(y) and m > 2:
    days += 1

days += d-1

print(day[(6 + days) % 7])
