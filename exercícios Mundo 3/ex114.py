"""
    Crie um código em PYTHON que teste se o site PUDIM está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('Site indisponível')
else:
    print('Site funcionando :)')
