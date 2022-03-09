#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçoes de pagamento:
# - a vista em dinheiro\cheque = 10;;;;;;;;;;5 desconto; a vista cartão = 5% desconto; - 2 x no cartao= preço formal; - 3 ou mais vezes no cartão = juros de 20%
from time import sleep
print('=' * 30)
produto = float(input('Informe o valor do produto que deseja comprar: '))
sleep(0.3)
print('=' * 30)
print('''CONDIÇÕES DE PAGAMENTO: 
[1] - À VISTA DINEHIRO OU CHEQUE 10% desconto;
[2] - À VISTA CARTÃO - 5% desconto;
[3] - 2 x no cartão - preço formal;
[4] - 3 ou mais vezes no cartão = juros de 20%''')
opção = int(input('Escolha a forma de pagamento: '))
print('=' * 30)
if opção == 1:
    v = produto - (produto * 0.10)
    print(f'Você escolheu a opção 1, o valor final ficou R${v}')
elif opção == 2:
    v = produto - (produto * 0.05)
    print(f'Você escolheu a opção 2, o valor final ficou R${v}')
elif opção == 3:
    v = produto
    print(f'Você optou pelo opção 3, o valor ficou R${v}')
elif opção == 4:
    v = produto + (produto * 0.20)
    vparc = int(input('Quantas parcelas? '))
    parcela = v / vparc
    print(f'Você optou pela opção 4, o valor final ficou R${v}')
    print(f'O valor da pracela ficou R${parcela}')
else:
    print('MUITO OBRIGADO PELA PREFERÊNCIA!! VOLTE SEMPRE')

print('=' * 30)
print('VOLTE SEMPRE!!!')
