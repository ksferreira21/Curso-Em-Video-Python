# Programa que valida entrada Float e Int, com tratamentos de erros presentes.
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


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;32mO Usuário decidiu não digitar esse número\033[m')
            return 0
        else:
            return num

        
Int = leiaInt('Digite um número inteiro: ')
Real = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {Int} e o real foi {Real}')
# Desenvolvido por Kaiky - 2025
