# Faça um programa que tenha uma função chamada MAIOR(), que receva vários parametros com valores interios. Seu prorama tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('=' * 30)
    print('\nAnalisando os valores passados... ')#\n ==> para nova linha
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#programa pricipal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 5, 9)
maior(6)
maior(0)