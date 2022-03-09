teste = list()
teste.append('Diego')
teste.append(38)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

turma = [['JOão', 19], ['Ana', 33], ['JOaquim', 13], ['Maria', 45]]
print(turma[2][0])
for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade')

dado = list()
for c in range(0, 3):
    dado.append(str(input('NOme: ')))
    dado.append(int(input('Idade: ')))
    turma.append(dado[:])
    dado.clear()

print(dado)
totmai = totmen = 0
for p in turma:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'TEmos {totmai} maiores e {totmen} menores de idade.')