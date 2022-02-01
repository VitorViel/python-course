from time import sleep
from random import choice
#Exercicio 1
'''
for i in range(10,1,-1):
  print(f"{i}!")
  sleep(1)
'''

#Exercicio 2
'''
for i in range(2,52,2):
  print(f"{i}!")
'''

#Exercicio 3
'''
n = 0
for i in range(0,500,3):
  n += i
  print(f"{n}")
'''

#Exercicio 4
'''
num = int(input("num\n-> "))
for i in range(1,11):
  print(f"{num * i}")
'''

#Exercicio 5
'''
num1 = int(input("num1\n-> "))
num2 = int(input("num2\n-> "))
soma = 0

if num1 % 2 ==0 and num2 % 2 ==0:
  for i in range(num1, num2 - 1 ,2):
    soma = soma + i
else:
  print("Digite 2 valores pares")

print(soma)
'''

#Exercicio 6
'''
num = int(input("num\n-> "))
operacao = str(input("operacao + - ou *\n-> "))
pa = int(input("agora, digite o número da PA\n-> "))

if operacao == '+':
  for i in range(0,10):
    print(f"{num + pa}")
    num += pa
elif operacao == '-':
  for i in range(0,10):
    print(f"{num - pa}")
    num -= pa
elif operacao == '*':
  for i in range(0,10):
    print(f"{num * pa}")
    num *= pa
else:
  print("Digite uma operação válida")
'''

#Exercicio 7
'''
num = int(input("num\n-> "))
contador = 0

for i in range(1, num + 1):
  if num % i == 0:
    contador += 1

if contador == 2:
  print("O seu número é primo")
  
else: 
  print("O seu número não é primo")
'''

#Exercicio 8
'''
palindrome, ja ta feito
'''

#Exercicio 9
'''
maior = 0
menor = 0
for i in range(1,7):
  ano = int(input(f"Digite o ano de nascimento da {i} pessoa\n-> "))
  if 2022 - ano > 18:
    maior += 1
  else:
    menor += 1
    
print(f"{maior} pessoas são maiores de idade")
print(f"{menor} pessoas são menores de idade")
'''

#Exercicio 10
'''
maior = 0    
menor = 1000
for i in range(1,6):
  peso = float(input(f"Digite o peso da {i} pessoa\n-> "))
  if peso > maior:
    maior = peso
  if peso < menor:
    menor = peso
    
print(f"{menor} é o menor peso")
print(f"{maior} é o maior peso")
'''

#Exercicio 11
'''
f_nova = 0
m_velho = ''
m_idade_velho = 0
for i in range(1,5):
  nome = str(input(f"Digite o nome da {i} pessoa\n-> "))
  idade = int(input(f"Digite a idade da {i} pessoa\n-> "))
  sexo = str(input(f"Digite o sexo da {i} pessoa[m] ou [f]\n-> "))
  
  if sexo == 'f' and idade < 20:
    f_nova += 1
    
  if sexo == 'm' and idade > m_idade_velho:
    nome_homem_mais_velho = nome
  
  idade += idade
  
print(f"A média de idade é {idade//4}")
print(f"{f_nova} pessoas são mulheres e tem menos de 20 anos")
print(f"{nome_homem_mais_velho} é o homem mais velho")  
'''

#Exercicio 58
'''
n = choice(range(1,11))
escolha = 0
print(n)
while escolha != n:
  escolha = int(input("Digite um numero de 1 a 10 para adivinhar qual eu escolhi"))
  if escolha != n:
    print("Vc errou")
print("Parabens, voce acertou")  
'''

#Exercicio 64
'''
v = 0
numero = 0
qtd_numero = 0

while v != 999:
  v = int(input("valor\n-> "))
  if v != 999:
    numero += v
    qtd_numero += 1
  
print(f"Você decidiu parar...\nvc digitou {qtd_numero} numeros\nCom a soma de {numero}")
'''

#Exercicio 65
jogar = str(input("Olá! o que quer fazer? [jogar] [sair]\n-> "))

if jogar == 'jogar':
  maior = 0
  menor = 10000
  soma = 0
  continuar = ''
  qtd_numeros = 0

  while continuar != 's':
    n = int(input("Digite um número\n-> "))
    qtd_numeros += 1
    soma += n
    if n > maior:
      maior = n
    if n < menor:
      menor = n
    continuar = str(input("digite 's' para sair do jogo ou 'c' para continuar jogando...\n-> "))
  
  print("Vc decidiu sair")
  print(f"A média entre os números que vc escreveu é {soma / qtd_numeros}")
  print(f"O maior número digitado é {maior}")
  print(f"O menor número digitado é {menor}")
      