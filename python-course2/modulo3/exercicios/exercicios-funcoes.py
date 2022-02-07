from time import sleep

def mostraLinha():
    print('-' * 30)
'''96 funcoes com largura e altrua
def area(lar,com):
    print(f'Largura = {lar} & Altura = {com}\nA área é de = {lar * com}m²')
mostraLinha()
l = int(input('Digite o valor da largura\n-> '))
c = int(input('Digite o valor do comprimento\n-> '))
area(l,c)
mostraLinha()
'''

'''97 frase adaptavel
def mostraLinha(tamanhoFrase):
    print('-' * tamanhoFrase)

def escreva(frase):
    mostraLinha(tam)
    print(f'  {frase}')
    mostraLinha(tam)

fr = str(input('Digite uma frase\n-> '))
tam = len(fr) + 4
escreva(fr)
'''

'''98 contador com 3 tipos 
def contador(a,b,c):
    if c == 0:
        c = 1
    if c < 0:
        c = c * - 1
    
    print(f'De {a} até {b} de {c} em {c}')
    
    if a > b:
        while a >= b:
            print(a, end=' ')
            sleep(0.5)
            a -= c
        print()
    elif a < b:
        while b >= a:
            print(a, end=' ')
            sleep(0.5)
            a += c
        print()

mostraLinha()

contador(0,10,1)
contador(10,0,2)

mostraLinha()
print('Agora é sua vez! escolha o seu ponto de partida, o ponto final, e o passo! EX: 2 10 2')
i = int(input('-> '))
f = int(input('-> '))
p = int(input('-> '))

contador(i, f, p)
'''

'''Exercicio 99 funcao maior()'''
lista = []
def maior(lista):
    maior_num = 0
    for c in range(0,len(lista)):
        if c == 0:
            maior_num = lista[c]
        if lista[c] > maior_num:
            maior_num = lista[c]
    print(f'O maior número de todos os digitadas foi {maior_num}')

while True:
    num = int(input('Digite um número para adicionar na lista: '))
    lista.append(num)
    continuar = str(input('Deseja continuar adicionando números?\n -> ')).upper()
    if continuar == 'N':
        break

maior(lista)



