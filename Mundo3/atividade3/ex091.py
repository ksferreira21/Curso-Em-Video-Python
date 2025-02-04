# Programa que cria um dicionário com 4 jogadores e 4 dados. Mostra o resultado de cada dado.
from random import randint
from time import sleep
print('Valores Sorteados: ')

dados = {'Jogador 1' : randint(1, 6),
        'Jogador 2' : randint(1, 6),
        'Jogador 3' : randint(1, 6),
        'Jogador 4' : randint(1, 6)
        }
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# Desenvolvido por Kaiky - 2025
