# Programa que utiliza o pacote useful, para metade, dobro, aumento e redução de um valor determinado pelo o úsuario
from useful import moeda

p = float(input('Digite o preço R$\033[32m'))
print('\033[m')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} o valor fica {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Reduzindo 13% de {moeda.moeda(p)} o valor fica {moeda.moeda(moeda.reducao(p, 13))}')
# Desenvolvido por Kaiky - 2025