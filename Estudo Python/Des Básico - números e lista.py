#Faça um programa que leia 20 números inteiros e armazene-os numa lista. Armazenar numeors pares e impares em listas separadas
num = [[], [], []]
valor = 0

for c in range(1, 21):
    valor = int(input('Informe um número: '))
    num[2].append(valor)
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)


print(f'Lista numeros pares {num[0]}')
print(f'Lista numeros impares {num[1]}')
print(f'Lista completa {num[2]}')






