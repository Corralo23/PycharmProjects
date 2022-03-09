#Crie um programa que leia NOME ANO DE NASCIMENTO e CTPS e cadastre-os (com idade) em um DICIONÁRIO. Se CTPS for diferente de 0, o dicionário recebera tbm o ANO DE CONTRATAÇÃO E O SALÁRIO.
# Calcule e acresente além da idade, com quantos anos a pessoa vai se aposentar
from time import time
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = float(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario:R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k}:  {v}')




