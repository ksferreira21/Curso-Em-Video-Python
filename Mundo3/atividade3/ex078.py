# Programa que lista os seus valores dizendo a sua posição e qual é o maior e menor.
lista = []

for c, num in enumerate(range(0, 5)):
    lista.append(int(input(f'Digite um valor para a posição {c + 1}: ')))

posicaoMax = lista.index(max(lista))
posicaoMin = lista.index(min(lista))

print(f'''{'-=-' * 20}
O maior valor digitado foi {max(lista)} na posições {posicaoMax + 1}... 
O menor valor digitado foi {min(lista)} na posições {posicaoMin + 1}...
{'-=-' * 20}''')
# Desenvolvido por Kaiky 2025