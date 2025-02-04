# Programa que faz uma contagem regressiva determinada e uma que possa escolher
from time import sleep

def mensagem(msg):
    print('-' * 40)
    print(f'{msg.center(40)}')
    print('-' * 40)

def contagem(inicio, fim, passo):
    if passo == 0:
        print('Passo inválido! Usando passo 1 por padrão.')
        passo = 1

    if inicio > fim and passo > 0:
        passo = -passo
    
    mensagem(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    fim = fim + 1 if passo > 0 else fim - 1

    for c in range(inicio, fim, passo):
        sleep(0.5)
        print(c, end=', ', flush=True)
    
    print('FIM!\n')

# Contagens automáticas
contagem(1, 10, 1)
contagem(10, 0, 2)

mensagem('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)
# Desenvolvido por Kaiky - 2025
