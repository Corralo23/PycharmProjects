#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de DETALHES DE APROVEITAMENTO de cada jogador
time = list()
jogador = dict()
partida_gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou:'))
    for c in range(0, tot):
        partida_gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partida_gols[:]
    jogador['total'] = sum(partida_gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar[S/N]? ')).upper()
        if resp in 'SN':
            break
        print('ERRO!!!! Responda Apenas S ou N. ')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'i:<15', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
        print(f'{k:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!!! Não existe jogador com esse código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}: ')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'  No jogo {i + 1} fez {g} gols.')
        print('-' * 40)
print(' <<< VOLTE SEMPRE >>> ')


