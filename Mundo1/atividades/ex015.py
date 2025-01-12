#Alguel de carros
def main():
    dias = int(input('Quantos dias alugados? '))
    km = float(input('Quantos Km rodados? '))
    total = (dias * 60) + (km * 0.15)
    print(f'O total a pagar é de R${total:.2f}')
if __name__ == '__main__':
    main()
# Desenvolvido por Kaiky 2025