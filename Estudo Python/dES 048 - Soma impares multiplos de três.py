# Faça um programa que calcule a soma entre todos os números que são multiplos de três e que se encontram no intervalo de 1 até 500
s = 0
cont = 0
for n in range(0, 501, 3):
    print(n, end=' ')
    s = s + n
    cont = cont + 1
print(f'\nSoma dos valores solicitados é {s}')
print(f'\nTemos {cont} números multiplos de 3')
print('FIM!!!')

#if c % 3 == 0:
#print(c)