# Crie uma tupla preenchida comos 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: a)Os 5 primeiros; b) Os últimos 4 colocados; c) Times em ordem alfabética; d) Em que posição está a Chapecoense
times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'America-MG', 'Atletico_GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

#5 primeiros
print(f'Os 5 primeiros times do campeonato foram: {times[0:5]}', end='')

#4 ultimos
print(f'\nOs 4 times rebaixados desse ano foram: {times[16:21]}', end='')

# Times em ordem alfabética
print(f'\nA lista dos times em ordem alfabética: {sorted(times)}', end='')

# Posição da Chapecoense

print(f'\nA Chapecoense ficou na posição : {times.index("Chapecoense") +1}', end='')
