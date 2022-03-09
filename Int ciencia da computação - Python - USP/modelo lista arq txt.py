nome = ''
result = ''
while nome != 'sair':
    nome = input('Digite o nome: ')
    if nome == 'sair':
        break
    tel = input('Digite o tel: ')
    result += '\n'+ nome + '\t' + tel
arq = open('../Estudo Python/contatos.txt', 'w')
arq.write('Nome\t Telefone' + result)
arq.close()
arq = open('../Estudo Python/contatos.txt', 'r')
lista = arq.readlines()

for i in lista:
    print(i)
arq.close()