#Crie um programa que declare uma MATRIZ de dimesnão 3 x 3 e preencha com valores idos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): #linha da matriz
    for c in range(0, 3): #coluna da matriz
        matriz[l][c] = int(input(f'Digite um valor para {l} e {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()