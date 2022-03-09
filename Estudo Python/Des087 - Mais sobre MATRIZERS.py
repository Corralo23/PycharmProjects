# Aprimore o desafio anterior mostrando no final: a) A soma de todos os valores pares digitados;
#b) A soma dos valores da terceira coluna; c) O maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = soma_col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l} e {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos pares é de {par}')
for l in range(0, 3):
    soma_col += matriz[l][2]
print(f'A soma da 3ª coluna é {soma_col} ')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é {maior}')

