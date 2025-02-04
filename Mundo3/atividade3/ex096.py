# Programa que calcula a área de um terreno retangular. 
print('-=' * 30)
print(f'{"Controle de terrenos":^60}')
print('-=' * 30)

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


# Programa principal
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)
# Desenvolvido por Kaiky - 2025
