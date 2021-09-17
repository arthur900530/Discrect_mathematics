def rec(n):
    if n == 1:
        return 1
    return 2*rec(n-1) + 7

def rec2(n):
    return 1 + 8*(2**(n-1) - 1)

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# for i in range(1,10):
#     print(rec(i),',',rec2(i))

print(fib(20))