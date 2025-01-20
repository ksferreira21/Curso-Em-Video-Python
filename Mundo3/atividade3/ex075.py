# Programa que transforma os seus números em tuplas
nt = (int(input('Digite um número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite mais outro número: ')),
    int(input('Digite esse último número: ')))

# Conta quantas vezes o número 9 aparece na tupla
print(f'O número 9 apareceu {nt.count(9)} vez(es) na tupla.')

# Exibe a posição do número 3 na tupla
try:
    print(f'O número 3 aparece na posição {nt.index(3)} da tupla.')
except ValueError:
    print('O número 3 não foi encontrado na tupla.')

# Encontra os números pares na tupla
print(f'Os números pares digitados foram: ', end='')
for n in nt:
    if n % 2 == 0:
        print(n, end=', ')
print('e só.')
# Desenvolvido por Kaiky 2025
