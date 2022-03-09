#Faça um programa que leia o preço de um produto e mostre seu novo preço com desconto de 5%;
v = float(input('Diga o valor do produto: '))
d = v - (v * 0.05)
print(f'O valor do produto com 5% de desconto é de R${d :.2f}')