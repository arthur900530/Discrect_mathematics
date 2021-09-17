def lcm(a,b):
    gcd = 1
    for n in range(1,min(a,b)+1):
        if a % n == 0 and b % n == 0:
            gcd = n
    return a*b/gcd

print(lcm(100,100))