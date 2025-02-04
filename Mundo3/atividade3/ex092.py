# Programa que lê o nome, ano de nascimento, carteira de trabalho e se tiver, o ano de contratação e o sálario de um trabalhador. Monta um dicionário com essas informações e calcula e acrescenta, além da idade, com quantos anos a pessoa vai se aposentar.
dados = dict()

while True:
    dados['nome'] = input('Nome: ')
    ano = int(input('Ano de Nascimento: '))
    dados['idade'] = 2025 - ano
    dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

    if dados['ctps'] == 0:
        break

    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['sálario'] = float(input('Sálario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - 2025)
    break

print('-=' * 30)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
    
# Desenvolvido por Kaiky - 2025
