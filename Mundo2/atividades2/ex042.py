# Programa que diz se pode formar triângulo e o seu tipo V.2
try:
    r1 = float(input('Digite o valor da primeira reta: '))
    r2 = float(input('Digite o valor da segunda reta: '))
    r3 = float(input('Digite o valor da terceira reta: '))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Podem formar um triângulo!')
        if r1 == r2 and r1 == r3 and r2 == r3:
            tipo = 'Equilátero'
        elif r1 != r2 and r1 != r3 and r2 != r3:
            tipo = 'Escaleno'
        else:
            tipo = 'Isósceles'
        print(f'O tipo do seu triângulo é {tipo}')
    else:
        print('Não pode formar um triângulo.')
        
except ValueError:
    print('\033[31mPor favor, insira um ano válido.\033[m')
# Desenvolvido por Kaiky 2025
