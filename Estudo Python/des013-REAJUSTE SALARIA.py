#FAça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aument.
s = float(input('Informe o valor de seu salário R$'))
d = s + (s * 0.15)
print(f'Com o reajuste de 15%, o salário de R${s} vai passar a ser de R${d :.2f}')