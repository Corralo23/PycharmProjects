#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# a) Quantas pessoas foram cadastradas; b) Uma listagem com as pessoas mais pesadas;
# c) uma listagem comas pesoas mais leves
listagem = []
cadastro = []
peso_maior = peso_menor = 0

while True:
    listagem.append(str(input('Nome: ')))
    listagem.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        peso_maior = peso_menor = listagem[1]
    else:
        if listagem[1] > peso_maior:
            peso_maior = listagem[1]
        if listagem[1] < peso_menor:
            peso_menor = listagem[1]
    cadastro.append(listagem[:])
    listagem.clear()
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break

print(cadastro)
print(f'Foram cadastrados {len(cadastro)} pessoas')
print(f'O maior peso foi de {peso_maior}KG de ', end='')
for p in cadastro:
    if p[1] == peso_maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {peso_menor}KG de ', end='')
for p in cadastro:
    if p[1] == peso_menor:
        print(f'[{p[0]}]', end='')