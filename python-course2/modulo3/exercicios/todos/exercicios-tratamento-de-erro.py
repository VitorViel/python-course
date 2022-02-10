'''113 tratamento com int e float com excecoes
def leiaint(msg):
  while True:
    try:
      nova_msg = int(input(msg))
    except (ValueError,TypeError):
      print('Valor inserido não é válido!')
    except (KeyboardInterrupt):
      print('O usuario não completou a inserção de dados!')
    else:
      print(f'O valor digitado foi {nova_msg}, e ele é um tipo INT!')
      break
msg = leiaint('Digite um número int!: ')
'''

'''114 verifica se o site é acessível ou n'''
import urllib
import urllib.request

try:
  urldosite = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
  print('\033[031mDeu erro\033m[')
else:
  print(f'\033[32mO site está pronto para uso\033[m')