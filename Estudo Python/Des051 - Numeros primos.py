#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' -')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\033[m\nO número {n} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo')



