#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input('Infome um valor real qualquer: '))
print(f'O valor informado foi {num}, sendo que sua parte inteira é {trunc(num)}')