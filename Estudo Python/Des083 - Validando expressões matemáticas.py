# Crie um programa onde o usuário digite uma expressãoqualquer que use parenteses.
# Seu aplicativo deverá analisar se a expresão passada está com os parenteses abertos e fechados na ordem correta
expressao = str(input('Digite a expressão: '))
lista = []
for arg in expressao:
    if arg == '(':
        lista.append('(')
    elif arg == ')':
        if len(arg) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
