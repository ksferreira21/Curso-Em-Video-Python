from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O valor da hipotenusa: {hipotenusa:.2f}')
# Programa que descobre o valor da hipotenusa de acordo com seu cateto oposto e cateto adjacente
# Desenvolvido por Kaiky 2025