def mostra_preco(n):
  return f'{n:.2f}'.replace(',','.')

def aumentar(n,p=0):
  p = p / 100
  n = n + n * p
  return n

def diminuir(n,p=0):
  p = p / 100
  n = n - n * p
  return n

def dobro(n):
  return n * 2

def metade(n):
  return n / 2

def resumo(preco, taxar = 0, taxaa = 0):
  print('-'*30)
  print('RESUMO DO VALOR'.center(30))  
  print('-'*30)
  print(f'Dobro do preco: \t{dobro(preco)}')
  print(f'Metade do preco: \t{metade(preco)}')
  print(f'Com {taxar}% de desconto: \t{diminuir(preco, taxar)}')    
  print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa)}')
  