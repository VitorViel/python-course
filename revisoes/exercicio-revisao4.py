#Exercicio 1
'''
velocidade = float(input("Digite a velocidade do carro\n-> "))

if velocidade > 80:
  print(f"Sua velocidade de {velocidade} Km/h foi maior que o permitido! Você acaba de ser multado!")
  print(f"Sua multa é baseada em R$7,00 a cada Km acima do limite, ou seja, sua multa é de R${(velocidade - 80) * 7:.1f}0!")
  
else:
  print("Tudo certo... Boa viagem :)")
'''


#Exercicio 2
'''
numero = int(input("Digite um número\n-> "))

if numero % 2 == 0:
  print(f"Seu número {numero} é par!")

else:
  print(f"Seu número {numero} é impar!")
'''


#Exercicio 3
'''
distancia = int(input("Digite a distância da sua viagem\n-> "))

if distancia <= 200:
  distancia = distancia * 0.50
  print(f"O preço a ser cobrado é de R${distancia}0 reais!")

else:
  distancia = distancia * 0.45
  print(f"O preço a ser cobrado é de R${distancia}0 reais!")
'''


#Exercicio 4
'''
salario = int(input("Digite o salário a ser ajustado\n-> "))

if salario > 1250 :
  salario = salario + salario * 10 / 100
  print(f"O salário ajustado deu um total de R${salario}0!")

else:
  salario = salario + salario * 15 / 100
  print(f"O salário ajustado deu um total de R${salario}0!")
'''


#Exercicio 5 
'''
valor = int(input("Digite um valor INT\n-> "))

if valor >= 0:
  valor = valor ** 0.5
  print(f"A raíz quadrada do seu número positivo natural é {valor}!")

else:
  print("Valor inválido!")
'''


#Exercicio 6
'''
lado1 = int(input("Digite o primeiro lado do possível triângulo\n-> "))
lado2 = int(input("Digite o segundo lado do possível triângulo\n-> "))
lado3 = int(input("Digite o terceiro lado do possível triângulo\n-> "))

if lado1 + lado2 > lado3:
  print(f"Os números dos lados {lado1}, {lado2} e {lado3}, podem formar um triângulo!")
  
elif lado1 + lado3 > lado2:
  print(f"Os números dos lados {lado1}, {lado2} e {lado3}, podem formar um triângulo!")
  
elif lado2 + lado3 > lado1:
  print(f"Os números dos lados {lado1}, {lado2} e {lado3}, podem formar um triângulo!")
  
else:
  print("Com os números digitados não é possível formar um triângulo!")
'''


#Exercicio 7
'''
numero1 = int(input("Digite qualquer número\n-> "))
numero2 = int(input("Digite qualquer número novamente\n-> "))

print(f"Ótimo! Seus números são {numero1} e {numero2}!")
print("O que deseja fazer com eles?\nEscolha uma das opções abaixo!")

operacao = int(input("[1] -> SOMAR\n[2] -> SUBTRAIR\n[3] -> MULTIPLICAR\n[4] -> DIVIDIR\n-> "))

if operacao == 1:
  print(f"SOMA! Tudo bem... A soma dos seus números {numero1} e {numero2} é igual a {numero1 + numero2}")
elif operacao == 2:
  print(f"SUBTRAÇÃO! Tudo bem... A subtração dos seus números {numero1} e {numero2} é igual a {numero1 - numero2}")
elif operacao == 3:
  print(f"MULTIPLICAÇÃO! Tudo bem... A multiplicação dos seus números {numero1} e {numero2} é igual a {numero1 * numero2}")
elif operacao == 4:
  print(f"DIVISÃO! Tudo bem... A divisão dos seus números {numero1} e {numero2} é igual a {numero1 / numero2}")
else:
  print("Digite uma das 4 opções!")  
'''


#Exercicio 8
'''
valor1 = int(input("Digite um valor qualquer\n-> "))
valor2 = int(input("Digite novamente um valor qualquer\n-> "))

if valor1 > valor2:
  print(f"O maior valor é {valor1}! e a subtração entre eles é {valor1 - valor2}")
  
elif valor2 > valor1:
  print(f"O maior valor é {valor2}! e a subtração entre eles é {valor2 - valor1}")
  
else:
  print(f"Os valores são iguais!")
'''


#Exercicio 9
'''
valor_casa = int(input("Digite o valor da casa desejada\n-> "))

salario = int(input("Digite o seu salário\n-> "))

qtd_anos = int(input("Digite a quantidade de anos que deseja pagar\n -> "))

prestacao = valor_casa / (qtd_anos * 12)

qtd_meses = qtd_anos * 12

if prestacao < salario * 30 / 100:
  print(f"Empréstimo realizado com sucesso! O total a pagar por mês é R${prestacao:.1f}0 e a quantidade de tempo é de {qtd_anos} anos, ao todo {qtd_meses} meses")
  
else:
  print("Não é possivel realizar a operação pois a prestação é maior que 30 por cento do seu salário")
'''


#Exercicio 10
'''
preco = int(input("Digite o preço do produto\n-> "))

preco_mg = preco + preco * 7 / 100
preco_sp = preco + preco * 12 / 100
preco_rj = preco + preco * 15 / 100
preco_ms = preco + preco * 8 / 100

estado = str(input("Digite a sigla do estado em que o produto será enviado\n-> MG\n-> SP\n-> RJ\n-> MS\n-> "))

if estado == 'mg':
  print(f"O preço a se pagar do produto com um acréscimo de 7% de imposto, será R${preco_mg:.2f}")
elif estado == 'sp':
  print(f"O preço a se pagar do produto com um acréscimo de 12% de imposto, será R${preco_sp:.2f}")
elif estado == 'rj':
  print(f"O preço a se pagar do produto com um acréscimo de 15% de imposto, será R${preco_rj:.2f}")
elif estado == 'ms':
  print(f"O preço a se pagar do produto com um acréscimo de 8% de imposto, será R${preco_ms:.2f}")
else:
  print("Digite uma das 4 opções!")  
'''


#Exercicio 11
'''
preco = int(input("Digite o preço do produto\n-> "))

preco_dinheiro_cheque = preco - preco * 10 / 100
preco_cartao = preco - preco * 5 / 100
preco_2x_cartao = preco 
preco_3x_cartao = preco + preco * 20 / 100

metodo = int(input("[1] -> DINHEIRO OU CHEQUE (10% DE DESCONTO)\n[2] -> CARTÃO (5% DE DESCONTO)\n[3] ->EM ATÉ 2 VEZES NO CARTÃO (PREÇO NORMAL)\n[4] -> 3 VEZES OU MAIS NO CARTÃO (20% JUROS)\n-> "))

if metodo == 1:
  print(f"->DINHEIRO OU CHEQUE<-\nO preço a se pagar com um desconto de 10%, será R${preco_dinheiro_cheque:.2f}")
elif metodo == 2:
  print(f"->À VISTA NO CARTÃO<-\nO preço a se pagar com um desconto de 5%, será R${preco_cartao:.2f}")
elif metodo == 3:
  print(f"->EM ATÉ 2 VEZES NO CARTÃO<-\nO preço a se pagar será R${preco_2x_cartao:.2f}")
elif metodo == 4:
  print(f"->EM 3 VEZES OU MAIS NO CARTÃO<-\nO preço a se pagar com 20% de juros, será R${preco_3x_cartao:.2f}")
else:
  print("Digite uma das 4 opções!")  
'''

#Exercicio 12
'''  
altura = float(input("Digite sua altura em metros e centimetros (Exemplo: 1.75)\n-> "))
sexo = str(input("Digite a inicial do seu sexo (Exemplo: M)\n-> "))

peso_ideal_m = (72.7 * altura) - 58
peso_ideal_f = (62.1 * altura) - 44.7

if sexo == 'm':
    print(f"O peso ideal pra uma pessoa masculina com uma altura de {altura} M, é de {peso_ideal_f:.1f}Kg")
  
elif sexo == 'f':
  print(f"O peso ideal pra uma pessoa feminina com uma altura de {altura} M, é de {peso_ideal_f:.1f}Kg")

else:
  print("Digite M ou F!")
'''

