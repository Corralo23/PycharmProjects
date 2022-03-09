#Crie um código em Python que teste se o site PUDIM está acessível pleo computador usado
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessíve no momento')
else:
    print('Tudo Ok')
    print(site.read())