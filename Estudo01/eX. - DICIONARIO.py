dic = {'Salgado': 4.50,
       'Lanche': 6.50,
       'Suco': 3.00,
       'Refrigerante': 3.50,
       'Doce': 1.00}
print(dic, end=' ')
print()
print('-=' * 30)
print()

classe = {'Ana': 4.5,
          'Beatriz': 6.5,
          'Geraldo': 1.0,
          'JOsé': 10.0,
          'Maria': 9.5}
notas = classe.values()
media = sum(notas) / 5
print(f'{classe}')
print(f'A media da classe é {media}. ', end='')