def MinMax(temperaturas):
    print(f'A menor temperatura do mês foi: {minima(temperaturas)} Cº.')
    print(f'A maior temperatura do mês foi: {maxima(temperaturas)} Cº.')


def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min


def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max


def test_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != 0:
        print(f'Valor errado para array {temp}')
        print(f'O valor esperado {valor_esperado}, valor calculado: {valor_calculado}')


def testa_minima():
    print('Iniciando testes')
    test_pontual([0], 0)
    test_pontual([0, 0, 0, 0, 0, 0], 0)
    test_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    test_pontual([30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 24, 22], 0)
    test_pontual([-15, -12, 0, 20, 30], 0)
print('Teste finalizado')

testa_minima()