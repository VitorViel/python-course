'''
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Vitor'
teste[1] = '18'

galera.append(teste[:])
print(galera[0][0])
print(galera[1][0])
'''

'''
galera = [['Vitor', 17],['Andre', 18],['Ana', 19],['Nicoli', 20]]

for c in galera:
    print(c[0])
'''

'''
galera = list()
dados = list()

for c in range(0,3):
    dados.append(str(input('Nome\n-> ')))
    dados.append(int(input('Idade\n-> ')))
    galera.append(dados[:])
    dados.clear()

print(galera) 
   '''