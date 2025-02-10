def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, Digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;32mO Usuário decidiu não digitar esse número\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def text(msg):
    print(linha())
    print(msg.center(42))
    print(linha())



def interface(lista):    
    text('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção:\033[m ')
    return opc

