#Crie um programa que leia numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando flab

tot = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    tot += 1
print(f'Você digitou {tot} números e a soma deles é {s}')

print('Até logo!!!')

