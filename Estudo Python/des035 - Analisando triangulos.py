#Desenvolva um programa que leia o comprimento de três retas e dia ao usuário se elas podem ou não formar um triângulo
r1 = float(input('Informe a reta do triangulo: '))
r2 = float(input('informe a 2º reta do triangulo: '))
r3 = float(input('Informe a 3ª reta do trinagulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Considerando as medidas informadas, elas podem formar um triângulo')
else:
    print(f'Considerando as medidas informas, elas não podem formar um triângulo')