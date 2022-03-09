#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cid = str(input('Informe o nome da sua cidade: ')).upper()
print(cid[:5] == 'SANTO')