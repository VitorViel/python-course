from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq) == True:
    print(f'Arquivo {arq} encontrado!')
else:
    criarArquivo(arq)


cabecalho('SERVIÇO DE PESSOAS')

while True:
    resposta = menu(['Cadastrar nova pessoa na lista', 'Ver lista de pessoas já cadastradas','Sair do programa'])
    if resposta == 1:
        cabecalho('Cadastro de nova pessoa...')
        nome = str(input('Digite o nome da pessoa a ser cadastrada: '))
        idade = leiaint('Digite a idade da pessoa a ser cadastrada: ')
        cadastrar(arq,nome,idade)
        print(linha())
    elif resposta == 2:
        cabecalho('Ver lista de pessoas já cadastradas...')
        lerArquivo(arq)
        print(linha())
    elif resposta == 3:
        cabecalho('Até logo!')
        break
    else: 
        print('\033[31mErro! Digite uma opção válida\033[m')
        sleep(2)
        continue