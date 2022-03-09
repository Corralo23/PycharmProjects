# Crie um programa que vai ler vários números e colocar em uma lista: depois disso mostre: a) Quantos numeros foram digitados
# b)A lista de valores ordenada de forma decrescente; c ) Se o valor 5 foidigitado e está ou não na lista
num = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar[S/N]: '))
    if resp in 'Nn':
        break

print(num)
print(f'Foram digitados {len(num)} numeros')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente {num}')
if 5 in num:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')