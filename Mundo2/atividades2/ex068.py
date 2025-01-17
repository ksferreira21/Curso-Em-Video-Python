# Jogo de Par ou Ímpar V1.0.0
import random

rodadas = 0
while True:
    # Validação do número e da escolha foram realizadas para impedir que a sequencia seja quebrada!
    while True:
        
        try:
            playerN = int(input('\033[1;36mDigite um valor: \033[m'))  # Azul claro
            playerPoI = input('\033[1;35mPar ou ímpar? [P/I] \033[m').upper()  # Roxo
            if playerPoI not in ['P', 'I']:
                raise ValueError('Escolha inválida!')
            break
        except ValueError as e:
            print(f"\033[1;31m{e}\033[m" if str(e) != 'Escolha inválida!' else "\033[1;31mEscolha inválida! Digite 'P' para Par ou 'I' para Ímpar.\033[m")
    
    cpuN = random.randint(0, 10)
    resultado = playerN + cpuN

    print(f'''{'-' * 43}
\033[1;33mVocê escolheu:\033[m {'\033[1;34mPar\033[m' if playerPoI == 'P' else '\033[1;32mÍmpar\033[m'}!
A \033[1;31mCPU\033[m escolheu o número \033[1;37m{cpuN}\033[m, e a soma deu \033[1;36m{resultado}\033[m!
{'-' * 43}''', end='')

    if (playerPoI == 'P' and resultado % 2 == 0) or (playerPoI == 'I' and resultado % 2 == 1):
        print('\033[1;32m\nVocê \033[1;32mVENCEU!\033[m')  # Verde claro para vitória
    else:
        print(f'\033[1;31m\nVocê \033[1;31mPERDEU!\033[m \n{"-=-" * 14}')
        break

    rodadas += 1
    print(f'\033[1;34mVamos Jogar novamente... \033[m\n\033[1;36m{"-=-" * 14}\033[m')

print(f'\033[1;33mJogo finalizado, você venceu \033[1;37m{rodadas} rodada{"s" if rodadas > 1 or rodadas == 0 else ""}\033[m')
# Desenvolvido por Kaiky 2025
