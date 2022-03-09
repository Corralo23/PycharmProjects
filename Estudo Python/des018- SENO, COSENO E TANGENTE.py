#FAça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
from math import *
a = float(input('Informe um angulo qualquer: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print(f'Você informou o anulo de {a}. O seno desse angulo é {seno :.2f}, seu cosseno é {cos :.2f} e a tangente é {tan :.2f}')