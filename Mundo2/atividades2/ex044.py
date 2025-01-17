# Programa com opções de pagamento, com diversos descontos e juros de acordo com sua escolha.
try:
    preco = float(input('Qual o valor do produto? R$').strip())

    if 0 >= preco:
        print('\033[1;31mEntrada Inválida\033[m')
    else:
        print(f'''{'-=-' * 20}
(1) À Vista no dinheiro/cheque (10% de desconto)
(2) À vista no cartão: (5% de desconto)
(3) Em até 2x no cartão: (Preço normal)
(4) Em até 3x no cartão: (20% juros)
{'-=-' * 20}''')

        resposta = int(input('Qual será a forma de pagamento? ').strip())

    if resposta == 1 or resposta == 2:
        if resposta == 1:
            desconto = preco - (preco * 0.10)
        elif resposta == 2:
            desconto = preco - (preco * 0.05)
        print(f'O valor do produto de R${preco:.2f} recebeu o desconto e está agora: R${desconto:.2f}')

    elif resposta == 3 or resposta == 4:
        if resposta == 3:
            parcelas = 2
            preco_parcelas = preco / 2
        else:
            parcelas = 3
            preco_parcelas = (preco + (preco * 0.2)) / 3

        print(f'O valor do produto de R${preco:.2f}, parcelado em {parcelas}x {'recebeu juros de 20% com isso tem como valor: ' if resposta > 3 else "tem como valor: "}R${preco_parcelas:.2f}')
    else:
        print('\033[1;31mEntrada Inválida\033[m')

except Exception as e:
    print('\033[1;35mInsira o valor corretamente.\033[m')
# Desenvolvido por Kaiky 2025
