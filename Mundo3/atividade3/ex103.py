# Programa que pede o nome e a quantidade de gols. Caso não tenha, será convertido em <desconhecido> e 0 gols.
def dados(nome='', gols=''):
    if not nome.strip():
        nome = '<desconhecido>'

    if not gols.isdigit():
        gols = 0

    else:
        gols = int(gols)

    print(f'O jogador {nome} fez {gols} gol(s).')

# Programa principal
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')

dados(nome, gols)
# Desenvolvido por Kaiky - 2025
