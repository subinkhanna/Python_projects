
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@logger
def add(a, b, count=0):
    return a + b

def main():
    c = add(3, 40, count=1)
    print(c)

if __name__ == "__main__":
    main()