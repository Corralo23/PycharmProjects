#Exercicio 1 da lista de exercícios sobre vetores.
# Dados n > 0 e uma sequencia com n numeros reais, imprimi-los na ordem inversa a da leitura
def main():
    n = int(input('Digite o valor: '))
    cont = 0
    seq = []
    while cont < n:
        num = int(input('Digite um numero: '))
        seq.append(num)
        cont += 1

    print(f'Sequencia original: {seq}')
