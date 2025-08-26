def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    res = 1
    for n in range(1, 21):
        res = lcm(res, n)
    return res
