def isPrime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

# print(isPrime(7))

def nthPrime(n):
    count = 0
    start = 2
    while True:
        if isPrime(start):
            count += 1
        if count == n:
            break
        start += 1
    return start

print(nthPrime(100))
