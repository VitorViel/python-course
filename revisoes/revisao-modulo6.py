import random
import math
from random import choice

#Exercicio 1
'''
dado = [1,2,3,4,5,6]
jogar = str(input("Digite 'jogar' para lançar o dado!\n-> "))

if jogar == 'jogar':
  exibe_lado = (choice(dado))
  print(f"O dado foi lançado! Seu valor é {exibe_lado}")
else:
  print("Ok! O dado não será lançado")
'''

#Exercicio 2
'''
escolha = str(input("Impar ou par? (Digite impar ou par!)\n ->")).lower()

if escolha == 'impar' or escolha == 'par':
    valor1 = int(input(f"Muito bem! você escolheu {escolha}! Agora digite o primeiro valor escolhido\n-> "))
    valor2 = random.randint(0,10)
    resultado = valor1 + valor2
    print(f"Você escolheu {valor1}, eu escolho {valor2}, a soma é {resultado}. Portanto...")

    if escolha == 'impar':
        if resultado % 2 == 0:
            print("Voce perdeu! kkkk achei fácil")
        else:
            print("Voce ganhou... parabens :(")

    elif escolha == 'par':
        if resultado % 2 == 0:
            print("Voce ganhou... parabens :(")
        else:
            print("Voce perdeu! kkkk achei fácil")
    else:
            print("Digite uma das opções disponiveis")
else:
    print("Digite uma das 2 opções!")
'''

#Exercicio 3
'''
cartas = '4COPAS 7OUROS REISESPADAS'.split()
escolhida = (choice(cartas))
print(escolhida)

print(f"Olá usuário! A sua missão é adivinhar a carta que eu escolhi")
print(f"Essas foram minhas opções {cartas}")
escolha_usuario = int(input("Digite [1] para 4 de Copas, [2] para 7 de Ouros e [3] para Reis de espadas"))

if escolha_usuario == 1:
  if escolhida == '4COPAS':
    print(f"Parabéns, você adivinhou!\nA carta escolhida era {escolhida}")
  elif escolhida == '7OUROS':
    print(f"Você errou!\nA carta escolhida era {escolhida}")
  elif escolhida == 'REISESPADAS':
    print(f"Você errou!\nA carta escolhida era {escolhida}")

elif escolha_usuario == 2:
  if escolhida == '4COPAS':
    print(f"Você errou!\nA carta escolhida era {escolhida}")
  elif escolhida == '7OUROS':
    print(f"Parabéns, você adivinhou!\nA carta escolhida era {escolhida}")
  elif escolhida == 'REISESPADAS':
    print(f"Você errou!\nA carta escolhida era {escolhida}")

elif escolha_usuario == 3:
  if escolhida == '4COPAS':
    print(f"Você errou!\nA carta escolhida era {escolhida}")
  elif escolhida == '7OUROS':
    print(f"Você errou!\nA carta escolhida era {escolhida}")
  elif escolhida == 'REISESPADAS':
    print(f"Parabéns, você adivinhou!\nA carta escolhida era {escolhida}")
    
else:
  print("Digite um dos números respectivos ás cartas!")
'''

#Exercicio 4
'''
opcoes = [5,10,15,20]
escolhido = (choice(opcoes))
print("Olá usuário! Você deve adivinhar o número que eu escolhi")
print(f"Minhas opções foram {opcoes}")
print(escolhido)
escolha_usuario = int(input("Digite seu primeiro palpite\n-> "))


if escolha_usuario == escolhido:
  print("Parabéns! Você adivinhou")
else:
  print(f"Você errou! O número que eu escolhi era {escolhido}!")
'''

#Exercicio 5
'''
from random import choice

pontos_jogador1 = 0
pontos_jogador2 = 0
pontos_empate = 0
opcoes = "pe pa t".split()
    
while (pontos_jogador1 < 3) and (pontos_jogador2 < 3) and (pontos_empate < 3):
    jogada1 = str(input("[Pe] Pedra [Pa] Papel ou [T] tesoura?")).lower()
    jogada2 = (choice(opcoes))   
    if jogada1 == 'pa' or jogada1 == 'pe' or jogada1 == 't':
      if jogada1 == 'pe':
        if jogada2 == 'pe':
          print(f"Eu escolhi o mesmo que vc, o jogo empatou!")
          pontos_empate += 1
        elif jogada2 == 'pa':
          print(f"Você escolheu pedra! Eu escolhi papel, eu ganhei")
          pontos_jogador2 += 1
        elif jogada2 == 't':
          print(f"Parabéns, vc ganhou! Eu escolhi tesoura!")
          pontos_jogador1 += 1

      elif jogada1 == 'pa':
        if jogada2 == 'pe':
          print("Parabéns, vc ganhou! Eu escolhi pedra!")
          pontos_jogador1 += 1
        elif jogada2 == 'pa':
          print(f"Eu escolhi o mesmo que vc, o jogo empatou!")
          pontos_empate += 1
        elif jogada2 == 't':
          print(f"Você escolheu papel! Eu escolhi tesoura, eu ganhei")
          pontos_jogador2 += 1
        
      elif jogada1 == 't':
        if jogada2 == 'pe':
          print("Você escolheu tesoura! Eu escolhi pedra, eu ganhei")
          pontos_jogador2 += 1
        elif jogada2 == 'pa':
          print(f"Parabéns, vc ganhou! Eu escolhi papel!")
          pontos_jogador1 += 1
        elif jogada2 == 't':
          print(f"Eu escolhi o mesmo que vc, o jogo empatou!")
          pontos_empate += 1  
      
      print("quem pegar 3 pontos primeiro, ganha!")
      print(f"Seus pontos: {pontos_jogador1}")
      print(f"Meus pontos: {pontos_jogador2}")
      print(f"Pontos do empate: {pontos_empate}")
    else:
      print("Escolha uma das opções!")

if pontos_jogador1 == 3:
  print("Parabéns, você ganhou este duelo!")
elif pontos_jogador2 == 3:
  print("Eu ganhei o duelo!") 
elif pontos_empate == 3:
  print("O jogo empatou!")           
'''

#Exercicio 6
'''
valor = float(input("Digite um valor float(com casa decimal)\n-> "))
valor_arredondado = math.ceil(valor)
valor_fatorial = math.factorial(valor_arredondado)

print(f"O valor digitado é {valor}")
print(f"e seu valor arredondado para mais é de {valor_arredondado}")
print(f"e seu valor fatorial é de {valor_fatorial}")
'''

#Exercicio 7
'''
alunos = str(input("Digite o nome dos alunos\n-> ")).strip(" ").split()
escolhido = choice(alunos)

print(f"O aluno escolhido para apresentar o projeto é o {escolhido}")
'''

#Exercicio 8
'''
nome = str(input("Digite o seu nome completo\n-> ")).strip()
separado = nome.split()
junto = ' '.join(separado)
escolhido = ((choice(separado)))
print(f"Seja bem-vindo {junto}! De todo o seu nome, eu achei mais bonito o {escolhido}")

#print(f"Meu nome favorito no seu nome completo é {choice(nome.split())}")
'''