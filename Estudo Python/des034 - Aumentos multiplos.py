#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para saários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Informe o valor de seu salário:R$ '))
if salario > 1250:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print(f'Seu salário de {salario} vai ser reajustado para R${aumento}.')
