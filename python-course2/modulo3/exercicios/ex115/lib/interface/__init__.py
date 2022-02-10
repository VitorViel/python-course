def leiaint(msg):
  while True:
    try:
      nova_msg = int(input(msg))
    except (ValueError,TypeError):
      print('Valor inserido não é válido!')
      continue
    except (KeyboardInterrupt):
      print('O usuario não completou a inserção de dados!')
      continue
    else:
      return nova_msg

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(f'\033[33m{txt.center(42)}\033[m')
    print(linha())

def menu(lista):
    for c in range(0,len(lista)):
        print(f'\033[36m{c + 1}\033[m == \033[34m{lista[c]}\033[m')
    print(linha())
    opc = leiaint('Digite sua opção: ')
    return opc


