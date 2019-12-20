# a
def update_situatie_student(student, c):
    if student["nr_crd"] < c:
        student.update({"situatie": "Nepromovat"})
    else:
        student.update({"situatie": "Promovat"})


# b
def sort_studenti(lst):
    lst.sort(key=lambda e: (e["grupa"], -e["nr_crd"]))


t = [
    {
        "nume": "Popa Ion",
        "grupa": 133,
        "nr_crd": 40,
    },
    {
        "nume": "Popescu Daniel",
        "grupa": 131,
        "nr_crd": 45
    },
    {
        "nume": "Ionescu David",
        "grupa": 133,
        "nr_crd": 65
    },
    {
        "nume": "Ion Matei",
        "grupa": 105,
        "nr_crd": 20
    },
    {
        "nume": "Anton George",
        "grupa": 133,
        "nr_crd": 29
    }
]
c = int(input())
for i in t:
    update_situatie_student(i, c)

sort_studenti(t)

print(t)
