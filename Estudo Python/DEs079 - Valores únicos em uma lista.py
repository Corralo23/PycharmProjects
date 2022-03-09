# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastra-los em uma lista.
# Caso o número já exista la dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente
num = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
num.sort()
print(num)