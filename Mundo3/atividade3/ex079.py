# Programa que lê os números e escreve sua ordem, com algumas regras implementadas.
lista = []
while True:
    try:
        numero = int(input("Digite um número (ou -1 para sair): "))

        if numero == -1:
            break

        if numero in lista:
            print("Número já existe na lista. Desconsiderado.")
        else:
            lista.append(numero)
            print(f"{numero} adicionado com sucesso.")
    
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print('-=-' * 15)
lista.sort()
print(f'Você digitou os valores: {lista}')

# Desenvolvido por Kaiky 2025
