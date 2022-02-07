'''Exercicio 90 leia nome e media e a situação
dic = {}
dic['nome'] = str(input('nome\n-> '))
dic['media'] = int(input(f'media do(a) aluno(a) {dic["nome"]}\n-> '))
if dic['media'] < 7:
  dic['sit'] = 'reprovado'
else:
  dic['sit'] = 'aprovado'

print('_-' * 30)
for k,v in dic.items():
  print(f'{k} = {v}')
print('_-' * 30)
'''

from operator import itemgetter
from random import randint
from time import sleep
'''Exercicio 91 jogo de dados sem input
jogadas = {}
maior = 0
jogadas['jogador1'] = randint(1,6)
jogadas['jogador2'] = randint(1,6)
jogadas['jogador3'] = randint(1,6)
jogadas['jogador4'] = randint(1,6)

rankin = []
for k, v  in jogadas.items():
  if v > maior:
    maior = v
    nome_maior = k

for k,v in jogadas.items():
  print(f'Jogador {k} tirou = {v}')
  sleep(1)

print('O(s) jogador(es) vencedor(es) foi(ram) -> ', end='')
for k, v in jogadas.items():
  if v == maior:
    print(f'{k}...', end = ' ')
print(f'com o valor de {maior}')

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('=================== RANKING =================')
for i, v in enumerate(ranking):
  print(f'=    {i + 1}° lugar : {v[0]} com {v[1]} pontos...    =')
  sleep(1)
print('=============================================')
'''

'''Exercicio 92 lista com carteira de trabalho
usuario = {}
usuario['nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Digite seu ano de nascimento: '))
usuario['idade'] = 2022 - nascimento
usuario['carteira'] = int(input('Digite seu numero de carteira de trabalho (0 caso não tenha): '))

if usuario['carteira'] != 0:
  usuario['ano_contratacao'] = int(input('Digite seu ano de contratação: '))
  usuario['salario'] = float(input('Digite o seu salário: '))
  usuario['anos_restantes'] = 62 - usuario['idade']

for k,v in usuario.items():
  if k == 'salario':
    print(f'{k} = R${v}')
  else:
    print(f'{k} = {v}')
'''

'''Exercicio 93 aproveitamento com jogadores'''


'''Exercicio 94 acima da media de idade do grupo
galera = []
pessoa = {}
soma = media = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Digite o nome: '))
  pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()
  if pessoa['sexo'] not in 'MF':
    while True:
      print('Erro! Digite um sexo válido [M/F] ')
      pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()
      if pessoa['sexo'] in 'MF':
        break
  pessoa['idade'] = int(input('Digite a idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())
  print('Usuário adicionado.')
  
  continuar = ' '
  while True:
    continuar = str(input('Deseja continuar? [S/N]\n-> ')).upper()
    if continuar not in 'SN':
      print('Erro! Digite apenas S para Sim e N para não!')
    else:
      break
  if continuar == 'N':
    break
  
media = soma//len(galera)
print('*' * 30)

print(f'{len(galera)} pessoas foram cadastradas.')
print(f'A média das idades é {media}')
print(f'As mulheres cadastradas foram ', end = '')
for p in galera:
  if p['sexo'] == 'F':
    print(f'{p["nome"]}...', end = '')
print()

print('A lista de pessoas com idade acima da média é ', end = '')
for p in galera:
  if p['idade'] >= media:
    print(f'{p["nome"]}...', end = '')
    
print('*' * 30)
'''
    
'''
jogador = {}
aproveitamento = []

jogador['nome'] = str(input('Digite o nome do jogador: '))
qtd_part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

for c in range (0,qtd_part):
  aproveitamento.append(int(input(f'Quantos gols no {c + 1}° jogo?: ')))
  jogador['gols'] = aproveitamento.copy()

print(aproveitamento)
print(jogador)

print(f'Analisando dados do jogador {jogador["nome"]}...')
total = sum(jogador['gols'])
sleep(1)
print('#' * 30)
for k,v in jogador.items():
  print(f'{k} = {v}')
print(f'Quantidade de partidas = {qtd_part}')
print(f'Total de gols = {total}')
print('#' * 30)

print('=-' * 30)
for c in range(0,qtd_part):
  print(f'Na {c + 1}° partida, fez {jogador["gols"][c]}')    
print('=-' * 30)
'''

'''Aprimoramento do exercicio de futebol
jogador = {}
aproveitamento = []
jogadores = []

while True:
  jogador.clear()
  jogador['nome'] = str(input('Digite o nome do seu jogador: '))
  qtd_partida = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

  aproveitamento.clear()

  for c in range (0,qtd_partida):
    aproveitamento.append(int(input(f'Quantos gols na {c + 1} partida?: ')))
  jogador['gols'] = aproveitamento.copy()
  
  print('Jogador adicionado!')

  jogadores.append(jogador.copy())

  continuar = str(input('Deseja continuar? [S-N]: ')).upper()
  if continuar == 'N':
    break

print(jogadores)

print('=-' * 30)
print('COD', end='')
for k in jogador.keys():
  print(f'  {k}  ', end='')
print()

for k,v in enumerate(jogadores):
  print(f'{k}   ', end='')
  for d in v.values():
    print(f' {d}  ',end='')
  print()
print('=-' * 30)

while True:
  cod = int(input('Digite o código [COD] do jogador que deseja inspecionar: ("999" cancela)\n-> '))
  if cod == 999 or cod >= len(jogadores):
    print('GG')
    break
  print(f'Analisando dados do jogador {jogadores[cod]["nome"]}...')
  sleep(1)
  for c, g in enumerate(jogadores[cod]['gols']):
    print(f'No {c + 1}° jogo fez {g} gols...')
  print(f'Tendo um total de {sum(jogadores[cod]["gols"])} gols')
'''
