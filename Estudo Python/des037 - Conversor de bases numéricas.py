#Escrever um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 - BINÁRIO; 2 - OCTAL; 3 - HEXADECIMAL
print('=' * 30)
num = int(input('Informe um número inteiro para escolher a base de conversão: '))
print('=' * 30)
print('''Escolha uma das opções: 
1 - BINÁRIO: 
2 - OCTAL: 
3 - HEXADECIMAL: 
4 - SAIR''')
print('=' * 30)
opção = int(input('Escolha sua opção: '))
print('=' * 30)
if opção == 1:
    print(f'Você escolheu a opção 1, a conversção fica {bin(num)}')
elif opção == 2:
    print(f'Você escolheu a opção 2, a conversção fica {oct(num)}')
elif opção == 3:
    print(f'Você escolheu a opção 3, a conversção fica {hex(num)}')
elif opção == 4:
    print(f'Você escolheu a opção 4 SAIR')
print('VOLTE SEMPRE')