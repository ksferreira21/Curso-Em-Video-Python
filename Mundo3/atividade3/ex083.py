# Programa que analisa expressão númerica e diz se é válida ou não!
expressao = str(input('Digite a expressão: '))
parenteses_controlados = []

# Verifica parênteses balanceados
for caractere in expressao:
    if caractere == '(':
        parenteses_controlados.append('(')

    elif caractere == ')':
        if len(parenteses_controlados) > 0:
            parenteses_controlados.pop()

        else:
            parenteses_controlados.append(')')
            break

# Verifica se a expressão é válida
if len(parenteses_controlados) == 0:

    if expressao[0] in '+-*/' or expressao[-1] in '+-*/':  # Verifica se começa ou termina com operador
        print('A expressão não é válida! (Início ou fim com operador)')

    else:
        print('A expressão é válida!')

else:
    print('A expressão não é válida! (Parênteses desbalanceados)')
# Desenvolvido por Kaiky - 2025
