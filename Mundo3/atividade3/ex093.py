# Programa que lê o nome de um jogador, quantas partidas ele jogou e quantos gols ele fez em cada partida. Monta um dicionário com essas informações e mostra o total de gols feitos.

nome = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
gols = list()
total = 0

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    total += gols[c]
dados = {'nome': nome, 'gols': gols, 'total': total}

print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(gols):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {total} gols.')
# Desenvolvido por Kaiky - 2025
