def fatoria(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n -1
    return fat


def num_binomial(n, k):
    return fatoria(n) / (fatoria(k) * fatoria(n - k))

print(num_binomial(5, 3))


