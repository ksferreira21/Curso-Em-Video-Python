# Programa que lê a quantidade de termo e assim ele mostra os primeiros elementos de uma Sequência de Fibonacci.
t = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3

print(f'{'~' * 51}\n{t1} > {t2}', end='')

while cont <= t:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1

print(f' > Fim\n {'~' * 50 }')
# Desenvolvido por Kaiky 2025
