def teste():
    x = 8
    print(f'N função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')

#def teste(b):
    #b += 4
    #c = 2
    #print(f'A dentro vale {a}')
    #print(f'B dentro vale {b}')
    #print(f'C dentro vale {c}')

#a = 5
#teste(a)
#print(f'A fora vale {a}')

def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fra vale {n1}')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

print(somar(3, 2, 5))
r1 = somar(7, 3, 6)
r2 = somar(3, 9)
r3 = somar(5)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')