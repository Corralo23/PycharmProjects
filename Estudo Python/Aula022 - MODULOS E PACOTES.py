#codigo das funções foi separado na pasta UTEIS, para o código não ficar muito extenso

#from uteis import fatorial, dobro, triplo --> essa é uma forma de importar as funções, porem pode gerar confusão no progrmaa
#import uteis # esse é o melhor jeito para deixar o programa sem problemas
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}!')
print(f'O triplo de {num} é {numeros.triplo(num)}')
