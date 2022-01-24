'''
frase = str(input("Digite a frase escolhida\n-> "))
tamanho = len(frase)
contador = 0
letras_juntas = ''

while contador < tamanho:
    letra_separadas = frase[contador]
    letras_juntas += letra_separadas
    print(letras_juntas)
    contador += 1
'''

frase = str(input("Digite sua frase escolhida\n ->"))
tamanho = len(frase)

while tamanho > 0:
    diminuindo_frase = frase[0:tamanho]
    tamanho -= 1
    print(diminuindo_frase)
