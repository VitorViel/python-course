import pygame

escolha = int(input("Digite 1 para escutar [Alerta de follow] // 2 para escutar [Alerta de sub] \\ 3 para escutar o pai do cachorro loko falando q gosta do raulzito\n-> "))

if escolha == 1:
  pygame.init()
  pygame.mixer.music.load('alertafollow.wav')
  pygame.mixer.music.play()
  input()
  pygame.event.wait()

elif escolha == 2:
  pygame.init()
  pygame.mixer.music.load('alertasub.wav')
  pygame.mixer.music.play()
  input()
  pygame.event.wait()

elif escolha == 3:
  pygame.init()
  pygame.mixer.music.load('kchorro.wav')
  pygame.mixer.music.play()
  input()
  pygame.event.wait()
  
else:
  print("Digite uma das opções! 1 2 ou 3")