from lib.interface import *
from lib.interface import linha
from time import sleep

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt',encoding='utf-8')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def criarArquivo(arq):
    try:
        a = open(arq, 'wt+',encoding='utf-8')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso XD')

def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um erro ao tentar ler o arquivo solicitado')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            sleep(1)
    finally:
        a.close()

def cadastrar(arq,nome = 'desconhecido',idade = 0):
    try:
        a = open(arq, 'at',encoding='utf-8')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro no cadastro de nova pessoa')
        else:
            print(f'Registro de {nome} realizado com sucesso!')
            a.close()
