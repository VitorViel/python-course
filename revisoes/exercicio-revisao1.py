#Exercicio 1
'''
print("Hello World!")
'''

#Exercicio 2
'''
nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))

print(f"Olá {nome}!\nVocê tem {idade} anos e pesa {peso} Kilos")
'''

#Exercicio 3
'''
numero = int(input("Digite o número escolhido -> "))
print(f"Muito bem! O seu número é {numero}, o seu sucessor é {numero + 1} e o seu antecessor é {numero - 1}")
'''

#Exercicio 4
'''
valor = int(input("Digite o número escolhido -> "))
print(f"Muito bem! O valor escolhido é {valor}, seu dobro é de {valor*2}, seu triplo {valor*3} e sua raíz quadrada é de {valor ** (1/2)}")
'''

#Exercicio 5
'''
ano_nascimento = int(input("Digite o seu ano de nascimento -> "))
print(f"Muito bem! O seu ano de nascimento é {ano_nascimento} e por isso, você tem {2021 - ano_nascimento} ou {2022 - ano_nascimento} anos de idade")
'''

#Exercicio 6
'''
preco = float(input("Digite o preço do produto -> "))
#preco_desconto = preco - preco*25/100
print(f"O preço do produto é R${preco}0, com 25% de desconto é R${preco - preco*25/100}0!")
'''

#Exercicio 7
'''
salario = int(input("Digite o salário a ser aumentado -> "))
print(f"Muito bem! O salário é de R${salario}, aplicando os 75% de aumento, o salário será ajustado para R${salario + salario * 75 / 100}0 ")
'''

#Exercicio 8
'''
valor = int(input("Digite qualquer número para ver sua tabuada! -> "))
print(f"{valor * 1}\n{valor * 2}\n{valor * 3}\n{valor * 4}\n{valor * 5}\n{valor * 6}\n{valor * 7}\n{valor * 8}\n{valor * 9}\n{valor * 10}\n")
'''

#Exercicio 9
'''
tipo1 = int(input("Digite qualquer numero inteiro -> "))
tipo2 = str(input("Digite qualquer palavra -> "))

print(f"O tipo da sua primeira inserção é...")
print(type(tipo1))
print(f"O tipo da sua segunda inserção é...")
print(type(tipo2))

print("Portanto, o resultado de comparação é... ")

print(tipo1 == tipo2)
'''

#Exercicio 10
"""
km_rodados = float(input("Digite os kilometros rodados pelo carro -> "))
qtd_dias = int(input("Digite a quantidade de dias que o cliente usou o carro -> "))

resultado_geral = 60 * qtd_dias + 0.15 * km_rodados

print(f"Kilometros = {km_rodados}\nQuantidade de dias em que o carro foi utilizado = {qtd_dias}")
print(f"O preço a pagar pelo cliente é de R${resultado_geral}0")
"""

#Exercicio 11
'''
idade = int(input("Digite sua idade -> "))

idade_total_dias = idade * 365
idade_dias = idade_total_dias % 30 
idade_meses = idade_total_dias // 30

print(f"Ok! Você tem em {idade} anos de vida, já passou por {idade_meses} meses e {idade_dias} dias de vida!")
'''

#Exercicio 12
'''
premio = float(780.000)

print(f"O premio total é de R${premio}00!")

premio_primeiro_jogador = premio * 46 / 100
premio_segundo_jogador = premio * 32 / 100
premio = premio - premio_segundo_jogador - premio_primeiro_jogador
premio_terceiro_jogador = premio

print(f"O primeiro jogador ficará com R${premio_primeiro_jogador:.3f}.\nJá o segundo jogador, ficará com R${premio_segundo_jogador:.3f}.\nE o terceiro jogador ficará com os R${premio_terceiro_jogador:.3f} restantes!")
'''

#Exercicio 13
'''
celsius = int(input("Digite a temperatura(em Celsius) que deseja converter para farenheint -> "))

fahr = celsius * 1.8 + 32

print(f"Sua temperatura em Celsius é {celsius}°, e em Fahrenreint é {fahr}")
'''
  
#Exercicio 14
'''
nota1 = float(input("Digite a primeira nota do aluno -> "))
nota2 = float(input("Digite a segunda nota do aluno -> "))
nota3 = float(input("Digite a terceira nota do aluno -> "))
nota4 = float(input("Digite a quarta nota do aluno -> "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média total do aluno é {media:.2f}")
'''

#Exercicio 15

# largura = int(input("Digite a largura da área em metros -> "))
# altura = int(input("Digite a altura da área em metros -> "))

# area = largura * altura;

# litro_tinta = 2
# qtd_tinta = area / litro_tinta

# print(f"A quantidade de litros de tinta necessária para pintar {area} Metros quadrados, é de {qtd_tinta} Litros!")



