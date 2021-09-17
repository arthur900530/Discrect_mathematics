def add_up_to(n):
    if n == 1:
        return 1
    return n + add_up_to(n-1)

print(add_up_to(100))
