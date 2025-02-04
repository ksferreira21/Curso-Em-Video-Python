# Programa que cria uma função chamada frufru() que recebe uma mensagem como parâmetro e mostra uma mensagem formatada.
def frufru(msg):
    size = len(msg) + 4
    print('~' * size)
    print(f'  {msg}')
    print('~' * size)


#Programa incial
frufru('Kaiky')
frufru('Curso em Vídeo - Python Mundo 3')
frufru('CeV')  

# Desenvolvido por Kaiky - 2025