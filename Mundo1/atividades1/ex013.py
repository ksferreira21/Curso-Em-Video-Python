salario = float(input('\033[33mQual é o salário inicial? \033[32mR$\033[m'))
aumento = int(input('\033[33mQual foi o seu aumento? \033[34m%\033[m'))
salariof = salario + (salario * aumento / 100)
print(f'Um funcionário que ganhava \033[31mR${salario:.2f}\033[m, com \033[34m{aumento}%\033[m, passa a receber \033[32mR${salariof:.2f}\033[m')
# Programa que analisa seu sálario e adicona um aumento.
# Desenvolvido por Kaiky 2025