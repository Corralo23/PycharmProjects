# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista já
# na posição correta de inserção(sem usar o sort()). NO final, mostre a lista ordenada na tela
lista = []
for n in range(0, 5):
    num = int(input('Digite um número: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('Numero adicionado no final da lista')
    else:
        pos = 0 #posição do número na lista
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, num)
                print(f'Numero adicionado na posição {pos}')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')