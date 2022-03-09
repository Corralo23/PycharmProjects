def fib(n):
    if n < 1:
        return False
    if n < 3:
        return 1

    elem1 = elem2 = 1
    tot = 0
    for i in range(3, n + 1):
        tot = elem1 + elem2
        elem1, elem2 = elem2, tot
    return tot


for n in range(1, 10): # teste
    print(n, '->', fib(n))

