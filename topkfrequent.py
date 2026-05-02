from collections import Counter
import heapq

nums = [1,1,1,2,2,3] 
k = 2

result = []

counts = Counter(nums)
print(counts)
print(heapq.nlargest(k, counts.keys(), key=counts.get))