#fAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA(), QUE RECEBE AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A AREA DO TERRENO

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')


print(' << CONTROLE DE TERRENO >> ')
print('-' * 30)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(l, c)