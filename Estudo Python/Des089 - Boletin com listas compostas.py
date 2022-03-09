# Crie um programa que leia nome e duas notas de ´varios alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar a nota individual de cada aluno
lista = list()

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
print(lista)
print('=' * 35)
print(f'{"No.":<5}{"Nome":<10}{"Média":>10}')
print('=' * 35)
for i, n in enumerate(lista):
    print(f'{i:<5}{n[0]:<10}{n[2]:>10.2f}')
while True:
    print('apertando 999 interrompe o programa')
    aluno = int(input('Mostrar nota de qual aluno?'))
    if aluno == 999:
        print('Volte sempre. Programa encerrado')
        break
    if aluno <= len(lista) - 1:
        print(f'As notas de {lista[aluno][0]} são {lista[aluno][1]}')