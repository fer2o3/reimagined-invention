def chain(n, memo):
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        nxt = n // 2
    else:
        nxt = 3 * n + 1

    memo[n] = 1 + chain(nxt, memo)
    return memo[n]


def solve():
    memo = {1: 1}
    max_i, max_len = 1, 1

    for i in range(2, 1000001):
        length = chain(i, memo)
        if length > max_len:
            max_len, max_i = length, i

    return max_i
