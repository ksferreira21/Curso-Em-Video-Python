from packet115.interface import text, interface
from packet115.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    criarTXT(arq)

while True:
    resposta = interface(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção que vai listar o conteúdo do arquivo(dados.txt).
        lerTXT(arq)

    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa.
        text('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)

    elif resposta == 3:
        # Opção para sair do sistema.
        text('\033[1;32mSaindo do sistema! Volte sempre.\033[m'. center(51))
        break

    else:
        # Mensagem de erro ao digitar um número inteiro inválido.
        print('\033[1;31mError: Digite um número inteiro válido!\033[m')
        
    sleep(2)