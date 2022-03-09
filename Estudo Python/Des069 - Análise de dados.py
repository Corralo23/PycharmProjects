#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
#a) quantas pessoas com mais de 18 anos; b) quantos homens foram cadastrados; c) quantas mulheres tem menos de 20 anos
maior = menor = homem = 1
resp = ' '
while True:
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo[M/F]: ')).strip().upper()[0]
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp in 'Ss':
        if idade >= 18:
            maior += 1

        elif sexo == 'M':
            homem += 1

        elif sexo == 'F' and idade < 20:
            menor += 1
    else:
        break

print(f'Foram cadastradas {maior} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {menor} mulheres menores de 18 anos')
print('Até logo!!!!')