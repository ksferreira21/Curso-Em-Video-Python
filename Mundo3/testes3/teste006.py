def soma(*  valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')


soma(5, 2)
soma(2, 9, 4)



'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''



'''def contador(* núm):
    total = sum(núm)
    for valor in núm:
        print(f'{valor} ', end='')
    print(f'-> Total: {total}')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''



'''def soma(a, b, c=0):
    print(f'A = {a}, B = {b} e C = {c}')
    s = a + b + c
    print(f'A soma de A + B = {s}')


# Programa principal
soma(a=4, b=5)
soma(7, 2)
soma(3, 9, 5)'''
# Testado por 