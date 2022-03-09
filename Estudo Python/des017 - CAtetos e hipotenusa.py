#FAça um programa que leia a hipotenusa
from math import hypot
ca = float(input('Informe o valor do cateto a: '))
cb = float(input('Informe o valor do cateto b: '))
print(f'Considerando os valor dos catetos {ca} e {cb} temos a hipotenusa {hypot(ca, cb)}')