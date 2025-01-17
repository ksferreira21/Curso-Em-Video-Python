# Programa de taubada usando o while True e o Break
while True:
    num = int(input('Digite um número inteiro, para ver sua tabuada: '))
    if num < 0:
        break
    print('-'* 30)
    for n2 in range(1, 11):
        print(f'{num} x {n2:2} = {num*n2:02}')
    print('-'* 30)
print('\033[1;31mPROGRAMA TABUADA FINALIZADO. Volte sempre!\033[m')
# Desenvolvido por Kaiky 2025
