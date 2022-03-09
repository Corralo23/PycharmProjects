palavras = ('ferrari', 'lamborguini', 'porsche', 'audi', 'mercedez-benz', 'lotus')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as seguintes vogais:  ', end='')
    for l in p:
        if l in 'a e i o u':
            print(l, end='-')
