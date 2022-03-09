#FAça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo numa lista
from random import randint
mega = list()
jogo_mega = list()
print('=' * 40)
print('=' * 5, 'JOGOS DA MEGA', '=' * 5)
print('=' * 40)
jogos = int(input('Quantos jogos vai fazer: '))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    jogo_mega.append(mega[:])
    mega.clear()
    tot += 1
print(f'Sorteando {jogos} jogos')
for n, s in enumerate(jogo_mega):
    print(F'Jogo{n + 1}: {s}')
