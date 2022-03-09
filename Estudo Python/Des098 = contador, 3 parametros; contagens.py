#Faça um programa que tenha uma função chamada CONTADOR(), que receba três parametros: INICIO, FIM E PASSO. Seu progama tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1; b) De 10 até 0, de 2 e 2; c) uma contagem personalizada
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 30)
    print(f'Contagem de {i} até {p} em {p}')
    sleep(0.6)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)#flush=True é para fazer a contagem de 1 em 1 sem bug
            sleep(0.3)
            cont += p
        print('<<FIM>>')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.3)
        print('<<FIM>>')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 35)
print('Agora é a sua vez: ')
ini = int(input('Ínicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
