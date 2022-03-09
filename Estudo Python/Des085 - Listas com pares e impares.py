# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastra-los em uma lista única que mantenha
# separados os valores pares e impares. NO final, mostre os valores pares e impares em ordem crescente.
lista = [[], []]
num = 0
for n in range(0, 8):
    num = int(input('Sigite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
#num[0].sort()
#num[1].sort()
print(lista)
print(f'Os números pares digitados: {num[0].sort()}')
print(f'Os números impares digitados: {num[1].sort()}')
