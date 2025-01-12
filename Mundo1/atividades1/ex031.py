from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.YELLOW + 'Qual a distância da viagem em km? ', end='')
distancia = float(input())
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem será de {Fore.GREEN}R${preco:.2f}{Style.RESET_ALL}')
# Developed by Kaiky 2025
