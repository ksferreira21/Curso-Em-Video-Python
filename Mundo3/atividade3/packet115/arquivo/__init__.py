from packet115.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarTXT(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as e:
        print(f'Houve um erro na criação dos {nome} \nError: {e}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerTXT(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        text('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'Nome: {dado[0]:<30}Idade:{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'Houve um problema na abertura do arquivo {arq}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} ADICIONADO!')
            a.close()
