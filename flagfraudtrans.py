from collections import defaultdict, deque

requests = [
        ("user1", 1),
        ("user1", 10),
        ("user1", 20),
        ("user1", 30),
        ("user1", 40),
        ("user1", 50),  # should be rejected
        ("user1", 70),  # should be allowed (timestamp 1 expired)
        ("user2", 1),
        ("user2", 10),
        ("user2", 20),
        ("user2", 30),
        ("user2", 40),
        ("user2", 50),  
        ("user2", 70),  
    ]

userReq = defaultdict(deque)

flagged = set()

for u,t in requests:

    q = userReq[u]

    if q and t - q[0] > 60:
        q.popleft()

    q.append(t)

    if len(q) >= 3:
        flagged.add(u)

print(flagged)
print(list(flagged))

