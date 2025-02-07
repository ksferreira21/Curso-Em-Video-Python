# Programa que mostra o manual do comando especificado, usando o pydoc (OBS: Estou usando VSCODE)
from time import sleep
import pydoc

def manual():
    """
        Este programa fornece um sistema de ajuda interativo para comandos Python.
        O usuário pode digitar um comando para obter seu manual de uso, 
        visualizando a documentação completa de cada função ou módulo.

        O sistema continuará até que o usuário digite "fim" para encerrar a execução.

        As principais funcionalidades incluem:
        - Exibição de uma tela de boas-vindas colorida e estilizada.
        - Exibição de manuais de comandos com cores de destaque.
        - Um formato limpo e organizado para facilitar a leitura da documentação.
        - Capacidade de fornecer mensagens de erro caso o comando digitado não seja válido.

        O comando é acessado através da função `pydoc.render_doc`, que coleta a documentação 
        do comando ou função em questão, apresentando-a de forma amigável.
    """
    while True:
        print('\033[1;36m~' * (len('CENTRAL DE AJUDA PYHELP') + 2))
        print(f'\033[1;36m CENTRAL DE AJUDA PYHELP'.center(len('CENTRAL DE AJUDA PYHELP') + 2))
        print('~' * (len('CENTRAL DE AJUDA PYHELP') + 2))
        print('\033[m')
        
        comando = str(input('\033[1;33mQue comando você deseja ver o manual? [FIM para sair.] \033[m').lower())
        if comando.lower() == 'fim':
            break
        elif comando.lower() == 'manual':
            print('\033[1;31mATENÇÃO PARA SAIR DO MANUAL DO COMANDO TERÁ QUE PRESSIONAR \033[1;32m(Q)\033[m\033[1;31m!!\033[m')
            sleep(3)
            help(manual)
        else:
            print('\033[1;35m~' * (len(f'MANUAL DO COMANDO "{comando}"') + 2))
            print(f'\033[1;35m MANUAL DO COMANDO "{comando}"'.center(len(f'MANUAL DO COMANDO "{comando}"') + 2))
            print('\033[1;35m~' * (len(f'MANUAL DO COMANDO "{comando}"') + 2))
            sleep(2)
            
            try:
                doc = pydoc.render_doc(comando)
                print(f'\033[1;107m{doc}\033[m')
            except Exception as e:
                print(f'\033[1;31mOcorreu um erro ao acessar o comando {comando}: {e}\033[m')


# Programa principal
manual()
print('\033[1;31mExecução Encerrada!\033[m')

# Desenvolvido por Kaiky - 2025
