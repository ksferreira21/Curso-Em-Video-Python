# Programa com um menu de opções de matemática.
from time import sleep

def valores():
    while True:
        try:
            p1 = int(input('\033[1;34mPrimeiro valor: \033[m'))
            p2 = int(input('\033[1;34mSegundo valor: \033[m'))
            return p1, p2
        except ValueError as error:
            print(f'\033[1;31mErro: {error}, Tente Novamente!\033[m')

def saindo():
    for i in range(3):
        print(f'\033[1;35mSaindo.' + '.' * i, end='\r')
        sleep(1)
        print(' ' * 50, end='\r')

p1, p2 = valores()
resposta = 0

while resposta != 5:
    print(f'''{"\033[1;33m-=-\033[m" * 8} 
\033[1;33m[ 1 ] somar
\033[1;32m[ 2 ] multiplicar 
\033[1;34m[ 3 ] maior 
\033[1;36m[ 4 ] novos números
\033[1;35m[ 5 ] sair\033[m
{"\033[1;33m-=-\033[m" * 8} ''')
    
    try:
        resposta = int(input('\033[1;36m>>>> Qual a sua resposta? \033[m'))
        if 1 <= resposta <= 5:
            if resposta == 1:
                soma = p1 + p2
                print(f'\033[1;33mA soma de {p1} + {p2} = {soma}\033[m')
            elif resposta == 2:
                multiplicar = p1 * p2
                print(f'\033[1;32mA multiplicação de {p1} x {p2} = {multiplicar}\033[m')
            elif resposta == 3:
                if p1 > p2:
                    print(f'\033[1;34m{p1} > {p2}\033[m')
                elif p2 > p1:
                    print(f'\033[1;34m{p2} > {p1}\033[m')
                else:
                    print(f'\033[1;34m{p1} = {p2}\033[m')
            elif resposta == 4:
                p1, p2 = valores()  # Atualiza os valores de p1 e p2
            elif resposta == 5:
                saindo()  # Animação de sair, so para deixar bonito
                print('\033[1;35mPrograma Finalizado!\033[m')
                break  # Quebra o loop
        else:
            print('\033[1;31mEntrada Inválida, tente novamente! Digite um número entre 1 e 5.\033[m')

    except ValueError as e:
        print(f'\033[1;31mOcorreu um erro ({e})! Tente novamente!\033[m')
# Desenvolvido por Kaiky 2025
