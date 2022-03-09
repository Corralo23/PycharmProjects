# Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte ao usuário qual será valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cedulas de cada valor serão entregues. Notas de 1, 10, 20 e 50
valor = int(input('Informe o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


