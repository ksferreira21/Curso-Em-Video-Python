# Programa de prestação mensal e empréstimo.

valor_da_casa = float(input('Qual é o preço da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos você irá pagar? '))

prestacao = valor_da_casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pegar uma casa de R${valor_da_casa:.2f} em {anos:.0f} anos a prestação será de R${prestacao:.2f} e você ganha R${salario:.2f}')

if prestacao <= minimo:
    print(f'Empréstimo \033[93mAprovado\033[m!')
else:
    print('Seu empréstimo ultrapassou 30% do seu salário por isso foi \033[31mNEGADO\033[m!')
# Desenvolvido por Kaiky 2025
