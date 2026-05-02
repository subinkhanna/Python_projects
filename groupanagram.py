from collections import defaultdict

res = defaultdict(list)

strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
    count = [0]*26
    for c in s:
        count[ord(c) - ord("a")] += 1
    print(count)
    res[tuple(count)].append(s)

print(res.values())
## return list(res.values())
print(type(res.values()))




