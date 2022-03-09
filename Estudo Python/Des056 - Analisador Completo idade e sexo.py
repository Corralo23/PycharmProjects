#Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas.NO final do progrma mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulhres tem menos de 20 anos

mediaidade = 0
maioridade = 0
nomevelho = 0
totmulher20 = 0
somaidade = 0
for p in range(1, 5):
    nome = str(input('NOme: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe o sexo [F\M]: ')).upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridade} anos e seu nome é {nomevelho}')
print(f'No grupo de pessoas acima relaciona temos {totmulher20} mulher com menos de 20 anos')




