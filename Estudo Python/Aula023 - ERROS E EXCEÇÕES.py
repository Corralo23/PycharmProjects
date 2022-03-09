try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b #caso a divisão de 0 ou for digitado alguma letra ao invez de numero ou ex.: '2'

#except:
#    print('Infelizmene tivemos um problema :( ')
except Exception as erro: # posso ter vários except dentro do código
    print(f'Problema encontrado foi {erro.__class__}')
#except (ValuerErro, TypeError):
#   print('Tivemos um problema com os tipos de dados que você digitou

#except ZeroDivisionError:
#   print('Não é possivel dividir um número por 0

#except KeyboardInterrupt:
#   print('O usuario preferiu não informar os dados


else: #caso dê certo
    print(f'O resultado é {r}')

finally: #certo/falha
    print('Volte sempre! muito obrigado!')
