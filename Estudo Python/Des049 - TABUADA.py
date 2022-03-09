# REFAÇA O DESAFIO 9, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAÇO FOR.
from time import sleep
n = int(input('Diga o número que você quer saber a tabuada? '))
for c in range(0, 11):
    print(f'{n} x {c} = {n * c}')
    sleep(0.5)

print('Até logo!!')