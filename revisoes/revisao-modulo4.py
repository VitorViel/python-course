escolha = int(input("Escolha uma das 4 opções abaixo\n[1] -> INT\n[2] -> STR\n[3] -> FLOAT\n[4] -> BOOL\n-> "))

if escolha == 1:
  valor1 = int(input("Digite seu número abaixo\n-> "))
elif escolha == 2:
  valor1 = str(input("Digite sua mensagem abaixo\n-> "))
elif escolha == 3:
  valor1 = float(input("Digite seu número FLOAT abaixo\n-> "))
elif escolha == 4:
  valor1 = bool(input("Digite seu valor boolean\n-> "))
else:
  print("Digite uma das 4 opções!")  

escolha2 = int(input("Digite novamente uma das 4 opções abaixo\n[1] -> INT\n[2] -> STR\n[3] -> FLOAT\n[4] -> BOOL\n-> "))

if escolha2 == 1:
  valor2 = int(input("Digite seu número abaixo\n-> "))
elif escolha2 == 2:
  valor22 = str(input("Digite sua mensagem abaixo\n-> "))
elif escolha2 == 3:
  valor2 = float(input("Digite seu número FLOAT abaixo\n-> "))
elif escolha2 == 4:
  valor2 = bool(input("Digite seu valor boolean\n-> "))
else:
  print("Digite uma das 4 opções!")

tipo_valor1 = type(valor1) 
tipo_valor2 = type(valor2) 

print(f"O seu primeiro dado foi do tipo {tipo_valor1}\nE o dado do seu segundo valor foi do tipo {tipo_valor2}\nPor isso...")

if type(valor1) == type(valor2):
  print("\nOs dois tipos de valores que você escolheu são iguais!")
  
else:
  print("\nOs dois tipos de valores que você escolheu não são iguais!")