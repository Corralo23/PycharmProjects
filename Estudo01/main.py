while True:
    nome = str(input('Qual o seu nome?'))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
f = str(input('digite uma frase: ')).upper().replace(' ', '')
print(f'{f}')