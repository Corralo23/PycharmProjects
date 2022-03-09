#Crie um programa que leia 2 valores e mostre um menu na tela: [1] SOMAR; [2] MULTIPLICAR; [3] MAIOR;
# [4] NOVOS NUMEROS; [5] SAIR DO PROGRAMA. Seu programa deverá realizar a operação solicitada em cada caso.
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''QUAL OPERAÇÃO VOCÊ DESEJA REALIZAR:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual sua opçao: '))

    if opcao == 1:
        n = num1 + num2
        print(f'A soma dos valores informado é {n}.')
    elif opcao == 2:
        n = num1 * num2
        print(f'A multiplicação dos valores informados é {n}')
    elif opcao == 3:
        if num1 > num2:
            n = num1
        else:
            n = num2
        print(f'O maior valor é {n}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Informe o primeiro valor: '))
        num2 = int(input('Informe o segundo valor: '))
    elif opcao == 5:
        print('Programa encerrado')
    else:
        print('Opção inválida. Tente novamente.')
    print('=' * 30)
print('Fim do programa. Volte sempre!')



