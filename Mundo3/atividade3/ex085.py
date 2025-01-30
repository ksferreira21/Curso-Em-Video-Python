num = [[],[]]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[1].sort()
num[0].sort()
print(f'Os valores pares são: {num[0]} \nOs valores ímpares são: {num[1]}')