# Programa que descobre o fatorial e da uma opção de ver o cálculo total ou não.
def fatorial(numero=0, mostrar=False):  

    print('-' * 30)

    resultado = 1
    if mostrar == True:
        while numero > 1:
            print(f'{numero}', end=' x ')
            numero -= 1
            resultado += resultado * numero
        print(f'1 =', end=' ')
    elif mostrar == False:
        while numero > 1:
            numero -= 1
            resultado += resultado * numero
    return resultado


numero = int(input('Digite um número para descobrir o seu fatorial: '))
mostrar = input('Você quer o cálculo total? [Y/N] ')
if mostrar.upper() in 'Y':
    mostrar = True
else:
    mostrar = False
print(fatorial(numero, mostrar))
# Desenvolvido por Kaiky - 2025
