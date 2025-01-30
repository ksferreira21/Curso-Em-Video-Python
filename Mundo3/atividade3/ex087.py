# Programa que mostra a matriz escolhida pelo o usuário e mostra algumas coisas específicas.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = mai = somac = 0
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor de [{l}],[{c}]: '))

print('-=' * 30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()

print('-=' * 30)
print(f'A soma dos valores pares são: {par}')

for l in range (0,3):
    somac += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somac}')

for c in range (0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

print('-=' * 30)
# Desenvolvido por Kaiky - 2025