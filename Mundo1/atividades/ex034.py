# Aumento salarial
salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora.')