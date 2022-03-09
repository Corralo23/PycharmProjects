from des115A.LIB.interface import *
from des115A.LIB import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt serve para fazer a leitura do arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt+ cria o arquivo caso ele não exista, o + é fundamental para criar o arquivo
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())

