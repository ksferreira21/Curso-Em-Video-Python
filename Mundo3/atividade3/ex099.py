# Programa que analisa valores, e diz qual e o maior e se não tiver valores, ele avisa.
from time import sleep

def maior(*num):
    print('-=' * 20)
    print("Analisando os valores passados...")

    if len(num) == 0:
        print(f'{num} Foram informados {len(num)} valores ao todo.')
        print("Nenhum número reconhecido.")
    else:
        print(f'{num} Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado é {max(num)}.')
    sleep(1)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('-=' * 20)
# Desenvolvido por Kaiky - 2025
