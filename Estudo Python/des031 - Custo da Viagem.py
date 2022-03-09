#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para biagens de até 200km e R$0,45 para biagens mais longas
viagem = int(input('Informe a distância de sua viagem: '))
if viagem <= 200:
    custo = viagem * 0.50
    print(f'O custo de sua viagem foi de {custo}')
else:
    custo = viagem * 0.45
    print(f'o custo de sua viagem é de {custo}')

#custo = viagem * 0.50 if viagem <= 200 else viagem * 0.45