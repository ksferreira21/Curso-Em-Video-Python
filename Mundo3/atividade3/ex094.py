# Programa que lê o nome, sexo, idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostra:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as pessoas com idade acima da média.

dados = dict()
tPesosas = list()
media_de_idade = 0
acima_da_media = 0
mulheres = list()
total_idade = 0

while True:
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo: [M/F] ').upper()
    dados['idade'] = int(input('Idade: '))
    tPesosas.append(dados.copy())

    total_idade += dados['idade']
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    continuar = str(input('Quer continuar? [S/N] ').upper())
    if continuar == 'N':
        break

media_de_idade = total_idade / len(tPesosas)

print('-=' * 30)
print(f'A) Ao todo temos {len(tPesosas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_de_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram: {", ".join(mulheres)}')
print(f'D) Lista de pessoas que estão acima da média: ')

for p in tPesosas:
    if p['idade'] > media_de_idade:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
print()
# Desenvolvido por Kaiky - 2025