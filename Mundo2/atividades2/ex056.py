# Programa que coleta informações de 5 pessoas, calcula a média de idade, identifica a pessoa mais velha e conta quantas mulheres têm menos de 20 anos.
media_de_idade = 0
mais_velho_idade = 0
mais_velho_nome = ''
menor_20 = 0

for i in range(1, 5):
    print(f'{i}ª Pessoa'.center(50, "="))
    nome = str(input('Digite o nome: ').strip())
    try:
        idade = int(input('Digite a idade: ').strip())
        sexo = str(input('Digite o sexo, [M/F]  ').upper().strip())
        if sexo not in ['M', 'F']:
            print("Entrada inválida! Digite M para Masculino ou F para Feminino.")
            break
        else:
            media_de_idade += idade
            if idade < 20 and sexo == 'F': 
                menor_20 += 1
            if idade > mais_velho_idade:
                mais_velho_idade = idade
                mais_velho_nome = nome
    except Exception as e:
        print(f'Error: {e}')
        break

print(f'''A média de idade é {media_de_idade / 4:.0f} anos.
A pessoa mais velha é {mais_velho_nome} com seus {mais_velho_idade} anos.
Tem {menor_20} mulheres com idade menor de 20 anos.''')
# Desenvolvido por Kaiky 2025
