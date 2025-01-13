# Programa que descobre o peso de 5 pessoas é diz qual foi o maior e o menor peso.

maior = 0
menor = float('inf')

for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa? '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso registrado foi {maior:.1f}kg e o menor foi {menor:.1f}kg')
# Desenvolvido por Kaiky 2025
