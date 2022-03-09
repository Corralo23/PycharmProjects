# Aula sobre listas e como utiliza-las em Python. As listas são variáveis compostas
# que permitem armazenar vários valores em uma mesma estrutura, acessiveis por chaves individuais.
# Listas são mutáveis, podem ser alteradas
# Del lista[3]; lista.pop(3) ou lista.remove('nome do item') ==> para remover itens da lista
# EX.:
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
num.remove(5)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(8)
valores.append(7)
for v in valores:
    print(f'{v}...', end='')

valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A {a}')
print(f'Lista b {b}')