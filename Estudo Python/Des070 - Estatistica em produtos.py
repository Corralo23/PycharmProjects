# Crie um programa que leia o nome e o preço de váriosprodutos., O programa deverá perguntar se o usuário vai continuar ou não. No final mostre:
#a) qual é o total gasto na compra; b) quantos produtos custam mais de R$1.000,00; c) qual é o nome do produto mais barato
total = mais = menor = cont = 0
barato = ''
resp = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto R$'))
    cont += 1
    total += preco
    resp = str(input('Quer continuar[S/N]: '))
    if resp in 'Ss':
        if preco > 1000:
            mais += 1
        if cont == 1:
            menor = preco
            barato = produto
        else:
            if preco < menor:
                menor = preco
                barato = produto
    else:
        break

print(f'O total das compras foi R${total}.')
print(f'foram adquiridos {mais} com o valor acima de R$1.000,00.')
print(f'O produto mais barato foi a {barato}, que custa R${menor}')