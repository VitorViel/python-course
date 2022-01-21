### STR ###
# strip(" ") = manda ignorar o que é passado dentro dos parenteses 
# upper = tudo digitado vai pra letra maiúscula
# lower = tudo digitado vai pra letra minuscula
# capitalize = deixa a primeira letra maiúscula
# len(variavel) = mostra quantas letras tem na variavel
# count (' ') = conta o que eu passar como parametro
# islower = retorna true ou false se tudo e minusculo
# isupper = retorna true ou false se tudo e maiusculo
# [0:4:1] = exibe começando da primeira letra, ate a quarta, de um em um
# .split = separa as palavras da frase
# .join(variavel) = juntou as palavras separadas

'''
exercicio Palindrome sem For
frase = str(input("Digite seu nome\n -> ")).strip(" ").lower()
palavras = frase.split()
juntas = ''.join(palavras)

inverso = juntas[::-1]
print(inverso)

if inverso == juntas:
  print(f"A sua palavra/frase é um palindrome!")
  
else:
  print("A sua palavra/frase não é um palindrome!")
'''

'''
exemplo com len e count

print(f"O nome {nome1} tem {len(nome1) - nome1.count(' ')} caracteres")

print(frase[0:5:2])
'''

'''
Sistema adaptável primeiro até o último nome
nome = str(input("Digite seu nome completo\n-> ")).strip(" ")
print(f"Olá {nome}\nSeu primeiro nome até o último em sequência é:")
nome = nome.split();

for i in range(0, len(nome)):
  print(nome[i])
'''

