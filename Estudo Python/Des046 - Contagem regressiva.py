# Faça um programa que mosre na tela uma contagem regressiva para o estouro de fogos de arifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c, end='- ')
    sleep(0.5)
print('BuuM!! BUUM!!! ')
