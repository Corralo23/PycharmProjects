#Faça um programa que leia un número qualquer e ostre o seu fatorial.
import math
n = int(input('Informe um número para calcular a fatorial: '))
fat = math.factorial(n)
print(f'O fatorial de {n} é : {fat}.')

n1 = int(input('Diga um número: '))
c = n1
f = 1
print(f'Calculando {n1}!= ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f' {f}')
