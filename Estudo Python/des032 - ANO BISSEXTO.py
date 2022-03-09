
from datetime import date
from calendar import isleap

ano = int(input('Informe o ano que você quer saber se é bissexto: '))
if isleap(ano):
    print('É BISSEXTO')
else:
    print('NÃO É BISSEXTO')


ano = int(input('Que ano você quer analisar? Digite 0 se quiser verificar o ano atual'))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!!')
else:
    print(f'O ano {ano} não é BISSEXTO')