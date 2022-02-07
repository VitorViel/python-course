'''
nome = str(input("nome\n-> "))
aotodo = len(nome) - nome.count(' ')
print(aotodo)
primeiro = nome.split()[0]
print(len(primeiro))
'''

'''
num = int(input("num\n-> "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"{u} unidades")
print(f"{d} dezenas")
print(f"{c} centenas")
print(f"{m} milhares")
'''

'''
nome = str(input("nome\n-> "))
silvas = nome.count('silva')

if silvas == True:
  print("Vc tem silva no nome")
else:
  print("vc n tem silva no nome")
'''

'''
frase = str(input("frase\n-> ")).strip().lower()
print(f"sua frase tem {frase.count('a')} letras A")
print(f"sua primeira posicao é {frase.find('a') + 1}")
print(f"sua ultima posicao é {frase.rfind('a') + 1}")
'''

'''
nome = str(input("nome\n-> ")).strip().split()
primeiro = nome[0]
ultimo = nome[len(nome)-1]
print(f"Seu primeiro nome = {primeiro}")
print(f"Seu ultimo nome = {ultimo}")
'''

'''
numero1 = int(input("numero1\n-> "))
numero2 = int(input("numero2\n-> "))
numero3 = int(input("numero3\n-> "))
menor = numero1
maior = numero1
if numero2 > maior:
  maior = numero2
if numero3 > maior:
  maior = numero3
  
print(f"O seu maior numero é {maior}")

if numero2 < menor:
  menor = numero2
if numero3 < menor:
  menor = numero3
  
print(f"E o seu menor número é {menor}")
'''
