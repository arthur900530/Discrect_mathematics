def pascalTriangle(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    p = pascalTriangle(n-1)
    p2 = [1]

    for i in range(len(p)-1):
        p2.append(p[i] + p[i+1])

    p2.append(1)
    return p2

print(pascalTriangle(6))