#fAÇA UM PROGRAMA QUE LEIA NOME E MEDIA DE UM ALNO, GUARDANDO TBM A SITUAÇÃO EM UM DICIOÁRIO. NO FINAL MOSTRE A ESTRUTUARA NA TELA
aluno = dict()
situação = list()
while True:
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input('nota: '))
    situação.append(aluno.copy())
    if aluno['media'] >= 7:
        aluno['situação'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['situação'] = 'Reprovado'
    print('=' * 30)
    for k, v in aluno.items(): #K = keys -chave ==> V =values - valor ===> items - conjunto K  e V
        print(f' - {k} é igual a {v}')
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break

