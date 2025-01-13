# Programa que descobre se o número é ou não é um número primo
numero_primo = int(input('Digite um número inteiro: ').strip())
tot = 0

for i in range(1, numero_primo + 1):
    if numero_primo % i == 0:
        print('\033[1;33m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print(f'{i}', end=' ')

print(f'\n\033[mO número {numero_primo} foi diviśivel \033[1;33m{tot}x\033[m')

if  tot == 2:
    print(f'Seu número {numero_primo} é um número primo!')
else:
    print(f'Seu número {numero_primo} não é um número primo!')

# Desenvolvivo por Kaiky 2025
