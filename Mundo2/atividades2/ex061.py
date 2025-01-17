# Programa que mostra os primeiros termos de uma P.A usando while
pTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o razao da P.A: '))

termo = pTermo
i = 1

while i <= 10:
    print(f'\033[1m{termo}', end=' → ')
    termo += razao
    i += 1

print('Fim.')
# Desenvolvido por Kaiky 2025
