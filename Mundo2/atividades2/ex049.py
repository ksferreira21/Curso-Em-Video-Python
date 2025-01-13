# Tabuada V2.0
num = int(input('\033[33mDigite um número para ver sua tabuada:\033[m '))

print('\033[1;92m-+-\033[m' * 4)

for i in range(1, 11):
    resultado = num * i
    print(f'\033[31m{num}\033[m x \033[36m{i:2}\033[m = \033[1;35m{resultado:02}\033[m')

print('\033[1;92m-=-\033[m' * 4)
# Achei genial...
# Desenvolvido pro Kaiky 2025
