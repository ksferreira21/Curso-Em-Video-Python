# Pedra Papel e Tesoura V1.0.0!
from random import choice
from time import sleep
try:
    def jokenpo_animacao():
        print('\033[93mJo.\033[0m', end='\r')
        sleep(1)
        print('\033[93mKen..\033[0m', end='\r')
        sleep(1)
        print('\033[93mPô...\033[0m', end='\r')
        sleep(1)
        print(' ' * 50, end='\r')

    print(f"\033[92m{'BEM VINDO AO JOKENPÔ!':=^50}\033[0m")

    sleep(2)

    jokenpo = ["Pedra", "Papel", "Tesoura"]
    cpu = choice(jokenpo)

    g = "\033[92mVocê ganhou!\033[0m"
    e = "\033[93mEMPATE!\033[0m"
    p = "\033[91mVocê perdeu!\033[0m"

    print(f'''{ '\033[94m-=-\033[0m' * 17 }
\033[96m{"Escolha sua mão": ^50}\033[0m
\033[96m{"(1) Pedra": ^50}\033[0m
\033[96m{"(2) Papel": ^50}\033[0m
\033[96m{"(3) Tesoura": ^52}\033[0m  
{ '\033[94m-=-\033[0m' * 17 }''')

    player_input = int(input('Sua mão: '))
    if player_input == 1:
        player = "Pedra"
    elif player_input == 2:
        player = "Papel"
    elif player_input == 3:
        player = "Tesoura"
    else:
        print("\033[91mEscolha inválida!\033[0m")
        quit()

    jokenpo_animacao()

    if player == "Pedra" and cpu == "Tesoura" or player == "Papel" and cpu == "Pedra" or player == "Tesoura" and cpu == "Papel":
        resultado = g
    elif player == "Pedra" and cpu == "Pedra" or player == "Papel" and cpu == "Papel" or player == "Tesoura" and cpu == "Tesoura":
        resultado = e
    elif player == "Pedra" and cpu == "Papel" or player == "Papel" and cpu == "Tesoura" or player == "Tesoura" and cpu == "Pedra":
        resultado = p

    print(f'{'\033[96m=-=\033[m'* 17}\n\033[95mVocê escolheu \033[1m{player}\033[0;95m e a cpu escolheu \033[1m{cpu}\033[0;95m, ou seja: \n\033[1m{resultado}\033[0;95m \n{'\033[96m=-=\033[m'* 17}')

except Exception as e:
    print(f'Error: {e}')
# Desenvolvido por Kaiky 2025
