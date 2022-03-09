#S = 0
#for x in range(3, 334, 3):
   # S = S + x
#print(f'Soma = {S} ')

#S = 0
#for contador in range(1, 11):
#    nota = float(input('Digite a nota: '))
#    S = S + nota
#print(f'Media: {S / 10}')

while True:
    num = int(input('Digite um número para a tabuada: '))
    for sequencia in range(1, 11):
        print(f'{num} x {sequencia} = {num * sequencia}')
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('<<<   MUITO OBRIGADO   >>>')
