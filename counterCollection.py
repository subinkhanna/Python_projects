from collections import Counter

a = ["Subin Khanna", "Subin Khanna"]
a = "Subin Khanna"
b = Counter(a)
print(b.values())

print(b.most_common(1)[0][0])

print(list(b.elements()))