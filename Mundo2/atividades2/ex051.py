# Programa que mostra os primeiros termos de uma P.A
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))
decimo = termo1 + (10 - 1) * razao

for i in range(termo1, decimo + razao, razao):
    print(f'\033[1m{i}', end= ' → ')

print('FIM...\033[m')
# Desenvolvido por Kaiky 2025
