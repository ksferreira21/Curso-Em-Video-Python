#Analisador de nome
from time import sleep
def analise():
    for i in range(3):
        print(f'\033[91mAnalisando seu perfil.' + '.' * i + '\033[m', end='\r')
        sleep(1)
        print(' ' * 30, end='\r')
nome = str(input('\033[31mQual é o seu nome completo? \033[m').title().strip())
analise()
print(f'''\033[36m{nome}:\033[m
\033[32mO seu nome com todas as letras maiúsculas é {nome.upper()} 
\033[33mO seu nome com todas as letras minúsculas é {nome.lower()}
\033[34mSeu nome no total tem {len(nome) - nome.count(' ')} letras
\033[35mE o seu primeiro nome {nome.split()[0]} tem {nome.find(' ')} letras\033[m''')
