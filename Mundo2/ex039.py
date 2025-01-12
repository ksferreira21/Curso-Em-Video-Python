from datetime import date
from colorama import Fore, Style, init

init()

try:
    ano_do_nascimento = int(input(Fore.CYAN + 'Em que ano você nasceu? ' + Style.RESET_ALL))
    ano_atual = date.today().year
    idade = ano_atual - ano_do_nascimento

    if ano_do_nascimento <= 0 or ano_do_nascimento > ano_atual or ano_do_nascimento < ano_atual - 120:
        print(Fore.RED + f"Por favor, insira um ano válido (É quase impossível que você tenha {idade} anos)" + Style.RESET_ALL)
    else:
        if idade == 18:
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f'Já é hora de se alistar ao serviço militar. Pois você tem ou vai completar {idade} anos.' + Style.RESET_ALL)
        elif idade > 18:
            tempo_passado = idade - 18
            print(Fore.YELLOW + f'Você passou do tempo de se alistar ao serviço militar, corra para se alistar o quanto antes, pois já passou {tempo_passado} ano{"" if tempo_passado == 1 else "s"}.' + Style.RESET_ALL)
        else:
            tempo_faltando = 18 - idade
            print(Fore.BLUE + f'Você ainda vai ter que se alistar, pois falta {tempo_faltando} ano{"" if tempo_faltando == 1 else "s"} para completar 18 anos.' + Style.RESET_ALL)
except ValueError:
    print(Fore.RED + 'Por favor, insira um ano válido.' + Style.RESET_ALL)

# Desenvolvido por Kaiky 2025
