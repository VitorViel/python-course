'''Exercicio 78 add num na lista e ver o maior e o menor
v = []
maior = 0
menor = 1000
pos_maior = -1
pos_menor = -1
for c in range (0,5):
    v.append(int(input('Digite um valor para adicionar na lista\n-> ')))

for c,n in enumerate(v):
    if n > maior:
        maior = n
        pos_maior = c

    if n < menor:
        menor = n
        pos_menor = c


print(f'O maior número digitado foi {maior} na posicao {pos_maior + 1}')
print(f'O menor número digitado foi {menor} na posicao {pos_menor + 1}')
'''

'''78 AINDA
lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um número na posiçaõ {c}\n-> ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]

print(f'Os numeros digitados foram {lista}')
print(f'O maior número foi {maior} na(s) posição(ões) ', end='')

for c,v in enumerate(lista):
    if v == maior:
        print(f'{c + 1}...', end='')
print()
print(f'O menor número foi {menor} na(s) posição(ões) ', end='')

for c,v in enumerate(lista):
    if v == menor:
        print(f'{c + 1}...', end='')
'''
'''
OOOOOOOOOOOOOOOOOUUUUUUUUUUU
print(f'O maior número digitado foi {max(lista)} na posição {lista.index(max(lista)) + 1}\nE o menor foi {min(lista)} na posiçao {lista.index(min(lista)) + 1}')
'''


'''Exercicio 79 add num nas listas e n pode ter igual la dentro
l = []
while True:
    novo = int(input('Digite um valor\n-> '))
    if novo in l:
        print(f'O seu número {novo} já existe na lista, digite outro!')
    else:
        l.append(novo)
    continuar = ' '
    while continuar not in ('SN'):
        continuar = str(input('Deseja continuar? [S/N]\n-> ')).upper()
    if continuar == 'N':
        break

print(f'Voce digitou os valores {l.sort()}')
'''

'''Exercicio 80 tenso de organizar sem o sort()
list = []
for c in range (0,5):
    novo = int(input('Digite o número a ser adicionado\n-> '))
    if c == 0  or novo > list[-1]:
        list.append(novo)
        print(f'Numero {novo} adicionado ao final da fila')
    else:
        pos = 0
        while pos < len(list):
            if novo < list[pos]:
                list.insert(pos, novo)
                print(f'Numero {novo} adicionado com sucesso na posoção {pos}°')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem sem o sort ficaram {list}')
print('=-' * 30)
'''


'''Exercicio 81 lista com maior menor, e a posicao 5
l = []
tem_cinco = False
qtd_num = 0
while True:
    novo = int(input('Digite um número\n-> '))
    l.append(novo)
    qtd_num += 1
    if novo == 5:
        tem_cinco = True
    continuar = ' '
    if continuar not in ('SN'):
        continuar = str(input('Deseja continuar? [S/N]\n-> ')).upper()
    if continuar == 'N':
        break

print('Você decidiu parar...')
print(f'Você digitou {qtd_num} números')
l.sort(reverse = True)
print(f'Os números em forma invertida ficaram assim\n=> {l}')
if tem_cinco == True:
    print('O valor 5 esteve presente na lista')
else:
    print('O valor 5 não esteve presente')
'''


'''Exercicio 82 listas com pares e impares
lista = []
lista_pares = []
lista_impares = []
while True:
    novo = int(input('Digite o número a ser adicionaodo\n-> '))
    lista.append(novo)
    if novo % 2 == 0:
        lista_pares.append(novo)
    else:
        lista_impares.append(novo)
    continuar = ' '
    while continuar not in ('SN'):
        continuar = str(input('Deseja continuar? [S/N]\n-> ')).upper()
    if continuar == 'N':
        break
print('Voce decidiu parar...')
print(f'A lista total é\n-> {lista}')
print(f'A lista de pares é\n-> {lista_pares}')
print(f'A lista de impares é\n-> {lista_impares}')
'''


'''Exercicio 83 verificar se a expressão está correta
exp = str(input('Digite a expressão a ser verificada\n-> '))
fecha1 = exp.count('(')
fecha2 = exp.count(')')
fecha3 = exp.count('{')
fecha4 = exp.count('}')
fecha5 = exp.count('[')
fecha6 = exp.count(']')

fecha = fecha1 + fecha2 + fecha3 + fecha4 + fecha5 + fecha6
print(fecha)
if fecha % 2 == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é valida')
'''
