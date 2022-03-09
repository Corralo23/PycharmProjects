#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
computador = randint(0, 10)
print('====  JOGO DE ADIVINHAÇÃO  ====')
print('=' * 20)
print('Vou pensar em um número....')
sleep(0.3)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite??? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... tente novamente.')
print(f'Parabéns!! Voce acertou com {palpite} palpites')



