def fatoria(k):
    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1
        k_fat *= cont

    return k_fat


print(f'0! = {fatoria(0)}')
print(f'1! = {fatoria(1)}')
print(f'5! = {fatoria(5)}')
print(f'17! = {fatoria(17)}')