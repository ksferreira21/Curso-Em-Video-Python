#Ordem de apresentação
from random import shuffle
n1 = str(input('Qual o nome do primeiro aluno: '))
n2 = str(input('Qual o nome do segundo aluno: '))
n3 = str(input('Qual o nome do terceiro aluno: '))
n4 = str(input('Qual o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
ordem_apresentacao = ', '.join(lista)
print(f'A ordem de apresentação é {ordem_apresentacao}')