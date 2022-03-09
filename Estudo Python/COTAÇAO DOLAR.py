# 1) DECLARANDO AS LIBS DO PYTHON
import requests
import json

# 2) aCESSANDO A API
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

# 3) DESSERIALIZAÇÃO DO RETORNO DA API
cotacao = requisicao.json()

# 4) CONHECENDO A ESTRUTURA DE DADOS:
print(cotacao)

# 5) MANIPULANDO AS INFORMAÇÕES:

print('#### COTAÇÃO DO DOLAR ####')
print('Moeda: '+ cotacao['USD']['name'])
print('Data: '+ cotacao['USD']['create_date'])
print('Valor atual: R$' + cotacao['USD']['bid'])
