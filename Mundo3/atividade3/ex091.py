# Programa que cria um dicionário com 4 jogadores e 4 dados. Mostra o resultado de cada dado.
from random import randint
from time import sleep
from operator import itemgetter
print('Valores Sorteados: ')

dados = {'Jogador 1' : randint(1, 6),
        'Jogador 2' : randint(1, 6),
        'Jogador 3' : randint(1, 6),
        'Jogador 4' : randint(1, 6)
        }
ranking = dict()

for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print('-=' * 30)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-=' * 30)

print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com ({v[1]})')
    sleep(1)
# Desenvolvido por Kaiky - 2025
