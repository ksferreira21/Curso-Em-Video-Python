def conversor():
    temp = float(input('\033[33mQual a temperatura em ºC? \033[32m'))
    f = ((temp * 9) / 5) + 32
    print(f'A temperatura de \033[31m{temp}ºC\033[m corresponde a \033[32m{f}ºF\033[m')

if __name__ == '__main__':
    conversor()
# Desenvolvido por Kaiky Ferreira 2025