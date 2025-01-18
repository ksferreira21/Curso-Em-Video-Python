# Programa desenvolvido para analisar sexo e idade, e entregar informações no final.

RED, GREEN, YELLOW, CYAN, BLUE, MAGENTA, RESET = '\033[31m', '\033[32m', '\033[33m', '\033[36m', '\033[34m', '\033[35m', '\033[m'

maior_de_idade = mulher_vinte = q_homens = 0

while True:
    print(f"{YELLOW}{'-' * 20}\n{CYAN}CADASTRE UMA PESSOA{RESET}\n{YELLOW}{'-' * 20}{RESET}")

    while True:
        try:
            idade = int(input(f"{GREEN}Idade: {RESET}")); break
        except ValueError:
            print(f"{RED}Digite um número válido.{RESET}")

    sexo = input(f"{GREEN}Sexo [M/F]: {RESET}").upper().strip()

    while sexo not in 'MF':
        sexo = input(f"{RED}Inválido! Digite [M/F]: {RESET}").upper().strip()

    if idade > 18: maior_de_idade += 1
    if sexo == 'M': q_homens += 1
    if sexo == 'F' and idade < 20: mulher_vinte += 1

    if input(f"{MAGENTA}Quer continuar? [S/N]: {RESET}").upper().strip() == 'N': break

plural_homens = 'ns' if q_homens != 1 else 'm'
plural_mulheres = 'es' if mulher_vinte != 1 else ''

print(f"""{YELLOW}{'-=-' * 20}{RESET}\n
{CYAN}Total de pessoas com mais de 18 anos: {BLUE}{maior_de_idade}.{RESET}
{CYAN}Ao todo temos {BLUE}{q_homens} home{plural_homens}{RESET} {CYAN}cadastrado{'s' if q_homens != 1 else ''}{RESET}.
{CYAN}E temos {BLUE}{mulher_vinte} mulher{plural_mulheres}{RESET} {CYAN}com menos de 20 anos.\n{RESET}
{YELLOW}{'-=-' * 20}{RESET}""")
# Testei algumas coisinhas nesse programa
# Desenvolvido por Kaiky 2025
