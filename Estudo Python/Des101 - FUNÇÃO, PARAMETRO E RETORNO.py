#Crie um programa que tenha uma FUNÇÃO  chamada VOTO() que vai receber como PARÂMETRO O ANO DE NASCIMENTO de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleiçoes.

def voto(ano):
   from datetime import date
   atual = date.today().year
   idade = atual - ano

   if idade < 16:
        return f' Com {idade} anos: NÃO VOTA.'
   elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto OPCIONAL.'
   else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

DN = int(input('Em que ano você nasceu: '))
print(voto(DN))
