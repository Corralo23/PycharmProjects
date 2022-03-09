#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
# O primeiro é maior; O segundo é maior; Os dois são iguais
n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Os valores informados são iguais')