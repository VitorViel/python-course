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

