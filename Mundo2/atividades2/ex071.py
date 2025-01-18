# Programa que simula um caixa eletrônico
print(f'{"==" * 25}\n{"BANCO DO DEV":^50}\n{"==" * 25}')
saque = int(input("Digite o saque: R$").strip())

total = saque
din = 50
t_dinheiro = 0

while True:
    if total >= din:
        total -= din
        t_dinheiro += 1

    else:
        if t_dinheiro > 0:
            print(f'Total de {t_dinheiro} dinulas de R${din}')
        if din == 50:
            din = 20
        elif din == 20:
            din = 10
        elif din == 10:
            din = 1  

        t_dinheiro = 0
        if total == 0:
            break

print(f'{"==" * 25}\nVolte sempre ao BANCO DO DEV! Tenha uma boa vida!.')
# Desenvolvido por Kaiky 2025
