#Crie um programa que tenha a FUNÇÃO LEIAiNT(), que vai funcionar de forma semelhante a funçao input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico EX.: n = leiaInt('Digite um n')
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO!! Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor


#programa principal

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')