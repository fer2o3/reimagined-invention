def solve():
    a, b = 1, 2
    res = 0
    while a <= 4000000:
        if a % 2 == 0:
            res += a
        a, b = b, a + b

    return res
