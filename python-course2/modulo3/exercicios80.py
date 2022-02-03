'''Exercicio 84 lista com nome e peso
atualiza = []
galera = []
maior = menor = 0
while True:
  atualiza.append(str(input('Digite o nome a ser adicionado\n-> ')))
  atualiza.append(float(input('Digite o peso a ser adicionado\n-> ')))
  if len(galera) == 0:
    maior = menor = atualiza[1]
    
  else:
    if atualiza[1] > maior:
      maior = atualiza[1]
    elif atualiza[1] < menor:
      menor = atualiza[1]
  galera.append(atualiza[:])

  continuar = ' '
  while continuar not in ('SN'):
    continuar = str(input('Deseja continuar? [S/N]\n-> ')).upper()
  if continuar == 'N':
    break
  atualiza.clear()
print('Você decidiu parar...')
print(f'{len(galera)} pessoas foram adicionadas')
print('As pessoas com os nomes', end=' ')
for p in galera:
  if p[1] == maior:
    print(f'{p[0]}... ', end = '')
print(f'São as que tem o maior peso com {maior}KG')

print('As pessoas com os nomes', end=' ')
for p in galera:
  if p[1] == menor:
    print(f'{p[0]}... ', end='')
print(f'São as que tem o menor peso com {menor}KG')
'''

'''Exercicio 85 manipulação pares e impares com lista dentro de lista
lista = [[], []]
for c in range(1,8):
  numero = int(input(f'Digite o {c + 1}° valor\n-> '))
  if numero % 2 == 0:
    lista[0].append(numero)
  else:
    lista[1].append(numero)

print(f'Os valores digitados foram {lista}')

lista[0].sort()
print(f'A lista de pares ficou {lista[0]}')
lista[1].sort()
print(f'A lista de ímpares ficou {lista[1]}')
'''

'''Exercicio 86 matrizes 
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input('Digite o valor pra ser adicionado a matriz\n-> '))
print('-=' * 30)
for l in range(0,3):
  for c in range(0,3):
    print(f'[{matriz[l][c]:^6}]', end=' ')
  print()
print('-=' * 30)
'''

