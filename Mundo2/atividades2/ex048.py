# Programa que soma número ímpares entre 1 até o seu número escolhido.
soma = 0
contador = 0
fim = int(input('Digite um número inteiro para definir o final da sequência (de 1 até o número escolhido): ').strip())
for i in range(1, fim, 2):
    if i % 3 == 0:
        contador += 1
        soma += i

print(f'A soma de todos os {contador} números divisíveis por 3, de 1 até {fim} é igual a {soma}')
# Desenvolvido por Kaiky 2025
