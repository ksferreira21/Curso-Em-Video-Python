# Programa que lista a suas compras informando, o valor final, quantos itens foi + de 1000 reais e qual foi o mais barato.
print(f'{"--" * 15}\n{'LOJA DO TIGRINHO':^30}\n{"--" * 15}')

total = 0
mais_de_mil = 0
barato_nome = ''
barato_valor = float('Inf')

while True:
    n_produto = str(input('Nome do produto: '))
    preco = int(input('Preço R$'))
    stop = str(input('Quer continuar? [S/N]').upper().strip()[0])
    print('==' * 15)
    total += preco

    if preco > 1000:
        mais_de_mil += 1

    if preco < barato_valor:
        barato_valor = preco
        barato_nome = n_produto

    if stop == 'N':
        print(f'{"--" * 15}\n{"FIM DO PROGRAMA":^30}\n{"--" * 15}')
        break

print(f'''O total da compra foi: R${total:.2f}
Produtos custando mais de R$1000.00: {mais_de_mil}
O produto mais barato foi {barato_nome} que custa R${barato_valor:.2f}''')
# Desenvolvido por Kaiky 2025
