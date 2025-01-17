# Programa que soma os números digitados, excluindo o número '999' que faz com que o loop quebre
soma = cont = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))

print(f'A soma dos {cont} números é {soma}.')
# Desenvolvido por Kaiky 2025
