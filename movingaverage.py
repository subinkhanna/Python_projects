from collections import deque

class Movingavg:
    def __init__(self, k):
        self.k = k
        self.window = deque()
        self.sum = 0.0

    def nextitem(self, x):
        
        self.window.append(x)
        self.sum += x

        if len(self.window) > self.k:
            removed = self.window.popleft()
            self.sum -= removed
        
        return f"{(self.sum / len(self.window)):.2f}"




def main():
    ma = Movingavg(5)
    print(ma.nextitem(1))
    print(ma.nextitem(2))
    print(ma.nextitem(3))
    print(ma.nextitem(4))
    print(ma.nextitem(5))
    print(ma.nextitem(6))
    print(ma.nextitem(7))
    print(ma.nextitem(0))
    print(ma.window)


if __name__ == "__main__":
    main()


