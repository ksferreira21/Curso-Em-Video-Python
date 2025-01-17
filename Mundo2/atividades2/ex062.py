# Programa feito para descobrir os primeiros termos usando while, com opção de aumentar as casas.
pTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A: '))

termo = pTermo
i = 1
ate = 10

while i != 0:
    while i <= ate:
        print(f'{termo}', end=' > ')
        termo += razao
        i += 1
    print('Fim')
    ate = int(input('\nQuantas casas a mais? '))
    i = 1
# Desenvolvido por Kaiky 2025
