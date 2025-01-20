# Programa que faz um tupla aleatória e diz qual o maior e o menor número
from random import randint

tupla_aleatoria = tuple(randint(1, 10) for _ in range(5))

tupla_organizada = sorted(tupla_aleatoria)

print(f'A ordem aleatória foi {tupla_aleatoria} e o \nMaior número é {max(tupla_aleatoria)} \nMenor número é {min(tupla_aleatoria)}')
# Desenvolvido por Kaiky 2025
