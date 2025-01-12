# Análise de número
numero = int(input('\033[36mDigite um número de 0 a 9999:\033[m '))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10
print(f'''\033[35mMilhar: {milhar}\033[m
\033[34mCentena: {centena}\033[m
\033[33mDezena: {dezena}\033[m
\033[32mUnidade: {unidade}\033[m''')
# Desenvolvido por Kaiky 2025