def aumentar(v=0, taxa=0, formato=False):
    """
    --> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param v: 0 preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado com ou sem formato
    """
    res = v + (v * taxa/100)
    return res if format is False else moeda(res)


def diminuir(v=0, taxa=0, formato=False):
    res = v - (v * taxa/100)
    return res if format is False else moeda(res)


def dobro(v=0, formato=False):
    res = v * 2
    return res if not format else moeda(res)


def metade(v=0, formato=False):
    res = v / 2
    return res if not format else moeda(res)


def moeda(v=0, moeda=0):
    return f'{moeda}{v:8.2f}'.replace('.', ',')


def resumo(v=0, taxaa=10, taxar=5):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: R$\t{moeda(v)}')
    print(f'Dobro do preço: R$\t{dobro(v, True)}')
    print(f'Metade do preço: R$\t{metade(v, True)}')
    print(f'{taxaa}% de aumento: R$\t{aumentar(v, taxaa, True)}')
    print(f'{taxar}% de redução: R$\t{diminuir(v, taxar, True)}')
    print('=' * 30)
