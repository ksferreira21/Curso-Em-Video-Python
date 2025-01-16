from random import randint
from time import sleep
import pygame

pygame.init()
tentativas = 1

def pensando():
    for i in range(3):
        print(f'\033[33mPensando{"." * i}\033[m', end='\r')
        sleep(1)
    print(' ' * 20, end='\r')

def musica():
    pygame.mixer.music.load('/home/kaiky/Music/ex028.mp3')
    pygame.mixer.music.play()

def victory():
    pygame.mixer.music.load('/home/kaiky/Music/victory.mp3')
    pygame.mixer.music.play()
    sleep(5)

def escolher_dificuldade():
    while True:
        dificuldade = str(input('\033[1;35mDigite a dificuldade (F/N/D/S):\033[m ').upper().strip()[0])
        if dificuldade == 'F':
            return 'Fácil', randint(1, 10)
        elif dificuldade == 'N':
            return 'Normal', randint(1, 1000)
        elif dificuldade == 'D':
            return 'Difícil', randint(1, 10000)
        elif dificuldade == 'S':
            return 'Secreta', randint(1, 1000000)
        else:
            print('Entrada inválida! Tente novamente.')

print(f"\033[32m{' '*50}\n{'-=-'*13} \nBEM VINDO AO JOGO DA ADIVINHAÇÃO V2.0!\n{'-=-'*13}\033[m")
sleep(3)
print('\033[34mPara começar escolha a dificuldade: \033[m')
sleep(2)

dificuldade, cpu = escolher_dificuldade()

print(f'Dificuldade selecionada: \033[1;32m{dificuldade}\033[m')

print('\033[36mIrei pensar em número de acordo com a dificuldade...\033[m')
pensando()
print('\033[7;32mBOA SORTE!\033[m')
musica()
sleep(1)

while True:
    try:
        player = int(input('Digite o número: '))
        break
    except ValueError:
        print("Por favor, insira um número válido.")

while player != cpu:
    tentativas += 1
    if player > cpu:
        player = int(input(f"Tente \033[1;31mDIMINUIR\033[m o valor \033[1;33m{player}\033[m... \nDigite um novo número: "))
    else:
        player = int(input(f"Tente \033[1;32mAUMENTAR\033[m o valor \033[1;33m{player}\033[m... \nDigite um novo número: "))

victory()
print(f'Você venceu em {tentativas} tentativas! O número escolhido era \033[33m{cpu}\033[m')
