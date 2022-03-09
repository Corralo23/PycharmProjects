# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('arroz', 4.60, 'feijão', 5.85, 'massa', 3.90, 'pão', 5.50,
            'cerveja', 40.80, 'chocolate', 5.30, 'queijo', 14.30, 'presunto', 9.90)
print('=' * 40)
print('Preços dos Produtos')
print('=' * 40)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<35}', end='')
    else:
        print(f'R${produtos[p]:>}')