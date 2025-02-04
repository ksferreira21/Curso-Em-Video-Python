# Programa que lê a média do aluno e monta um dicionário
dados = dict()
dados['nome'] = input('Digite o nome do aluno: ')
dados['media'] = float(input('Digite a média do aluno: '))

if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'

else:
    dados['situação'] = 'Reprovado'

print(f'O aluno {dados["nome"]} foi {dados["situação"]} com média {dados["media"]}')
# Desenvolvido por Kaiky - 2025
