#Nessa aula vamos aprender como criar estruturas condicionais aninhadas usando os comandos IF..ELIF....ELSE em programas Python
nome = str(input('Qual o seu nome: '))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print('Tenha um bom dia')