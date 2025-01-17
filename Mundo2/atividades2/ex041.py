# Programa que diz o seu rank com atleta de acordo com sua idade
from datetime import date

try:
    nascimento = int(input('\033[34mEm que ano você nasceu? \033[m'))
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    if nascimento <= 0 or nascimento > ano_atual or nascimento < ano_atual - 120 :
        print('\033[31mIdade Inválida\033[m')

    else:
        if 1 <= idade <= 9:
            rank = '\033[32mMIRIM\033[m'
        elif 9 <= idade <= 14:
            rank = '\033[33mINFANTIL\033[m'
        elif 14 <= idade <= 19:
            rank = '\033[36mJUNIOR\033[m'
        elif 19 <= idade <= 20:
            rank = '\033[35mSÊNIOR\033[m'
        elif idade > 20:
            rank = '\033[31mMASTER\033[m'

        print(f'O atleta tem {idade} anos \nPor conta de sua idade o seu nível é: {rank}')

except ValueError:
    print('\033[31mPor favor, insira um ano válido.\033[m')
# Desenvolvido por Kaiky 2025
