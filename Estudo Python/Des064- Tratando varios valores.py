#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = soma = tot = 0
n = int(input('Diga um valor: [999 - stop]: '))
while n != 999:
    soma += n
    tot += 1
    n = int(input('diga um valor: [999 - stop]: '))

print(f'Foram digitador {tot} numeros')
print(f'A soma dos numeros é {soma}')