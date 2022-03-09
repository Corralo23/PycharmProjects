#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km\h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite.
v = int(input('Informe a velocidade que você passou no radar: '))
if v >= 80:
    print('Você está acima da velocidade limite. VOCÊ SERÁ MULTADO')
    multa = (v - 80) * 7
    print(f'VOCÊ FOI MULTADO EM R${multa}')
else:
    print('Você está dentro da velocidade permitida. PARABÉNS!!!')