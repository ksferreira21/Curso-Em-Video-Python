# Programa que lê a mensagem e diz se o programa é um palíndromo ou não
mensagem = str(input('Digite uma mensagem: ').strip().upper())

lista = mensagem.split()
sem_espaço = ''.join(lista)
inverso = ''

for texto in range(len(sem_espaço) - 1, -1, -1):
    inverso += sem_espaço[texto]

print(f'A mensagem {sem_espaço} tem como seu inverso {inverso}')

if inverso == sem_espaço:
    print(f'A mensagem "{mensagem.capitalize()}" é um palíndromo!')
else:
    print(f'A mensagem "{mensagem.capitalize()}" não é um palíndromo!')
# Desenvolvido por Kaiky 2025
