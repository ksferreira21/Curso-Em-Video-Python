# Programa que mostra as vogais das palavras que estão na lista
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')

    for vogais in palavra:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
print()
# Desenvolvido por Kaiky 2025