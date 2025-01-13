# Programa que faz uma contagem regressiva de 10 até 0 com 1 segundo entre elas
from time import sleep
from emoji import emojize

print('\033[1;31mContagem regressiva para a explosão dos fogos!\033[m')

for contagem in range(10, -1, -1):
    print(f'\033[1;33m\r{contagem} ' + '\033[m', end='', flush=True) # Utilizei o 'flush=True' para ter uma abordagem em tempo real, sem atrasos no terminal.  
    sleep(1)
print(' ' * 30, end='\r')

print(emojize(':fireworks: \033[1;91mBOOM!\033[m :fireworks:'))
# Desenvolvido por Kaiky 2025
