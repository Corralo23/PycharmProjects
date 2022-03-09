# Nessa aula vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis
# compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura acessíveis por chaves individuais


lanche = 'hamburguer', 'suco', 'pizza', 'pudim', 'batata frita'

for comida in lanche:
    print((f'Eu vou comer {comida}'))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print('Comi pra caramba')


# Mais exemplos de tuplas

a = (2,5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(4))

pessoa = ('Diego', 38, 'M', 75.5)
del(pessoa)  # Só pode deltar a tupla inteira, pois ela não aceita que se delete apenas um item.
print(pessoa)