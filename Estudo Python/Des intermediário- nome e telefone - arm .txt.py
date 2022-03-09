# Faça um programa que leia o nome e telefone de um usuário e armazene em um arquivo de texto (.txt)
'''
r -> usando somente para ler algo
w -> usado somente para escrever algo
r+ -> usado para ler e escrever algo
a -> usado para acrescentar algo
'''
nome = ''
result = ''
while nome != 'sair':
    nome = input('Digite o nome: ')
    if nome == 'sair':
        break
    tel = input('Digite o tel: ')
    result += '\n'+ nome + '\t' + tel
arq = open('contatos.txt', 'w')
arq.write('Nome\t Telefone' + result)
arq.close()
arq = open('contatos.txt', 'r')
lista = arq.readlines()

for i in lista:
    print(i)
arq.close()