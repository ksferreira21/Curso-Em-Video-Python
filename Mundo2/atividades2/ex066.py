# Programa feito para somar os números digitados desconsiderando o 999 utilizado while True e Break
num = soma = contador = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break # Quebra de loop
    soma += num
    contador += 1
print(f'A soma dos {contador} números tem como sua soma: {soma}!')
# Desenvolvido por Kaiky
