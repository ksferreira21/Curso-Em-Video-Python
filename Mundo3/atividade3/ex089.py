# Programa que lê a media do aluno e monta uma lista
dados = []
while True:
    aluno = [input('Digite o nome do aluno: '), float(input('Digite a 1ª nota do aluno: ')), float(input('Digite a 2ª nota do aluno: '))]
    dados.append(aluno[:])
    stop = input('Você quer continuar? ')
    if stop in 'Nn':
        break
print()
print('=' * 70)
print('BOLETIM DA ESCOLA'.center(70))
print('=' * 70)
print(f'{"POSIÇÃO"} | {"NOME":.<30} {"NOTA 1"} | {"NOTA 2"} | {"MÉDIA GERAL"}')
for pos, c in enumerate(dados):
    print(f'{pos:.<7} | {dados[pos][0]:.<30} {dados[pos][1]:<4}   | {dados[pos][2]:<4}   | {(dados[pos][1] + dados[pos][2])/2:.1f}')
while True:
    nota = int(input('\nDigite a posição do aluno que você deseja ver as notas: [999 para encerrar] '))
    if nota == 999:
        break
    for pos, c in enumerate(dados):
        if nota == pos:
            print(f'\nAs notas do(a) aluno(a) {dados[pos][0]} são:\nNOTA 1: {dados[pos][1]}\nNOTA 2: {dados[pos][2]}')

print('EXECUÇÃO ENCERRADA!')    