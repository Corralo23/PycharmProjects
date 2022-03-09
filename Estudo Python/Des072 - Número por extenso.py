# Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero a vinte.
# Seu progrma deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

for n in num:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Número inválido. Tente novamente!', end='')
print(f'Você digitou o número {num[n]}')


# Forma como o professor resolveu o problema
#while True:
 #   n = int(input('Digite um número entre 0 e 20: '))
  #  if 0 <= n <= 20:
   #     break
#    print('Número inválido. Tente novamente!', end='')
#print(f'Você digitou o número {num[n]}')