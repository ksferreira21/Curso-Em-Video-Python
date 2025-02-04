# Programa que sorteia uma lista de 5 números, destaca os números pares e depois soma.
from random import randint

nums = list()

def sorteia():
    for s in range(5):
        nums.append(randint(1, 10))
    print(f'A lista sorteada foi {nums}')

def somaPar():
    soma = 0
    for num in nums:
        if num % 2 == 0:
            soma += num
            print(f'\033[31m{num}\033[0m', end=' ')
        else:
            print(num, end=' ')
    print(f'\nA soma dos números pares é igual a {soma}')

sorteia()
somaPar()
# Desenvolvido por Kaiky - 2025
