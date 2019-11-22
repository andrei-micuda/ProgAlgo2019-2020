fhandle = open("inventar.txt")

data = fhandle.readlines()

mag = dict()

for entry in data:
  entry = entry.split()
  mag[entry[0]] = set()
  for tmp in entry:
    if tmp.isnumeric():
      mag[entry[0]].add(tmp)

# a
for k, v in mag.items():
  print(k, end = ": ")
  print(v)

print()

# c
union = set()

for v in mag.values():
  union = union.union(v)

print(union)
print()

# b
intersection = union.copy()

for v in mag.values():
  intersection = intersection.intersection(v)

print(intersection)
print()

# d
print("DIFF")
for k, entry in mag.items():
  diff = entry.copy()
  print(k, end = ": ")
  for v in mag.values():
    if entry != v:
      diff -= v
  print(diff)
