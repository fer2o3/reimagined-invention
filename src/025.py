def solve():
    a, b, i = 0, 1, 0
    while True:
        a, b = b, a + b
        i += 1
        if len(str(a)) == 1000:
            return i
