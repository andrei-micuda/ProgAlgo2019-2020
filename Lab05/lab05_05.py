with open("activitati.txt") as fin:
    n = int(fin.readline())
    lst_activitati = []
    for line in fin:
        lst_activitati.append(tuple(map(int, line.split())))

t_curr = 0
H = None
with open("intarzieri.txt", 'w') as fout:
    fout.writelines(["Interval".center(10), "Termen".center(10), "Intarziere".center(10), '\n'])
    for d, t in sorted(lst_activitati, key=lambda e: e[1]):
        fout.writelines([f"{t_curr}-->{t_curr+d}".center(10), str(t).center(10), str(max(0, t_curr+d-t)).center(10), '\n'])
        if H is None or H < t_curr+d-t:
            H = t_curr+d-t
        t_curr += d

    fout.write(f"Intarzierea maxima: {H}")
