# Programa para realizar uma visão sobre as posicões de alguns times na tabela
tabela = (
    "Santos", "Mirassol", "Sport", "Ceará", "Novorizontino",
    "Goiás", "Operário", "América-MG", "Vila Nova", "Avaí",
    "Amazonas", "Coritiba", "Paysandu", "Botafogo-SP", "Chapecoense",
    "CRB", "Ponte Preta", "Ituano", "Brusque", "Guarani"
)  # Brasileiro Série B 2024

# Exibindo os 5 primeiros
print("Os 5 primeiros colocados:")
for pos, time in enumerate(tabela[0:5], start=1):
    print(f"Ficou em {pos}ª o time {time}")

# Exibindo os 4 últimos
print("\nOs 4 últimos colocados:")
for pos, time in enumerate(tabela[16: ], start= 17):  # Feito para pegar os últimas posições diretamente
    print(f"Ficou na posição {pos}ª o time {time}")

# Times ordenados em ordem alfabética
resultado = ", ".join(sorted(tabela))
print(f"\nClubes ordenados em ordem alfabética: \n{resultado}.")

# Em que posição está o time Chapecoense
time = "Chapecoense"
posicao = tabela.index(time) + 1
print(f"\nO time {time} está na posição {posicao}ª.")
# Desenvolvido por Kaiky 2025
