# Folosind un dicționar, să se numere de câte ori apare fiecare caracter într-un text de tip "lorem ipsum".
# s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
s = input()

freq = dict()

for char in s:
    freq[char] = freq.get(char, 0) + 1

for k, v in freq.items():
    print(k, v, sep = ": ")
