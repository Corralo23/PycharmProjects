#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = str(input('Diga seu sexo [M/F]: ')).strip().upper()[0] #[0] fatiamento === para pegar apenas a primeira letra da resposta

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, diga o seu sexo [M/F]:')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso')



