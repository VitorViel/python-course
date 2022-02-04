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

'''Exercicio 93 aproveitamento com jogadores
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou?: '))
total_gols = 0

for c in range (0,qtd_partidas):
  partidas.append(int(input(f'Quantos gols na {c + 1}° partida?: ')))
  total_gols += 1
jogador['gols'] = partidas[:]
jogador['total'] = sum(jogador['gols'])
print('Calculando valores...')
sleep(1)

for i, v in jogador.items():
  print(f'{i} = {v}')
  
print(f'      O jogador {jogador["nome"]} jogou {qtd_partidas} partidas...')
print('=============================================')
for i, v in enumerate(jogador['gols']):
  print(f'      Na {i+1} partida o {jogador["nome"]} fez {v} gols')
print(f'      Foi um total de {jogador["total"]} gols!')
print('=============================================')
'''
