def ano_bissexto(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True


def dias_mes(ano, mes):
    if ano < 1582 or mes < 1 or mes > 12:
        return None
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = dias[mes - 1]
    if mes == 2 and ano_bissexto(ano):
        res = 29
    return res

test_data = [1900, 2000, 2016, 1987]
test_mes = [2, 2, 1, 11]
test_results = [False, True, True, False]
test_result = [28, 29, 31, 30]

for i in range(len(test_data)):
    yr = test_data[i]
    mo = test_mes[i]
    print(yr, mo, '=>', end='')
    result = ano_bissexto(yr)
    results = dias_mes(yr, mo)
    if result == test_results[i]:
        print('OK')
    elif result == test_result[i]:
        print('OK')
    else:
        print('Failed')