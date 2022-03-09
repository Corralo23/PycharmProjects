#fAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA
num = int(input('Digite um número para ser calculado na tabuada: '))

for c in range(1, 11):
     m = num * c
     print(f'{num} x {m} = {num * c}')

