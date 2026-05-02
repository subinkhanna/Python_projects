from collections import defaultdict

res = defaultdict(list)

strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
    key =  tuple(sorted(s))
    res[key].append(s)

print(res.values())
## return list(res.values())
##print(type(res.values()))