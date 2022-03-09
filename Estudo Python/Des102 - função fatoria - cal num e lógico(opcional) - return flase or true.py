#Crie um programa que tenha uma FUNÇÃO FATORIA() que receba dois parametros: o primeiro que indique o número a calcular e o outro chamado SHOW,
# que será um valor LÓGICO(OPCIONAL) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatoria(n, show=False):
    """
    >> Calcula o FAtorial de um número:
    :param n: O número a ser calculado
    :param show: {opcional} Mostrar ou não a conta ==> show=True => mostra; show=False ou não colocar nada => NÃO MOSTRA
    :return: O VALOR DO fATORIA DE UM NÚMERO n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='') #end='' ==> é o lógico opcional
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#programa principal
print(fatoria(5, show=True))