''#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
v1 = int(input('digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite outro valor'))
if v1 > v2 and v1 > v3:
    print('O primerio valor é maior')
if v2 > v3 and v2 > v3:
    print('O segundo valor é maior')
else:
    print('O terceiro valor é maior')

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'O menor valor digitado foi {menor}')
print(f'o maior valor digitado foi {maior}')
