# Programa que utiliza pacote useful, para metade, dobro, aumento e redução de um valor determinado pelo o úsuario, com um validador de número.
from useful import moeda, dado

n = dado.leitor_de_dinheiro('Digite o preço: R$\033[32m')
print('\033[m')
moeda.resumo(n, 35, 22)
# Desenvolvido por Kaiky - 2025
