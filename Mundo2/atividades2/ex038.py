try:    
    n1 = int(input('Digite um número: ').strip())
    n2 = int(input('Digite um número: ').strip())
    
    if n1 > n2:
        maior = n1
        print(f'O primeiro número digitado ({n1}) é maior que {n2}')
    elif n2 > n1:
        maior = n2
        print(f'O segundo número digitado ({n2}) é maior que {n1}')
    else:
        print(f'Os números {n1},{n2} são iguais.')

except ValueError:
    print('Entrada Inválida')
# Desenvolvido por Kaiky 2025
