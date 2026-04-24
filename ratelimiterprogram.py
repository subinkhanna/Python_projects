from collections import defaultdict, deque
from typing import Dict, Tuple

class Ratelimiter:
    def __init__(self, limit: int = 5, window: int=60):
#        self.limit = limit
#        self.window = window
        self.user_requests = defaultdict(deque)
        self.user_config: Dict[str, Tuple[int, int]] = {}

    def set_user_config(self, user_id:str, limit:int, window: int):
        self.user_config[user_id] = (limit, window)

    def allow_requests(self, user_id:str, timestamp:int) -> bool:
        requests = self.user_requests[user_id]

        limit, window = self.user_config.get(user_id,(5,60))

#        while requests and timestamp - requests[0] >= self.window:
        while requests and timestamp - requests[0] >= window:    
            requests.popleft()

#        if len(requests) < self.limit:
        if len(requests) < limit:
            requests.append(timestamp)
            return True

        return False

def main():
    limiter = Ratelimiter()
    limiter.set_user_config("user1", 2, 30)
    limiter.set_user_config("user2", 5, 60)
    
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
    
    for user_id, timestamp in requests:
        allowed = limiter.allow_requests(user_id, timestamp)
        print(f"Request from {user_id} at {timestamp}: {allowed}")


if __name__ == "__main__":
    main()