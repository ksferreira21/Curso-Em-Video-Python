# Exibir números pares em uma linha, sem vírgula após o último número
for i in range(2, 51, 2):
    if i != 50:
        print(i, end=', ')
    else:
        print(i, end='') # Só para não ter ',' depois do 50.

print('\nFIM')
# Desenvolvido por Kaiky 2025