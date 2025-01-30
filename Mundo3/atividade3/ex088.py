# Programa que faz uma especulação aleatória sobre a mega sena
from random import randint

lista = list()
jogos = list()
quantasx = int(input('Quantos jogos para sortear? '))
tot = 1

while tot <= quantasx:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista: 
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
# Desenvolvido por Kaiky - 2025
