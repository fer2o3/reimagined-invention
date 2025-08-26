def solve():
    a = sum(i * i for i in range(1, 101))
    b = sum(i for i in range(1, 101)) ** 2
    return b - a
