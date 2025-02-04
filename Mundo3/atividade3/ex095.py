# Programa que lê o nome, ano de nascimento, carteira de trabalho e se tiver, o ano de contratação e o sálario de um trabalhador. Monta um dicionário com essas informações e calcula e acrescenta, além da idade, com quantos anos a pessoa vai se aposentar.
gols = list()
total = 0
dados = dict()
jogadores = list()  

while True:
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    
    gols.clear()  
    total = 0  
    
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        total += gols[c]

    dados['gols'] = gols.copy()  
    dados['total'] = total

    jogadores.append(dados.copy())  

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 50)
print('Aproveitamento dos jogadores:')
print('-=' * 50)
print(f'{"POSIÇÃO":<7} | {"NOME":<20} | {"PARTIDAS":>10} | {"GOLS":>5} |')

for pos, jogador in enumerate(jogadores):
    print(f'{pos + 1:<7} | {jogador["nome"]:<20} | {len(jogador["gols"]):>10} | {jogador["total"]:>5} |')


while True:
    nota = int(input('\nDigite a posição do jogador que você deseja ver o aproveitamento (0 para encerrar): '))
    if nota == 0:
        break
    if 1 <= nota <= len(jogadores):
        jogador = jogadores[nota - 1]  # Acha o jogador pelo índice
        print(f'\nO aproveitamento do jogador(a) {jogador["nome"]} em suas {len(jogador["gols"])} partidas foi:')
        for i, g in enumerate(jogador["gols"]):
            print(f'{i + 1}ª partida: {g} gols')
    else:
        print("Posição inválida! Digite um número correto.")

print('<< VOLTE SEMPRE >>')
# Desenvolvido por Kaiky - 2025
