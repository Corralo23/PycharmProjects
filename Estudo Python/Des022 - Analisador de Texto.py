#Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiusculas; - todas as letras minúsculas;
# - quantras letras ao todo sem contar os espaços; #- quantas letras tem o primeiro nome
nome = str(input('Informe seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))

#separa = nome.split() ==> print(len(separa[0][0])