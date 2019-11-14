# Să se determine cuvântul care apare cel mai des într-o propoziție dată, precum și cuvântul care apare cel mai rar. Dacă sunt mai multe
# posibilități, se vor afișa cuvintele cele mai mici din punct de vedere lexicografic.

s = input()

words = s.split()

for i in range(len(words)):
    x_new = ''
    for tmp in words[i]:
        if tmp.isalpha() or tmp == '-':
            x_new += tmp
    words[i] = x_new

freq = dict()

for word in words:
    freq[word] = freq.get(word, 0) + 1

max_ap = max(freq.values())
min_ap = min(freq.values())

max_words = []
min_words = []

for k, v in freq.items():
    if v == max_ap:
        max_words.append(k)
    if v == min_ap:
        min_words.append(k)

max_words.sort()
min_words.sort()

print(max_words[0], min_words[0])
