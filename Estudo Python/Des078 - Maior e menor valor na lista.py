# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
# qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = []
for n in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
print(f'O mair valor digitado foi  {max(lista)}')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'O maior valor está na posição {i}; ', end='')
print(f'\nO menor valor digitado foi {min(lista)}')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'O menor valor está na posição {i}', end='')


# resolução professor
#mai = 0
#men = 0
#if c == 0:
#    mai = men = lista[n]
#else:
#    if lista[n] > mai:
#        mai = lista[n]
#    if lista [n] < men:
#        men = lista[n]
