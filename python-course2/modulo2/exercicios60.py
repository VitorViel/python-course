import random

''' Exercicio de fatorial 60
n = int(input('Digite um numero para ver o seu fatorial\n-> '))
c = n
f = 1
while c > 0:
    print(f'{c} ', end = '')
    print('X ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print(f'{f}', end = '')
'''

''' Exercicio tabuada condição parada 67
n = 0

while True:
    n = int(input('Digite um número para ver a tabuada\n-> '))

    if n < 0:
        break

    for c in range (1,11):
        print(f'{n} x {c} = {c*n}')
        c -= 1

print(f'Você decidiu parar... ')
'''

'''Exercicio Par ou Impar 68
while True:
    escolha_jogador = str(input('Par ou impar? [P] [I]')).lower()
    numero_pc = random.randint(0,11)
    numero_jogador = int(input('Digite seu número\n-> '))
    contador_vitorias = 0
    if numero_pc + numero_jogador % 2 == 0:
        if escolha_jogador == 'p':
            print("Parabéns, você ganhou da máquina :(")
            contador_vitorias += 1
        else:
            print('Ganhei!! Máquina > humanos rsrs')
            break
    else:
        if escolha_jogador == 'i':
            print('Parabéns! vc escolheu impar, e o número é impar você ganhou da máquina :(')
            contador_vitorias += 1
        else:
            print('Ganhei!! Máquina > humanos rsrs')
            break

print(f"O seu número de vitórias foi {contador_vitorias} vez(es)")
'''

'''Exercicio 69 Analise de dados em grupo
maioridade = 0
conta_macho = 0
conta_femea = 0
while True:
    print('-' * 30, end = '')
    print("Cadastro de pessoa física", end = '')
    print('-' * 30)
    idade = int(input('Digite a idade\n-> '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]\n-> ')).upper()
    if sexo == 'M':
        conta_macho += 1
    if sexo == 'F' and idade < 20:
        conta_femea += 1
    continuar  = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]\n-> ')).upper()
    if continuar == 'N':
        break
print(f'Voce decidiu sair...\n{maioridade} pessoas tem mais de 18 anos\n{conta_macho} pessoas são homens\n{conta_femea} pessoas são mulheres com mais de 20 anos')
'''

'''Exercicio 70 estatistica em produtos
preco_total = 0
conta_preco = 0
menor = 1000000
nome_mais_caro = ' '
while True:
    print('*' * 30)
    print('CADASTRO DE PRODUTO')
    print('*' * 30)
    nome = str(input('Digite o nome do produto\n-> '))
    preco = float(input('Digite o preço do produto\n-> R$'))
    preco_total += preco
    if preco > 1000:
        conta_preco += 1
    if preco < menor:
        menor = preco
        nome_mais_caro = nome
    continuar = ' '
    while continuar not in ('SN'):
        continuar = str(input('Deseja continuar?')).upper()
    if continuar == 'N':
        break

print(f'Você decidiu parar...\nO total de sua compra é de R${preco_total}\n{conta_preco} produtos custam mais de R$1000\n{nome_mais_caro} é o nome do produto mais barato')
'''

'''Exercicio 71 brabo Caixa Eletronico
while True:
    print('#' * 30)
    print('          BANCO ADP')
    print('#' * 30)
    dinheiro = int(input('Digite o valor que gostaria de sacar\n-> '))
    print('Você deverá sacar...')

    descontado = dinheiro//50
    print(f'{descontado} cédulas de 50')
    dinheiro = dinheiro - descontado*50

    descontado = dinheiro//20
    print(f'{descontado} cédulas de 20')
    dinheiro = dinheiro - descontado*20

    descontado = dinheiro//10
    print(f'{descontado} cédulas de 10')
    dinheiro = dinheiro - descontado*10

    descontado = dinheiro//1
    print(f'{descontado} cédulas de 1')
    dinheiro = dinheiro - descontado*1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]\n=> ')).upper()
    if continuar == 'N':
        break
print('Falou XD')
'''




