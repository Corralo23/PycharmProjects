#Crie um MÓDULO chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(percentual), DIMINUIR(), DOBRO() E METADE().
#Faça também um prorama que importe esse módulo e use algumas dessas funções
import moeda


valor = float(input('Digite um valor: RS '))
print(f'A metade de {valor} é R${moeda.metade(valor)}')
print(f'O dobro de {valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor)}')