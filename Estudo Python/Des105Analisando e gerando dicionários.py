#Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - quantidade de notas; - A marior nota; - A menor nota; - A média da turma; - A situação (opciona); - Adicione também as DOCSTRINGS

def notas(*n, sit=False): # o * diz que irão ser adicionados vários elementos
    """
    --> Função para analisar notas e situção de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias) ---> função *
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


#programa principal
resp = notas(9, 8.5, 5.5, 2.5, 4.5, sit=True) #sit=True ==> é situação opcional, se quiser saber a media, senão não vai aparecer
print(resp)