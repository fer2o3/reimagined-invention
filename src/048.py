def solve():
    res = 0
    for i in range(1, 1001):
        res += pow(i, i)
    return str(res)[-10:]
