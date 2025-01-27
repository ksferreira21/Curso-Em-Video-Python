# Programa para criar uma lista ordenada manualmente sem usar .sort()
numeros = []  # Lista onde os números serão armazenados

print("Este programa organiza os números que você digitar, sem usar .sort().")

# Loop para coletar 5 números
for i in range(0, 5):
    numero = int(input('Digite um número: '))
    for posicao, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(posicao, numero)
            print(f'O número {numero} foi inserido na posição {posicao}.')
            break
    else:
        numeros.append(numero)
        print(f'O número {numero} foi inserido na última posição ({len(numeros) - 1}).')

print(f'Os números digitados, em ordem, são: {numeros}')
# Desenvolvido por Kaiky - 2025