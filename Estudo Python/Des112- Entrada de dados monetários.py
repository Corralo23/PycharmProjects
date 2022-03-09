#Dentro do pacote UTILIDADESCEV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chaada LEIADINHEIRO(),
# que seja capaz de funcionar como a função input(), mas com uma calidação de dados para aceitar apenas valores qeu sejam monetários
import moedaa
from des112.utilidadescev import moeda
from des112.utilidadescev import dado
from des112.utilidadescev import resumo

valor = dado.leiaDinheiro('Digite um valor: RS ')
moedaa.resumo(valor, 10, 25)


