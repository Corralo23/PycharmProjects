# Faça um programa que leia apenas os números pares que está no intervalo entre 1 e 50
from time import sleep
for c in range(0, 52, 2):
    print(c, end=' -')
    sleep(0.3)
print('FIM!!!')

for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' -')
        sleep(0.3)
print('FIM!!')