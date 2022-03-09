#Crie um programa que leia o ano de nascieto de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

ano = date.today().year
totmaior = 0
totmenor = 0
for pess in range(0, 7):
    dn = int(input(f'Informe o ano de nascimento{pess}: '))
    idade = ano - dn
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')

