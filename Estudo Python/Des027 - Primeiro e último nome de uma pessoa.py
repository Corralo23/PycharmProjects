#Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o ultimo nome separadamente
n = str(input('Informe seu nome completo: ')).strip()
nome = n.split()
print(nome)
print(f'O primeiro nome é {nome[0]}')
print(f'O ultimo nome é {nome[len(nome) - 1]}')