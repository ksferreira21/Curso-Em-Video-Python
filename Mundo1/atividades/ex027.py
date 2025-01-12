# Programa para descobrir primeiro e último nome.
nome = str(input('\033[1;33mDigite seu nome completo: \033[m').title().strip())
separar_o_nome = nome.split()
print(f'''Muito prazer em te conhecer \033[1;32m{nome}\033[m!
Seu primeiro nome é \033[1;34m{separar_o_nome[0]}\033[m
Seu último nome é \033[1;31m{separar_o_nome[-1]}\033[m''')
# Desenvolvido por Kaiky 2025
