#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Informe seu peso {p}: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')