def solve():
    num = 999999
    prime = [True for _ in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)

    return primes[10000]
