def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')



"""def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'No função teste, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, n vale {x}')

"""



'''def somar(a=0, b=0, c=0):
    s = a + b + c
    if s == 0:
        print(f'Nenhum número digitado.')
    else:
        print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar(2)
somar(c=3, a=2)
somar()
'''



'''
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por Kaiky
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2,10,2)
help(contador)'''

# Testado por Kaiky - 2025
