'''113 tratamento com int e float com excecoes'''
def leiaint(msg):
  while True:
    try:
      n = int(input(msg))
    except (TypeError, ValueError):
      print('\033[31mPor favor, digite o tipo de valor inteiro!\033[m')
      continue
    except KeyboardInterrupt:
      print('O usuário não completou a inserção de dados')
      break
    else:
      print(f'Ok! Você digitou um valor de número do tipo int {n}!')
      break
    
msg = leiaint('Digite um número int!: ')

