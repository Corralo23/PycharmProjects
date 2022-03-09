#FAça um programa que tenha uma função chamada FICHA(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz d mosgrtar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>', gols=0):
       print(f'O jogador {nome} fez {gols} gols no campeonato')

#programa princial
n = str(input(' O nome do jogador: '))
g = str(input(f'quantos gols marcou: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
