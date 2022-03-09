#Faça um programa que leia o ano de nascimeto de um jovem e informe de acordo com a sua idade se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se ja passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

dn = int(input('Informe o ano de seu nascimento: '))
ano = date.today().year
idade = ano - dn
tempo = idade - 18
print(idade)
if idade == 18:
    print(f'Voce esta com {idade}, prazo limite para o alistamento')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você está com {idade}, fique atento ao prazo para alistamento.')
elif idade > 18:
    saldo = idade - 1
    print(f'Você está com {idade}, já passou {tempo} anos do seu alistamento')
