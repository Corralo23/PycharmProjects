#Crie um programa que sorteia a ordem de apresenção de trabalhos dos alunos.
# FAça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

n1 = str(input('Nome do aluno: '))
n2 = str(input('Nome do aluno: '))
n3 = str(input('Nome do aluno: '))
n4 = str(input('Nome do aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação será {lista}')