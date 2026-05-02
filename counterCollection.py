from collections import Counter

a = ["Subin Khanna", "Subin Khanna", "Neha"]
#a = "Subin Khanna"
b = Counter(a)
print(b)
print(b.values())
print(b.most_common)
print(b.most_common(2)[0][0])

print(list(b.elements()))