from useful import moeda, dado

n = dado.leitor_de_dinheiro('Digite o preço: R$\033[32m')
print('\033[m')
moeda.resumo(n, 35, 22)