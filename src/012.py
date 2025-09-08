def count_divisors(n):
    i = 2
    res = 0
    while i * i <= n:
        if i * i == n:
            res += 1
        elif n % i == 0:
            res += 2
        i += 1
    return res


def solve():
    res = 0
    triangle = 0
    for i in range(9999999):
        triangle += i
        if count_divisors(triangle) > 500:
            break
    return triangle
