def MinMax(temperaturas):
    print(f'A menor temperatura do mês foi: {minima(temperaturas)} Cº.')
    print(f'A maior temperatura do mês foi: {maxima(temperaturas)} Cº.')


def minima(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min


def testa_minima():
    print('Iniciando testes')


