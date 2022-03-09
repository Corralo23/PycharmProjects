#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python.
# veja como utilizar o código \033[m com todas as suas principais possibilidades
#\033[style;text; backm
#\033[0;33;44m ==> 0 = estilo da letra; 33 = cor do texto; 44 = fundo do texto
#0 = none(normal); 1 = bold(negrito); 4 = underline(sublinhado; 7 negative
#30-branco; 31-vermelho; 32-verde; 33-amarelo; 34-azul; 35roxo; 36-auzlesverdeado; 37-cinza
#back- 40-branco; 41-vermelho; 42-verde; 43-amarelo; 44-azul; 45roxo; 46-auzlesverdeado; 47-cinza

print('\033[7;30;47molá mundo!\033[m')
print('\033[4;31mola mundo\033[m')
print('\033[4;33mola mundo\033[m')
print('\033[4;37mola mundo\033[m')
s = 'prova de python'
print(len(s))

x = 'curso de python no cursoemvideo'
print(x[:5])
y = 3 * 5 + 4 ** 2
print(y)