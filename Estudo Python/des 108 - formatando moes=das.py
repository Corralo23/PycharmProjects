import moedas


valor = float(input('Digite um valor: RS '))
print(f'A metade de {moedas.moeda(valor)} é R${moedas.moeda(moedas.metade(valor))}')
print(f'O dobro de {moedas.moeda(valor)} é R${moedas.moeda(moedas.dobro(valor))}')
print(f'Aumentando 10%, temos R${moedas.moeda(moedas.aumentar(valor))}')