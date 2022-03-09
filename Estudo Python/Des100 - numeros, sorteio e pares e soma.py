#FAça um programa que tenha uma lista chamada NUMEROS e duas FUNÇÕES CHAMADAS SORTEIO() E SOMAPAR(),. A primeira função vai sortear 5 númros e vai coloca-os dentro da lista,
# e a segunda função vai mostrar a soma entre todos os vaores pares sorteados pela função anterios.

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('\n<<PRONTO>>')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')



numeros = list()
sorteia(numeros)
somaPar(numeros)
