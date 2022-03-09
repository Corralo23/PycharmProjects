#a = 4
#b = 5
#s = a + b

#print(s)
#a = 8
#b = 9
#s = a + b
#print(s)

#a = 2
#b = 1
#s = a + b
#print(s)
print('=' * 40)
#programa principal
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)

def contador(*num):
    print(sum(num))


contador(2, 1, 7)
contador(8, 6)
contador(4, 5, 8, 3)
print('=' * 40)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print('=' * 40)
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)