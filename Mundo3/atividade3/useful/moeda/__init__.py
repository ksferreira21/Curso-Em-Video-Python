def metade(n=0, format=False):
    num = n / 2
    return num if not format else moeda(num)  


def dobro(n=0, format=False):
    num = n * 2
    return num if not format else moeda(num)  


def aumento(n=0, P_aumentar=0, format=False):
    num = n + (n * P_aumentar / 100)
    return num if not format is False else moeda(num)


def reducao(n=0, P_reduzir=0, format=False):
    num = n - (n * P_reduzir / 100)
    return num if not format is False else moeda(num)


def moeda(n=0):
    num = f'R${n:.2f}'
    return num 

def resumo(n=0, P_aumentar=0, P_reduzir=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(n)}')
    print(f'{"Dobro do preço:":<20}{dobro(n, True)}')
    print(f'{"Metade do preço:":<20}{metade(n, True)}')
    print(f'{f"{P_aumentar:.0f}% de aumento:":<20}{aumento(n, P_aumentar)}')
    print(f'{f"{P_reduzir:.0f}% de redução:":<20}{reducao(n, P_reduzir)}')
    print('-' * 30)
