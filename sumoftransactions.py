transactions = [
    ("user1", 100),
    ("user2", 200),
    ("user1", 300),
    ("user2", -50),
    ("user3", 100),
    ("user4", 200),
    ("user3", 300),
    ("user2", -50),
]

from collections import defaultdict

def sumOfTransactions(transactions):
    balance = defaultdict(float)

    for u, b in transactions:
        balance[u] += b

#    print(dict(balance))
    return balance

sums = sumOfTransactions(transactions)

import heapq

result_2_largest = heapq.nlargest(2, sums.keys(), key=sums.get)

print(result_2_largest)
