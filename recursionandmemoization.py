##Recursion + Memoization = Dynamic programming
memory = {}
def find_fibo(n):
    if n in memory:
        return memory[n]
    
    if n <= 2:
        result = 1
    else:
        result = find_fibo(n-1) + find_fibo(n-2)

    memory[n] = result
    return result

print(find_fibo(100))