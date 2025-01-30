# Programa que lê o nome da pessoa e o seu peso e em seguida diz qual o mais pesado e qual o mais leve.
temp = []
princ = []
mai = men = 0
total = 0
while True:

    temp.append(str(input('Digite o seu nome: ')))
    temp.append(float(input('Digite o seu peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] > mai:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    total += 1

    stop = str(input('Continue? [S/N] '))
    if stop in 'Nn':
        break
print(f'Ao todo foram cadastrados {total} pessoas.')
print(f'O maior peso foi de {mai}kg, peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f' {p[0]}')
print(f'O menor peso foi de {men}kg, peso de', end='')
for p in princ:
    if p[1] == men:
        print(f' {p[0]}')
# Desenvolvido por Kaiky - 2025
