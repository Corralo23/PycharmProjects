#Faça um programa que mostre a tabuada de váriosnúmeros, um de cada vez, para cada valor digitado pelo usuário.
# O programa interrompido quando o número solicitado for negativo

#n = int(input('Informe um numero para a tabuada: '))
while True:
    n = int(input('Informe um numero para a tabuada: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')

print('Até logo!!!')