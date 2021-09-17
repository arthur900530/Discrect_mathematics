def gcd(a,b):
    if a>b:
        c = a
        a = b
        b = c
    return a if b%a==0 else gcd(b%a,a)

print(gcd(55,10))