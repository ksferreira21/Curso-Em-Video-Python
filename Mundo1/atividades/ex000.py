#Testando as coisas!
n1 = int(input('\033[34mDigite um número: \033[m'))
n2 = int(input('\033[34mDigite um número: \033[m'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = round(n1 ** n2, 3)
r = n1 % n2
print(f'''\033[32mA soma é {s},
O produto é {m}
A divisão é {d:.2f}
A divisão inteira é {di}
A potência é {e:.3e}
O resto da divisão é {r}\033[m''')
# Desenvolvido por Kaiky 2025