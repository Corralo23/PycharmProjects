#Modifique as funções que foram criadas no desafio 107 para que elas aceiem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108


import moedas


valor = float(input('Digite um valor: RS '))
print(f'A metade de {moedas.moeda(valor)} é R${moedas.metade(valor, True)}')
print(f'O dobro de {moedas.moeda(valor)} é R${moedas.dobro(valor, True)}')
print(f'Aumentando 10%, temos R${moedas.aumentar(valor, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(valor, 13, True)}')