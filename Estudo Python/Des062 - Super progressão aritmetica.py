#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais algum termo. O programa encerrara quando ele disser que quer mostrar 0 termoprimeiro = int(input('Primeiro termo: '))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end='- ')
        termo += razao
        cont += 1
    print('pausa.....')
    mais = int(input('Quantos termos você quer mostrar mais: '))
print('The End!!!!')
