# Programa que identifica o gênero da pessoa e se for diferente de [M/F] da uma mensagem de tente novamente!
sexo = str(input('Qual é o seu sexo? [M/F] ').strip().upper()[0])

while sexo not in ['M', 'F']:
    sexo = str(input('Dados inválidos. Tente novamente: [M/F] ').upper().strip()[0])
    
print(f'O seu sexo {'masculino' if sexo == 'M' else 'Feminino'}, foi registrado com SUCESSO!')
# Desenvolvido por Kaiky 2025
