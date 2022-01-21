#Exercicio 1
'''
nome = str(input("Digite seu nome\n-> "))
nome_maius = nome.upper()
nome_minus = nome.lower();

print(f"{nome_minus}\n{nome_maius}")
'''

#Exercicio 2
'''
nome = str(input("Digite seu nome\n-> ")).lower()
print(f"Seu nome ao contrário é {nome[::-1]}")
'''

#Exercicio 3
'''
nome = str(input("Digite seu nome completo\n-> ")).strip()
nome_maius = nome.upper()
nome_minus = nome.lower();
print(f"Seu nome em minúsculo:\n{nome_minus}\n e em maiúsculo:\n{nome_maius}")

print(f"Com {len(nome) - nome.count(' ')} caracteres")

nome = nome.split()
print(f"E com {len(nome[0])} caracteres no primeiro nome")
'''

#Exercicio 4
'''
frase = str(input("Digite sua frase\n-> ")).strip()
print(f" Sua frase tem {frase.count(' ')} espaços\n{frase.count('a')} vezes a letra A\n{frase.count('i')} vezes a letra i\ne {frase.count('o')} vezes a letra O")
'''

#Exercicio 5
'''
nome = str(input("Digite seu nome\n -> ")).upper()
for i in range(0, 5): print(nome)
'''

#Exercicio 6
'''
palavra = str(input("Digite uma palavra/frase pra ver se ela é palíndrome ou não\n-> ")).strip(" ").lower()
exibe_palavra =  palavra[::-1];
palavras = palavra.split()
juntas = ''.join(palavras)
invertida = juntas[::-1]

print(f"A sua palavra é : {palavra} e sua forma invertida é : {exibe_palavra}")

if juntas == invertida:
  print("Parabéns! Sua palavra/frase é palíndrome")
else:
  print("Sua palavra/frase não é palíndrome!")
'''

#Exercicio 7
'''
nome = str(input("Digite seu nome completo\n-> ")).strip()
print(f"Seu nome completo é {nome}")

print(f"Seu primeiro e último nome são: {nome.split()[0] + ' ' +  nome.split()[len(nome.split()) - 1]}")
print(f"Seu nome do meio é {nome.split()[1]}")
'''

#Exercicio 8

nome1 = str(input("Digite um nome com mais de uma palavra\n -> ")).strip(" ")
nome2 = str(input("Digite outro nome com mais de uma palavra\n -> ")).strip(" ")

if (len(nome1) - nome1.count(' ')) > (len(nome2) - nome2.count(' ')):
  print(f"O prmeiro nome digitado é maior que o segundo!")
  
elif (len(nome2) - nome2.count(' ')) > (len(nome1) - nome1.count(' ')):
  print("O segundo nome digitado é maior que o primeiro!")
  
else:
  print("Os dois nomes digitados tem a mesma quantidade de caracteres")

if  nome1.split()[len(nome1[:-2:-1])] > nome2.split()[len(nome2[:-2:-1])]:
  print("O ultimo nome do segundo nome inserido é o menor!")
  
elif nome1.split()[len(nome1[:-2:-1])] < nome2.split()[len(nome2[:-2:-1])]:
  print("O ultimo nome do primeiro nome é o menor!")
  
else:
  print("Os dois ultimos nomes tem a mesma quantidade de caracteres")
  
print(f"Os dois nomes do meio invertidos são {nome1.split()[1][::-1] + ' ' + nome2.split()[1][::-1] }")