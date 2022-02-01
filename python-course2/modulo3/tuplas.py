import random
'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
'''
'''
for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
for pos,c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}° :P')
'''
'''
#sorted() organiza as tuplas
print(sorted(lanche))
a = 1,2,3,4
b = 5,6,7,8
c = a + b
print(c.count(6))
print(c.index(2))
del(c)'''

'''Exercicio 72 tuplas com numeros
while True:
    a = ('zero','um','dois','tes','quatro','cinco','seis','sete','oitro','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
    num = int(input('Digite um número entre 0 e 20 para ver por extenso\n-> '))
    if num < 0 or num > 20:
        print('Numero invalido!')
    else:
        break
print(a[num])'''

'''Exercicio 73 tabela brasileirao
a = 'sp','ge','cam','cor','fla','chape','san','pal'
print(f'os 4 primeiros {a[:5]}')
print(f'os 4 ultimos {a[-4:]}')
print(f'organizando eles em ordem alfabética {sorted(a)}')
print(f'a chape ta na {a.index("chape")+ 1}° posição')
'''

'''Exercicio 74 num aleatorio em tuplas
a = random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)
print(f'Os números sorteados foram -> {a}')
maior = a[0]
menor = a[0]
for c in range(0,len(a)):
    if a[c]> maior:
        maior = a[c]
    if a[c] < menor:
        menor = a[c]
#------------ OR ------------
print(f'O menor numero foi {max(a)}')
print(f'O maior numero foi {min(a)}')
'''

'''Exercicio 75 tupla mostrar quantas vzs nmr foi digitado
l = (int(input('digite o 1\n-> ')),int(input('digite o 2\n-> ')),int(input('digite o 3\n-> ')),int(input('digite o 4\n-> ')))  
print(f'O nove apareceu {l.count(9)} vezes')
if 3 in l:
    print(f'O tres apareceu na {l.index(3) + 1}° posicao')
else:
    print('O tres nao apareceu')
    
print('os números pares foram\n-> ', end='')
for c in l:
    if c % 2 == 0:
        print(c, end=' ')
'''
