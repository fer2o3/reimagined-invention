def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def solve():
    return factorial(2 * 20) // (factorial(20) * factorial(20))
