#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
d = float(input('Diga quanto em dinheiro você tem na carteira: R$'))
dol = d / 3.27
print(f'Você tem R${d}. A cotação do dolar está em R$3.27. Logo, você poderá comprar ${dol :.2f} dolares.')
