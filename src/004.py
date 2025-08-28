def solve():
    palindromes = []
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                palindromes.append(prod)
    return max(palindromes)
