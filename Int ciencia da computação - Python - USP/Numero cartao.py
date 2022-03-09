meuCartao = int(input('Digite o numero do seu cartao: '))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input('Digite o numero do proximo cartao de credito: '))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print('Obaaa!!! Meu cartão está la')
else:
    print('OPSS!!! Meu cartão não está la')
