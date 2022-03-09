#Crie um pequeno sisema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo e texto simples.
#o sistema só vai ter 2 opç~es: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from des115A.LIB.interface import *
from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('saindo do sistema...Até logo!!')
        break
    else:
        print('\033[32mERRO! Digite uma opção válida!\033[m')
    sleep(2)