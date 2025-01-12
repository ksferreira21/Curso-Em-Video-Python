n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
# A função input() lê o que o usuário digita.
# Descobrir o tipo primitivo do valor digitado.
# Desenvolvido por: Kaiky 2025