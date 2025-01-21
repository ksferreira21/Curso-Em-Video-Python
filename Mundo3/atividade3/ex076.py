# Programa que faz uma lista de produtos e seus respectivos preços em formato de tabela
lista = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print(f'{"--" * 19}\n{"LISTA DE PREÇOS":^36}\n{"--" * 19}')
for produtos in range(0, len(lista)):
    if produtos % 2 == 0:
        print(f'{lista[produtos]:.<30}', end='')
    else:
        print(f'R${lista[produtos]:>6.2f}')
print('--' * 19)
# Desenvolvido por Kaiky 2025
