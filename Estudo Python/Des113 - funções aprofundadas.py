# Reeescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#aproveite e crie também uma função leiaFloat() com a mesma funcionalidade
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError): #se escrever o número ou colocar algum outro caracter
            print('\033[31mERRO!! Por favor, digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt): # se não digitar nenhum número ou espaço
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')


