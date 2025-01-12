from time import sleep
from emoji import emojize
from desafio005 import saindo

nome = str(input('\033[34mQual é o seu nome completo?\033[m ').strip())

def login():
    for i in range(3):
        print('\033[34mLogando/Calculando.' + '.' * i + '\033[m', end='\r')
        sleep(1)
        print(' ' * 30, end='\r')
login()

print(f'Logado como: {nome}')
n1 = float(input('\033[34mQual foi a sua primeira nota?\033[m ').strip())
n2 = float(input('\033[34mQual foi a sua segunda nota?\033[m ').strip())
media = (n1 + n2) / 2

if media < 4.8:
    print(emojize(f'\033[31mVocê deve melhorar sua nota, pois sua média foi {media:.1f}, e por conta de {4.8 - media:.1f} você não alcançou a média. :disappointed_face:\033[m'))
elif 4.8 <= media <= 6.4:
    print(emojize(f'\033[33mParabéns, sua nota foi aceitável: {media:.1f} :neutral_face:\033[m'))
elif 6.4 < media <= 8:
    print(emojize(f'\033[32mSua nota foi EXTREMAMENTE BOA, continue assim! {media:.1f} :star-struck:\033[m'))
else:
    print(emojize(f'\033[31mFoi colocada uma nota acima de 8. Entrada inválida :warning:\033[m'))
    saindo()

# Desenvolvido por Kaiky 2025

'''import emoji
nome = str(input('\033[34mQual o seu nome?\033[m ').title().strip())
if 'Kaiky' in nome:
    print(emoji.emojize('\033[32mQue nome lindo você tem! :face_with_hand_over_mouth:\033[m'))
else:
    print(emoji.emojize('\033[31mQue nome feio :face_vomiting:\033[m'))
print(f'\033[34mBom dia, {nome}!\033[m')'''