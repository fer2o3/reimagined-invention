def solve():
    num = 2000000
    prime = [True for _ in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    sum = 0
    for p in range(2, num + 1):
        if prime[p]:
            sum += p

    return sum
