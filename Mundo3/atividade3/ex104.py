# Programa que valida a sua resposta até receber um número.
def leiaint(msg):

    while True:
        n = input(msg)
        if not n.isdigit():
            print(f'\033[1;31mERRO!, digite um valor válido.\033[m')

        else:
            return int(n)
        
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
# Desenvolvido por Kaiky - 2025
