# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# a) Quantas vezes apareceu o valor 9; b) Em que posição foi digitado o primeiro valor 3; c) Quais foram os números pares
num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Os valores digitados foram: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3) +1}ª posição')
else:
    print(f'O numero 3 não foi digitado')

for n in num:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram os numeros: {n}')