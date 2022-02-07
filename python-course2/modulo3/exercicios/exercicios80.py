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

'''Exercicio 86 e 87 matrizes
soma_pares = 0
soma_terceira = 0
maior_segunda = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input('Digite o valor pra ser adicionado a matriz\n-> '))
    if l == 1:
      if matriz[l][c] > maior_segunda:
        maior_segunda = matriz[l][c]
    if matriz[l][c] % 2 == 0:
      soma_pares += matriz[l][c]
    if c == 2:
      soma_terceira += matriz[l][c]
print('-=' * 30)
for l in range(0,3):
  for c in range(0,3):
    print(f'[{matriz[l][c]:^6}]', end=' ')
  print()
print('-=' * 30)
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores ta terceira coluna é {soma_terceira}')
print(f'O maior valor da segunda linha é {maior_segunda}')
'''

from random import randint
'''Exercicio 88 ajude na mega sena
from random import randint
from time import sleep
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=-= SORTEANDO {quantidade_jogos} JOGOS =-=-=-=')
sleep(1)
for c in range(0, quantidade_jogos):
    jogo = []
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
    sleep(1)
print('=-=-=-=-= < BOA SORTE! > =-=-=-=-=')
'''

'''Exercicio 89 sistema completo de boletim'''

ficha = []

while True:
  nome = str(input('Nome\n-> '))
  nota1 = float(input('nota1\n-> '))
  nota2 = float(input('nota2\n-> '))
  media = (nota1 + nota2) / 2
  ficha.append([nome,[nota1,nota2],media])
  continuar = str(input('continuar? [S/N]'))
  if continuar in 'Nn':
    break

print('*'*15, end='')
print('BOLETIM', end='')
print('*'*15,)
print('N° ///// NOME //// MÉDIA')
print('-------------------------')
for i, a in enumerate(ficha):
  print(f'{i} ///// {a[0]} ///// {a[2]}')
print('*'*35)

while True:
  aluno = int(input('Digite o número do aluno que deseja ver as notas [999 encerra]\n-> '))
  if aluno == 999:
    print('Foi um prazer')
    break
  if aluno <= len(ficha) - 1:
    print(f'As notas do aluno {aluno}° == {ficha[aluno][0]} e {ficha[aluno][1]}')
print('GG')
  
  
  



