#cRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR

numero = int(input('diga um número:  '))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é IMPAR.')
