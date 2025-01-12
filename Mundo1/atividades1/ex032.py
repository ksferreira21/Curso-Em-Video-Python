#Progama que lê se o ano é bissexto
from datetime import date

ano = int(input('\033[33mDigite um ano para saber se é bissexto, coloque 0 para acessar o seu ano: \033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[34m{ano}\033[m é \033[32mbissexto!\033[m')
else:
    print(f'O ano \033[34m{ano}\033[m não é \033[31mbissexto!\033[m')
# Desenvolvido por Kaiky 2025
