from time import sleep
for c in range(0, 5):
    print(c)
print('fim')

for d in range(9, 0, -1):
    print(d)
    sleep(0.3)

n = int(input('Digite um número? '))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('início? '))
f = int(input('fim'))
p = int(input('passo')) #passo é ordem de número que será contado
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0,3):
    n = int(input('Digite um valor: '))
print('fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores {s}')