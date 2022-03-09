largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

while altura > 0:
    aux = 0
    while aux < largura:
        print('#', end='')
        aux += 1
    altura -= 1
    print()



