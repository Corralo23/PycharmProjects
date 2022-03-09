# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores impares digitados respectivamente. Ao final, mostre as tres listas
num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
print(num)
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os numeros pares digitads: {par}.')
print(f'Os numeros impraes digitados{impar}.')

