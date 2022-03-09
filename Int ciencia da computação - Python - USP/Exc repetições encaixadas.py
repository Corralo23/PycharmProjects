#Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos, indicando também a multiplicidade de cada fator

def main():
    n = int(input('Digite um numero > 1: '))
    fator = 2     # primeiro fator
    while n != 1:   # aqui vai contar a multiplicidade de fator em n
        mult = 0
        while n % fator == 0:
            n = n / fator
            mult = mult + 1

        #aqui vai imprimir a multiplicidade do fator
        if mult != 0:
            print(f'Fator {fator} multiplicidade {mult}')

        fator = fator + 1


main()     # chama a função principal
