def maior_elemento(* num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'\nO maior valor informad foi {maior}.')



maior_elemento(2, 9, 4, 5, 7, 1)