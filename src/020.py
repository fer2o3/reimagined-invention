def solve():
    num = 1
    for i in range(2, 101):
        num *= i
    return sum([int(j) for j in str(num)])
