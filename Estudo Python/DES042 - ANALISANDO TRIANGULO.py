#REforça o desafio 35 dos triângulos, acresentando  recurso de mostrar que tipo de triângulo será formado
#EQUILATERO = LADOS IGUAIS; ISOSCELES = 2 LADOS IGUAIS; ESCALENO = TODOS OS LADOS DIFERENTES
r1 = float(input('Lado 1 do triangulo: '))
r2 = float(input('Lado 2 do triangulo: '))
r3 = float(input('Lado 3 do triangulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Considerando as medidas informadas, elas podem formar um triângulo', end='')
    if r1 == r2 == r3:
        print('Triangulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('triangulo ESCALENO')
    else:
        print('Triangulo ISOSCELES')
else:
    print('Não pode formar um triangulo')