# Programa que descobre quantas pessoas são maiores de idade e menores de idade.
from datetime import date
data_atual = date.today().year

maior_de_idade = 0
menor_de_idade = 0

for i in range(1, 8):
    pessoa = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = data_atual - pessoa
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f'Temos {maior_de_idade} pessoas maiores de idade e {menor_de_idade} pessoas menores de idade.')
# Desenvolvido por Kaiky 2025
