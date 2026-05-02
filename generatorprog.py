def read_file(file_path):
    with open(file_path) as r:
        for line in r:
            yield line.strip()

file_path = "C:\\Users\\mk\\Desktop\\Preparation notes.txt"

for l in read_file(file_path):
    print(l)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for x in fibonacci(100):
    print(x)