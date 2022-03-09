import pandas as pd
import openpyxl
from twilio.rest import Client

#Passo a passo da solução

#Your Account SID from twilio.com/console
account_sid = "ACfbe0b6709f5a3ff9082f03a3c29192a1"
#Your Auth Token from twilio.com/console
auth_token = "b24300e020356fad375caa15ca0ef8e5"
client = Client(account_sid, auth_token)

#Abrir os 6 arquivos de excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mês {mes} alguém bateua meta. Vendedor: {vendedor}, Vendas: {vendas}.')
        message = client.messages.create(
            to="+5554999432585",
            from_="+18065152715",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.' )
        print(message.sid)


#Para cada arquivo:
# Verificar se algum valor na coluna vendas daquele arquivo é maior que R$55.000



# Se for maior que 55mil -> Enviar SMS com o nome, o mês e as vendas do vendedor




