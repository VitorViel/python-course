try:
  a = (int(input('Digite um número A: ')))
  b = (int(input('Digite um número A: ')))
  c  = a / b
except Exception (ValueError, TypeError):
  print('Algo deu errado na inserção e cálculo de valores')
except Exception (ZeroDivisionError):
  print('Não é possivel dividir um número por zero')
except Exception (KeyboardInterrupt):
  print('O usuário não digitou nada em algum dos campos')
except Exception as erro:
  print(f'O erro encontrado foi {erro.__cause__}')
else:
  print(f'O resultado é {c}')
finally:
  print('Muito obrigado, até a próxima!')  