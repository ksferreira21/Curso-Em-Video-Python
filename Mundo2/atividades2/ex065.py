# Programa com intuito de ler seus números e dizer, qual é o maior e menor entre eles.
resposta = ''
maior = quant = 0
menor = float('inf')

while resposta != 'N':
    n1 = int(input('Digite um número: ').split())
    resposta = str(input('Quer continuar? [S/N] ').upper().split()[0])
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    quant += 1

print(f'O maior número entre os \033[33m{quant}\033[m números tem como o maior \033[1;32m{maior}\033[m e o menor \033[1;31m{menor}\033[m')
# Desenvolvido por Kaiky 2025
