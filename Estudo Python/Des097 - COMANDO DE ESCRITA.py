#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEA UM TEXTO QUALQUER COM PARÃMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTAVEL
def escreva(msg):
    tam = len(msg)
    print('=' * tam)
    print(msg) #print(f'  {msg}') ===> para deixar centralizado
    print('=' * tam)


escreva('  CURSO EM PYTHON  ')
escreva(' PALMEIRAS NÃO TEM MUNDIAL ')
escreva('   JAGUARAS   ')
