# Jogo de adivinhação CPU X PLAYER1
from time import sleep
from random import randint
import pygame
from emoji import emojize

def pensando():
    for i in range(3):
        print(f'\033[33mPensando.{ "." * i }\033[m', end='\r')
        sleep(1)
        print(' ' * 20, end='\r')

def musica():
    pygame.init()
    pygame.mixer.music.load('/home/kaiky/Music/ex028.mp3')
    pygame.mixer.music.play()

def victory():
    pygame.init()
    pygame.mixer.music.load('/home/kaiky/Music/victory.mp3')
    pygame.mixer.music.play()
    sleep(5)

def derrota():
    pygame.init()
    pygame.mixer.music.load('/home/kaiky/Music/defeat.mp3')
    pygame.mixer.music.play()
    sleep(4)

print(f"\033[32m{' '*50}\n{'-=-'*11} \nBEM VINDO AO JOGO DA ADIVINHAÇÃO!\n{'-=-'*11}\033[m")
sleep(3)
print('\033[34mPara começar, irei pensar em um número de 1 a 10, e você deve descobrir.\033[m')
sleep(2)

pensando()
cpu = randint(1, 10)
print('\033[35mPRONTO! Pensei em um número entre 1 e 10. Acha que pode adivinhar? Vamos descobrir!\033[m')

musica()
player_input = input('\033[36mEm que número a CPU pensou? \033[m').strip()

if player_input.lower() == 'dev.k':
    print(f"\033[31mA resposta é {cpu}.\033[m")
    player_input = input('\033[36mAgora, em que número a CPU pensou? \033[m').strip()

if not player_input.isdigit() or not (1 <= int(player_input) <= 10):
    print('\033[31mEntrada Inválida! Por favor, insira um número entre 1 e 10.\033[m')
else:
    player = int(player_input)
    sleep(1)
    if player == cpu:
        print(emojize('\033[32mPARABÉNS VOCÊ ACERTOU!! :check_mark_button:\033[m'))
        victory()
    else:
        print(emojize('\033[31mQue pena! Você errou. \nGAME OVER :cross_mark:\033[m'))
        derrota()
    print(f'\033[33mO número escolhido pela CPU foi \033[31m{cpu}\033[33m e o seu número foi \033[34m{player}\033[33m! \nJOGO FINALIZADO.\033[m')

# Desenvolvido Por Kaiky 2025
