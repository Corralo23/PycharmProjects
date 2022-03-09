from time import sleep
def contador(i, f, p): #i - inicio da contagem; f = fim da contagem; p = passo da contagem
    c = i
    while c <= f:
        print(f'{c}', end='-')
        c += p
        sleep(0.3)
    print('fim')

contador(2, 40, 2)

def somar(a=0, b=0, c=0): # o 0 serve para deixar o valor como opcional, caso não seja informado algum valor, ele será considerado 0
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: não tem return
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar()

help(print)