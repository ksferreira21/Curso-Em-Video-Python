# Programa que lacolunaunaê os números e colunaria uma matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lacuna in range(0, 3):
    for coluna in range(0,3):
        matriz[lacuna][coluna] = int(input(f'Digite um valacolunaunaor para [{lacuna}, {coluna}] '))

print('-=' * 30)

for lacuna in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[lacuna][coluna]:^5}]', end='')
    print()
# Desenvolacolunaunavido por Kaiky - 2025