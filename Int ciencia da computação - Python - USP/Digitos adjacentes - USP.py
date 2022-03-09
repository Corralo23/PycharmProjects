n = int(input('Digite um número inteiro: '))
adjacentes = False
n1 = n % 10
n = n // 10
d = 0

while n > 0 and not adjacentes:
    n2 = n % 10
    n = n // 10
    if n2 == n1:
        adjacentes = True
    n1 = n2
if adjacentes:
    print('sim')
else:
    print('não')