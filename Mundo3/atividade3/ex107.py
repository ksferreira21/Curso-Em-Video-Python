# Programa que utiliza o pacote useful, para metade, dobro, aumento e redução de um valor determinado pelo o úsuario
from useful import moeda

p = float(input('Digite o preço R$\033[32m'))
print('\033[m')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} o valor fica {moeda.aumento(p, 10)}')
print(f'Reduzindo 13% de {p} o valor fica {moeda.reducao(p, 13)}')
# Desenvolvido por Kaiky - 2025
