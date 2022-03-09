#Escreva um programa  para aprovar o emprestimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
print('=' * 30)
print('PROGRAMA MINHA CASA MINHA DÍVIDA')
print('=' * 30)
valor = float(input('Informe o valor a ser financiado? R$'))
salario = float(input('Informe seu salário: R$'))
tempo = int(input('Informe o tempo que vai querer pagar o imóvel em meses? '))
prest = valor / tempo
if prest <= salario *0.30:
    print(f'Seu financiamento foi aprovado, sua prestação sera de R${prest :.2f}.')
else:
    print('O empréstimo foi negado, excede o limite de 30% de seu salário')

