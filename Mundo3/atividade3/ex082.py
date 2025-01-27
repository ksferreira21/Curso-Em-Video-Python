# Programa que lê a lista onde os números serão armazenados e em seguida forma outras listas pares e ímpares.
lista = []

while True:
    resposta = int(input('Digite um valor (-1 para sair): '))
    if resposta == -1:
        break
    else:
        lista.append(resposta)

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'''{'-=-' * 30}
Lista: {lista}
Lista Par: {pares}
Lista Ímpar: {impares}
{'-=-' * 30}''')
# Desenvolvido por Kaiky - 2025
