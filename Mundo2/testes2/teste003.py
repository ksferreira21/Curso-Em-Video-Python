s = cont = n = 0
n = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram {cont} número e sua soma é {s}')
# Testado por Kaiky 2025!
