#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o prelo a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado
km = float(input('Informe a quantia de KM rodados com o carro: '))
d = int(input('Informe o numero de dias em que o carro ficou alugado: '))
vk = km * 0.15
vd = d * 60
print(f'O condutor rodou {km}km com o carro por {d} dias. Assim, o valor do aluguel é de {vk + vd}.')