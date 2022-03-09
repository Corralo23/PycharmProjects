decrescente = True
anterior = int(input("diga o primeiro número da sequencia: "))
valor = 1
while valor != 0 and decrescente:
    valor = int(input('Diga o proximo número da sequencia: '))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print('A sequencia está em ordem decrescente!')
else:
    print('A sequencia não está em ordem decrescente!')