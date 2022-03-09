#A confederação nacional de natação precisa e um programa que leia o ano de nascimento de um atleta e mosre sua categoria de acordo com sua idade:
#até 9 - mirim; 9a 14 = infantil: 14 a 19= junior; 19 a 25 = senior; acima de 25 = master
from datetime import date

dn = int(input('Informe o ano de seu nascimento: '))
ano = date.today().year
idade = ano - dn
print(f'Você tem {idade} anos. Sua categoria é: ')
print('=' * 30)
if idade < 9:
    print('categoria MIRIM')
elif 14 > idade >= 9:
    print('Categoria INFANTIL')
elif 19 > idade >= 14:
    print('categoria JUNIOR')
elif 25 > idade >= 19:
    print('categoria SENIOR')
else:
    print('categoria MASTER')

print('BOA SORTE ATLETA')