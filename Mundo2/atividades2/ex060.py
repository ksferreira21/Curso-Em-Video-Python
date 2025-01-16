# Programa feito para ler o número e descobrir seu fatorial.
from time import sleep
def calculando():
    for i in range(3):
        print('Calculando.' + '.' * i, end='\r')
        sleep(0.5)
        print(' ' * 50, end='\r')

n = int(input('Digite um número para descobrir o seu fatorial: '))
c = n
f = 1

calculando()

print(f'{n}! = ', end='' )

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
# Desenvolvido por Kaiky 2025
