# print('\033[7;33;44mOla mundo!\033[m')

nome = str(input("nome\n-> "))
'''escolha =int(input(f"Olá {nome}! Prazer em te conhecer digite:\n[1] nome em vermelho\n[2] nome em amarelo\n[3] nome em azul"))

if escolha == 1:
  print(f'\033[1;31;47m{nome}\033[m')
elif escolha == 2:
  print(f'\033[1;33;47m{nome}\033[m')
elif escolha == 3:
  print(f'\033[1;34;47m{nome}\033[m')
'''

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m,',
         'roxo':'\033[35m',
         'pretoebranco':'\033[7;30m'}

print(f"{cores['roxo']}{nome}{cores['limpa']}")