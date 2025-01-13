# Programa que lê números pares e faz a soma entre eles (SOMENTE)
s = 0
contador = 0
for i in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        contador += 1

print(f'A soma dos {contador} número pares é: {s}')
# Desenvolvido por Kaiky 2025
