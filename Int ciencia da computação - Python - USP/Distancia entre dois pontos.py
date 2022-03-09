import math
n1 = int(input('Informe um número para x1:'))
n2 = int(input('Informe um númeor para y1: '))
n3 = int(input('Informe um número para x2: '))
n4 = int(input('Informe um número para y2: '))
d = math.sqrt((n1 - n3) ** 2 + (n2 - n4) ** 2)

if d >= 10:
    print('longe')
else:
    print('perto')
