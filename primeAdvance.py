def isPrime(n):
    plist = factorPrime(n)
    if len(plist) == 1:
        return True
    else:
        return False


def factorPrime(a):
    f = []
    n = 2
    while a > 1:
        if a % n == 0:
            if n not in f:
                f.append(n)
            a /= n
        else:
            n += 1
    return f

print(isPrime(11))