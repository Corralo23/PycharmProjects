#fAÇA UM PROGRAMA QUE JOGEU PAR OU IMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER,
# MOSTRANDO O TATAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint
v = 0
while True:
    jogador = int(input('Diga um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I]:  ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}.', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')

    if tipo == 'P':
       if total % 2 == 0:
            print('Você venceu!!!!')
            v += 1
       else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!!!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('vamos jogar novamennte....')
print('GAME OVER!!!!')
