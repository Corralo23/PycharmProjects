#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
# EX.: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split() # split para gerar uma lista
junto = ''.join(palavra) # juntou a lista para eliminar os espaçs em branco
inverso = ''
for letra in range(len(junto) -1, -1, -1): # aqui foi feito o inverso (foi da ultima letra até a primeira voltando uma letra === -1, -1, -1)
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É POLÍNDROMO!!!')
else:
    print('Não é polindromo')