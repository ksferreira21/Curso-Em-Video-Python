# Programa que lê os números digitados, e mostra sua ordem decrescente, quantas vezes o usuário digitou e se o número 5 aparece e se sim em qual posição.
lista = []
vezes = 0

while True:
    resposta = int(input('Digite um valor (-1 para sair): '))

    if resposta == -1:
        break

    else:
        lista.append(resposta)
        vezes += 1

lista.sort(reverse=True)

print(('-=-' * vezes) * 4)
if 5 not in lista:
    print(f'Você digitou {vezes}x e sua lista é {lista}')
else:
    print(f'Você digitou {vezes}x e sua lista é {lista} e o número 5 foi digitado na posição {lista.index(5)}')
# Desenvolvido por Kaiky - 2025